class contacto:

    def __init__(self,id,name,phone):
        self.name = name
        self.phone = phone
        self.id = id
    
    def __str__(self):
        return f"Name: {self.name}, Number: {self.phone}"
