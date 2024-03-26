import math 
import numpy as np
import matplotlib.pyplot as plt

iterasi = 10
a = 5
b = -5
c = 6
d = -2
x = np.linspace(-10, 10, 400)
fx = a*x**3 + b*x**2 + c*x + d
fxl = np.zeros(iterasi+1, dtype=float)
fxu = np.zeros(iterasi+1, dtype=float)
fxr = np.zeros(iterasi+1, dtype=float)
y = np.zeros_like(x)

coef = [a,b,c,d]
akar = np.roots(coef)
print("Akar-akar dari persamaan tersebut adalah:")
for i, root in enumerate(akar):
    print(f"Akar-{i+1}: {root}")

eksak = akar[2].real
x2 = eksak
xl = np.zeros(iterasi+1, dtype=float)
xu = np.zeros(iterasi+1, dtype=float)
xr = np.zeros(iterasi+1, dtype=float)
epsT = np.zeros(iterasi+1, dtype=float)
epsA = np.zeros(iterasi+1, dtype=float)
# Nilai awal xl dan xu
xl[0] = 0
xu[0] = 1

# Iterasi menggunakan metode bisection
for i in range(iterasi):
    fxl[i] = a*xl[i]**3 + b*xl[i]**2 + c*xl[i] + d
    fxu[i] = a*xu[i]**3 + b*xu[i]**2 + c*xu[i] + d
    xr[i] = xl[i] - fxl[i]*((xu[i]-xl[i])/(fxu[i]-fxl[i]))
    fxr[i] = a*xr[i]**3 + b*xr[i]**2 + c*xr[i] + d
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
    if epsA[i] < 10 and epsA[i] != 0:
        break
    #xr[i+1] = xr[i]

for i in range(iterasi+1):
    print("Iterasi {}: xl = {}, xu = {}, xr = {}, epsT = {}, epsA = {}".format(i+1, xl[i], xu[i], xr[i], epsT[i],epsA[i]))
    #print (fxl[i],"pro",fxr[i])

print("Akar-akar dari persamaan kuadrat adalah:", akar[0], "dan", akar[1],"serta",akar[2],eksak)

# Plot grafik
plt.plot(x, fx, label='y = 5x^3 - 5x^2 + 6x + 2')
plt.axhline(0, color='black', linewidth=0.5)  # Menambahkan garis horizontal di y = 0

# Menambahkan garis vertikal di lokasi akar yang ditemukan
for root in akar:
    plt.axvline(root.real, color='red', linestyle='--', linewidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik y = 5x^3 - 5x^2 + 6x + 2 dan y = 0')

plt.grid(True)
plt.legend()
plt.show()
