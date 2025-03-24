import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import quad
from noises import *
from filesig import *

signal_functions = {
    "1": {"name": "szum o rozkładzie jednostajnym", "func": uniform_dist_noise_function, "params": ["A"],
          "type": "continuous"},
    "2": {"name": "szum gaussowski", "func": normal_dist_noise_function, "params": ["A"], "type": "continuous"},
    "3": {"name": "sygnał sinusoidalny", "func": sin_signal_function, "params": ["A", "T"], "type": "continuous"},
    "4": {"name": "sygnał sinusoidalny wyprostowany jednopołówkowo", "func": half_wave_rectified_sin_signal_function,
          "params": ["A", "T"], "type": "continuous"},
    "5": {"name": "sygnał sinusoidalny wyprostowany dwupołówkowo", "func": full_wave_rectified_sin_signal_function,
          "params": ["A", "T"], "type": "continuous"},
    "6": {"name": "sygnał prostokątny", "func": rectangular_signal_function, "params": ["A", "T", "kw", "t1"],
          "type": "continuous"},
    "7": {"name": "sygnał prostokątny symetryczny", "func": rectangular_symmetrical_signal_function,
          "params": ["A", "T", "kw", "t1"], "type": "continuous"},
    "8": {"name": "sygnał trójkątny", "func": triangle_signal_function, "params": ["A", "T", "kw", "t1"],
          "type": "continuous"},
    "9": {"name": "skok jednostkowy", "func": unit_jump_function, "params": ["A", "ts"], "type": "continuous"},
    "10": {"name": "impuls jednostkowy", "func": unit_impulse_function, "params": ["A", "ns"], "type": "discrete"},
    "11": {"name": "szum impulsowy", "func": impulse_noise_function, "params": ["A", "p"], "type": "discrete"},
}

t1_domain = 0
t2_domain = 10
f_sampling = 50

signals = {}


def generate_domain():
    return np.delete(np.linspace(t1_domain, t2_domain, int(f_sampling * (t2_domain - t1_domain)) + 1), -1)


def generate_signal():
    print("\n-- Wybierz rodzaj sygnału/szumu --")
    for key, info in signal_functions.items():
        print(f"{key}. {info['name']}")
    choice = input("Wybierz numer funkcji: ").strip()
    if choice not in signal_functions:
        print("Nieprawidłowy wybór funkcji.")
        return

    params = {}

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

    func = signal_functions[choice]["func"]
    if int(choice) == 10:
        params['ns'] = x[int(params['ns'])]
        print(f"Po przypisaniu: params['ns'] = {params['ns']}")

    y = np.array([func(t, *[params[p] for p in signal_functions[choice]["params"]]) for t in x])
    signals[label] = {"name": signal_functions[choice]["name"], "x": x, "y": y,
                      "type": signal_functions[choice]["type"]}
    print(f"Sygnał '{label}' ({signal_functions[choice]['name']}) został wygenerowany.\n")

    param_values = tuple(
        params[p] for p in signal_functions[choice]["params"])

    if signals[label]["type"] == "continuous":
        calculate_continous_params(func, param_values)
    else:
        calculate_dicreet_params(x, y)
    show_plot(label)


def arithmetic_operation():
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
    # if signals[label1]["x"] == "continuous" and signals[label1]["y"] == "continuous":
    #     type = "continuous"
    # else:
    #     type = "discrete"
    type = "discrete"

    print("\nWybierz operację arytmetyczną:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    op = input("Twój wybór: ").strip()

    y_result = y1.copy()

    if op == "1":
        for i, val in enumerate(x2):
            if val in x1:
                idx = np.where(x1 == val)[0][0]
                y_result[idx] += y2[i]
        op_name = "dodawania"
    elif op == "2":
        for i, val in enumerate(x2):
            if val in x1:
                idx = np.where(x1 == val)[0][0]
                y_result[idx] -= y2[i]
        op_name = "odejmowania"
    elif op == "3":
        for i, val in enumerate(x2):
            if val in x1:
                idx = np.where(x1 == val)[0][0]
                y_result[idx] *= y2[i]
        op_name = "mnożenia"
    elif op == "4":
        for i, val in enumerate(x2):
            if val in x1:
                idx = np.where(x1 == val)[0][0]
                if y2[i] == 0:
                    y_result[idx] = 0
                else:
                    y_result[idx] /= y2[i]
        op_name = "dzielenia"
    else:
        print("Nieprawidłowy wybór operacji.")
        return

    result_label = input("Podaj etykietę dla wyniku operacji: ").strip()
    if result_label == "":
        print("Etykieta nie może być pusta.")
        return
    signals[result_label] = {"name": f"Wynik {op_name} ({label1} i {label2})", "x": x1, "y": y_result, "type": type}
    print(f"Operacja {op_name} wykonana. Wynik zapisano jako '{result_label}'.\n")
    calculate_dicreet_params(x1, y_result)
    show_plot(result_label)


def show_plot(label_choice):
    # if not signals:
    #     print("Brak wygenerowanych sygnałów. Najpierw wygeneruj sygnał.")
    #     return
    #
    # print("\n-- Dostępne sygnały do wykresu --")
    # for label, info in signals.items():
    #     print(f"{label}: {info['name']}")
    # label_choice = input("Wybierz etykietę sygnału do wyświetlenia: ").strip()
    # if label_choice not in signals:
    #     print("Nieprawidłowa etykieta.")
    #     return

    bins = int(input("Podaj ilość przedziałów (od 5 do 20): ").strip())
    if bins < 5 or bins > 20:
        print("Nieprawidłowe wartości")
        return

    x = signals[label_choice]["x"]
    y = signals[label_choice]["y"]

    fig, axes = plt.subplots(2, 1, figsize=(10, 6), gridspec_kw={'height_ratios': [2, 1]})

    if signals[label_choice]["type"] == "continuous":
        axes[0].plot(x, y, color="red", label=signals[label_choice]["name"])
    else:
        axes[0].scatter(x, y, color="red", label=signals[label_choice]["name"], s=2)
    # axes[0].scatter(x, y, color="red", label=signals[label_choice]["name"])
    axes[0].plot(x, np.zeros_like(x), color="blue", linestyle="dashed")
    axes[0].set_xticks(np.arange(int(min(x)), int(max(x)) + 1, 1))
    axes[0].set_xlabel("Czas")
    axes[0].set_ylabel("Amplituda")
    axes[0].set_title(f"Wykres sygnału: {label_choice} - {signals[label_choice]['name']}")
    axes[0].legend()
    axes[0].grid(True)

    axes[1].hist(y, bins=bins, color='gray', edgecolor='black', alpha=0.7)
    axes[1].set_xlabel("Amplituda")
    axes[1].set_ylabel("Częstotliwość")
    axes[1].set_title("Histogram amplitud sygnału")

    plt.tight_layout()
    plt.show()


def calculate_dicreet_params(x, y):
    # Wartość średnia
    mean_value = np.sum(y) / len(y)
    print(f"Wartość średnia: {mean_value:.4f}")
    # Wartość średnia bezwzględna
    abs_mean_value = np.sum(np.abs(y)) / len(y)
    print(f"Wartość średnia bezwzględna: {abs_mean_value:.4f}")
    # Moc średnia
    power_value = np.sum(np.power(y, 2)) / len(y)
    print(f"Moc średnia: {power_value:.4f}")
    # Wariancja
    variance = np.sum(np.power((y - mean_value), 2)) / len(y)
    print(f"Wariancja: {variance:.4f}")
    # Wartość skuteczna
    rms_value = np.sqrt(power_value)
    print(f"Wartość skuteczna (RMS): {rms_value:.4f}")

    return mean_value, abs_mean_value, power_value, variance, rms_value


def calculate_continous_params(func, param_values):
    # Wartość średnia
    integral = quad(func, t1_domain, t2_domain, args=param_values, limit=1000)[0]
    mean_value = integral / (t2_domain - t1_domain)
    print(f"Wartość średnia: {mean_value:.4f}")

    # Wartość średnia bezwzględna
    integral = quad(lambda t: np.abs(func(t, *param_values)), t1_domain, t2_domain, limit=1000)[0]
    abs_mean_value = integral / (t2_domain - t1_domain)
    print(f"Wartość średnia bezwzględna: {abs_mean_value:.4f}")

    # Moc średnia
    integral = quad(lambda t: np.power(func(t, *param_values), 2), t1_domain, t2_domain, limit=1000)[0]
    power_value = integral / (t2_domain - t1_domain)
    print(f"Moc średnia: {power_value:.4f}")

    # Wariancja
    variance_integral = \
        quad(lambda t: np.power(func(t, *param_values) - mean_value, 2), t1_domain, t2_domain, limit=1000)[0]
    variance = variance_integral / (t2_domain - t1_domain)
    print(f"Wariancja: {variance:.4f}")

    # Wartość skuteczna
    rms_value = np.sqrt(power_value)
    print(f"Wartość skuteczna: {rms_value:.4f}")

    return mean_value, abs_mean_value, power_value, variance, rms_value


def change_domain():
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


def save():
    print("\n-- Dostępne sygnały --")
    for label, info in signals.items():
        print(f"{label}: {info['name']}")
    label = input("Wybierz etykietę sygnału do zapisu:").strip()
    if label in signals:
        signal_info = signals[label]
        y = signal_info["y"]
        start_time = t1_domain
        fs = f_sampling
        # if signal_info["type"] == "continuous":
        #     is_continuous = 1
        # elif signal_info["type"] == "discrete":
        #     is_continuous = 0
        is_continuous = 0
    else:
        try:
            start_time = float(input("Podaj czas początkowy: "))
            fs = float(input("Podaj częstotliwość próbkowania: "))
        except ValueError:
            print("Błędne wartości parametrów.")
        values_str = input("Podaj wartości amplitud (oddzielone spacjami): ")
        try:
            y = np.array([float(v) for v in values_str.split()])
        except Exception as e:
            print("Błędne wartości sygnału:", e)
    filename = input("Podaj nazwę pliku do zapisu: ").strip()
    is_complex = np.iscomplexobj(y)
    try:
        save_signal_to_file(filename, y, start_time, fs, is_complex, is_continuous)
    except Exception as e:
        print("Błąd zapisu do pliku:", e)


def load():
    filename = input("Podaj nazwę pliku do wczytania: ").strip()
    try:
        start_time, fs, is_continuous, y = read_signal_from_file(filename)
        f_type = "continuous" if is_continuous else "discrete"
        print(f'TEST DLA FS: {fs}')
        label = input("Podaj etykietę dla wczytanego sygnału: ").strip()
        x = start_time + np.arange(len(y)) / fs
        signals[label] = {"name": f"Sygnał z pliku {filename}", "x": x, "y": y, "type": f_type,
                          "start_time": start_time,
                          "fs": fs}
        print(f"Sygnał '{label}' wczytany pomyślnie.")
        calculate_dicreet_params(x, y)
        show_plot(label)

    except Exception as e:
        print("Błąd wczytywania pliku:", e)


def main_menu():
    while True:
        print("==========================================")
        print("              MENU GŁÓWNE                ")
        print("==========================================")
        print("1. Wygeneruj sygnał/szum")
        print("2. Operacje arytmetyczne na sygnałach")
        print("3. Zmień parametry domeny (t1, t2, f)")
        print("4. Zapis do pliku")
        print("5. Odczyt z pliku")
        print("6. Wyjście")
        choice = input("Wybierz opcję: ").strip()

        if choice == "1":
            generate_signal()
        elif choice == "2":
            arithmetic_operation()
        elif choice == "3":
            change_domain()
        elif choice == "4":
            save()
        elif choice == "5":
            load()
        elif choice == "6":
            print("Koniec programu.")
            break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.\n")


if __name__ == "__main__":
    main_menu()
