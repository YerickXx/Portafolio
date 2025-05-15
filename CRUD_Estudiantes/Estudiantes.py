from Objeto_Persona import *


class estudiante(persona): #--------> herencia del objeto padre 
   

    def __init__(self, nombre, altura, genero,id,apellido): # ---------> inclusion de 2 atributos extra ademas de los del padre
           super().__init__(nombre, altura, genero)
           self.id = id
           self.__apellido = apellido
     
   
    def calificacion(self):
        return "Su nota final es de: 90"
    
    def to_dic(self): #formateo para el json
         return  {
             "nombre":self.id,
             "apellido":self.__apellido
         }
    def get_name(self): #getteo del atributo privado
     return self.__apellido
    
    def set_LastName(self,nuevo_apellido): #setteo de un nuevo valor al atributo
        self.__apellido = nuevo_apellido

