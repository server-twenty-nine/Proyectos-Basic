


#for i in range(8):
 
 #print("imprimo", i*4)

#for n in range (57,78):
 
 #   n+=3
  #  print("imprimo", n)
for i in range(81,57,-3):
    print(i)

print("-----")
cont=4
while cont < 36:
    print(cont)
    cont=cont+4

    print("-----")
cont=81
while cont > 57 :
    print(cont)
    cont=cont-3

    cont=4
sum=0
while cont<36:
    sum=sum+cont
    print(cont)
    cont=cont+4
print("la suma es:",sum)
print(((4+32)/2)*8 )


'''
mensaje : "Hoy es viernes, y la clase Empieza de 7:30 a 10:00 pm"
- Contar cuantas veces se usa la letra e
- Reemplazar pm por PM
- Calcular la longitud de la cadena
- Convertir todo a Mayúscula
'''

mensaje = "Hoy es viernes y la clase Empieza de 7:30 a 10:00 pm"

#1
print(mensaje.count("e"))
#2
print(mensaje.replace("pm","PM"))
#3
print(len(mensaje))
#4
print(mensaje.upper())

"""
Ejercicio 3
   En la tupla siguiente :
   datos = (15,16,17,18,19,20)
   se pide calcular la longitud la tupla y el promedio
   del primer y ultimo elemento de la tupla
   tupla =(15,16,17,18,19,20)
lont = int(len(tuple))
primi = tupla[-lont]
ulti =tupla[lont-1]

prom = int(ulti+primi/2)
print("primer elemento es :", primi)
print("ultimo  elemento es :", ulti)
print("el promedio de los elemento es :", prom)
"""



'''
Ejercicio : En la tupla dada,

mi_tupla = (10,20,30,40,50,60,70)

a) mostrar los valores  usando slice:
- (10,30,50)
- (50,)
- (40,50,60)
- (60, 70)

b) recorrer la tupla usando un for
y mostrar todos los valores a excepcion del 40 y 70

'''
"""""
mi_tupla = (10,20,30,40,50,60,70)
print( mi_tupla[1:50:20])
"""
"""
 Dado el siguiente conjunto de datos
 DNI , NOMBRE , APELLIDO PATERNO
 -------------------------------
 001 , JAIME , GOMEZ
 002 , MARIA, GUZMAN
 003 , PEDRO , FLORES
  Agregar a  ROCIO PEREZ con DNI 004
 Modificar a JAIME GOMEZ por JAIME GALVEZ
"""
"""""
nombre = {"001":"MARIA, GUZMAN"}
def rest (s1,s2,w3=0):
    rpt= s1+s2+w3
    return rpt
"""
class Instituto:
    def __init__(self, nombre, telefono, sede, direccion, ruc):
        self.nombre = nombre
        self.telefono = telefono
        self.sede = sede
        self.direccion = direccion 
        self.ruc= ruc
def salida(self):
        print(f"Bienvenido a {self.nombre}")
        print(f"Nuestro telefono es {self.telefono}")
        print(f"Nuestra sede es {self.sede}")
        print(f"Nuestra direccion es {self.direccion}")
        print(f"Nuestro RUC  es {self.ruc}")
        insti = Instituto("Tecsup","01056034","ATE", "av circunvalacion", "1000343043")
print(insti.salida())