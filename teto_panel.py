import subprocess
import wiringpi as wp
import time

RIGHT_ARM_PIN = 5
LEFT_ARM_PIN = 6
RIGHT_LEG_PIN = 13
LEFT_LEG_PIN = 19
HEAD_PIN = 26

RIGHT_ARM_VOICE = ['6.は〜い、握手ね.wav', 
                   '2.どんなマイクも握ります.wav',
                   '3.きみに会ったら〜.wav']

LEFT_ARM_VOICE = ['1.フランスパン食べたいな.wav',
                  '4.手、繋ぎたいの？.wav',
                  '5.今日は来てくれてありがと.wav']

RIGHT_LEG_VOICE = ['7.ちょっと、変なとこ触らないでよね.wav', 
                   '8.わぁ！くすぐったいってば.wav',
                   '9.これ以上は、事務所NGだよー.wav']

LEFT_LEG_VOICE = ['10.君は実に馬鹿だな.wav', 
                  '11.なーにを考えてるのかなぁ.wav ',
                  '12.もしかして、ボクに見惚れてた？.wav']

HEAD_VOICE = ['13.撫でてもらえるのは嬉しいなぁ.wav', 
              '14.今日の髪型キマってるでしょ.wav',
              '15.アイドルやってる重音テトです〜.wav']

def pin_setup():
    wp.wiringPiSetupGpio()
    wp.pinMode(RIGHT_ARM_PIN, 0)
    wp.pinMode(LEFT_ARM_PIN, 0)
    wp.pinMode(RIGHT_LEG_PIN, 0)
    wp.pinMode(LEFT_LEG_PIN, 0)
    wp.pinMode(HEAD_PIN, 0)

def check_tilt_and_aplay(vc):
    # must be pull-down
    if(wp.digitalRead(RIGHT_ARM_PIN) == 1):
        subprocess.call("aplay voice/" + RIGHT_ARM_VOICE[vc], shell=True)
        return True
    if(wp.digitalRead(LEFT_ARM_PIN) == 1):
        subprocess.call("aplay voice/" + LEFT_ARM_VOICE[vc], shell=True)
        return True
    if(wp.digitalRead(RIGHT_LEG_PIN) == 1):
        subprocess.call("aplay voice/" + RIGHT_LEG_VOICE[vc], shell=True)
        return True
    if(wp.digitalRead(LEFT_LEG_PIN) == 1):
        subprocess.call("aplay voice/" + LEFT_LEG_VOICE[vc]_, shell=True)
        return True
    if(wp.digitalRead(HEAD_PIN) == 1):
        subprocess.call("aplay voice/" + HEAD_VOICE[vc], shell=True)
        return True

    return False

def test_voice():
    subprocess.call("aplay voice/test.wav", shell=True)

if __name__ == '__main__':
    voice_counter = 0
    test_voice()
    pin_setup()
    while True:
        if check_tilt_and_aplay(voice_counter % 3):
            voice_counter = voice_counter + 1
        time.sleep(0.5)
