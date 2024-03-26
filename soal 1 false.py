import math 
import numpy as np
import matplotlib.pyplot as plt

def quadratic(a, b, c):
    diskriminan = b**2 - 4*a*c
    if diskriminan > 0:
        x1 = (-b + math.sqrt(diskriminan)) / (2*a)
        x2 = (-b - math.sqrt(diskriminan)) / (2*a)
        return x1, x2
    elif diskriminan == 0:
        x = -b / (2*a)
        return x, x
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(abs(diskriminan)) / (2*a)
        return (real_part + imaginary_part*1j), (real_part - imaginary_part*1j)

iterasi = 7
a = -0.5
b = 2.5
c = 4.5
x = np.linspace(-10, 10, 400)
fx = a*x**2 + b*x + c
fxl = np.zeros(iterasi+1, dtype=float)
fxu = np.zeros(iterasi+1, dtype=float)
fxr = np.zeros(iterasi+1, dtype=float)
y = np.zeros_like(x)
x1, x2 = quadratic(a, b, c)
eksak = x2

xl = np.zeros(iterasi+1, dtype=float)
xu = np.zeros(iterasi+1, dtype=float)
xr = np.zeros(iterasi+1, dtype=float)
epsT = np.zeros(iterasi+1, dtype=float)
epsA = np.zeros(iterasi+1, dtype=float)

xl[0] = 5
xu[0] = 10

for i in range(iterasi):
    fxl[i] = a*xl[i]**2 + b*xl[i] + c
    fxu[i] = a*xu[i]**2 + b*xu[i] + c
    xr[i] = xl[i] - fxl[i]*((xu[i]-xl[i])/(fxu[i]-fxl[i]))
    fxr[i] = a*xr[i]**2 + b*xr[i] + c
    test = fxr[i]*fxl[i]
    if test < 0:
        xu[i+1] = xr[i]
        xl[i+1] = xl[i]
    elif test > 0:
        xl[i+1] = xr[i]
        xu[i+1] = xu[i]
    else:
        break
    epsT[i] = abs((eksak - xr[i])) * 100
    epsA[i] = abs((xr[i] - xr[i-1]) / xr[i]) * 100 if i != 0 else 0

# Iterasi menggunakan metode bisection
    #xr[i+1] = xr[i]

for i in range(iterasi+1):
    print("Iterasi {}: xl = {}, xu = {}, xr = {}, epsT = {}, epsA = {}".format(i+1, xl[i], xu[i], xr[i], epsT[i],epsA[i]))

print("Akar-akar dari persamaan kuadrat adalah:", x1, "dan", x2)

# Plot grafik
plt.plot(x, fx, label='y = -0.5x^2 + 2.5x + 4.5')
plt.plot(x, y, label='y = 0') 

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik y = -0.5x^2 + 2.5x + 4.5 dan y = 0')

plt.grid(True)
plt.legend()
plt.show()