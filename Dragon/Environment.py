from TokenType import *
from Expr import *

class Environment:
    def __init__(self,name = None):
        self.values = {}
        self.name = name

    # a variable definition binds a new name to a value.
    def define(self, name: str, type_value):
        self.values[name] = type_value


    def get(self, name: Token):
        if name in self.values:
            return self.values[name]
        return False


    def assign(self, name: Token, value) -> None:
        if name in self.values:
            self.values[name] = value
            return

    
    



    