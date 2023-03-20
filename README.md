<div id="top"></div>
<!--
*** Template from: https://github.com/othneildrew/Best-README-Template
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT LOGO -->
<br />
<!-- <div align="center">
  <a href="https://github.com/MarkMa512/smart-hostel">
    <img src="media/team_logo.png" alt="Logo" width="137" height="69">
  </a> -->

<h3 align="center">Smart Kitchen Management System</h3>

  <p align="center">
    a IS215 Digital Business Technologies and Transformation Project
    <br />
    <a href="https://github.com/MarkMa512/smart-hostel"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://youtu.be/VCjBWMjaBcI">View Video Demo</a>
    ·
    <a href="https://github.com/MarkMa512/smart-hostel/issues">Report Bug</a>
    ·
    <a href="https://github.com/MarkMa512/smart-hostel/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#dashboard-screenshot">Dashboard Screenshoot</a></li>
        <li><a href="#video-demo">Video Demo</a></li>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#directories">Directories</a></li>
        <li><a href="#architectural-diagram">Architectural Diagram</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#sensors-and-device-configuration">Sensors and device configuration</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Dashboard Screenshoot
<!-- <img
  align="center"
  src="media/dashboard_table.png"
  alt="dashboard_table"
  title="dashboard_table"
  style="display: inline-block; margin: 0 auto; max-width: 200px"> -->

### Video Demo
<!-- [![Video Demo](https://img.youtube.com/vi/VCjBWMjaBcI/0.jpg)](https://www.youtube.com/watch?v=VCjBWMjaBcI) -->


### Built With
* [Micro:bits](https://microbit.org/)
* [Python](https://www.python.org)
* [Go](https://go.dev)
* [MQTT Client Telegram Bot](https://github.com/xDWart/mqtg-bot)


<p align="right">(<a href="#top">back to top</a>)</p>

### Directories
- [`/gateway`](https://github.com/MarkMa512/smart-hostel/tree/master/sensor_and_gateway): gateway porgam

- [`/media`](https://github.com/MarkMa512/smart-hostel/tree/master/media): photos of models, setup and illustrations

- [`/microbit`](): program for microbit micro-controller

- [`/mqtg-bot`](https://github.com/MarkMa512/smart-hostel/tree/master/front_end): mqtg-bot backend program, forked from: [MQTT Client Telegram Bot](https://github.com/xDWart/mqtg-bot)




### Architectural Diagram

<img
  align="center"
  src="media/architectural_design.png"
  alt="dashboard_table"
  title="dashboard_table"
  style="display: inline-block; margin: 0 auto; max-width: 200px">


<!-- GETTING STARTED -->
## Getting Started

### Prerequisites
1. Ensure [Python 3.9](https://www.python.org/downloads/) or higher is installed; Ensure [pip](https://pip.pypa.io/en/stable/installation/) is installed. 
2. Ensure [go1.20.2](https://go.dev/doc/install) or higher is installed

### Sensors and device configuration
1. microbit and sensors
- Micro-controller: [Micro:bit V2](https://microbit.org/new-microbit/)
- Micro-controller Program: [`/microbit/microbit.py`](https://github.com/MarkMa512/smart-hostel/blob/master/microbit/microbit.py) 
- Extension board: [KittenBot IOBIT V2.0 for micro:bit](https://www.kittenbot.cc/products/kittenbot-iobit-v2-0-for-microbit) 
- Sensors: 
  - MQ5 Sensor 
    - AO: Pin0 S
    - DO: Empty
    - GND: G
    - VCC: 3V
  - MQ2 Sensor 
    - AO: Pin2 S
    - DO: Empty
    - GND: G
    - VCC: 3V
  - HC-SR-04 Ultrasonic Distance Sensor
    - Vcc: 3V
    - Trig: Pin15 S
    - Echo: Pin16 S
    - Gnd: G 
<!-- <img
  align="center"
  src="media/door_microbit_setup.png"
  alt="dashboard_table"
  title="dashboard_table"
  style="display: inline-block; margin: 0 auto; max-width: 200px"> -->


### Installation

1. Clone the repo onto the respective machines
   ```sh
    git clone --recursive https://github.com/MarkMa512/smart-hostel.git
   ```
2. Setup the Microbits according to <a href="#sensors-and-device-configuration">Sensors and device configuration</a>

3. Gateway Machine: Using terminal (macOS) or Command Prompt (Windows)  
  - Enter `gateway` directory:  
    ```sh 
    cd gateway
    ```
  - Install the dependencies 
    ```sh
    pip install -r requirement.txt
    ```
  - run `gateway.py`:  
    ```sh
    python3 gateway.py
    ```
    or 
    ```sh
    python gateway.py
    ```

4. Back-end Machine and Telegram Setup: Please refer to [`mqtg-bot/README.md`](https://github.com/MarkMa512/smart-hostel/tree/master/back_end#readme)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
- [x] Event 1: Temperature exceeded ``
  - The Light sensor on sensor_microbit_door_microbit (implemented) and sensor_microbit_window_microbit (planned) detects the light level and compares it against a threshhold value. 
- [x] Event 2: Make large noise after lights out hours 
  - The Loudness sensor on sensor_microbit_door_microbit (implemented) detects the loudness level and compare it against a threshold value. 
- [x] Event 3: Climbing out of window
  - PIR Motion sensor connected to sensor_microbit_window_microbit detect any movement outside of the window, and the Light sensor on ensor_microbit_window_microbit (planned) detect if there is any changes to the light level as people moves out. 
- [x] Event 4: Leave room after lights out hour 
    - People Counting: Activated by magnetic sensor detecting the magnetic door open, the Ultrasonic Distance Sensor facing inside the room detects a reduction in the distance, thus minus the people count by 1. 
- [x] Event 5:  Movement inside the room
  - Movement detection: When the door is locked (detected by the magnetic sensor), the ultasonic distance sensor inside and outside of the room are re-purposed as detecting movement inside the room or along the corridor. 


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
- A special thank to [Kunyah Cafe](https://www.fortitudeculina.org/) for supporting us with the project. 
- A special thank to [MQTT Client Telegram Bot](https://github.com/xDWart/mqtg-bot) for the backend go client program. 

<p align="right">(<a href="#top">back to top</a>)</p>