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
    # value : object 
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
class List: 
    elements: list['Expr'] 
    

    # def accept(self):
    #     return AstPrinter.visit_list_expr(self) 

# data class for length of a list
@dataclass
class ListLength:
    list : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_length_expr(self)


# data class for list is empty or not 
@dataclass
class ListIsEmpty:
    list : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_isempty_expr(self)

# data class for ListAccess 
@dataclass
class ListAccess:
    list : 'Expr'
    index : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_access_expr(self) 

# data class for head of a list
@dataclass
class ListHead:
    list : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_head_expr(self)

# data class for tail of a list
@dataclass
class ListTail:
    list : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_tail_expr(self)

# data class for ListSlice
@dataclass
class ListSlice:
    list : 'Expr'
    start : 'Expr'
    end : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_slice_expr(self) 

# dataclass for appending to a list
@dataclass
class ListAppend:
    list : 'Expr'
    element : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_append_expr(self)

# data class for poping last element from a list 
@dataclass
class ListPop:
    list : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_pop_expr(self) 
    
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
