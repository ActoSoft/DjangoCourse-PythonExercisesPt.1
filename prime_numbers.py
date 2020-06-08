'''NÚMEROS PRIMOS '''
num_primos=[]
for num in range(100, 200):
    if num > 1:
        if num == 2 or num == 3 or num == 5 or num == 7 :
            print(f'{num} es un número primo')
            num_primos.append(num)
        
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
            print(f'{num} es un número primo')
            num_primos.append(num)

print('La suma de los números primos es de: ',len(num_primos))
            

