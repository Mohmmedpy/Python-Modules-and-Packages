from my_package.calc_utils import sq,cu
from my_package.weather_utils import today_weather

x=int(input("choose 1 or 2: "))
if x==1:
    y=float(input("num: "))
    print("the square for your num is",sq(y))
    print("the cube for your num is",cu(y))
elif x==2:
    z=input("city: ")
    print(today_weather(z))



    