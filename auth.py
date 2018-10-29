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

    response_verify = myVoiceIt.voice_verification(nisha, "en-US", "Never forget tomorrow is a new day", os.path.abspath("voicePrint_toVerify.wav"))
    print(response_verify)

def createUser():
    voiceid_v1 = myVoiceIt.create_user()
    userid = voiceid_v1
    print(voiceid_v1['userId'])

def createEnrollment():
    response = myVoiceIt.create_voice_enrollment(nisha, "en-US", "Never forget tomorrow is a new day",
                                                  os.path.abspath("voicePrint.wav"))
    response1 = myVoiceIt.create_voice_enrollment(nisha, "en-US", "Never forget tomorrow is a new day",
                                                  os.path.abspath("voicePrint_1.wav"))
    response2 = myVoiceIt.create_voice_enrollment(nisha, "en-US", "Never forget tomorrow is a new day",
                                                  os.path.abspath("voicePrint_2.wav"))