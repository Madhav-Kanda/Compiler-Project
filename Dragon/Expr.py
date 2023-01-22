from dataclasses import dataclass
import Token

@dataclass
class Binary:
    left : 'Expr'
    operator : Token
    right : 'Expr'
    
@dataclass
class Grouping:
    expression : 'Expr'
    
@dataclass
class Literal:
    value : object
    
@dataclass
class Unary:
    operator : Token
    right : 'Expr'
 
   
Expr = Binary | Grouping | Literal | Unary