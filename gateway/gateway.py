#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import os
import subprocess
import re
import paho.mqtt.client as mqtt
import sys
import logging
import argparse
import time
from datetime import datetime

# Configure logging
logging.basicConfig(format="%(asctime)s %(levelname)s %(filename)s:%(funcName)s():%(lineno)i: %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S", level=logging.DEBUG)
logger = logging.getLogger(__name__)

# initlize the last motion time for people presence monitoring
last_motion_time = datetime.now()
print(str(last_motion_time))

mqttc = None

# a dictionary of the topics
GATEWAY = {
    "root": "is215g11t04",
    "full_reading": "is215g11t04/full_reading",
    "alert": "is215g11t04/alert",
    "control": "is215g11t04/control"
}

# create output cvs
output_csv_name = datetime.now().strftime('%d%m%Y-%H') + "_data.csv"
create_csv = open(output_csv_name, 'w')
create_csv.close()


# Handles the case when the serial port can't be found


def handle_missing_serial_port() -> None:
    print("Couldn't connect to the micro:bit. Try these steps:")
    print("1. Unplug your micro:bit")
    print("2. Close Tera Term, PuTTY, and all other apps using the micro:bit")
    print("3. Close all MakeCode browser tabs using the micro:bit")
    print("4. Run this app again")
    exit()


# Initializes the serial device. Tries to get the serial port that the micro:bit is connected to
def get_serial_dev_name() -> str:
    logger.info(f"sys.platform: {sys.platform}")
    logger.info(f"os.uname().release: {os.uname().release}")
    logger.info("")

    serial_dev_name = None
    if "microsoft" in os.uname().release.lower():  # Windows Subsystem for Linux

        # List the serial devices available
        try:
            stdout = subprocess.check_output("pwsh.exe -Command '[System.IO.Ports.SerialPort]::getportnames()'",
                                             shell=True).decode("utf-8").strip()
            if not stdout:
                handle_missing_serial_port()
        except subprocess.CalledProcessError:
            logger.error(
                f"Couldn't list serial ports: {e.output.decode('utf8').strip()}")
            handle_missing_serial_port()

        # Guess the serial device
        stdout = stdout.splitlines()[-1]
        serial_dev_name = re.search("COM([0-9]*)", stdout)
        if serial_dev_name:
            serial_dev_name = f"/dev/ttyS{serial_dev_name.group(1)}"

    elif "linux" in sys.platform.lower():  # Linux

        # List the serial devices available
        try:
            stdout = subprocess.check_output("ls /dev/ttyACM*", stderr=subprocess.STDOUT, shell=True).decode(
                "utf-8").strip()
            if not stdout:
                handle_missing_serial_port()
        except subprocess.CalledProcessError as e:
            logger.error(
                f"Couldn't list serial ports: {e.output.decode('utf8').strip()}")
            handle_missing_serial_port()

        # Guess the serial device
        serial_dev_name = re.search("(/dev/ttyACM[0-9]*)", stdout)
        if serial_dev_name:
            serial_dev_name = serial_dev_name.group(1)

    elif sys.platform == "darwin":  # macOS

        # List the serial devices available
        try:
            stdout = subprocess.check_output("ls /dev/cu.usbmodem*", stderr=subprocess.STDOUT, shell=True).decode(
                "utf-8").strip()
            if not stdout:
                handle_missing_serial_port()
        except subprocess.CalledProcessError:
            logger.error(
                f"Error listing serial ports: {e.output.decode('utf8').strip()}")
            handle_missing_serial_port()

        # Guess the serial device
        serial_dev_name = re.search("(/dev/cu.usbmodem[0-9]*)", stdout)
        if serial_dev_name:
            serial_dev_name = serial_dev_name.group(1)

    else:
        logger.error(f"Unknown sys.platform: {sys.platform}")
        exit()

    logger.info(f"serial_dev_name: {serial_dev_name}")
    logger.info("Serial ports available:")
    logger.info("")
    logger.info(stdout)

    if not serial_dev_name:
        handle_missing_serial_port()

    return serial_dev_name


# Handles an MQTT client connect event
# This function is called once just after the mqtt client is connected to the server.


def handle_mqtt_connack(client, userdata, flags, rc) -> None:
    logger.debug(f"MQTT broker said: {mqtt.connack_string(rc)}")
    if rc == 0:
        client.is_connected = True

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(f"{GATEWAY['control']}")
    logger.info(f"Subscribed to: {GATEWAY['control']}")
    logger.info(
        f"Publish something to {GATEWAY['control']} and the messages will appear here.")


# Checks data if there is any abnormalities to raise alerts


def alert_filter(output_dict: dict) -> None:
    time_stamp = datetime.now()

    temperature_alert = f"{time_stamp}: High Temperature Detected! "
    gas_alert = f"{time_stamp}: Combustible Gas Detetcted! "
    smoke_alert = f"{time_stamp}: Smoke Detected! "

    if int(output_dict["temperature"]) > 39:
        mqttc.publish(
            topic=f"{GATEWAY['alert']}", payload=temperature_alert, qos=1)
        logger.info(
            f"Publish | topic: {GATEWAY['alert']} | payload: {temperature_alert}")

    elif output_dict["gas_status"] != 0:
        mqttc.publish(
            topic=f"{GATEWAY['alert']}", payload=gas_alert, qos=1)
        logger.info(
            f"Publish | topic: {GATEWAY['alert']} | payload: {gas_alert}")

    elif output_dict["smoke_status"] != 0:
        mqttc.publish(
            topic=f"{GATEWAY['alert']}", payload=smoke_alert, qos=1)
        logger.info(
            f"Publish | topic: {GATEWAY['alert']} | payload: {smoke_alert}")
    else:
        logger.info("=== All parameter reading normal. ===")
        logger.info(
            f"Full Reading: {str(output_dict)}")

# Checks data if the PIR sensor has not detected motion for > 5mins


def motion_filter(output_dict: dict) -> None:
    global last_motion_time
    motion_alert = "No people monitoring for more than 5 min!"
    # if motion is dected
    if output_dict["motion_reading"] == "1":
        # update the motion time to the current time
        last_motion_time = datetime.now()
    # else ther is no motion
    else:
        # calculate the duration
        time_elapsed = datetime.now() - last_motion_time
        # if the time elapsed has exceeded 5 minutes
        if time_elapsed.total_seconds() > 300:
            mqttc.publish(
                topic=f"{GATEWAY['alert']}", payload=motion_alert, qos=1)
            logger.info(
                f"Publish | topic: {GATEWAY['alert']} | payload: {motion_alert}")

# Writes the reading to the csv file for data analysis


def write_to_csv(reading_str: str) -> None:
    global output_csv_name
    # open the output csv file we created
    output_csv = open(output_csv_name, 'a', newline='')
    # get the date time now
    now_datetime = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    line = (str(now_datetime) + "," + reading_str + "\n")
    # write the line to csv
    output_csv.write(line)
    output_csv.close()

# Covert payload string from microbit to a dictionary, with parameter as a list


def annotate_payload(payload: str, parameter_name_list: list) -> dict:
    # print(payload)
    # print(parameter_name_list)
    output_dict = {}
    payload_list = payload.split(",")
    for i in range(0, len(parameter_name_list)):
        output_dict[parameter_name_list[i]] = int(payload_list[i])
    # print(str(output_dict))
    return output_dict


# Handles incoming serial data


def handle_serial_data(s: serial.Serial) -> None:
    parameter_name_list = ["temperature",
                           "gas_status", "smoke_status", "motion_reading"]

    # decode the payload to a string
    payload = s.readline().decode("utf-8").strip()

    # annotate the payload string to a dict with parameter name
    output_dict = annotate_payload(payload, parameter_name_list)

    # write the payload into CSV
    write_to_csv(payload)
    # check for abnormal readings alerts
    alert_filter(output_dict)
    # moniter the activity level
    motion_filter(output_dict)

# Handles an incoming message from the MQTT broker.


def handle_mqtt_message(client, userdata, msg) -> None:
    logger.info(
        f"received msg | topic: {msg.topic} | payload: {msg.payload.decode('utf8')}")


def main() -> None:
    global mqttc

    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--device", type=str,
                        help="serial device to use, e.g. /dev/ttyS1")

    args = parser.parse_args()
    args_device = args.device

    # Create mqtt client
    mqttc = mqtt.Client()

    # Register callbacks
    mqttc.on_connect = handle_mqtt_connack
    mqttc.on_message = handle_mqtt_message

    # Connect to broker
    mqttc.is_connected = False
    mqttc.connect("broker.mqttdashboard.com")
    mqttc.loop_start()
    time_to_wait_secs = 1
    while not mqttc.is_connected and time_to_wait_secs > 0:
        time.sleep(0.1)
        time_to_wait_secs -= 0.1

    if time_to_wait_secs <= 0:
        logger.error(f"Can't connect to broker.mqttdashboard.com")
        return

    # Try to get the serial device name
    if args.device:
        serial_dev_name = args.device
    else:
        serial_dev_name = get_serial_dev_name()

    with serial.Serial(port=serial_dev_name, baudrate=115200, timeout=10) as s:
        # Sleep to make sure serial port has been opened before doing anything else
        time.sleep(1)

        # Reset the input and output buffers in case there is leftover data
        s.reset_input_buffer()
        s.reset_output_buffer()

        # Loopy loop
        while True:
            try:
                # Read from the serial port
                if s.in_waiting > 0:
                    handle_serial_data(s)
            except KeyboardInterrupt:
                print("CAUGHT CTRL-C, exiting!")
                sys.exit(0)
    # mqttc.loop_stop()


if __name__ == "__main__":
    main()
