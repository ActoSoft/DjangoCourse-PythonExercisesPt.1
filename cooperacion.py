
selection = 'Si'

names = []

donativos = []

while selection == 'Si':
    
	name = input('Ingresa el nombre de la persona: ')

	names.append(name.capitalize())

	donativo = float(input('Ingresa el monto que donó: '))

	donativos.append(donativo)
	
	selection = input('¿Deseas ingresar a otra persona [Si/No]? ')
	
	
if len(names) > 1:
	total_donacion = float(sum(donativos))

	print(f'La suma total de la cooperación es de: {total_donacion:.2f}')

	total_names = len(names)

	mean = total_donacion/total_names

	print(f'El promedio de la cooperación es de: {mean:.2f}')

	print(f'La suma total de las personas que cooperaron es de: {total_names}')

	print(f'La primera persona en cooperar fue {names[0]} con la cantidad de {donativos[0]:.2f}')

	print(f'La última persona en cooperar fue {names[-1]} con la cantidad de {donativos[-1]:.2f}')

	minima = donativos.index(min(donativos))
	print(f'{names[minima]:} fue la persona que menos cooperó con una cantidad de {donativos[minima]:.2f} dólares')

	maxima = donativos.index(max(donativos))
	print(f'{names[maxima]} fue la persona que más cooperó con una cantidad de  {donativos[maxima]:.2f} dólares')


else: 
	print (f"Solo una persona ha cooperado, se muestra el siguiente apartado:"
	 f" {names[0]} ha aportado una cantidad de {donativos[0]}"
	"")

