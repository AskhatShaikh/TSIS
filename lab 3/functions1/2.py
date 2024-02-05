def FarenheitToCelcius(F):
    C = (5/9) * (F - 32)
    return C
F = int(input("F: "))
print("C:",FarenheitToCelcius(F))