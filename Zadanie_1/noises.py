import numpy as np


def uniform_dist_noise_function(t, A):
    return np.random.uniform(-A, A)


def normal_dist_noise_function(t, A):
    return A * np.random.normal(loc=0, scale=1)


def sin_signal_function(t, A, T):
    return A * np.sin((2 * np.pi / T) * (t))


def half_wave_rectified_sin_signal_function(t, A, T):
    return 0.5 * A * (np.sin((2 * np.pi / T) * (t)) + np.abs(np.sin((2 * np.pi / T) * (t))))


def full_wave_rectified_sin_signal_function(t, A, T):
    return 0.5 * A * np.abs(np.sin((2 * np.pi / T) * (t)))


def rectangular_signal_function(t, A, T, kw, t1):
    start_time = t1 + T * int(t // T)
    end_time = start_time + kw * T
    if start_time <= t < end_time:
        return A
    return 0


def rectangular_symmetrical_signal_function(t, A, T, kw, t1):
    start_time = t1 + T * int(t // T)
    end_time = start_time + kw * T
    if start_time <= t < end_time:
        return A
    start_time = end_time
    end_time = start_time + (T - kw * T)
    if start_time <= t < end_time:
        return -A
    return 0


def triangle_signal(A, T, t1, d, kw):
    f = 1000
    x = np.linspace(t1, t1 + d, int(f * d))
    y = np.zeros_like(x)

    C = range(int((t1 / T)), int((t1 + d) / T) + 1)

    for k in C:
        start_time = k * T + t1
        end_time = kw * T + k * T + t1

        mask_rise = (x >= start_time) & (x < end_time)
        y[mask_rise] = (A / (kw * T)) * (x[mask_rise] - k * T - t1)

        start_time = end_time
        end_time = T + k * T + t1
        mask_fall = (x >= start_time) & (x < end_time)
        y[mask_fall] = (-A / (T * (1 - kw))) * (x[mask_fall] - k * T - t1) + A / (1 - kw)

    return x, y


def triangle_signal_function(t, A, T, kw, t1):
    C = int((t - t1) // T)
    start_time = t1 + T * C
    end_time = start_time + kw * T
    if start_time <= t < end_time:
        return (A / (kw * T)) * (t - start_time)
    start_time = end_time
    end_time = start_time + (T - kw * T)
    if start_time <= t < end_time:
        return (-A / ((1 - kw) * T)) * (t - start_time) + A
    return 0


def unit_jump_function(t, A, ts):
    if t > ts:
        return A
    elif t == ts:
        return 0.5 * A
    return 0


def unit_impulse_function(t, A, ns):
    return A if t == ns else 0


def impulse_noise_function(t, A, p):
    return A if p > np.random.rand() else 0
