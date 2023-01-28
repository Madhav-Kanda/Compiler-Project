
class Environment:
    
    def __init__(self):
        self.values = {}
        
    def define(self,name, type_value):
        self.values[name] = type_value
        
    def get(self,name):
        if name.lexeme in self.values: return self.values[name.lexeme][1]
        
        raise RuntimeError(name, "Undefined variable '" + name.lexeme + "'." )
    
     
        
        