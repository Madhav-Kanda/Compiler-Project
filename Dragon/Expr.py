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
class Dictionary:
    elements: list[tuple['Expr','Expr']]

    # def accept(self):
    #     return AstPrinter.visit_dictionary_expr(self) 

@dataclass
class DictAccess:
    dict : 'Expr'
    key : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_dict_access_expr(self)

@dataclass
class DictLength:
    dict : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_dict_length_expr(self)

@dataclass
class DictAssign:
    dict : 'Expr'
    key : 'Expr'
    value : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_dict_assign_expr(self)

@dataclass
class DictAdd:
    dict : 'Expr'
    key : 'Expr'
    value : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_dict_add_expr(self)

@dataclass
class DictRemove:
    dict : 'Expr'
    key : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_dict_remove_expr(self) 

@dataclass
class DictFind:
    dict : 'Expr'
    key : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_dict_find_expr(self) 

@dataclass
class StringSlice:
    string : 'Expr'
    start : 'Expr'
    end : 'Expr'
    step: 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_string_slice_expr(self)
@dataclass
class StringAccess:
    string : 'Expr'
    index : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_string_access_expr(self)

@dataclass
class StringLength:
    string : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_string_length_expr(self)


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


# data class for list assign 
@dataclass
class ListAssign:
    list : 'Expr'
    index : 'Expr'
    value : 'Expr'

    # def accept(self):
    #     return AstPrinter.visit_list_assign_expr(self)

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

# data class for ListSlice with step
@dataclass
class ListSlice:
    list : 'Expr'
    start : 'Expr'
    end : 'Expr'
    step: 'Expr'

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
 
 
@dataclass
class CompiledFunction:
    entry: int
   
Expr = Binary | Grouping | Literal | Unary| Let | CompiledFunction

from ASTPrinter import AstPrinter
