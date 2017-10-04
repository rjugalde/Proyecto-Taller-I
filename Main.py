import csv

def LeerColumna(FilePath,column): 
	ListaSalida=[]
	with open("ArchivosEntrada/"+FilePath+".txt", 'r') as csvfile: ##Abre el archivo como un csv, independiente del formato
		func_reader = csv.reader(csvfile, delimiter=';', quotechar='|') #Extrae las filas del csv con el separador indicado, en este caso ;
		
		for fila in func_reader:
			print(fila)
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
		print("Es usted un:")
		print("1) cliente") 
		print("2) funcionario") 
		respuesta=input(": ")
		if respuesta == "1":
			while True:

				nombreCliente = input("Digite su login, o presione S para salir: ")

				if nombreCliente.lower()=="s":
					print("Saliendo...")
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
					print("Saliendo...")
					break
				elif loginFuncionarios(nombreFunc):
					LoopFuncionarios()

				else:
					print("Usuario incorrecto. Ingrese nuevamente el usuario.")
					print("")




def LoopFuncionarios():
	ListaFuncionarios=LeerArchivos("Funcionarios")
	while True:
		pass
	

def LoopClientes():
	while True:
		pass


		
Main()
