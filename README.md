# ddos_simulation
The DDoS Attack Simulation Dashboard is a web application designed to simulate Distributed Denial of Service (DDoS) attacks in a controlled environment
This educational tool is intended for cybersecurity professionals, IT managers, and students to understand how DDoS attacks function and how they impact target systems.
The application leverages the hping3 tool to generate synthetic traffic, providing insights into the effects of varying attack intensities and enabling users to test their mitigation strategies.

Features:
I) Web-Based Interface: A user-friendly dashboard accessible via any web browser.
II) Traffic Intensity Control: Allows users to specify the intensity of the traffic (measured in microseconds between packets) to simulate different scales of DDoS attacks.
III) Target IP Specification: Users can input the target IP address (IPv4) to direct the attack traffic.
IV) Start and Stop Controls: Simple buttons to start and stop the DDoS attack simulation.
V) Logging: Detailed logging of attack parameters and status updates, aiding in monitoring and analysis.
VI) Educational Insights: Informational sections explaining the importance of understanding DDoS attacks and their impact on network infrastructure.

Technologies Used: 
I) Backend: Flask (Python)
II) Frontend: HTML, CSS (embedded in HTML)
III) Traffic Generation: hping3
IV) Logging: Python's built-in logging module with RotatingFileHandler

Installation and Setup:
I) Python 3 Made on Thonny - Python IDE, can use alternatives such as VSC, etc.
II) Flask (pip install Flask).
III) hping3 (sudo apt-get install hping3).
IV) Runs on localhost (127.0.0.1:5000) when installed!

Disclaimer!!!
This tool is intended for educational purposes only. Use it responsibly and only in environments where you have explicit permission to conduct such simulations. Misuse of DDoS tools can lead to legal consequences.
© 2024 Marios Grivas. All rights reserved.
