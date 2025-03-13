import numpy as np
# def uni_dist_noise(A, t1, d):
#     f = 1000
#     x = np.linspace(t1, t1+d, int(f * d))
#     y = np.random.uniform(low=-A, high=A, size = len(x))
#     return x, y

def uniform_dist_noise_function(t, A):
    return np.random.uniform(-A, A)

# def normal_dist_noise(A, t1, d):
#     f = 1000
#     x = np.linspace(t1, t1+d, int(f * d))
#     y = A * np.random.normal(loc=0, scale=1, size=len(x))
#     return x, y

def normal_dist_noise_function(t, A):
    return A * np.random.normal(loc=0, scale=1)

# def sin_signal(A, T, t1, d):
#     f = 1000
#     x = np.linspace(t1, t1+d, int(f * d))
#     y = A * np.sin((2*np.pi / T) * (x - t1))
#     return x, y

def sin_signal_function(t, A, T):
    return A * np.sin((2 * np.pi / T) * (t))

# def half_wave_rectified_sin_signal(A, T, t1, d):
#     f = 1000
#     x = np.linspace(t1, t1+d, int(f * d))
#     y = 0.5 * A * ( np.sin((2*np.pi / T) * (x - t1)) + np.abs(np.sin((2* np.pi / T) * (x - t1))))
#     return x, y

def half_wave_rectified_sin_signal_function(t, A, T):
    return 0.5 * A * (np.sin((2 * np.pi / T) * (t)) + np.abs(np.sin((2 * np.pi / T) * (t))))


# def full_wave_rectified_sin_signal(A, T, t1, d):
#     f = 1000
#     x = np.linspace(t1, t1+d, int(f * d))
#     y = 0.5 * A * ( np.abs(np.sin((2* np.pi / T) * (x - t1))))
#     return x, y

def full_wave_rectified_sin_signal_function(t, A, T):
    return 0.5 * A * np.abs(np.sin((2 * np.pi / T) * (t)))

# def rectangular_signal(A, T, t1, d, kw):
#     f = 1000
#     x = np.linspace(t1, t1+d, int(f * d))
#     y = np.zeros_like(x)
#
#     C = list(range(t1, t1 + d + 1))
#     for k in C:
#         start_time = k * T + t1
#         end_time = kw * T + k * T + t1
#         y[(x >= start_time) & (x < end_time)] = A
#
#     return x, y

def rectangular_signal_function(t, A, T, kw, t1):
    start_time = t1 + T * int(t // T)
    end_time = start_time + kw * T
    if start_time <= t < end_time:
        return A
    return 0

# def rectangular_symmetrical_signal(A, T, t1, d, kw):
#     f = 1000
#     x = np.linspace(t1, t1+d, int(f * d))
#     y = np.zeros_like(x)
#
#     C = list(range(t1, t1 + d + 1))
#     for k in C:
#         start_time = k * T + t1
#         end_time = kw * T + k * T + t1
#         y[(x >= start_time) & (x < end_time)] = A
#
#         start_time = kw * T + k * T + t1
#         end_time = T + k * T + t1
#         y[(x >= start_time) & (x < end_time)] = -A
#
#     return x, y

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


# def triangle_signal(A, T, t1, d, kw):
#     f = 1000
#     x = np.linspace(t1, t1 + d, int(f * d))
#     y = np.zeros_like(x)
#
#     C = list(range(int(t1), int(t1 + d) + 1))
#
#     for k in C:
#         start_time = k * T + t1
#         end_time = kw * T + k * T + t1
#
#         mask_rise = (x >= start_time) & (x < end_time)
#         y[mask_rise] = (A / (kw * T)) * (x[mask_rise] - k * T - t1)
#
#         start_time = end_time
#         end_time = T + k * T + t1
#         mask_fall = (x >= start_time) & (x < end_time)
#         y[mask_fall] = (-A / (T * (1 - kw))) * (x[mask_fall] - k * T - t1) + A / (1 - kw)
#
#     return x, y

def triangle_signal_function(t, A, T, kw, t1):
    C = int((t - t1) // T)
    start_time = t1 + T * C
    end_time = start_time + kw * T
    if start_time <= t < end_time:
        return (A / (kw * T)) * (t - start_time)
    start_time = end_time
    end_time = start_time + (T - kw * T)
    if start_time <= t < end_time:
        return (-A / ((1 - kw) * T)) * (t - start_time) + A / (1 - kw)
    return 0

# def unit_jump(A, t1, d, ts):
#     f = 1000
#     if t1 < 0:
#         x = np.linspace(t1, d, f * d)
#     else:
#         x = np.linspace(t1, t1 + d, int(f * d))
#
#     x = np.linspace(t1,  d, f * d)
#     y = np.zeros_like(x)
#
#     y[x > ts] = A
#     y[x == ts] = 0.5*A
#
#     return x, y

def unit_jump_function(t, A, ts):
    if t > ts:
        return A
    elif t == ts:
        return 0.5 * A
    return 0

# def unit_impulse(A, n1, l, ns, f):
#     x = np.arange(n1, n1 + l, 1/f)
#     y = np.zeros_like(x)
#
#     y[x == ns] = A
#
#     return x, y

def unit_impulse_function(t, A, ns):
    return A if t == ns else 0

# def impulse_noise(A, t1, d, f, p):
#     x = np.arange(t1, t1 + d, 1/f)
#     y = np.zeros_like(x)
#
#     for i in range(len(x)):
#         if p > np.random.rand():
#             y[i] = A
#
#     return x, y

def impulse_noise_function(t, A, p):
    return A if p > np.random.rand() else 0