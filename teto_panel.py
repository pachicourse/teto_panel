import subprocess
def test():
    subprocess.call("aplay voice/test.wav", shell=True)

if __name__ == '__main__':
    test()

