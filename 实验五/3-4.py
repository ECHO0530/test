import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import decorate,read_wave
from thinkdsp import SinSignal

wave=read_wave('1.wav')

wave.make_spectrogram(512).plot(high=5000)
decorate(xlabel='Time (s)', ylabel='Frequency (Hz)')

plt.show()