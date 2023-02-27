from dataclasses import dataclass
from Expr import *
from enum import Enum
from typing import Optional
from Token import Token

class VarType(Enum):
    INT = 0
    FLOAT = 1
    STRING = 2
    DYNAMIC = 3
    FUN = 4
    BOOL = 5 # for boolean data type 

@dataclass
class Expression:
    expression : 'Expr'
    
@dataclass
class Var:
    name : Token
    type : VarType
    initializer : 'Expr'   

@dataclass
class If:
    condition: 'Expr'
    thenBranch: 'Stmt' 
    elseBranch: Optional['Stmt']

@dataclass
class While:
    condition: 'Expr'
    body: 'Stmt' 

@dataclass   
class Block:
    body : list['Stmt']

@dataclass
class Print:
    value : 'Expr'

@dataclass
class Function:
    name : Token
    type : VarType
    params : list
    body : Block

@dataclass
class Return:
    keyword : Token
    value : 'Expr'



Stmt = Expression| Print | Var | If |  While | Block | Function | Return 
    
