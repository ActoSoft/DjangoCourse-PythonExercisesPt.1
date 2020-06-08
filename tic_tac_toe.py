from random import randint

print('''BIENVENIDO AL JUEGO DE PIEDRA PAPEL O TIJERA''')




selection = 'Si'

while selection == 'Si':

    usuario = input('Elije una opción Piedra, Papel o Tijera: ')
    
    num_rand = randint(1,100)

    if num_rand > 1 and num_rand < 33:
        opcion_1 = 'Tijera'
        print(f'La cpu ha elegido {opcion_1}')
        if usuario == 'Tijera': 
            print('¡Es un empate!')
        elif usuario == 'Piedra': 
            print('Felicitaciones, has ganado')
        else: 
            print('Has perdido ;(, vuelve a intentarlo')
        

    elif num_rand > 33 and num_rand < 66:
        opcion_2 = 'Piedra'
        print(f'La cpu ha elegido {opcion_2}')
        if usuario == 'Tijera': 
            print('Has perdido ;(, vuelve a intentarlo')
        elif usuario == 'Papel': 
            print('Felicitaciones, has ganado')
        else: 
            print('¡Es un empate!')
    else: 
        opcion_3 = 'Papel'
        print(f'La cpu ha elegido {opcion_3}')
        if usuario == 'Tijera': 
            print('Felicitaciones, has ganado')
        elif usuario == 'Piedra': 
            print('Has perdido ;(, vuelve a intentarlo')
        else: 
            print('¡Es un empate!')
        
        
    
    selection = input('¿Quieres volver a jugar?\n [Si/No] ')

print('Hasta la vista baby!')