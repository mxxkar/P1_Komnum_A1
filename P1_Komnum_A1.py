import numpy as np
import matplotlib.pyplot as plt

persamaan = input("Program Bolzano untuk Persamaan f(x) = x^3 + 10 x^2 - 7 x - 196")
xl = float(input("Masukkan batas bawah : "))
xu = float(input("Masukkan batas atas : "))

def f(x):
    return (x*x*x) + (10*x*x) - (7*x) - 196

print("n          xl                xu              xr              f(xl)            f(xu)             f(xr)")
for i in range(0,301):
    xr = (xu+xl)/2
    print(i+1, "\t", format(xl,".5f"), "\t", format(xu,".5f"), "\t", format(xr, ".5f"), "\t", format(f(xl),".5f"), "\t", format(f(xu),".5f"), "\t", format(f(xr),".5f"))
        
    if f(xl)*f(xr)<0: xu=xr
    elif f(xl)*f(xr)>0: xl=xr
    elif f(xl)*f(xr)==0:
         xl = xr
         break
           
if i != 300 : print("Akar persamaannya adalah = ", format(xl, ".5f"))
elif i == 300: print ("Akar persamaan tidak dapat ditentukan dengan metode bolzano. Coba ubah nilai batas atas atau nilai batas bawah")

x = np.linspace(-5,10,100)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

plt.plot(x, f(x))
plt.grid()
plt.show()
