from math import pi
def volume(radius):
    volume = 4/3*pi*(radius**3)
    return volume

radius = int(input("Raduis:"))
print("Volume:", volume(radius))