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
    wp.pinMode(RIGHT_ARM_PIN, 0)
    wp.pinMode(LEFT_ARM_PIN, 0)
    wp.pinMode(RIGHT_LEG_PIN, 0)
    wp.pinMode(LEFT_LEG_PIN, 0)
    wp.pinMode(HEAD_PIN, 0)

def check_tilt_and_aplay():
    # must be pull-down
    if(wp.digitalRead(RIGHT_ARM_PIN) == 1):
        subprocess.call("aplay voice/right_arm.wav", shell=True)
        return
    if(wp.digitalRead(LEFT_ARM_PIN_LEG_PIN) == 1):
        subprocess.call("aplay voice/left_arm.wav", shell=True)
        return
    if(wp.digitalRead(RIGHT_LEG_PIN) == 1):
        subprocess.call("aplay voice/right_leg.wav", shell=True)
        return
    if(wp.digitalRead(LEFT_LEG_PIN) == 1):
        subprocess.call("aplay voice/left_leg.wav", shell=True)
        return
    if(wp.digitalRead(HEAD_PIN) == 1):
        subprocess.call("aplay voice/head.wav", shell=True)
        return

def test_voice():
    subprocess.call("aplay voice/test.wav", shell=True)

if __name__ == '__main__':
    test_voice()
    pin_setup()
    while True:
        check_tilt_and_aplay()
        time.sleep(0.5)
