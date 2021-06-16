import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import SquareSignal
from thinkdsp import decorate
from thinkdsp import SinSignal

square = SquareSignal(1100)
plt.subplot(2,1,1)
square.plot()
decorate(xlabel='Time (s)')

square = SquareSignal(1100).make_wave(duration=0.5, framerate=10000)
plt.subplot(2,1,2)
square.make_spectrum().plot()
decorate(xlabel='Frequency (Hz)')


plt.show()
