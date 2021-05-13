temperatura = float(input("ingrese la temperatura:"))
escala = input("ingrese escala c o f:")

# temp_f = (temperatura - 32) * 0,55556
# temp_c = (temperatura * 0,55556) + 32

if(escala == "f"):
    print("la temp es :", (temperatura - 32) * 32 )
elif(escala == "c"):
    print("la temp en F es :", (temperatura - 5/9) + 32)


print("fin")