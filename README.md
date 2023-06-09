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
<div align="center">
  <a href="https://github.com/MarkMa512/is215-smart-kitchen">
    <img src="media/logo.png" alt="Logo" width="200" >
  </a>

<h3 align="center">Smart Kitchen IoT Solution</h3>

  <p align="center">
    a IS215 Digital Business Technologies and Transformation Project
    <br />
    <a href="https://github.com/MarkMa512/is215-smart-kitchen"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://youtu.be/VCjBWMjaBcI">View Video Demo</a> -->
    ·
    <a href="https://github.com/MarkMa512/is215-smart-kitchen/issues">Report Bug</a>
    ·
    <a href="https://github.com/MarkMa512/is215-smart-kitchen/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#setup-and-screenshot">Dashboard Screenshoot</a></li>
        <!-- <li><a href="#video-demo">Video Demo</a></li> -->
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

### Setup and Screenshot
| Setup  | Screenshot |
| ------------- | ------------- |
| <img align="center" src="media/setup.png" style="display: inline-block; margin: 0 auto; max-width: 100%"> | <img align="center" src="media/bot_screenshot.png" style="display: inline-block; margin: 0 auto; max-width:30%"> |


<!-- ### Video Demo -->
<!-- [![Video Demo](https://img.youtube.com/vi/VCjBWMjaBcI/0.jpg)](https://www.youtube.com/watch?v=VCjBWMjaBcI) -->


### Built With
* [Micro:bits](https://microbit.org/)
* [Python](https://www.python.org)
* [Go](https://go.dev)
* [MQTT Client Telegram Bot](https://github.com/xDWart/mqtg-bot)


<p align="right">(<a href="#top">back to top</a>)</p>

### Directories
- [`/gateway`](https://github.com/MarkMa512/is215-smart-kitchen/tree/master/gateway): gateway porgam

- [`/media`](https://github.com/MarkMa512/is215-smart-kitchen/tree/master/media): photos of models, setup and illustrations

- [`/microbit`](https://github.com/MarkMa512/is215-smart-kitchen/tree/master/microbit): program for microbit micro-controller

- [`/mqtg-bot`](https://github.com/MarkMa512/mqtg-bot/tree/5c6da98b886681b305d1b75946812976c5dbb883): mqtg-bot backend program, forked from: [MQTT Client Telegram Bot](https://github.com/xDWart/mqtg-bot)




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

### Sensors and Device Configuration
1. microbit and sensors setup 
- Micro-controller: [Micro:bit V2](https://microbit.org/new-microbit/)
- Micro-controller Program: [`/microbit/microbit.py`](https://github.com/MarkMa512/is215-smart-kitchen/blob/master/microbit/microbit.py) 
- Extension board: [KittenBot IOBIT V2.0 for micro:bit](https://www.kittenbot.cc/products/kittenbot-iobit-v2-0-for-microbit) 
- Sensors configuration: 
  - [MQ5 Gas Sensor](https://wiki.seeedstudio.com/Grove-Gas_Sensor-MQ5/)
    - AO: Pin0 S
    - DO: Empty
    - GND: G
    - VCC: 3V
  - [MQ2 Gas/Smoke Sensor](https://wiki.seeedstudio.com/Grove-Gas_Sensor-MQ2/)
    - AO: Pin2 S
    - DO: Empty
    - GND: G
    - VCC: 3V
  - [HC-SR-04 Ultrasonic Distance Sensor](https://randomnerdtutorials.com/complete-guide-for-ultrasonic-sensor-hc-sr04/)
    - Vcc: 3V
    - Trig: Pin15 S
    - Echo: Pin16 S
    - Gnd: G

2. Microbit program  
  a. connect the Microbit to your machine via USB port.  
  b. visit: [micro:bit Python Editor](https://python.microbit.org/v/3)  
  c. copy the content from [`/microbit/microbit.py`](https://github.com/MarkMa512/is215-smart-kitchen/blob/master/microbit/microbit.py) to the editor  
  d. click `Send to micro:bit` button to flash the program to the microbit.  

### Installation

1. Clone the repo onto the respective machines
   ```sh
    git clone --recursive https://github.com/MarkMa512/is215-smart-kitchen.git
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

4. Back-end Machine and Telegram Bot Setup: Please refer to [`mqtg-bot/README.md`](https://github.com/MarkMa512/mqtg-bot)

5. HiveMQ Setup Information:  
  - MQTT Broker connection URL: 
    ```
    tcp://broker.hivemq.com:1883
    ```
  - Subscription: 
    ```
    is215g11t04/#
    ```

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
- [x] Event 1: Temperature exceeded TEMPERATURE_THRESHOLD 
  - Temperature readings are read from Microbit's inbuilt thermometer, and the reading has been passed to the [`/gateway/gateway.py`](https://github.com/MarkMa512/is215-smart-kitchen/blob/master/gateway/gateway.py) through serial communication. If the temperature has exceed the `TEMPERATURE_THRESHOLD` defined in the `alert_filter()` function, a high temperature alert will be sent off from the gateway program to the MQTT broker. 
  - Scenario: 
    - Fridge temperature monitoring 
    - Oven/Stove surrouding temperature monitoring

- [x] Event 2: Combustible gas leakage
  - Voltage readings are read off from the MQ5 sensor. When there is presence of combustible gases such as LPG and Natural Gas, the voltage will increase to above `GAS_THRESHOLD` defined in the [`/microbit/microbit.py`](https://github.com/MarkMa512/is215-smart-kitchen/blob/master/microbit/microbit.py), changing `gas_status` from 0 to 1. This will trigger the alarm and the display light on Microbit. This change will be detected by [`/gateway/gateway.py`](https://github.com/MarkMa512/is215-smart-kitchen/blob/master/gateway/gateway.py) via `alert_filter()` function, and an alart will be sent out to the MQTT broker. 
  - Scenario: 
    - Gas stove monitoring
    - Food storage monitoring (by changing gas sensor to MQ135 Air Quality Sensor)

- [x] Event 3: Smoke detection
  - Voltage readings are read off from the MQ2 sensor. When there is presence of smoke, the voltage will increase to above `SMOKE_THRESHOLD` defined in the [`/microbit/microbit.py`](https://github.com/MarkMa512/is215-smart-kitchen/blob/master/microbit/microbit.py), changing `smoke_status` from 0 to 1. This will trigger the alarm and the display light on Microbit. This change will be detected by [`/gateway/gateway.py`](https://github.com/MarkMa512/is215-smart-kitchen/blob/master/gateway/gateway.py) via `alert_filter()` function, and an alart will be sent out to the MQTT broker. 
  - Scenario: 
    - Fire and smoke detection
    - Over-cooking detection

- [x] Event 4: Unguarded stove / no motion detected
    - Distance reading are read off from the HC-SR-04 Ultrasonic Distance Sensor. When there are motions, the distance reading fluctuates, and the timing are recorded as `last_motion_time`. When there is no motion detetced for more than `TIME_THRESHOLD` defined in the `sonar_motion_filter()` function in [`/gateway/gateway.py`](https://github.com/MarkMa512/is215-smart-kitchen/blob/master/gateway/gateway.py), an alarm will be send out to the MQTT broker. 
    - Scenario: 
      - Ensuring critial locations are guarded by person
      - Detect the presence of person / object


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
- A special thank to [Kunyah Cafe](https://www.fortitudeculina.org/) for supporting us with the project. 
- A special thank to [MQTT Client Telegram Bot](https://github.com/xDWart/mqtg-bot) for the backend go client program. 

<p align="right">(<a href="#top">back to top</a>)</p>