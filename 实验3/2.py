from thinkdsp import read_wave
import matplotlib.pyplot as plt
from IPython.display import display

wave = read_wave('d:/学习/数字信号处理/实验三/新建文件夹/263868__kevcio__amen-break-a-160-bpm.wav')
wave.normalize()
wave.make_audio()
plt.subplot(4,1,1)
wave.plot()

segment = wave.segment(start=0.4, duration=0.1)
plt.subplot(4,1,2)
segment.plot()

spectrum = segment.make_spectrum()
plt.subplot(4,1,3)
spectrum.plot(high=7000)

spectrum.low_pass(5000)
spectrum.high_pass(500)
spectrum.band_stop(3000,5000)
plt.subplot(4,1,4)
spectrum.make_wave().make_audio()
spectrum.plot(high=7000)

wave = spectrum.make_wave()

wave.play('temp2.wav')
plt.show()

