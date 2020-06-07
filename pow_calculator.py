num_1 = int(input('Introduce un número: '))
num_2 = int(input('Introduce otro número: '))

if num_1 > num_2:

    exp_1 = num_2 ** num_1
    print(f"Se aplicará la siguiente fórmula: {num_1}^{num_2}, dando como resultado {exp_1}")

else: 
    exp_2 = num_2 ** num_1
    print(f"Se aplicará la siguiente fórmula: {num_2}^{num_1}, dando como resultado {exp_2}")