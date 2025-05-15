from Estudiantes import *
from Objeto_Persona import *
import random
import json

dic={
   "id":" ", 
   "apellido": " "
}


def create_json():
   try:
    with open('data.json', 'w') as json_file:
      json.dump(dic, json_file, indent=4)
   except Exception as e:
      print("se presento un error al abrir el archivo!",e)


def leer_json():
   try:
       with open("data.json", "r") as file:
         data = json.load(file)
         print(data)
   except Exception as e:
      print("Se produjo un error al intentar abrir el archivo",e)



def registrar(name, altura, genero, last_name): #funcion para registrar estudiantes 
 id = random.randint(1,100)

 if name.isalpha() and  last_name.isalpha():
     if altura.isdigit() and genero.isalpha():
       if id > 0 and id < 100: #   ------->validacion de inputs
         student1 = estudiante(name,altura,genero,id,last_name) #----------->creacion del objeto
         Name1 = student1.set_name(name) #------>setteo del nombre
         new_name = Name1
         lastName1 = student1.set_LastName(last_name)#----->setteo del apellido
         dic["id"] = id
         dic["apellido"] = last_name
         create_json()
         #json.dumps(student1.to_dic())

     print("El estudiante: ", new_name ,"de apellido: ", lastName1," mide: ",altura," es de genero: "
            , genero, " y fue guardado con el id: ",id," ha sido guardado de manera exitosa")# -------> mensaje guardado exitoso
 else:
   print("El nombre solo debe contener letras de la A-Z, por lo que el estudiante no se ha guardado!")# ----------> mensaje de error de registro
    
def mostrar(): #funcion para mostrar la lista de estudiantes registrados
    leer_json()


def borrar():# funcion para eliminar un estudiante mediante su apellido

   
 Id_Estudiante = input("Ingrese el apellido del estudiante que desea borrar: ")

 try:
    with open("data.json", "r") as file:
        data = json.load(file)

    encontrado = False
    for estudiante in data:
        if estudiante.get("apellido") == Id_Estudiante:
            data.remove(estudiante)
            encontrado = True
            break

    if encontrado:
        with open("data.json", "w") as file:
            json.dump(data, file, indent=4)
        print(f"El estudiante con el apellido '{Id_Estudiante}' ha sido eliminado.")
    else:
        print("¡El estudiante no está en la lista!")

 except Exception as e:
    print("Se produjo un error al intentar abrir el archivo:", e)