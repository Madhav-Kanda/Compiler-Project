from dataclasses import dataclass
from Expr import *
from enum import Enum

class VarType(Enum):
    INT = 0
    FLOAT = 1
    STRING = 2
    DYNAMIC = 3

@dataclass
class Expression:
    expression : 'Expr'
    
@dataclass
class Var:
    name : Token
    type : VarType
    initializer : 'Expr'    
    
Stmt = Expression | Var 

    
    