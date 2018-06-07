height = input("Ingrese el height: ")
while (height.isnumeric()):
    height = int(height)
    while height > 0:
        print(height * 'x')
        height -= 1
    height = input("Ingrese el height: ")
