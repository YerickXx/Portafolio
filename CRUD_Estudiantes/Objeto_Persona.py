class persona: # ------------> Objeto padre del cual se heredan atributos a los demas objetos
    
    def __init__(self,nombre,altura,genero): #metodo construcor
        self.__nombre = nombre #encapsulamiento acceso privado
        self.altura = altura
        self.genero = genero

        
    def get_name(self): #getteo del atributo privado
     return self.__nombre
    
    def set_name(self,nuevo_nombre): #setteo de un nuevo valor al atributo
        self.__nombre = nuevo_nombre

    def caminar(self):
        print(" la persona esta caminando")
    
    def comiendo(self):
        print ("La persona esta comiendo")
