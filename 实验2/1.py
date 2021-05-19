import matplotlib.pyplot as plt#调用python的一个绘图库
import numpy as np #调用库，用来进行实用的线性代数、傅里叶变换和随机数生成函数

x = np.linspace(0, 3 * np.pi, 100)#设置x轴范围，从0到3π，100个数据点，数据点越多，图像越平滑，显示越精确
y = np.sin(x)#对x取正弦

plt.rcParams['font.sans-serif']=['SimHei'] #设置字体，显示中文
plt.rcParams['axes.unicode_minus']=False #字符显示，可以显示出负号等
plt.subplot(1,2,1)#用三个数字来形成网格，代表有1行，2列，第三个数字是图形的索引号
plt.title(r'$f(x)=sin(x)$') #这个图形的名称
plt.plot(x, y)#用x轴和y轴的数据显示图形


x1 = [t*0.375*np.pi for t in x]#x1的公式，用中间量t*0.375*π，并把x赋给t
y1 = np.sin(x1)#y1的公式，sin（x1的值）
plt.subplot(1,2,2)#一行二列的第二张图
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') #图形名称，\omega来显示出Ω，frac{分子}{分母}来表示分数
plt.plot(x, y1)
plt.show()#显示出所有图像