from Environment import *
from Stmt import *

class EnvError(Exception):
    pass

class StackEnvironment:
    
    def __init__(self,dragon):
        self.stack = [Environment()]
        self.dragon = dragon
        self.buffer = []
        
    def enterBlock(self, function = None):
        if(function is None):
            self.stack.append(Environment())
        else :
            length = len(self.stack) -1
            while length!=-1:
                value = self.stack[length].get(function.lexeme)
                if value:
                    break
                else:
                    length -= 1
            if length==-1:
                self.error(function,"undefined function name")
            l = []
            j = len(self.stack) -1
            while j != length:
                l.append(self.stack.pop())
                j-=1
            if len(l)>0 : self.buffer.append(l)
            
        
    def exitBlock(self):
        if self.stack[-1].name is None:
            self.stack.pop()
        else:
            self.stack.pop()
            if(len(self.buffer)!=0):
                self.stack = self.stack+ self.buffer[-1]
                self.buffer.pop()
                
    def getEnvName(self):
        return self.stack[-1].name
        
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

                    case VarType.BOOL: 
                        if isinstance(cvalue,bool):
                            self.stack[length].assign(token.lexeme,(VarType.BOOL,cvalue))
                            return
                        self.error(token,"can't assign to Variable type bool")
                        
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

            case VarType.BOOL: 
                if isinstance(value,bool):
                    env.define(token.lexeme,(VarType.BOOL,value))
                    return
                self.error(token,"can't assign to Variable type bool")
                
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
            case VarType.FUN:
                env.define(token.lexeme,(VarType.FUN,value))
    
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
                    
                        
