from TokenType import *
from Expr import *
from Stmt import *
from typing import Tuple

@dataclass
class Label:
    target: int

class I:
    """The instructions for our stack VM."""
    @dataclass
    class PUSH:
        what: Literal

    @dataclass
    class ADD:
        pass

    @dataclass
    class SUB:
        pass

    @dataclass
    class MUL:
        pass

    @dataclass
    class DIV:
        pass

    @dataclass
    class QUOT:
        pass

    @dataclass
    class MODULO:
        pass

    @dataclass
    class EXP:
        pass

    @dataclass
    class AND:
        pass

    @dataclass
    class OR:
        pass

    @dataclass
    class EQ:
        pass

    @dataclass
    class NE:
        pass

    @dataclass
    class NEG:
        pass

    @dataclass
    class LT:
        pass

    @dataclass
    class GT:
        pass

    @dataclass
    class LE:
        pass

    @dataclass
    class GE:
        pass

    @dataclass
    class JMP:
        label: Label

    @dataclass
    class JMP_IF_FALSE:
        label: Label

    @dataclass
    class JMP_IF_TRUE:
        label: Label

    @dataclass
    class NOT:
        pass

    @dataclass
    class DUP:
        pass

    @dataclass
    class POP:
        pass

    @dataclass
    class LOAD:
        ID: int

    @dataclass
    class STORE:
        ID: int

    @dataclass
    class PRINT:
        pass

    @dataclass
    class PUSHFN:
        entry: Label

    @dataclass
    class CALL:
        ID: int

    @dataclass
    class RETURN:
        pass

    @dataclass
    class HALT:
        pass

    @dataclass
    class PUSHFN:
        offset: Label
        func_id: int

    @dataclass
    class LIST:
        length: int

    @dataclass
    class LISTLENGTH:
        pass

    @dataclass
    class LISTISEMPTY:
        pass

    @dataclass
    class LISTACCESS:
        pass

    @dataclass
    class LISTASSIGN:
        pass
    
    @dataclass
    class LISTHEAD:
        pass

    @dataclass
    class LISTTAIL:
        pass

    @dataclass
    class LISTSLICE:
        pass

    @dataclass
    class LISTAPPEND:
        pass

    @dataclass
    class LISTPOP:
        pass

    @dataclass
    class DICT:
        length: int

    @dataclass
    class DICTLENGTH:
        pass

    @dataclass
    class DICTACCESS:
        pass

    @dataclass
    class DICTASSIGN:
        pass

    @dataclass
    class DICTADD:
        pass

    @dataclass
    class DICTREMOVE:
        pass

    @dataclass
    class DICTFIND:
        pass


Instruction = (
      I.PUSH
    | I.AND
    | I.OR
    | I.ADD
    | I.SUB
    | I.MUL
    | I.DIV
    | I.QUOT
    | I.MODULO
    | I.NOT
    | I.JMP
    | I.JMP_IF_FALSE
    | I.JMP_IF_TRUE
    | I.DUP
    | I.POP
    | I.HALT
    | I.EQ
    | I.NE
    | I.LT
    | I.GT
    | I.LE
    | I.GE
    | I.NEG
    | I.LOAD
    | I.STORE
    | I.PUSHFN
    | I.CALL
    | I.RETURN
    | I.LIST 
    | I.LISTLENGTH
    | I.LISTISEMPTY
    | I.LISTACCESS
    | I.LISTASSIGN
    | I.LISTHEAD
    | I.LISTTAIL
    | I.LISTSLICE
    | I.LISTAPPEND
    | I.LISTPOP
    | I.DICT
    | I.DICTLENGTH
    | I.DICTACCESS
    | I.DICTASSIGN
    | I.DICTADD
    | I.DICTREMOVE
    | I.DICTFIND
    | I.PRINT

)