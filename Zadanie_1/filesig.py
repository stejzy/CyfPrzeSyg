import numpy as np
import struct
import matplotlib.pyplot as plt

# Definicja formatu nagłówka:
#   - start_time (double, 8 bajtów), fs (double, 8 bajtów),
#   - flag (int – 0 dla rzeczywistych, 1 dla zespolonych, 4 bajty) oraz
#   - n_samples (unsigned long long, 8 bajtów)
HEADER_FORMAT = "<ddIIQ"  # Używamy little-endian: d - double, I - unsigned int, Q - unsigned long long

# t1 = 0
# t2 = 1
# f = 1000
#
#
# x1 = np.delete(np.linspace(0, 1, 100 + 1), -1)  # 101 punktów
# x2 = np.delete(np.linspace(0, 1, 10 + 1), -1)   # 11 punktów
#
# print(x2)
# Tworzymy wartości y dla każdego x (stała wartość 1)
# y1 = np.ones_like(x1)
# y2 = np.ones_like(x2)
#
# common_y = y1.copy()
#
# # Dla każdego punktu w x2 dodajemy odpowiadającą mu wartość do odpowiedniego miejsca w x1
# for i, val in enumerate(x2):
#     if val in x1:
#         idx = np.where(x1 == val)[0][0]  # Znajdź indeks w x1
#         common_y[idx] += y2[i]  # Dodaj wartość y2 do odpowiedniego miejsca w common_y
#
# print("Wynikowa tablica y po dodaniu:", common_y)





# print(np.linspace(0, 1, int(f*(t2-t1))+1))




# def save_signal_to_file(filename, y, start_time=0.0, fs=1.0, is_complex=False):
#     """
#     Zapisuje sygnał do pliku binarnego.
#     W nagłówku zapisujemy: czas początkowy, częstotliwość próbkowania,
#     typ wartości (0 – rzeczywiste, 1 – zespolone) oraz liczbę próbek.
#     Następnie zapisujemy amplitudy próbek jako float64.
#     """
#     # Przygotowanie nagłówka
#     flag = 1 if is_complex else 0
#     header = struct.pack(HEADER_FORMAT, start_time, fs, flag, len(y))
#     with open(filename, "wb") as f:
#         f.write(header)
#         if is_complex:
#             # Zapisujemy naprzemiennie części rzeczywistą i urojoną
#             data = np.empty((len(y), 2), dtype=np.float64)
#             data[:, 0] = y.real
#             data[:, 1] = y.imag
#             data.tofile(f)
#         else:
#             y.astype(np.float64).tofile(f)
#     print(f"Zapisano sygnał do pliku: {filename}")
#
#
# def read_signal_from_file(filename):
#     """
#     Odczytuje sygnał z pliku binarnego według ustalonego formatu.
#     Zwraca: start_time, częstotliwość próbkowania, wektor amplitud.
#     Jeśli sygnał był zespolony, odtworzy części rzeczywistą i urojoną.
#     """
#     with open(filename, "rb") as f:
#         header_size = struct.calcsize(HEADER_FORMAT)
#         header_bytes = f.read(header_size)
#         start_time, fs, flag, n_samples = struct.unpack(HEADER_FORMAT, header_bytes)
#         is_complex = bool(flag)
#         if is_complex:
#             # Odczytujemy 2*n_samples wartości
#             data = np.fromfile(f, dtype=np.float64)
#             data = data.reshape((n_samples, 2))
#             y = data[:, 0] + 1j * data[:, 1]
#         else:
#             y = np.fromfile(f, dtype=np.float64)
#     return start_time, fs, y



