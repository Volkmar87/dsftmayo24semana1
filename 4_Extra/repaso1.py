# %%
mi_dic = {} # mi_dic = dict()

mi_dic['saludo'] = "hola"
mi_dic["direccion"] = ["calle de arriba", 34, True]
mi_dic['telefono'] = 12345

print(mi_dic)


otro = {}

mi_dic2 = {
    "saludo" : "hola",
    "despedida" : "adiós",
    "numero" : 7,  
    "otro_dic" : otro
}

# %%
mi_dic

# %%
mi_dic['notas'] = {
    'mates': 10,
    'lengua': 10
}

# %%
mi_dic

# %%
for clave in mi_dic:
    print(clave)
    print("el valor de la clave", clave, "es", mi_dic[clave])

# %%
mi_dic.get('silla', "No está silla")

# %%
3/0

# %%
try:
   
    mi_dic['silla']
    l = [3,4,5]
    l[8]
    3/0
    
except (KeyError, IndexError):
    print("no hay silla o te has salido de los índices")
except ZeroDivisionError:
    print("no se divide entre cero")
except:
    print("fallo")

# %%
l = [4,5,6]
l[8]

# %%
for valores in mi_dic.values():
    print(valores)

# %%
mi_dic.items()

# %%
for mi_tupla in mi_dic.items():
    print("clave", mi_tupla[0], "valor", mi_tupla[1])

# %%
mi_dic.keys()

# %%
mi_dic.values()

# %%
mi_set = {"rosas", "rosas", "tulipanes", "girasoles", True, (1,2,3)}

# %%
set([1,2,3,3,3,3,3])

# %%
mi_lista = [1,2,3,3,3,3,3,3]
otro_set = set(mi_lista)
print(mi_lista)

# %%
d = {'saludo': 'hola',
     'numero': 5}
set(d)

# %%
d2 = set("hola")
d2

# %%
len(d2)

# %%
def suma(num1, num2):
    return num1+num2

otra_igual = suma
otra_igual(2,3)



# %%
"hola" == "hola"

# %%
[1,2,3] is [1,2,3]

# %%
[1,2,3] == [1,2,3]

# %%
n1 = 70000000000000000000000000000000000000000000000000000000
n2 = 70000000000000000000000000000000000000000000000000000000
n1 is n2

# %%
def comprar_lavadora(**kwargs):
    print(kwargs)
    capacidad = kwargs.get("capacidad", "8 kg")
    return capacidad

print(comprar_lavadora(color="azul", version = 20.24, capacidad = "11 kg"))
    
    
    

# %%
def mega_mix(*args, **kwargs):
    print(args)
    print(kwargs)

mega_mix(2,3,4,5,numero = 6, color = "rojo", version = 2.0)

# %%
# 0! = 1
# 1! = 1 x 0! = 1
# 2! = 2 * 1! = 2 x 1 x 0!
# 3! = 3 x 2! = 3 x 2 x 1
# 4! 4 x 3 x2 x1 

# %%
def calcula_fact(numero):
    resultado = 1
    
    for n in range(numero):
        resultado = resultado * (n+1)
    return resultado

calcula_fact(5)

# %%
def calcula_fact_recursivo(numero):
    if numero == 0:
        return 1
    else:
        return numero * calcula_fact_recursivo(numero-1)
    
    
calcula_fact_recursivo(5)    

# %% [markdown]
# Una empresa usa dos listas  para guardar la información de sus empleados. Una lista guarda el nombre del empleado y la otra guarda su salario. Escribe un programa que cree esas dos listas originalmente vacías y que a través de un menú pueda hacer lo siguiente:
#     
# Inserta 1 para añadir un nuevo empleado y su salario
# 
# Inserta 2 para imprimir los nombres y salarios de todos los empleados
# 
# Inserta 3 para mostrar el número de empleados
# 
# Inserta 4 para imprimir los nombres de los empleados con sueldos superiores a 400000
# 
# Inserta 5 para subir un 5% los sueldos por debajo de 10000
# 
# Inserta 6 para mostrar el total de todos los salarios
# 
# Inserta 7 para salir del programa

# %%
l1 = [7,8,9]
l2 = ["a", "b", "c"]

for indice in range(len(l1)):
    if l1[indice] == 8:
        print(l2[indice])
        


# %%
# una lista para nombres y una lista para sueldos
lista_nombres = []
lista_salarios = []

# insertamos nuevos nombre-salario
def nuevo_empleado(nombre, salario):
    lista_nombres.append(nombre)
    lista_salarios.append(salario)

# imprimimos todos los nombre-salario
def imprime_empleados():
    for posicion in range(len(lista_nombres)):
        print("Nombre: ", lista_nombres[posicion], end = " ")
        print("Sueldo: ", lista_salarios[posicion], end = "\n")

# imprimir cantidad de empleados
def imprime_cantidad_empleados():
    print("Cantidad de empleados: ", len(lista_nombres))

# imprimir empleados con salarios mayores de 40 000 dolares
def sueldos_altos():

    print("Sueldos mayores de 40000:")

    # recorro la lista de sueldos
    for posicion in range(len(lista_nombres)):

        # si ese sueldo es mayor de 40 000, cojo el nombre
        if lista_salarios[posicion] > 40000:
            print(lista_nombres[posicion])


# dar un aumento de un 10% a los sueldos menores de 10 000
def aumento():
    # recorro la lista de sueldos
    for posicion in range(len(lista_salarios)):
        if lista_salarios[posicion] < 10000:
            lista_salarios[posicion] = lista_salarios[posicion] * 1.1

    print("¡Los sueldos bajos se han subido!")




# imprimir la suma total de todos los sueldos
def masa_salarial():
    total = sum(lista_salarios)
    print("Suma de todos los sueldos: ", total)

# menu
def menu():

    mensaje_inicial = """

¡Bienvenido!

Inserta 1 para añadir un nuevo empleado y su salario
Inserta 2 para imprimir los nombres y salarios de todos los empleados
Inserta 3 para mostrar el número de empleados
Inserta 4 para imprimir los nombres de los empleados con sueldos superiores a 400000
Inserta 5 para subir un 5% los sueldos por debajo de 10000
Inserta 6 para mostrar el total de todos los salarios            
Inserta 7 para salir del programa

    """
    
    print(mensaje_inicial)

    opcion = int(input("Inserta option: "))
    while opcion != 7:
        if opcion == 1:
            nombre = input("Nombre de empleado: ")
            salario = int(input("Salario: "))

            nuevo_empleado(nombre, salario)

        elif opcion == 2:
            imprime_empleados()

        elif opcion == 3:
            imprime_cantidad_empleados()

        elif opcion == 4:
            sueldos_altos()

        elif opcion == 5:
            aumento()

        elif opcion == 6:
            masa_salarial()

        print() # nueva linea
        opcion = int(input("Inserta opcion: "))

    print("¡Gracias por usar el programa!")
    
    # ejecutamos el programa
menu()          

# %%
int("7.2") #  "7.2" --> 7.2 --> 7

# %%
int(float("7.2"))

# %%
int(float("5.3"))

# %%
int(7.9)

# %%
class muneca:
    marca = "Famosa"
    
    def __init__(self, cabello, tamano, accesorios, nombre, asusta= True):
        self.cabello = cabello
        self.accesorios = accesorios
        self.nombre = nombre
        self.asusta = asusta
        self.mi_tamano = tamano
        
    def imprime_color_cabello(self):
        print("la muñeca", self.nombre, "tiene el cabello", self.cabello)
        
    def come_comida(self, comida):
        print("la muñeca", self.nombre, "está comiendo", comida)
        
muneca1 = muneca(accesorios="diadema", cabello ="rubia", tamano="grande", nombre= "Rosa")
print(muneca1.mi_tamano)
muneca1.__dict__

muneca1.imprime_color_cabello()
muneca1.come_comida("macarrones")
muneca.marca
muneca1.marca

# %%
mi_dic

# %%
def imprime_dic(**kwargs):
    print(kwargs)
    
imprime_dic(**mi_dic) 

# %%
def registro_de_sillas(**kwargs):
    
    return kwargs.get("material", "madera")

registro_de_sillas(peso = 10, brilla = False)

# %%
def busca_args(*args):
    if len(args) > 2:
        raise Exception("Esto no vale, lo siento!!")
    else:
        return args[0]
    
busca_args(8,9)
    


