import os
import wave
import pyaudio
import wave as wav
import numpy as np
from VoiceIt2 import *
from secrets import *



if __name__ == '__main__':
    myVoiceIt = VoiceIt2(key, token)
    allusers = myVoiceIt.get_all_users()
    print(allusers)


def createUser():
    voiceid_v1 = myVoiceIt.create_user()
    userid = voiceid_v1
    print(voiceid_v1['userId'])


