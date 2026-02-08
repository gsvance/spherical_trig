import numpy as np
import matplotlib.pyplot as plt

def sin(x):
    return np.sin(np.radians(x))

def cos(x):
    return np.cos(np.radians(x))

def tan(x):
    return np.tan(np.radians(x))

def arcsin(x):
    return np.degrees(np.arcsin(x))

def arccos(x):
    return np.degrees(np.arccos(x))

def arctan(x):
    return np.degrees(np.arctan(x))

def hav(x):
    return np.sin(np.radians(x/2.))**2

def archav(x):
    return np.degrees(2 * np.arcsin(np.sqrt(x)))

def deg(d, m=0, s=0):
    return np.sign(d) * (abs(d) + m/60. + s/3600.)

def dm(deg):
    sign = int(np.sign(deg))
    d = int(abs(deg))
    m = 60 * (abs(deg) - d)
    return sign * d, m

def dms(deg):
    sign = int(np.sign(deg))
    d = int(abs(deg))
    m = int(60 * (abs(deg) - d))
    s = 3600 * (abs(deg) - d - m/60.)
    return sign * d, m, s

def comp(x):
    return 90 - x

def linethru(xp, yp, slope, reach=1000):
    if slope == 'v':
        x = xp * np.ones(2)
        y = np.array([yp-reach, yp+reach])
    else:
        xreach = reach / np.sqrt(1 + slope**2)
        x = np.array([xp-xreach, xp+xreach])
        y = slope * (x - xp) + yp
    plt.plot(x, y)

def circlearound(xc, yc, radius):
    t = np.linspace(0, 2*pi, 1001)
    x = xc + radius * cos(t)
    y = yc + radius * sin(t)
    plt.plot(x, y)

