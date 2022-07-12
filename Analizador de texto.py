
texto = input("porfavor ingrese un texto: ").lower()
letras = []

letras.append(input("porfavor escribe una letra: ").lower())
letras.append(input("porfavor escribe una segunda letra: ").lower())
letras.append(input("porfavor escribe una ultima letras: ").lower())

print("\n")
print("la cantidad de letras que contiene el texto es: ")
cantidad_letras1 = texto.count(letras[0])
cantidad_letras2 = texto.count(letras[1])
cantidad_letras3 = texto.count(letras[2])
print(f"hemos encontado la letra '{letras[0]}' repetida {cantidad_letras1} veces")
print(f"hemos encontado la letra '{letras[1]}' repetida {cantidad_letras2} veces")
print(f"hemos encontado la letra '{letras[2]}' repetida {cantidad_letras3} veces")
print("\n")
print(f"el texto elegido tiene '{len(texto)}' letras")
print("\n")

cantidad_palabras = texto.split()
print(f"la cantidad de palabras que contiene el texto es '{len(cantidad_palabras)}' ")
print("\n")
letra_inicio = texto[0]
letra_fin = texto[-1]
print(f"la primer letra del texto es '{letra_inicio}' y la ultima letra es '{letra_fin}' ")
print("\n")
busqueda_palabra = "pajarito" in texto
dic = {True:"si", False:"no"}
print(f"la palabra pajaro aparece en el texto? {dic[busqueda_palabra]}")




