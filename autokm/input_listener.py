import sounddevice as sd
import queue
import pyaudio
import struct
import math
from datetime import datetime
import speech_recognition as sr

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        #r.adjust_for_ambient_noise(source, duration=0.5)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            
        except Exception as e:
            print("No Noise Detected")

    return said.lower()


def remove_activator(command):
    for word in ["pierre", "pier", "tapir", "apr", "beer", "repair"]:
        idx = command.find(word)
        
        if idx != -1:
            starting_idx = idx + len(word) + 1
            
            return command[starting_idx:]


def get_rms(block):
    SHORT_NORMALIZE = (1.0/32768.0)
    
    count = len(block)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, block )

    sum_squares = 0.0
    for sample in shorts:
        n = sample * SHORT_NORMALIZE
        sum_squares += n*n

    return math.sqrt( sum_squares / count )


def input_detector(activator, quick_input=False):
    #Detector Settings
    INITIAL_TAP_THRESHOLD = 0.030
    FORMAT = pyaudio.paInt16 
    CHANNELS = 1
    RATE = 44100  
    INPUT_BLOCK_TIME = 0.05
    INPUT_FRAMES_PER_BLOCK = int(RATE*INPUT_BLOCK_TIME)

    OVERSENSITIVE = 15.0/INPUT_BLOCK_TIME                    
    UNDERSENSITIVE = 120.0/INPUT_BLOCK_TIME # if we get this many quiet blocks in a row, decrease the threshold
    MAX_TAP_BLOCKS = 0.15/INPUT_BLOCK_TIME # if the noise was longer than this many blocks, it's not a 'tap'

    tap_threshold = INITIAL_TAP_THRESHOLD                  #]
    noisycount = MAX_TAP_BLOCKS+1                          #|---- Variables for noise detector...
    quietcount = 0                                         #|
    errorcount = 0  
    
    #Sound input setup
    pa = pyaudio.PyAudio()                                 #]
                                                           #|
    stream = pa.open(format = FORMAT,                      #|
             channels = CHANNELS,                          #|---- You always use this in pyaudio...
             rate = RATE,                                  #|
             input = True,                                 #|
             frames_per_buffer = INPUT_FRAMES_PER_BLOCK)   #] 
    
    
    #Code to detect noise
    for i in range(1000):
        block = stream.read(INPUT_FRAMES_PER_BLOCK)

        amplitude = get_rms(block)
        if amplitude > tap_threshold: # if its to loud...
            print("Listening")
            command = get_audio()
            command = command.lower()
            if activator in command or 'pier' in command or 'beer' in command or 'tapir' in command or "repair" in command:
                print("Raw Command: ", command)
                print("Clean Command: ", remove_activator(command))
                return remove_activator(command)
            
            print("End")

            quietcount = 0
            noisycount += 1
            
        if quick_input is True:
            if amplitude > tap_threshold*0:
                print("quick listen")
                command = get_audio()
                command = command.lower()

                print("end")
                return command

        else: # if its to quiet...
            if 1 <= noisycount <= MAX_TAP_BLOCKS:
                pass
            
            noisycount = 0
            quietcount += 1
            
            
#write a script to end pierre input after like 3 seconds if no sound detected (multithread for this)
if __name__ == "__main__":
    input_detector()