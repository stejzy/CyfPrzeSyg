import numpy as np
def uni_dist_noise(A, t1, d):
    f = 1000
    x = np.linspace(t1, t1+d, int(f * d))
    y = np.random.uniform(low=-A, high=A, size = len(x))
    return x, y

def normal_dist_noise(A, t1, d):
    f = 1000
    x = np.linspace(t1, t1+d, int(f * d))
    y = A * np.random.normal(loc=0, scale=1, size=len(x))
    return x, y

def sin_signal(A, T, t1, d):
    f = 1000
    x = np.linspace(t1, t1+d, int(f * d))
    y = A * np.sin((2*np.pi / T) * (x - t1))
    return x, y

def half_wave_rectified_sin_signal(A, T, t1, d):
    f = 1000
    x = np.linspace(t1, t1+d, int(f * d))
    y = 0.5 * A * ( np.sin((2*np.pi / T) * (x - t1)) + np.abs(np.sin((2* np.pi / T) * (x - t1))))
    return x, y

def full_wave_rectified_sin_signal(A, T, t1, d):
    f = 1000
    x = np.linspace(t1, t1+d, int(f * d))
    y = 0.5 * A * ( np.abs(np.sin((2* np.pi / T) * (x - t1))))
    return x, y

def rectangular_signal(A, T, t1, d, kw):
    f = 1000
    x = np.linspace(t1, t1+d, int(f * d))
    y = np.zeros_like(x)

    C = list(range(t1, t1 + d + 1))
    for k in C:
        start_time = k * T + t1
        end_time = kw * T + k * T + t1
        y[(x >= start_time) & (x < end_time)] = A

    return x, y

def rectangular_symmetrical_signal(A, T, t1, d, kw):
    f = 1000
    x = np.linspace(t1, t1+d, int(f * d))
    y = np.zeros_like(x)

    C = list(range(t1, t1 + d + 1))
    for k in C:
        start_time = k * T + t1
        end_time = kw * T + k * T + t1
        y[(x >= start_time) & (x < end_time)] = A

        start_time = kw * T + k * T + t1
        end_time = T + k * T + t1
        y[(x >= start_time) & (x < end_time)] = -A

    return x, y


def triangle_signal(A, T, t1, d, kw):
    f = 1000
    x = np.linspace(t1, t1 + d, int(f * d))
    y = np.zeros_like(x)

    C = list(range(int(t1), int(t1 + d) + 1))

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

def unit_jump(A, t1, d, ts):
    f = 1000
    if t1 < 0:
        x = np.linspace(t1, d, f * d)
    else:
        x = np.linspace(t1, t1 + d, int(f * d))

    x = np.linspace(t1,  d, f * d)
    y = np.zeros_like(x)

    y[x > ts] = A
    y[x == ts] = 0.5*A

    return x, y

def unit_impulse(A, n1, l, ns, f):
    x = np.arange(n1, n1 + l, 1/f)
    y = np.zeros_like(x)

    y[x == ns] = A

    return x, y