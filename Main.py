import csv


#Listas globales para manejo de los datos de los archivos

Funcionarios = []
Clientes = []

Agencias = []
Aerolineas = []
Aviones = []
Rutas = []

Trips = []
Tripulacion = []

Vuelos = []
Destinos = []


AsignacionVuelos = []
TripulaVuela = []
ClientesVuelo = []

def eliminarRepetidos(lista,idIndex):

	sinRepetidos = []
	sinRepetidos.append(lista[0])
	
	
	for item in lista:
		estaRepetido = False
		newItem = item[idIndex]
		
		for elem in sinRepetidos:
			if elem[idIndex] == newItem:
				estaRepetido = True
		if not estaRepetido:
			sinRepetidos.append(item)
	return sinRepetidos
        


def limpiarListas():
	
	global Funcionarios
	global Clientes

	global Agencias
	global Aerolineas
	global Aviones
	global Rutas

	global Trips
	global Tripulacion

	global Vuelos
	global Destinos


	global AsignacionVuelos
	global TripulaVuela 
	global ClientesVuelo

	Funcionarios = eliminarRepetidos(Funcionarios,0)
	Clientes = eliminarRepetidos(Clientes,0)

	Agencias = eliminarRepetidos(Agencias,0)
	#Aerolineas = eliminarRepetidos(Aerolineas,1)
	#Aviones = eliminarRepetidos(Aviones,2)
	#Rutas = eliminarRepetidos(Rutas,3)

	Trips = eliminarRepetidos(Trips,0)
	#Tripulacion = eliminarRepetidos(Tripulacion,0)

	#Vuelos = eliminarRepetidos(Vuelos,0)
	Destinos = eliminarRepetidos(Destinos,0)


	#AsignacionVuelos = eliminarRepetidos(AsignacionVuelos,0)
	#TripulaVuela = eliminarRepetidos(TripulaVuela,0)
	#ClientesVuelo = eliminarRepetidos(ClientesVuelo,0)



def loadMemory():

	global Funcionarios
	global Clientes

	global Agencias
	global Aerolineas
	global Aviones
	global Rutas

	global Trips
	global Tripulacion

	global Vuelos
	global Destinos


	global AsignacionVuelos
	global TripulaVuela 
	global ClientesVuelo


	Funcionarios.extend(LeerArchivos("Funcionarios"))
	Clientes.extend(LeerArchivos("Clientes"))

	Agencias.extend(LeerArchivos("Agencias"))
	Aerolineas.extend(LeerArchivos("Aerolineas"))
	Aviones.extend(LeerArchivos("Aviones"))
	Rutas.extend(LeerArchivos("Rutas"))

	Trips.extend(LeerArchivos("Trip"))
	Tripulacion.extend(LeerArchivos("Tripulacion"))

	Vuelos.extend(LeerArchivos("Vuelos"))
	Destinos.extend(LeerArchivos("Destinos"))


	AsignacionVuelos.extend(LeerArchivos("Asignacion de Vuelos"))
	TripulaVuela.extend(LeerArchivos("TripulaVuela"))
	ClientesVuelo.extend(LeerArchivos("ClientesVuelo"))

	
	

	



def LeerColumna(FilePath,column): 
	ListaSalida=[]
	with open("ArchivosEntrada/"+FilePath+".txt", 'r') as csvfile: ##Abre el archivo como un csv, independiente del formato
		func_reader = csv.reader(csvfile, delimiter=';', quotechar='|') #Extrae las filas del csv con el separador indicado, en este caso ;
		
		for fila in func_reader:
			
			ListaSalida.append(fila[column]) # Guarda en la lista de salida los strings de la columna i
	return ListaSalida

def ValidarArchivo(FilePath,idPos):
		Ids = LeerColumna(FilePath, idPos)
		validate = sorted(set(Ids))
		Ids.sort()

		if Ids == validate:
				return True
		else:
				return False
		
def LeerArchivos(FilePath):
	ListaSalida=[]
	with open("ArchivosEntrada/"+FilePath+".txt", 'r') as csvfile:
		func_reader = csv.reader(csvfile, delimiter=';', quotechar='|')
		for row in func_reader:
			ListaSalida+=[row]
	return ListaSalida


def loginFuncionarios(idFuncionario,):
	ListaFuncionarios=LeerColumna("Funcionarios",0)
	ListaNombres=LeerColumna("Funcionarios",1)
	if idFuncionario in ListaFuncionarios:
		index = ListaFuncionarios.index(idFuncionario)
		print("Bienvenido(a), "+ ListaNombres[index])
		return True
	else:
		return False
	
def loginClientes(idCliente):
	ListaClientes=LeerColumna("Clientes",0)
	ListaNombres=LeerColumna("Clientes",1)
	if idCliente in ListaClientes:
		index = ListaClientes.index(idCliente)
		print("Bienvenido(a), "+ ListaNombres[index])
		return True
	else:
		return False
	

		
def  Main():

	# if not ValidarArchivo("Funcionarios",0):
	# 	print("Hay identificadores repetidos en el archivo de funcionarios")
	# if not ValidarArchivo("Clientes",0):
	# 	print("Hay identificadores repetidos en el archivo de clientes")
		
	
	
	#else:

	loadMemory()
	limpiarListas()
	
	
	while True:
		
		print("Que desea hacer:")
		print("1) Iniciar sesión como cliente") 
		print("2) Iniciar sesión como funcionario")
		print("3) Reportes")
		print("S) Salir del sistema")
		
		respuesta=input(": ")
		print("")
		
		if respuesta == "1":
			while True:

				nombreCliente = input("Digite su login, o presione S para salir: ")

				if nombreCliente.lower()=="s":
					
					break
				elif loginClientes(nombreCliente):
					LoopClientes()

				else:
					print("Usuario incorrecto. Ingrese nuevamente el usuario.")
					print("")

		if respuesta == "2":
			while True:

				nombreFunc = input("Digite su login, o presione S para salir: ")       
				if nombreFunc.lower()=="s":
					
					break
				elif loginFuncionarios(nombreFunc):
					LoopFuncionarios()

				else:
					print("Usuario incorrecto. Ingrese nuevamente el usuario.")
					print("")

		if respuesta == "3":
			loopReportes()
		if respuesta == "s" or respuesta == "S":
			break


def LoopEliminar():
	while True:
		print("Que desea eliminar:")
		print("1) Aviones")
		print("2) Rutas")
		print("3) Vuelos")		
		print("4) Clientes")
		print("5) Asignación de vuelos")
		print("S) Salir")

		respuesta=input(": ")
		print("")
		
		if respuesta == "1":

			print("Aviones que se pueden eliminar:")
			for i in Aviones:
				print(i[1]+" | "+i[2])
			
			aerolinea = input("Digite la aerolinea: ")
			avion = input("Digite la placa: ")
			for item in Aviones[:]:
				if item[1] == aerolinea and item[2] == avion:
					Aviones.remove(item)
					print("Avion eliminado.")
					print("")
				
		if respuesta == "2":
			pass
		if respuesta == "3":
			pass
		if respuesta == "4":
			pass
		if respuesta == "5":
			pass
		if respuesta == "S":
			break

def LoopFuncionarios():
	while True:
		
		print("Que desea consultar:")
		print("1) Eliminar aviones, rutas, vuelos, clientes o asignacion de vuelos")
		print("2) Aerolíneas de una agencia")
		print("3) Vuelos de una Aerolínea")		
		print("4) Rutas de un vuelo")
		print("5) Asignación de vuelos")
		print("6) Puestos disponibles")
		print("7) Puesto de un funcionario")
		print("8) Horas de una ruta")
		print("9) Rango de un funcionario")
		print("S) Salir")
		
		respuesta=input(": ")
		print("")
		
		if respuesta == "1":
			
			LoopEliminar()
			
			
		if respuesta == "2":
			pass
		if respuesta == "3":
			pass
		if respuesta == "4":
			pass
		if respuesta == "5":
			pass
		if respuesta == "6":
			pass
		if respuesta == "7":
			pass
		if respuesta == "8":
			pass
		if respuesta == "9":
			pass
		if respuesta == "S":
			break
	

def LoopClientes():
	while True:
		
		print("Que desea consultar:")
		print("1) Agencias de viajes")
		print("2) Aerolíneas de una agencia")
		print("3) Vuelos de una Aerolínea")		
		print("4) Rutas de un vuelo")
		print("5) Asignación de vuelos")
		print("6) Puestos disponibles")
		print("7) Puesto de un funcionario")
		print("8) Horas de una ruta")
		print("9) Rango de un funcionario")
		print("S) Salir")
		
		respuesta=input(": ")
		print("")
		
		if respuesta == "1":
			pass
		if respuesta == "2":
			pass
		if respuesta == "3":
			pass
		if respuesta == "4":
			pass
		if respuesta == "5":
			pass
		if respuesta == "6":
			pass
		if respuesta == "7":
			pass
		if respuesta == "8":
			pass
		if respuesta == "9":
			pass
		if respuesta == "S":
			break

def loopReportes():
	while True:
		
		print("Que desea consultar:")
		print("1) Agencias de viajes")
		print("2) Aerolíneas de una agencia")
		print("3) Vuelos de una Aerolínea")		
		print("4) Rutas de un vuelo")
		print("5) Asignación de vuelos")
		print("6) Puestos disponibles")
		print("7) Puesto de un funcionario")
		print("8) Horas de una ruta")
		print("9) Rango de un funcionario")
		print("S) Salir")
		
		respuesta=input(": ")
		print("")
		
		if respuesta == "1":			
			for item in Agencias:
				print(item[0] +" | "+item[1])
			print("")
				
		if respuesta == "2":
			agencia = input("Digite el codigo de la agencia: ")
			for item in Aerolineas:
				if item[0] == agencia:
					print(item[0]+" | "+item[1]+" | "+item[2])
			print("")
				
		if respuesta == "3":
			vuelos = input("Digite el codigo de la aerolinea: ")
			for item in Vuelos:
				if item[1] == vuelos:
					print(item[0]+" | "+item[1]+" | "+item[2]+" | "+item[3]+" | "+item[4]+" | "+item[5])
			print("")
		if respuesta == "4":
			rutas = input("Digite la matricula del avion: ")
			for item in Rutas:
				if item[2] == rutas:
					print(item[0]+" | "+item[1]+" | "+item[2]+" | "+item[3]+" | "+item[4]+" | "+item[5])
			print("")
		if respuesta == "5":
			asignacion = input("Digite la matricula del avion: ")
			for item in AsignacionVuelos:
				if item[0] == asignacion:
					print(item[0]+" | "+item[1]+" | "+item[2]+" | "+item[3]+" | "+item[4])
			print("")
		if respuesta == "6":
			disponibles = input("Digite la matricula del avion: ")
			for item in Vuelos:
				if item[2] == rutas:
					print(item[2]+" | "+item[4])
			print("")
		if respuesta == "7":
			funcionarios = input("Digite el codigo del funcionario: ")
			for item in Funcionarios:
				if item[0] == funcionarios:
					print(item[1]+" | "+item[2])
			print("")
		if respuesta == "8":
			horas = input("Digite la matricula del avion: ")
			for item in Rutas:
				if item[2] == horas:
					print(item[0]+" | "+item[1]+" | "+item[2]+" | "+item[3]+" | "+item[4]+" | "+item[5]+" | "+item[6])
			print("")
		if respuesta == "9":
			rango = input("Digite el codigo del funcionario: ")
			for item in Funcionarios:
				if item[0] == rango:
					print(item[1]+" | "+item[2])
		if respuesta == "S":
			break
	
        

		
Main()
