h=int(input("Ingrese la hora de llegada: "))
m=int(input("Ingrese el minuto de llegada: "))
t=int(input("Ingrese duración del evento: "))
minutos=int(t%60)
horas=(t-minutos)/60
hs=int(h+horas)
ms=int(m+minutos)
if hs>23 and ms>59:
    hs=hs-23
    ms=ms-60
if hs<24 and ms>59:
    hs=hs+1
    ms=ms-60
print("La hora de salida es: ", hs,":", ms)
