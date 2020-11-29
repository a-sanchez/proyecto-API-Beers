class coctel():
    def __init__(self,*args):
        self.id=id
        self.name=name
        self.tag=tag
        self.alcohol=alcohol
        self.instructions = instructions
        self.imagen=imagen
        self.ingredients=ingredients
        
    def __str__(self):
        if self.tag !=None:
            #el dato depende del coctel
            return str(f"Coctels:"+"\n"+f"Name -> {self.name}"+"\n"+f"Tag -> {self.tag}"+"\n"+f"Alcohol -> {self.alcohol}"+"\n"+f"Instructions -> {self.instructions}"+"\n"+f"Imagen -> {self.imagen}"+"\n"+f"Ingredients -> {self.ingredients}")
        else:
            return str(f"Coctels:"+"\n"+f"Name -> {self.name}"+"\n"+f"Alcohol -> {self.alcohol}"+"\n"+f"Instructions -> {self.instructions}"+"\n"+f"Imagen -> {self.imagen}"+"\n"+f"Ingredients -> {self.ingredients}")
        
    def __eq__(self,Coctel2):
        if Coctel2.id != self.id:
            return False
        
        if Coctel2.name =! self.name:
            return False
        
        if Coctel2.tag =! self.tag:
            return False
        
        if Coctel2.alcohol =! self.tag:
            return False
        
        if Coctel2.instructions =! self.instructions:
            return False
        
        if Coctel2.imagen =! self.imagen:
            return False
        
        if Coctel2.ingredients =!self.ingredients:
            return False
        return True
        