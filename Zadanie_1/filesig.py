import numpy as np
import struct

HEADER_FORMAT = "<ddIIQ"


def save_signal_to_file(filename, y, start_time=0.0, fs=1000.0, is_complex=False, is_continuous=False):
    flag = 1 if is_complex else 0
    continuous_flag = 1 if is_continuous else 0
    header = struct.pack(HEADER_FORMAT, start_time, fs, flag, continuous_flag, len(y))
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
    with open(filename, "rb") as f:
        header_size = struct.calcsize(HEADER_FORMAT)
        header_bytes = f.read(header_size)
        start_time, fs, flag, continuous_flag, n_samples = struct.unpack(HEADER_FORMAT, header_bytes)
        is_complex = bool(flag)
        is_continuous = bool(continuous_flag)
        if is_complex:
            data = np.fromfile(f, dtype=np.float64)
            data = data.reshape((n_samples, 2))
            y = data[:, 0] + 1j * data[:, 1]
        else:
            y = np.fromfile(f, dtype=np.float64)
    return start_time, fs, is_continuous, y
