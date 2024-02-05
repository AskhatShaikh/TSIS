def my_function(grams):
    ounces = grams / 28.3495231
    return ounces
grams = float(input("Enter the weight in grams: "))
print("Ounces:" , my_function(grams))