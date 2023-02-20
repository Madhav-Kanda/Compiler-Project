from Environment import *
from Stmt import *

class EnvError(Exception):
    pass

class StackEnvironment:
    
    def __init__(self,dragon):
        self.stack = [Environment()]
        self.dragon = dragon
        
    def enterBlock(self):
        self.stack.append(Environment())
        
    def exitBlock(self):
        self.stack.pop()
        
    def changeValue(self,token, cvalue):
        length = len(self.stack) - 1
        while length != -1 :
            value = self.stack[length].get(token.lexeme)
            if value:
                match value[0]:
                    case VarType.INT: 
                        if isinstance(cvalue,int):
                            self.stack[length].assign(token.lexeme,(VarType.INT,cvalue))
                            return
                        self.error(token,"can't assign to Variable type int")
                        
                    case VarType.FLOAT: 
                        if isinstance(cvalue,float):
                            self.stack[length].assign(token.lexeme,(VarType.FLOAT,cvalue))
                            return
                        self.error(token,"can't assign to Variable type is float")
                    case VarType.STRING: 
                        if isinstance(cvalue,str):
                            self.stack[length].assign(token.lexeme,(VarType.STRING,cvalue))
                            return
                        self.error(token,"can't assign to Variable type is string")
                    case VarType.DYNAMIC: 
                            self.stack[length].assign(token.lexeme,(VarType.DYNAMIC,cvalue))
                            return
            length -=1
        self.error(token, "Variable is not defined")
                        
    def defineValue(self, token, type, value):
        env = self.stack[len(self.stack)-1]
        if env.get(token.lexeme):
            self.error(token, "Variable already exists")
        match type:
            case VarType.INT: 
                if isinstance(value,int):
                    env.define(token.lexeme,(VarType.INT,value))
                    return
                self.error(token,"can't assign to Variable type int")
                
            case VarType.FLOAT: 
                if isinstance(value,float):
                    env.define(token.lexeme,(VarType.FLOAT,value))
                    return
                self.error(token,"can't assign to Variable type is float")
            case VarType.STRING: 
                if isinstance(value,str):
                    env.define(token.lexeme,(VarType.STRING,value))
                    return
                self.error(token,"can't assign to Variable type is string")
            case VarType.DYNAMIC: 
                    env.define(token.lexeme,(VarType.DYNAMIC,value))
                    return
    
    def getValue(self, token):
        length = len(self.stack) - 1
        while length != -1 :
            value = self.stack[length].get(token.lexeme)
            if value:
                return value[1]
            length -=1
        self.error(token, "Variable is not defined")

    
    # checks the compatibility of the operations 
    # for example: an integer cannot be added to a string, this is incompatible
    # Type Checking

    def checkTypeCompatibility(self, token, lvalue, rvalue, operator):
        if (isinstance(lvalue, int) and isinstance(rvalue, int)) or \
           (isinstance(lvalue, float) and isinstance(rvalue, float)) or \
           (isinstance(lvalue, str) and isinstance(rvalue, str)):
            return True
        elif isinstance(lvalue, int) and isinstance(rvalue, float):
            return True
        elif isinstance(lvalue, float) and isinstance(rvalue, int):
            return True
        else:
            self.error(token, str(type(lvalue)) + " and " + str(type(rvalue)) + " are incompatible with the operator " + operator)


    # if both the operands are of string type, then some of the operations such as subtraction, multiplication and division won't work for these
    def stringbystring(self, token, lvalue, rvalue, operator):
        if (isinstance(lvalue, str) and isinstance(rvalue, str)):
            if (operator == "/") or (operator == "*") or (operator == "-"):
                self.error(token, str(type(lvalue)) + " and " + str(type(rvalue)) + " doesn't make sense with the particular operation " + operator)

            
    def error(self,token,message):
        self.dragon.error(token,message)
        raise EnvError()
                    
                        