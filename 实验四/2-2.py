import numpy as np
import matplotlib.pyplot as plt

from thinkdsp import decorate
from thinkdsp import Sinusoid
from thinkdsp import normalize, unbias
from thinkdsp import SawtoothSignal


sawtooth = SawtoothSignal().make_wave(duration=0.5, framerate=40000)
plt.subplot(4,1,1)
sawtooth.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

from thinkdsp import SquareSignal

sawtooth.make_spectrum().plot(color='gray')
square = SquareSignal(amp=0.5).make_wave(duration=0.5, framerate=40000)
plt.subplot(4,1,2)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')

from thinkdsp import TriangleSignal
plt.subplot(4,1,3)
sawtooth.make_spectrum().plot(color='gray')
triangle = TriangleSignal(amp=0.79).make_wave(duration=0.5, framerate=40000)
plt.subplot(4,1,4)
triangle.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')        

plt.show()