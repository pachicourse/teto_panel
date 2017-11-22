import subprocess
import wiringpi as wp
import time

RIGHT_ARM_PIN = 5
LEFT_ARM_PIN = 6
RIGHT_LEG_PIN = 13
LEFT_LEG_PIN = 19
HEAD_PIN = 26

def pin_setup():
    wp.wiringPiSetupGpio()
    wiringpi.pinMode(RIGHT_ARM_PIN, 0)
    wiringpi.pinMode(LEFT_ARM_PIN, 0)
    wiringpi.pinMode(RIGHT_LEG_PIN, 0)
    wiringpi.pinMode(LEFT_LEG_PIN, 0)
    wiringpi.pinMode(HEAD_PIN, 0)

def check_tilt_and_aplay():
    # must be pull-down
    if(wp.digitalRead(RIGHT_ARM_PIN) == 1):
        subprocess.call("aplay voice/test.wav", shell=True)
    if(wp.digitalRead(LEFT_ARM_PIN_LEG_PIN) == 1):
        subprocess.call("aplay voice/test.wav", shell=True)
    if(wp.digitalRead(RIGHT_LEG_PIN) == 1):
        subprocess.call("aplay voice/test.wav", shell=True)
    if(wp.digitalRead(LEFT_LEG_PIN) == 1):
        subprocess.call("aplay voice/test.wav", shell=True)
    if(wp.digitalRead(HEAD_PIN) == 1):
        subprocess.call("aplay voice/test.wav", shell=True)

def test_voice():
    subprocess.call("aplay voice/test.wav", shell=True)

if __name__ == '__main__':
    test_voice()
    pin_setup()
    while True:
        check_tilt_and_aplay()
        time.sleep(0.5)
