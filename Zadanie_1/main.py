import numpy as np

from noises import *
import matplotlib.pyplot as plt

# x, y = uni_dist_noise(10, 0, 5)
# x, y = normal_dist_noise(2, 0, 100)
# x, y = sin_signal(10, 6.28, 0, 10)
# x, y = half_wave_rectified_sin_signal(1, 4, 0, 10)
# x, y = full_wave_rectified_sin_signal(1, 5, 2, 7)
# x, y = rectangular_signal(1, 2, 0, 10, 0.5)
# x, y = rectangular_symmetrical_signal(1, 2, 0, 10, 0.5)
x, y = triangle_signal(1, 2, 0, 10, 0.5)
print(type(x))
print(type(y))


# x, y = unit_jump(5, -10, 10, 0)
# x, y = unit_impulse(1, 0, 10, 5, 5)


# plt.plot(x, y, color = "red")
# plt.scatter(x, y, color = "red", marker = "s", s=10)
# plt.plot(x, np.zeros_like(x), color = "blue", linestyle= "dashed")
# plt.xticks(np.arange(min(x), max(x)+1, 1))
# plt.show()

def plot_signal_and_histogram(x, y, bins=50):
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))

    # Wykres sygnału
    axs[0].plot(x, y)
    axs[0].set_title(f'Sygnał')
    axs[0].set_xlabel('Czas [s]')
    axs[0].set_ylabel('Amplituda')

    # Histogram
    axs[1].hist(y, bins=bins, edgecolor='black', alpha=0.7)
    axs[1].set_title(f'Histogram')
    axs[1].set_xlabel('Wartości')
    axs[1].set_ylabel('Liczność')

    plt.show()


plot_signal_and_histogram(x, y)