from TokenType import *
from Expr import *
from Stmt import *
from bytecode import ByteCode
from instructions import *

class Frame:
    locals: list[Literal]
    retaddr: int
    dynamicLink: 'Frame'

    def __init__(self, retaddr = -1, dynamicLink = None):
        MAX_LOCALS = 32
        self.locals = [None] * MAX_LOCALS
        self.retaddr = retaddr
        self.dynamicLink = dynamicLink

class VM:
    bytecode: ByteCode
    ip: int
    data: list[Literal]
    currentFrame: Frame
    id_to_target: dict[int, int]
    function_id: list[int]

    def load(self, bytecode):
        self.bytecode = bytecode
        self.restart()

    def restart(self):
        self.ip = 0
        self.data = []
        self.currentFrame = Frame()
        self.id_to_target = {}
        self.function_id = []

    def execute(self) -> Literal:
        while self.ip < len(self.bytecode.insns):
            match self.bytecode.insns[self.ip]:
                case I.PUSH(val):
                    self.data.append(val)
                    self.ip += 1
                case I.PUSHFN(Label(offset), func_id):
                    self.id_to_target[func_id] = offset
                    self.data.append(offset)
                    # self.data.append(CompiledFunction(offset))
                    self.ip += 1
                    self.function_id.append(func_id)
                case I.CALL(localID):
                    self.currentFrame = Frame (
                        retaddr=self.ip + 1,
                        dynamicLink=self.currentFrame
                    )

                    self.ip = self.id_to_target[localID]
                case I.RETURN():
                    # print(self.data)
                    self.ip = self.currentFrame.retaddr
                    self.currentFrame = self.currentFrame.dynamicLink
                case I.NEG():
                    op = self.data.pop()
                    self.data.append(-op)
                    self.ip += 1
                case I.AND():
                    right = self.data.pop()
                    left = self.data.pop()
                    val = left and right
                    self.data.append(val != 0)
                    self.ip += 1
                case I.OR():
                    right = self.data.pop()
                    left = self.data.pop()
                    val = left or right
                    self.data.append(val != 0)
                    self.ip += 1
                case I.ADD():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left+right)
                    self.ip += 1
                case I.SUB():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left-right)
                    self.ip += 1
                case I.MUL():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left*right)
                    self.ip += 1
                case I.DIV():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left/right)
                    self.ip += 1
                case I.MODULO():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left%right)
                    self.ip += 1
                case I.EXP():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left**right)
                    self.ip += 1
                case I.EQ():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left==right)
                    self.ip += 1
                case I.NE():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left!=right)
                    self.ip += 1
                case I.LT():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left<right)
                    self.ip += 1
                case I.GT():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left>right)
                    self.ip += 1
                case I.LE():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left<=right)
                    self.ip += 1
                case I.GE():
                    right = self.data.pop()
                    left = self.data.pop()
                    self.data.append(left>=right)
                    self.ip += 1
                case I.JMP(label):
                    self.ip = label.target
                case I.JMP_IF_FALSE(label):
                    op = self.data.pop()
                    if not op:
                        self.ip = label.target
                    else:
                        self.ip += 1
                case I.JMP_IF_TRUE(label):
                    op = self.data.pop()
                    if op:
                        self.ip = label.target
                    else:
                        self.ip += 1
                case I.NOT():
                    op = self.data.pop()
                    self.data.append(not op)
                    self.ip += 1
                case I.DUP():
                    op = self.data.pop()
                    self.data.append(op)
                    self.data.append(op)
                    self.ip += 1
                case I.POP():
                    self.data.pop()
                    self.ip += 1
                case I.LOAD(localID):
                    if (localID not in self.function_id):
                        self.data.append(self.currentFrame.locals[localID])
                    self.ip += 1
                case I.STORE(localID):
                    val = self.data.pop()
                    self.currentFrame.locals[localID] = val
                    self.ip += 1
                case I.PRINT():
                    val = self.data.pop()
                    print(val)
                    self.ip += 1
                
                case I.LIST():
                    val = self.data.pop()
                    self.data.append(val)
                    self.ip += 1
                case I.LISTLENGTH():
                    val = self.data.pop()
                    self.data.append(len(val))
                    self.ip += 1
                case I.LISTISEMPTY():
                    val = self.data.pop()
                    self.data.append(len(val) == 0)
                    self.ip += 1
                case I.LISTACCESS():
                    index = self.data.pop()
                    val = self.data.pop()
                    self.data.append(val[index])
                    self.ip += 1
                case I.LISTASSIGN():
                    index = self.data.pop()
                    val = self.data.pop()
                    list = self.data.pop()
                    list[index] = val
                    self.data.append(list)
                    self.ip += 1
                case I.LISTHEAD():
                    val = self.data.pop()
                    self.data.append(val[0])
                    self.ip += 1
                case I.LISTTAIL():
                    val = self.data.pop()
                    self.data.append(val[1:])
                    self.ip += 1
                case I.LISTSLICE():
                    step = self.data.pop()                    
                    end = self.data.pop()
                    start = self.data.pop()
                    val = self.data.pop()
                    if (step == None):
                        step = 1
                    self.data.append(val[start:end:step])
                    self.ip += 1
                case I.LISTAPPEND():
                    val = self.data.pop()
                    list = self.data.pop()
                    list.append(val)
                    self.data.append(list)
                    self.ip += 1
                case I.LISTPOP():
                    list = self.data.pop()
                    list.pop()
                    self.data.append(list)
                    self.ip += 1

                case I.DICT():
                    val = self.data.pop()
                    self.data.append(val)
                    self.ip += 1
                case I.DICTLENGTH():
                    val = self.data.pop()
                    self.data.append(len(val))
                    self.ip += 1
                case I.DICTACCESS():
                    key = self.data.pop()
                    val = self.data.pop()
                    self.data.append(val[key])
                    self.ip += 1
                case I.DICTASSIGN():
                    val = self.data.pop()
                    key = self.data.pop()
                    dict = self.data.pop()
                    dict[key] = val
                    self.data.append(dict)
                    self.ip += 1
                case I.DICTADD():
                    val = self.data.pop()
                    key = self.data.pop()
                    dict = self.data.pop()
                    dict[key] = val
                    self.data.append(dict)
                    self.ip += 1
                case I.DICTREMOVE():
                    key = self.data.pop()
                    dict = self.data.pop()
                    del dict[key]
                    self.data.append(dict)
                    self.ip += 1
                case I.DICTFIND():
                    key = self.data.pop()
                    dict = self.data.pop()
                    self.data.append(key in dict)
                    self.ip += 1
                case I.HALT():
                    return