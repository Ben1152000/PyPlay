
import pyaudio
from random import choice
from tone import tone
from noteValues import noteValues

#sudo apt-get install python-pyaudio
PyAudio = pyaudio.PyAudio

# On my computer, 40000 removes most static
bitrate = 40000

p = PyAudio()
stream = p.open(format = p.get_format_from_width(1), 
                channels = 1, 
                rate = bitrate,
                output = True)

### PLAY NOTES HERE:


c_chord = [noteValues['c', 6], noteValues['e', 6], noteValues['g', 6]]
a_chord = [noteValues['a', 5], noteValues['c', 6], noteValues['e', 6]]
f_chord = [noteValues['f', 5], noteValues['a', 5], noteValues['c', 6]]
g_chord = [noteValues['g', 5], noteValues['b', 5], noteValues['d', 6]]
tone(c_chord, 2, stream, bitrate)
tone(a_chord, 2, stream, bitrate)
tone(f_chord, 2, stream, bitrate)
tone(g_chord, 2, stream, bitrate)



###

stream.stop_stream()
stream.close()
p.terminate()