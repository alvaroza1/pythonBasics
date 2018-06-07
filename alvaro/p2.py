while True:
    num_1 = input("Ingrese el primero numero: ")
    num_2 = input("Ingrese el segundo numero: ")
    if(num_1.isnumeric() or num_2.isnumeric()):
        num_1 = int(num_1)
        num_2 = int(num_2)
        if(num_1 + num_2 > 10):
            break
        else:
            print("Suma: {}".format( num_1 + num_2))
    else:
        break
