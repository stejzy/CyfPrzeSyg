import matplotlib.pyplot as plt
from scipy.integrate import quad
import numpy as np

from noises import *
from filesig import *

# #Sygnały ciągłe

# A = 10  # amplituda szumu
# t1 = 0  # początek przedziału
# t2 = 5  # koniec przedziału
# f = 1000  # częstotliwość próbkowania
#
# x = np.linspace(t1, t2, int(f * (t2 - t1)))
# y = np.array([uniform_dist_noise_function(t, A) for t in x])

# x, y = normal_dist_noise(2, 0, 100)
# x, y = sin_signal_function(10, 6.28, 0, 10)
# x, y = half_wave_rectified_sin_signal(1, 4, 0, 10)
# x, y = full_wave_rectified_sin_signal(1, 5, 2, 7)
# x, y = rectangular_signal(1, 2, 0, 10, 0.5)

# A = 1  # amplituda
# T = 2  # okres
# t1 = 0  # początek przedziału
# t2 = 10  # koniec przedziału
# kw = 0.5  # współczynnik szerokości prostokąta
# f = 1000  # częstotliwość próbkowania
# x = np.linspace(t1, t2, int(f * (t2 - t1)))
# y = np.array([rectangular_signal_function(t, A, T, kw, t1) for t in x])

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



##Wartość średnia bezwzgledna

# integral = quad(rectangular_signal_function, t1, t2, args=(A, T, kw, t1), limit = 1000)[0]
# mean_value = np.abs(integral / (t2 - t1))
# print(mean_value)

#Dla dyskretnych
# mean_value = np.abs(np.sum(y) / len(y))
# print(mean_value)

# with open("plik.bin", "wb") as file:
#     x.tofile(file)
#     y.tofile(file)

##Wartość skuteczna

# integral = quad(rectangular_signal_function, t1, t2, args=(A, T, kw, t1), limit = 1000)[0]
# rms_value = np.sqrt(integral / (t2 - t1))
# print(rms_value)

# #Dla dyskretnych
# rms_value = np.sqrt(np.mean(y**2))
# print(rms_value)


##Wariancja

# integral = quad(rectangular_signal_function, t1, t2, args=(A, T, kw, t1), limit = 1000)[0]
# mean_value = np.abs(integral / (t2 - t1))
# variance_integral = quad(lambda t: (rectangular_signal_function(t, A, T, kw, t1) - mean_value)**2, t1, t2, limit = 1000)[0]
# variance = variance_integral / (t2 - t1)
# print(variance)

# #Dla dyskretnych
# rms_value = np.sqrt(np.mean(y**2))
# print(rms_value)


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




# plt.plot(x, y, color = "red")
# # plt.scatter(x, y, color = "red", marker = "s", s=10)
# plt.plot(x, np.zeros_like(x), color = "blue", linestyle= "dashed")
# plt.xticks(np.arange(min(x), max(x)+1, 1))
# plt.show()



signal_functions = {
    "1": {"name": "szum o rozkładzie jednostajnym", "func": uniform_dist_noise_function, "params": ["A"]},
    "2": {"name": "szum gaussowski", "func": normal_dist_noise_function, "params": ["A"]},
    "3": {"name": "sygnał sinusoidalny", "func": sin_signal_function, "params": ["A", "T"]},
    "4": {"name": "sygnał sinusoidalny wyprostowany jednopołówkowo", "func": half_wave_rectified_sin_signal_function, "params": ["A", "T"]},
    "5": {"name": "sygnał sinusoidalny wyprostowany dwupołówkowo", "func": full_wave_rectified_sin_signal_function, "params": ["A", "T"]},
    "6": {"name": "sygnał prostokątny", "func": rectangular_signal_function, "params": ["A", "T", "kw", "t1"]},
    "7": {"name": "sygnał prostokątny symetryczny", "func": rectangular_symmetrical_signal_function, "params": ["A", "T", "kw", "t1"]},
    "8": {"name": "sygnał trójkątny", "func": triangle_signal_function, "params": ["A", "T", "kw", "t1"]},
    "9": {"name": "skok jednostkowy", "func": unit_jump_function, "params": ["A", "ts"]},
    "10": {"name": "impuls jednostkowy", "func": unit_impulse_function, "params": ["A", "ns"]},
    "11": {"name": "szum impulsowy", "func": impulse_noise_function, "params": ["A", "p"]},
}

# Domyślne parametry domeny sygnału
t1_domain = 0    # początek
t2_domain = 10   # koniec
f_sampling = 1000  # częstotliwość próbkowania

signals = {}

def generate_domain():
    """Generuje wektor czasu wg aktualnych parametrów domeny."""
    return np.linspace(t1_domain, t2_domain, int(f_sampling * (t2_domain - t1_domain)))

def generate_signal():
    """Generuje pojedynczy sygnał wg wyboru użytkownika i zapisuje go pod podaną nazwą."""
    print("\n-- Wybierz rodzaj sygnału/szumu --")
    for key, info in signal_functions.items():
        print(f"{key}. {info['name']}")
    choice = input("Wybierz numer funkcji: ").strip()
    if choice not in signal_functions:
        print("Nieprawidłowy wybór funkcji.")
        return

    params = {}
    # Pobierz parametry specyficzne dla wybranej funkcji
    for param in signal_functions[choice]["params"]:
        while True:
            try:
                val = input(f"Podaj wartość parametru {param}: ").strip()
                params[param] = float(val)
                break
            except ValueError:
                print("Błędna wartość, spróbuj ponownie.")

    label = input("Podaj nazwę sygnału (unikatowa etykieta): ").strip()
    if label == "":
        print("Nazwa sygnału nie może być pusta.")
        return

    x = generate_domain()
    # Dla każdego punktu czasu wyznacz wartość sygnału. Uwaga:
    # Funkcje przyjmują parametry w kolejności: t, a potem pozostałe.
    func = signal_functions[choice]["func"]
    # Wygeneruj wektor y – dla funkcji wymagających dodatkowych parametrów (np. t1 w sygnale prostokątnym)
    y = np.array([func(t, *[params[p] for p in signal_functions[choice]["params"]]) for t in x])
    signals[label] = {"name": signal_functions[choice]["name"], "x": x, "y": y}
    print(f"Sygnał '{label}' ({signal_functions[choice]['name']}) został wygenerowany.\n")

def arithmetic_operation():
    """Wykonuje operację arytmetyczną na dwóch sygnałach."""
    if len(signals) < 2:
        print("Wygeneruj co najmniej dwa sygnały przed wykonaniem operacji.")
        return

    print("\n-- Dostępne sygnały --")
    for label, info in signals.items():
        print(f"{label}: {info['name']}")
    label1 = input("Wybierz etykietę pierwszego sygnału: ").strip()
    label2 = input("Wybierz etykietę drugiego sygnału: ").strip()

    if label1 not in signals or label2 not in signals:
        print("Podano nieprawidłowe etykiety.")
        return

    x1, y1 = signals[label1]["x"], signals[label1]["y"]
    x2, y2 = signals[label2]["x"], signals[label2]["y"]

    # Zakładamy, że domena (x) jest taka sama dla obu sygnałów.
    print("\nWybierz operację arytmetyczną:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    op = input("Twój wybór: ").strip()

    if op == "1":
        y_result = y1 + y2
        op_name = "dodawania"
    elif op == "2":
        y_result = y1 - y2
        op_name = "odejmowania"
    elif op == "3":
        y_result = y1 * y2
        op_name = "mnożenia"
    elif op == "4":
        # Unikamy dzielenia przez zero – tam gdzie y2 == 0, ustawiamy wynik na 0
        y_result = np.where(y2 == 0, 0, y1 / y2)
        op_name = "dzielenia"
    else:
        print("Nieprawidłowy wybór operacji.")
        return

    result_label = input("Podaj etykietę dla wyniku operacji: ").strip()
    if result_label == "":
        print("Etykieta nie może być pusta.")
        return
    signals[result_label] = {"name": f"Wynik {op_name} ({label1} i {label2})", "x": x1, "y": y_result}
    print(f"Operacja {op_name} wykonana. Wynik zapisano jako '{result_label}'.\n")

def show_plot():
    """Wyświetla wykres wybranego sygnału."""
    if not signals:
        print("Brak wygenerowanych sygnałów. Najpierw wygeneruj sygnał.")
        return

    print("\n-- Dostępne sygnały do wykresu --")
    for label, info in signals.items():
        print(f"{label}: {info['name']}")
    label_choice = input("Wybierz etykietę sygnału do wyświetlenia: ").strip()
    if label_choice not in signals:
        print("Nieprawidłowa etykieta.")
        return

    x = signals[label_choice]["x"]
    y = signals[label_choice]["y"]

    plt.figure(figsize=(10, 4))
    plt.plot(x, y, color="red", label=signals[label_choice]["name"])
    plt.plot(x, np.zeros_like(x), color="blue", linestyle="dashed")
    plt.xticks(np.arange(int(min(x)), int(max(x)) + 1, 1))
    plt.xlabel("Czas")
    plt.ylabel("Amplituda")
    plt.title(f"Wykres sygnału: {label_choice} - {signals[label_choice]['name']}")
    plt.legend()
    plt.grid(True)
    plt.show()

def change_domain():
    """Pozwala zmienić parametry domeny sygnału."""
    global t1_domain, t2_domain, f_sampling
    print(f"\nAktualna domena: t1 = {t1_domain}, t2 = {t2_domain}, f = {f_sampling}")
    inp = input("Podaj nową wartość t1 (lub naciśnij Enter, aby pozostawić): ").strip()
    if inp:
        try:
            t1_domain = float(inp)
        except ValueError:
            print("Nieprawidłowa wartość.")
    inp = input("Podaj nową wartość t2 (lub naciśnij Enter, aby pozostawić): ").strip()
    if inp:
        try:
            t2_domain = float(inp)
        except ValueError:
            print("Nieprawidłowa wartość.")
    inp = input("Podaj nową wartość f (częstotliwość próbkowania) (lub naciśnij Enter, aby pozostawić): ").strip()
    if inp:
        try:
            f_sampling = float(inp)
        except ValueError:
            print("Nieprawidłowa wartość.")
    print("Domena została zaktualizowana.\n")

def save_signal_to_file(filename, y, start_time=0.0, fs=1000.0, is_complex=False):
    """
    Zapisuje sygnał do pliku binarnego.
    W nagłówku zapisujemy: czas początkowy, częstotliwość próbkowania,
    typ wartości (0 – rzeczywiste, 1 – zespolone) oraz liczbę próbek.
    Następnie zapisujemy amplitudy próbek jako float64.
    """
    flag = 1 if is_complex else 0
    header = struct.pack(HEADER_FORMAT, start_time, fs, flag, len(y))
    with open(filename, "wb") as f:
        f.write(header)
        if is_complex:
            data = np.empty((len(y), 2), dtype=np.float64)
            data[:, 0] = y.real
            data[:, 1] = y.imag
            data.tofile(f)
        else:
            y.astype(np.float64).tofile(f)
    print(f"Zapisano sygnał do pliku: {filename}")

def read_signal_from_file(filename):
    """
    Odczytuje sygnał z pliku binarnego według ustalonego formatu.
    Zwraca: start_time, fs, y (wektor próbek).
    """
    with open(filename, "rb") as f:
        header_size = struct.calcsize(HEADER_FORMAT)
        header_bytes = f.read(header_size)
        start_time, fs, flag, n_samples = struct.unpack(HEADER_FORMAT, header_bytes)
        is_complex = bool(flag)
        if is_complex:
            data = np.fromfile(f, dtype=np.float64)
            data = data.reshape((n_samples, 2))
            y = data[:, 0] + 1j * data[:, 1]
        else:
            y = np.fromfile(f, dtype=np.float64)
    return start_time, fs, y


def main_menu():
    """Główne menu programu."""
    while True:
        print("==========================================")
        print("              MENU GŁÓWNE                ")
        print("==========================================")
        print("1. Wygeneruj sygnał/szum")
        print("2. Operacje arytmetyczne na sygnałach")
        print("3. Wyświetl wykres sygnału")
        print("4. Zmień parametry domeny (t1, t2, f)")
        print("5. Wyjście")
        print("6. Zapis do pliku")
        print("7. Odczyt z pliku")
        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            generate_signal()
        elif choice == "2":
            arithmetic_operation()
        elif choice == "3":
            show_plot()
        elif choice == "4":
            change_domain()
        elif choice == "5":
            print("Koniec programu.")
            break
        elif choice == "6":
            label = input("Podaj etykietę sygnału do zapisu (jeśli znajduje się w pamięci): ").strip()
            if label in signals:
                signal_info = signals[label]
                y = signal_info["y"]
                start_time = signal_info.get("start_time", 0.0)
                fs = signal_info.get("fs", 1.0)
            else:
                try:
                    start_time = float(input("Podaj czas początkowy: "))
                    fs = float(input("Podaj częstotliwość próbkowania: "))
                except ValueError:
                    print("Błędne wartości parametrów.")
                    continue
                values_str = input("Podaj wartości amplitud (oddzielone spacjami): ")
                try:
                    y = np.array([float(v) for v in values_str.split()])
                except Exception as e:
                    print("Błędne wartości sygnału:", e)
                    continue
            filename = input("Podaj nazwę pliku do zapisu: ").strip()
            is_complex = np.iscomplexobj(y)
            try:
                save_signal_to_file(filename, y, start_time, fs, is_complex)
            except Exception as e:
                print("Błąd zapisu do pliku:", e)
        elif choice == "7":
            filename = input("Podaj nazwę pliku do wczytania: ").strip()
            try:
                start_time, fs, y = read_signal_from_file(filename)
                label = input("Podaj etykietę dla wczytanego sygnału: ").strip()
                # Generujemy wektor czasu na podstawie start_time i fs
                x = start_time + np.arange(len(y)) / 1000
                signals[label] = {"name": f"Sygnał z pliku {filename}", "x": x, "y": y, "start_time": start_time,
                                  "fs": fs}
                print(f"Sygnał '{label}' wczytany pomyślnie.")
            except Exception as e:
                print("Błąd wczytywania pliku:", e)
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.\n")

if __name__ == "__main__":
    main_menu()