x_green = float(input("Xgreen: "))
x_red = float(input("Xnir: "))
x_nir = float(input("Xnir: "))


ndwi = (x_green - x_nir) / (x_green + x_nir)
ndvi = (x_nir - x_red) / (x_nir + x_red)

print("\nNDWI: ", ndwi)
print("NDVI: ", ndvi)