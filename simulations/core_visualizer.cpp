#include <SFML/Graphics.hpp>
#include <cmath>
#include <vector>
#include <random>
#include <chrono>
#include <sstream>
#include <iomanip>

const int WIDTH = 800;
const int HEIGHT = 800;

struct Point3D { float x, y, z; };

sf::Vector2f project(Point3D p, float angleX, float angleY) {
    float radX = angleX * 3.14159f / 180.0f;
    float radY = angleY * 3.14159f / 180.0f;
    float yt = p.y * cos(radX) - p.z * sin(radX);
    float zt = p.y * sin(radX) + p.z * cos(radX);
    float xt = p.x * cos(radY) - zt * sin(radY);
    float finalZ = p.x * sin(radY) + zt * cos(radY);
    float factor = 400.0f / (finalZ + 600.0f);
    return sf::Vector2f(xt * factor + WIDTH / 2.0f, yt * factor + HEIGHT / 2.0f);
}

void drawWireframeSphere(sf::RenderWindow& window, float radius, int lines, sf::Color color, float angleX, float angleY, float jitterLimit = 0.0f) {
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine generator(seed);
    std::uniform_real_distribution<float> dist(-jitterLimit, jitterLimit);

    for (int i = 0; i < lines; ++i) {
        float lat = 3.14159f * (-0.5f + (float)i / lines);
        sf::VertexArray line(sf::LinesStrip, lines + 1);
        for (int j = 0; j <= lines; ++j) {
            float lon = 2.0f * 3.14159f * (float)j / lines;
            float r = radius + (jitterLimit > 0 ? dist(generator) : 0);
            Point3D p = { 
                static_cast<float>(r * cos(lat) * cos(lon)), 
                static_cast<float>(r * cos(lat) * sin(lon)), 
                static_cast<float>(r * sin(lat)) 
            };
            line[j].position = project(p, angleX, angleY);
            line[j].color = color;
        }
        window.draw(line);
    }
}

int main() {
    sf::RenderWindow window(sf::VideoMode(WIDTH, HEIGHT), "CODE-GEO: JMC RESEARCH TERMINAL");
    window.setFramerateLimit(60);

    // FONT LOADING - Using standard Linux path
    sf::Font font;
    if (!font.loadFromFile("/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf")) {
        // Fallback if the path is different on your distro
        font.loadFromFile("/usr/share/fonts/dejavu/DejaVuSansMono.ttf");
    }

    sf::Text hud;
    hud.setFont(font);
    hud.setCharacterSize(14);
    hud.setFillColor(sf::Color(0, 255, 0, 200));

    float angleX = 0, angleY = 0;
    
    // Scanlines
    sf::VertexArray scanlines(sf::Lines);
    for(int i=0; i < HEIGHT; i+=4) {
        scanlines.append(sf::Vertex(sf::Vector2f(0, i), sf::Color(0, 255, 0, 15)));
        scanlines.append(sf::Vertex(sf::Vector2f(WIDTH, i), sf::Color(0, 255, 0, 15)));
    }

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) window.close();
        }

        window.clear(sf::Color(2, 5, 2));

        // 1. Draw Wireframes
        drawWireframeSphere(window, 220.0f, 16, sf::Color(0, 255, 0, 60), angleX, angleY, 0.0f);
        drawWireframeSphere(window, 85.0f, 12, sf::Color(255, 50, 50, 180), angleX, angleY, 12.0f);

        // 2. HUD DATA
        std::stringstream ss;
        ss << ">>> PROJECT CODE-GEO: LIVE FEED\n";
        ss << "REMNANT MASS: 62.7 M_SUN\n";
        ss << "CORE RADIUS: 1.57e-22m\n";
        ss << "SCRAMBLING: ACTIVE [2.816ms]\n";
        ss << "LATENCY: 652 Q-BITS/SEC\n";
        ss << "STATUS: CRITICAL JITTER";
        
        hud.setString(ss.str());
        hud.setPosition(20, 20);
        window.draw(hud);

        // 3. JMC Branding (Bottom Right)
        sf::Text footer("JMC DEEP SPACE - HOLLY v1.1", font, 12);
        footer.setFillColor(sf::Color(0, 255, 0, 100));
        footer.setPosition(580, 760);
        window.draw(footer);

        window.draw(scanlines);
        
        angleX += 0.7f;
        angleY += 0.5f;
        window.display();
    }
    return 0;
}
