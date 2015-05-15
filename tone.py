import math
import pyaudio
from graph import letterFreqPlot

def tone(FrequencyList, length, stream, BITRATE):

    NumberOfFrames = int(BITRATE * length)
    WAVEDATA = ''
    valueList = []

    # sine wave dampening
    ExtraFrames = []
    for Frequency in FrequencyList:
        ExtraFrames.append(NumberOfFrames % (2 * (BITRATE/Frequency)))
    print(ExtraFrames)

    # note sound
    for frame in range(NumberOfFrames - int(min(ExtraFrames))):
        localSum = 0
        for Frequency in FrequencyList:
            if frame < NumberOfFrames - int(ExtraFrames[FrequencyList.index(Frequency)]):
                localSum += int(128 + math.sin((math.pi * frame) / (BITRATE / Frequency)) * 127)
            else:
                localSum += int(128)
        valueList.append(localSum)
        WAVEDATA = WAVEDATA+chr(localSum / len(FrequencyList))
    #letterFreqPlot(valueList[-700:])

    stream.write(WAVEDATA)
