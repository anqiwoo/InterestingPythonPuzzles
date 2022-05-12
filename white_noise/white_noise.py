import imageio
import numpy as np
import matplotlib.pyplot as plt

nums = np.arange(100, 10000, 850)
for num in nums:
    noise = np.random.normal(0, 1, num)
    corr = np.correlate(noise, noise, mode='full')
    plt.plot(corr)
    # plt.savefig(f'figs/fig{num}.png')
    plt.savefig(f'fig{num}.png')
    plt.close()

with imageio.get_writer('whiteNoise.gif', mode='I') as writer:
    for num in nums:
        # image = imageio.imread(f'figs/fig{num}.png')
        image = imageio.imread(f'fig{num}.png')
        writer.append_data(image)
