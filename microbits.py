from microbit import *
import music
from machine import time_pulse_us

# Initialize the reading variables
gas_reading = 0
smoke_reading = 0
motion_reading = 0

# defeine the connection pins
# Note: Only pin0, pin1 and pin2 supports Analogue I/O
# pin0 for MQ5 gas sensor
gas_pin = pin0
# pin 1 for MQ2 smoke sensor
smoke_pin = pin2
# pin2 for PIR sensor
motion_pin = pin8

# set up the sonar
sonar_trig = pin15
sonar_echo = pin16
sonar_trig.write_digital(0)
sonar_echo.read_digital()


# Initialize status of gas and smoke reading
gas_status = 0
smoke_status = 0

# define threshold for gas and smoke reading
# adjust the threshold for caliberation under differnt envrionments
gas_threshold = 400
smoke_threshold = 600

while True:
    # obtain gas reading
    gas_reading = gas_pin.read_digital()
    # If the voltage reading is less than the threshold value
    if gas_reading >= gas_threshold:
        # combustible gas is detected
        gas_status = 1
    # if combustible gas is dected
    if gas_status != 0:
        # play the alert music
        # music.play(music.DADADADUM)
        # show the warning image
        display.show(Image.ANGRY)

    # obtain smoke reading
    smoke_reading = smoke_pin.read_digital()
    if smoke_reading >= smoke_threshold:
        smoke_status = 1
    if smoke_status != 0:
        # music.play(music.BA_DING)
        display.show(Image.CONFUSED)

    # people counting status: ultrasonic ranger
    sonar_trig.write_digital(1)
    sonar_trig.write_digital(0)

    micros = time_pulse_us(sonar_echo, 1)
    t_echo = micros / 1000000

    dist_cm = (t_echo / 2) * 34300

    dist_str = str(int(dist_cm))

    # Send the data to serial reading
    # print("g:", gas_reading, "s:", smoke_reading)
    print(temperature(), ",", gas_status, ",",
          smoke_status, ",", dist_str)

    # This does not work for microbit python
    # print(f"{temperature()},{gas_status},{smoke_status},{motion_reading}")

    # clear the gas status and smoke status with long press on button A
    if button_a.is_pressed():
        gas_status = 0
        smoke_status = 0
        display.clear()

    # for testing and simulation purposes
    if button_b.is_pressed():
        gas_status = 1
    sleep(2000)
