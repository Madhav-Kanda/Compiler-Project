from TokenType import *
from Expr import *
from Stmt import Stmt
from dataclasses import dataclass
from dragon import *

class Environment:
    def __init__(self, enclosing = None):
        self.enclosing = enclosing
        self.values = {}

    # a variable definition binds a new name to a value.
    def define(self, name: str, type_value) -> None:
        self.values[name] = type_value

    # checks if the required variable is in the mapping or not, 
    # if yes, then simply return the value of the variable
    # if no, then generate a error
    def get(self, name: Token) -> object:
        if name.lexeme in self.values:
            if self.values[name.lexeme] is None:
                raise Dragon.error(name, "Uninitialized variable '" + name.lexeme + "'.")
            return self.values[name.lexeme]

        if self.enclosing is not None:
            return self.enclosing.get(name)

        raise Dragon.error(name, "Undefined variable '" + name.lexeme + "'.")


    # assigning the variable a value, 
    # if the variable is not found in the environment, we check in the enclosing one
    # in this manner, it walks the whole chain
    # if we reach an environment with no enclosing one, and still not found the variable
    # to be assigned, then report an error
    def assign(self, name: Token, value) -> None:
        if name.lexeme in self.values:
            self.values[name.lexeme] = value
            return

        if self.enclosing is not None:
            self.enclosing.assign(name, value)
            return

        raise Dragon.error(name, "Undefined variable '" + name.lexeme + "'.")

    
    



    