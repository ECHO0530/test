import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal
from thinkdsp import decorate
from thinkdsp import SinSignal


triangle = TriangleSignal(440).make_wave(duration=0.01)
plt.subplot(2,1,1)
triangle.plot()
decorate(xlabel='Time (s)')

spectrum = triangle.make_spectrum()
spectrum.hs[0]
print(spectrum.hs[0])

spectrum.hs[0] = 100
plt.subplot(2,1,2)
triangle.plot(color='red')
spectrum.make_wave().plot()
decorate(xlabel='Time (s)')

plt.show()
