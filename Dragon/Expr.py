from dataclasses import dataclass
import Token

@dataclass
class Binary:
    left : 'Expr'
    operator : Token
    right : 'Expr'
    
    def accept(self):
        return AstPrinter.visit_binary_expr(self)
        

## Defining the node for the call expression which takes in callee experession and the list of expression for argumennts & also stores the token for closing paranthesis
@dataclass
class Call:
    callee : Token
    arguments : list['Expr']

    # def accept(self):
    #     return AstPrinter.visit_call_expr(self)        
    
@dataclass
class Grouping:
    expression : 'Expr'
    
    def accept(self):
        return AstPrinter.visit_grouping_expr(self)
    
@dataclass
class Literal:
    value : bool | int | float | str
    def accept(self):
        return AstPrinter.visit_literal_expr(self)
    
@dataclass
class Unary:
    operator : Token
    right : 'Expr'
    
    def accept(self):
        return AstPrinter.visit_unary_expr(self)

@dataclass
class Variable:
    name: Token

    def accept(self):
        return AstPrinter.visit_variable_expr(self)
    
@dataclass
class Assign:
    name : Token
    value : 'Expr'

    def accept(self):
        return AstPrinter.visit_assign_expr(self)
    
@dataclass
class Let:
    name: Token
    e1: 'Expr'
    e2: 'Expr'
 
   
Expr = Binary | Grouping | Literal | Unary| Let

from ASTPrinter import AstPrinter
