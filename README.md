# DDoS Attack Simulation Dashboard

The DDoS Attack Simulation Dashboard is a web application designed to simulate Distributed Denial of Service (DDoS) attacks in a controlled environment. This educational tool is intended for cybersecurity professionals, IT managers, and students to understand how DDoS attacks function and how they impact target systems. The application leverages the hping3 tool to generate synthetic traffic, providing insights into the effects of varying attack intensities and enabling users to test their mitigation strategies.

![ddos_sim](https://github.com/user-attachments/assets/1764f85f-d0c2-48d0-9080-563e5b20228b)

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation and Setup](#installation-and-setup)
- [Usage](#usage)
- [Disclaimer](#disclaimer)
- [License](#license)

## Introduction

The DDoS Attack Simulation Dashboard provides a user-friendly platform to simulate DDoS attacks. By generating synthetic traffic, users can observe the impacts on target systems and refine their defensive measures.

## Features

1. **Web-Based Interface**: A user-friendly dashboard accessible via any web browser.
2. **Traffic Intensity Control**: Allows users to specify the intensity of the traffic (measured in microseconds between packets) to simulate different scales of DDoS attacks.
3. **Target IP Specification**: Users can input the target IP address (IPv4) to direct the attack traffic.
4. **Start and Stop Controls**: Simple buttons to start and stop the DDoS attack simulation.
5. **Logging**: Detailed logging of attack parameters and status updates, aiding in monitoring and analysis.
6. **Educational Insights**: Informational sections explaining the importance of understanding DDoS attacks and their impact on network infrastructure.

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS (embedded in HTML)
- **Traffic Generation**: hping3
- **Logging**: Python's built-in logging module with RotatingFileHandler

## Installation and Setup

1. **Python 3**: Install Python 
    ```bash
   sudo apt install python3 python3-pip
2. **Flask**: Install Flask using pip:
   ```bash
   pip3 install Flask==2.2.3
3. **hping3**: Install hping3:
    ```bash
   sudo apt-get install hping3
4. Linux Terminal:
   ```bash
   git clone https://github.com/Unf0undedOmn1s/ddos_simulation
   cd ddos_simulation
   python app.py / python3 app.py

## Usage
Run the application by navigating to its folder using the terminal: **python3 app.py**
    Open a web browser and navigate to http://127.0.0.1:5000.
    Use the dashboard to set the target IP address and control the traffic intensity.
    Start and stop the DDoS attack simulation using the provided buttons.
    Monitor the logs for detailed information on the attack parameters and status updates.

## Disclaimer

This tool is intended for educational purposes only. Use it responsibly and only in environments where you have explicit permission to conduct such simulations. Misuse of DDoS tools can lead to legal consequences.

## License
© 2024 Marios Grivas. All rights reserved.
