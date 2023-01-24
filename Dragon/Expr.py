from dataclasses import dataclass
import Token

@dataclass
class Binary:
    left : 'Expr'
    operator : Token
    right : 'Expr'
    
    def accept(self):
        return AstPrinter.visit_binary_expr(self)
        
    
@dataclass
class Grouping:
    expression : 'Expr'
    
    def accept(self):
        return AstPrinter.visit_grouping_expr(self)
    
@dataclass
class Literal:
    value : bool | int | float
    def accept(self):
        return AstPrinter.visit_literal_expr(self)
    
@dataclass
class Unary:
    operator : Token
    right : 'Expr'
    
    def accept(self):
        return AstPrinter.visit_unary_expr(self)
 
   
Expr = Binary | Grouping | Literal | Unary

from ASTPrinter import AstPrinter
