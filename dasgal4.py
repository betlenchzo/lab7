import math
shape=input("Dvrs oruul (square, triangle, circle, rectangle)=")
if shape=="square":
    a=float(input("taliin urt oruul=" ))
    s=(a**2)
elif shape=="rectangle":
    w=float(input("tegsh untsugtiin urguniig oruul="))
    h=float(input("tegsh untsugtiin urt oruul="))
    s=w*h
elif shape =="circle":
    r=float(input("radius oruul="))
    s=math.pi*(r**2)
elif shape=="triangle":
    b=float(input("suuriin urt="))
    x=float(input("hajuugiin urt="))
    s=(b*x)/2
else:
    print("buruu dvrs oruulsan baina.")
print(s)
