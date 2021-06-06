import matplotlib.pyplot as plt
from thinkdsp import read_wave

def stretch(wave, factor):
    wave.ts *= factor
    wave.framerate /= factor

stretch(wave3, 0.5)
wave3.make_audio()

    wave3.plot()