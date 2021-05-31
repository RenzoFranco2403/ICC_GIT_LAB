print("Quinceavo Ejercicio:")
print("15850 decimal a sistema hexadecimal")

Num = 15850

Re1 = Num % 16
Ree1 = Num // 16

Re2 = Ree1 % 16
Ree2 = Ree1 // 16

Re3 = Ree2 % 16
Ree3 = Ree2 // 16

Re4 = Ree3 % 16
Ree4 = Ree3 // 16

if (Re4 < 0):
    print(0)

elif (Re4 <= 1):
    print(Re4, end=""),
else:
    if (Re4 < 10):
        print(Re4, end=""),
if (Re4 == 10):
    print("A", end=""),
if (Re4 == 11):
    print("B", end=""),
if (Re4 == 12):
    print("C", end=""),
if (Re4 == 13):
    print("D", end=""),
if (Re4 == 14):
    print("E", end=""),
if (Re4 == 15):
    print("F", end=""),

if (Re3 < 0):
    print(0)
elif (Re3 <= 1):
    print(Re3, end="")
else:
    if (Re3 < 10):
        print(Re3, end=""),
if (Re3 == 10):
    print("A", end=""),
if (Re3 == 11):
    print("B", end=""),
if (Re3 == 12):
    print("C", end=""),
if (Re3 == 13):
    print("D", end=""),
if (Re3 == 14):
    print("E", end=""),
if (Re3 == 15):
    print("F", end=""),

if (Re2 < 0):
    print(0)
elif (Re2 <= 1):
    print(Re2, end=""),
else:
    if (Re2 < 10):
        print(Re2, end=""),
if (Re2 == 10):
    print("A", end=""),
if (Re2 == 11):
    print("B", end=""),
if (Re2 == 12):
    print("C", end=""),
if (Re2 == 13):
    print("D", end=""),
if (Re2 == 14):
    print("E", end=""),
if (Re2 == 15):
    print("F", end=""),

if (Re1 < 0):
    print(0)

elif (Re1 <= 1):
    print(Re1, end="")

else:
    if (Re1 < 10):
        print(Re1, end=""),
if (Re1 == 10):
    print("A", end=""),
if (Re1 == 11):
    print("B", end=""),
if (Re1 == 12):
    print("C", end=""),
if (Re1 == 13):
    print("D", end=""),
if (Re1 == 14):
    print("E", end=""),
if (Re1 == 15):
    print("F", end=""),