'''
# Time Series Decomposition
Original Series  = Trend/Cycle + Seasonal + Error/Residual

# Seasonal-Trend Decomposition using LOESS Regression (STL)
- How it works with Anomaly Detection:
    1. fit the STL to the data
    2. get the trend, seasonal, and residual part
    3. let estimated = trend + seasonal and plot the estimated and original data together (visually anomaly detection)
    4. use the residual and its mean and std to weed out anomaly values

- Example code: https://github.com/ritvikmath/Time-Series-Analysis/blob/master/STL%20Decomposition.ipynb

- Official doc on statsmodels.tsa.seasonal.STL: https://www.statsmodels.org/devel/generated/statsmodels.tsa.seasonal.STL.html 
'''

import pandas as pd
from statsmodels.tsa.seasonal import STL
import matplotlib.pyplot as plt
from datetime import datetime

'''
# 能否通过seasonal序列做fft变换得到频域分量判断周期性?
1. 快速傅里叶变换（Fast Fourier Transform，FFT）是一种可在O(nlogn)时间内完成的离散傅里叶变换（Discrete Fourier transform，DFT）算法。在算法竞赛中的运用主要是用来加速多项式的乘法。DFT的本质是将离散的时域序列用有限个余弦波和正弦波合成。


2. 判断时序周期性的方法（ref：https://zhuanlan.zhihu.com/p/43136171）：
    - 对数据进行平滑处理（用STL提取Seasonal序列）；
    - 找到时间序列的周期T；
    - 以T为分割点，对序列进行分割。假设序列的长度是n，分割后就会有n/T个单元；
    - 比较这n/T个单元的相似度，如果比较相似，则说明具有周期性，如果不是，则不具有周期性；
        - 比较相似度的方法：
            - 皮尔逊相关系数
            - 曲线拟合方法
            - NLP中求语音片段相似度的方法--DTW距离（DTW通过把时间序列进行延伸和缩短，来计算两个时间序列性之间的相似性。）
              python中有dtw包，直接可以计算两个时间序列的相似度：
              dist, cost, acc, path = dtw(x, y, dist=lambda x, y: np.linalg.norm(x - y, ord=1))
              返回值中dist代表距离，如果dist越大，则距离越大，两个时间序列越不相似。
              假如有N个时间单元的话，就需要求N-1次距离。我们将所有的距离值保存到一个列表中，根据设置的阈值，就可以判断出是否具有周期性。DTW的阈值到底设置多少比较合适？到目前为止，还没有一个比较好的思路。我们是通过观察所有曲线来区设置该阈值。

3. 如何通过seasonal序列做fft变换得到频域分量判断周期性:
    - 2相当于是直接根据seasonal序列进行时序周期性判断。
    - 根据要求，另一种判断时间序列周期性的方法是将seasonal序列通过FFT变换得到频域分量。
        - 时域周期对应频域离散：如果通过FFT变换得到的频域是离散的，那么有一个最小的分辨频率，这个自然对应了时域的最大波长，即时域的周期性。比如频率为40的正弦波频域表现是什么样的呢，只有40Hz处的点有值。（ref：https://www.zhihu.com/question/26448935）

# The scipy.fft Module - https://realpython.com/python-scipy-fft/
- The scipy.fft module is newer and should be preferred over scipy.fftpack. 
- SciPy’s fast Fourier transform (FFT) implementation contains more features and is more likely to get bug fixes than NumPy’s implementation. If given a choice, you should use the SciPy implementation.

Fourier analysis is a field that studies how a mathematical function can be decomposed into a series of simpler trigonometric functions. The Fourier transform is a tool from this field for decomposing a function into its component frequencies.

the Fourier transform is a tool that allows you to take a signal and see the power of each frequency in it. Take a look at the important terms in that sentence:
- A signal is information that changes over time. For example, audio, video, and voltage traces are all examples of signals.
- A frequency is the speed at which something repeats. For example, clocks tick at a frequency of one hertz (Hz), or one repetition per second.
- Power, in this case, just means the strength of each frequency.

In general, you need the Fourier transform if you need to look at the frequencies in a signal. 
If working with a signal in the time domain is difficult, then using the Fourier transform to move it into the frequency domain is worth trying.
    - In the time domain, a signal is a wave that varies in amplitude (y-axis) over time (x-axis). The horizontal axis represents time, and the vertical axis represents amplitude.
    - In the frequency domain, a signal is represented as a series of frequencies (x-axis) that each have an associated power (y-axis).

'''
