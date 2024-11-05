from hal import hal_input_switch as switch
from hal import hal_led as led
import time

def blink_led(delay, duration):
    start_time = time.time()
    while (time.time() - start_time) < duration:
        led.set_output(0, 1)
        time.sleep(delay)
        led.set_output(0, 0)
        time.sleep(delay)

def main():
    led.init()
    switch.init()

    while True:
        if switch.read_slide_switch() == 0:  # Assuming 1 is the "right position"
            blink_led(0.05, 5)  # 0.05s on, 0.05s off for 10 Hz blinking for 5 seconds
            led.set_output(0, 0)  # Turn off the LED after blinking
        else:
            led.set_output(0, 0)  # Ensure LED stays off if switch is not in the right position

# Run the main function
if __name__ == "__main__":
    main()