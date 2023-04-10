from Stmt import *

class EnvError(Exception):
    pass
class frame:
    
    def __init__(self, dragon):
        global_env = {}
        self.stack = [global_env]
        self.dragon = dragon
        
    def getEnvName(self):
        if 'name' in self.stack[-1] : return self.stack[-1]['name']
        else : raise EnvError()
        
    def enterBlock(self,token):
        
        new_dict= {}
        new_dict['name'] = token.lexeme
        prev = self.stack[-1]
        for i in prev:
            if i=='name': continue
            new_dict[i] = (prev[i][0],prev[i][1],0)
        self.stack.append(new_dict)
            
    def exitBlock(self):
        last = self.stack[-1]
        slast = self.stack[-2]
        for i in last:
            if i=='name': continue
            if last[i][2]==0:
                slast[i] = (last[i][0],last[i][1],slast[i][2])
        self.stack.pop()
        
    def changeValue(self,token, cvalue):
        length = len(self.stack) - 1
        value = None
        if token.lexeme in self.stack[length]:
            value = self.stack[length][token.lexeme]
        if value:
            match value[0]:
                case VarType.INT: 
                    if isinstance(cvalue,int) or isinstance(cvalue,float) :
                        self.stack[length][token.lexeme] = (VarType.INT,int(cvalue),self.stack[length][token.lexeme][2])
                        return
                    self.error(token,"can't assign to Variable type int")

                case VarType.BOOL: 
                    if isinstance(cvalue,bool):
                        self.stack[length][token.lexeme] = (VarType.BOOL,cvalue,self.stack[length][token.lexeme][2])
                        return
                    self.error(token,"can't assign to Variable type bool")
                    
                case VarType.FLOAT: 
                    if isinstance(cvalue,float) or isinstance(cvalue,int):
                        self.stack[length][token.lexeme] = (VarType.FLOAT,float(cvalue),self.stack[length][token.lexeme][2])
                        return
                    self.error(token,"can't assign to Variable type is float")
                case VarType.STRING: 
                    if isinstance(cvalue,str):
                        self.stack[length][token.lexeme] = (VarType.STRING,cvalue,self.stack[length][token.lexeme][2])
                        return
                    self.error(token,"can't assign to Variable type is string")
                case VarType.DYNAMIC: 
                        self.stack[length][token.lexeme] = (VarType.DYNAMIC,cvalue,self.stack[length][token.lexeme][2])
                        return
        self.error(token, "Variable is not defined")  
        
    def defineValue(self, token, type, value):
        env = self.stack[-1]
        match type:
            case VarType.INT: 
                if isinstance(value,int) or isinstance(value,float):
                    env[token.lexeme] = (VarType.INT,int(value),1)
                    return
                self.error(token,"can't assign to Variable type int")

            case VarType.BOOL: 
                if isinstance(value,bool):
                    env[token.lexeme] = (VarType.BOOL,value,1)
                    return
                self.error(token,"can't assign to Variable type bool")
                
            case VarType.FLOAT: 
                if isinstance(value,float) or isinstance(value,int) :
                    env[token.lexeme] = (VarType.FLOAT,float(value),1)
                    return
                self.error(token,"can't assign to Variable type is float")
            case VarType.STRING: 
                if isinstance(value,str):
                    env[token.lexeme] =(VarType.STRING,value,1)
                    return
                self.error(token,"can't assign to Variable type is string")
            case VarType.DYNAMIC: 
                    env[token.lexeme] = (VarType.DYNAMIC,value,1)
                    return
            case VarType.FUN:
                env[token.lexeme]=(VarType.FUN,value,1)      
                
    def getValue(self, token):
        return self.stack[-1][token.lexeme][1]
    
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
    
        
    
        