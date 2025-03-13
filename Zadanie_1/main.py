import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

from noises import *

# #Sygnały ciągłe

# A = 10  # amplituda szumu
# t1 = 0  # początek przedziału
# t2 = 5  # koniec przedziału
# f = 1000  # częstotliwość próbkowania
#
# x = np.linspace(t1, t2, int(f * (t2 - t1)))
# y = np.array([uniform_dist_noise_function(t, A) for t in x])

# x, y = normal_dist_noise(2, 0, 100)
# x, y = sin_signal(10, 6.28, 0, 10)
# x, y = half_wave_rectified_sin_signal(1, 4, 0, 10)
# x, y = full_wave_rectified_sin_signal(1, 5, 2, 7)
# x, y = rectangular_signal(1, 2, 0, 10, 0.5)

A = 1  # amplituda
T = 2  # okres
t1 = 0  # początek przedziału
t2 = 10  # koniec przedziału
kw = 0.5  # współczynnik szerokości prostokąta
f = 1000  # częstotliwość próbkowania
x = np.linspace(t1, t2, int(f * (t2 - t1)))
y = np.array([rectangular_signal_function(t, A, T, kw, t1) for t in x])

# x, y = rectangular_symmetrical_signal(1, 2, 0, 10, 0.5)
# x, y = triangle_signal(1, 2, 0, 10, 0.5)
# x, y = unit_jump(5, -10, 10, 0)

# A = 2  # amplituda
# t1 = -10  # początek przedziału
# t2 = 10  # koniec przedziału
# ts = 0  # czas skoku
# f = 1000  # częstotliwość próbkowania
#
# x = np.linspace(t1, t2, int(f * (t2 - t1)))
# y = np.array([unit_jump_function(t, A, ts) for t in x])

# #Sygnały dyskretne
# x, y = unit_impulse(1, 0, 10, 5, 5)
# x, y = impulse_noise(1, 0, 10, 5, 1)

# A = 1
# t1 = 0
# d = 10
# f = 5
# p = 0.5
#
# x = np.arange(t1, t1+d, 1/f)
# y = np.array([impulse_noise_function(t, A, p) for t in x])


##Wartość średnia

# #Dla ciągłych
# integral = quad(unit_jump_function, t1, t2, args=(A, ts), limit = 1000)[0]
# mean_value = integral / (t2 - t1)
# print(mean_value)

##Dla dyskretnych
# mean_value = np.sum(y) / len(y)
# print(mean_value)



# #Wartość średnia bezwzgledna

# integral = quad(rectangular_signal_function, t1, t2, args=(A, T, kw, t1), limit = 1000)[0]
# mean_value = np.abs(integral / (t2 - t1))
# print(mean_value)

#Dla dyskretnych
# mean_value = np.abs(np.sum(y) / len(y))
# print(mean_value)

# with open("plik.bin", "wb") as file:
#     x.tofile(file)
#     y.tofile(file)

#Moc średnia sygnału:
#Dla ciągłych
# integral = quad(rectangular_signal_function, t1, t2, args=(A,T, kw, t1), limit = 1000)[0]
# power_value = np.power(integral / (t2 - t1), 2)
# print(power_value)

#Dla dyskretnych
# power_value = np.power(np.sum(y) / len(y), 2)
# print(power_value)

# with open("plik.bin", "rb") as file:
#     data = np.fromfile(file, dtype = np.float64)
#
#     n =  int(len(data)/2)
#
#     x = data[:n]
#     y = data[n:]


# Oblicznaie parametrów




plt.plot(x, y, color = "red")
# plt.scatter(x, y, color = "red", marker = "s", s=10)
plt.plot(x, np.zeros_like(x), color = "blue", linestyle= "dashed")
plt.xticks(np.arange(min(x), max(x)+1, 1))
plt.show()
