import numpy as np
import matplotlib.pyplot as plt
from thinkdsp import TriangleSignal
from thinkdsp import SquareSignal
from thinkdsp import SawtoothSignal
from thinkdsp import decorate
from thinkdsp import SinSignal

def filter_spectrum(spectrum):
    """Divides the spectrum through by the fs.
    
    spectrum: Spectrum object
    """
    # avoid division by 0
    spectrum.hs[1:] /= spectrum.fs[1:]
    spectrum.hs[0] = 0

wave = TriangleSignal(freq=440).make_wave(duration=0.5)
spectrum = wave.make_spectrum()
plt.subplot(3,1,1)
spectrum.plot(high=10000, color='red')
filter_spectrum(spectrum)
spectrum.scale(440)
spectrum.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

wave2=square = SquareSignal(1100).make_wave(duration=0.5)
spectrum2 = wave2.make_spectrum()
plt.subplot(3,1,2)
spectrum2.plot(high=10000, color='red')
filter_spectrum(spectrum2)
spectrum2.scale(440)
spectrum2.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

wave3=sawtooth = SawtoothSignal().make_wave(duration=0.5)
spectrum3 = wave3.make_spectrum()
plt.subplot(3,1,3)
spectrum3.plot(high=10000, color='red')
filter_spectrum(spectrum3)
spectrum3.scale(440)
spectrum3.plot(high=10000)
decorate(xlabel='Frequency (Hz)')

plt.show()