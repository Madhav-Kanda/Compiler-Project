from  Expr import *
from Stmt import *
from StackEnvironment import *

class TypeError(Exception):
    pass

class Parameter(Exception):
    pass

class ReturnValue(Exception):
    def __init__(self,value):
        self.value = value

class Interpreter:
    
    def __init__(self, statements,dragon):
        self.env = StackEnvironment(dragon)
        self.statements= statements
        self.dragon = dragon
        
    def interprete(self):
        for statement in self.statements:
            self.evalStatement(statement)
            
        
    def evalStatement(self,statement):
        
        match statement:
            case Expression(expression):
                self.evalExpression(expression)
            case Var(name,type,initializer):
                value = self.evalExpression(initializer)
                self.env.defineValue(name,type,value)
            case If(condition,thenBranch,elseBranch):
                value = self.evalExpression(condition)
                if value: self.evalStatement(thenBranch)
                elif elseBranch is not None : self.evalStatement(elseBranch)
            case While(condition,body):
                while self.evalExpression(statement.condition):
                    self.evalStatement(body)
            case Block(body):
                self.env.enterBlock()
                for statement in body:
                    self.evalStatement(statement)
                self.env.exitBlock()
            case Print(value):
                final_value = self.evalExpression(value)
                print(final_value)
            case Return(keyword,value):
                value = self.evalExpression(value)
                keyword.lexeme = self.env.getEnvName()
                while  keyword.lexeme is None:
                    self.env.stack.pop()
                    keyword.lexeme = self.env.getEnvName()
                funobj = self.env.getValue(keyword)
                    
                keyword.lexeme = "return" 
                if len(self.env.stack)==0:
                    raise TypeError
                if self.Typecheck(funobj.type,value):
                    self.env.exitBlock()
                    raise ReturnValue(value)
                else :
                    self.dragon.error(keyword,"invalid return type")
                    self.env.exitBlock()
                    raise TypeError
            case Function(name,type,params,body):
                self.env.defineValue(name,VarType.FUN,statement)
                    
             
        
    def evalExpression(self,expression):
        
        match expression:
            case Binary(left,operator,right):
                return self.evalBinary(expression)  
            case Grouping(expression):
                return self.evalExpression(expression)
            case Literal(value):
                return value
            case Unary(operator,right):
                if operator=="!": return not self.evalExpression(right)
                if operator=="-": return -1*self.evalExpression(right)
            case Variable(name):
                return self.env.getValue(name)
            case Assign(name,value):
                final_value = self.evalExpression(value)
                self.env.changeValue(name,final_value)
                return final_value
            case Call(callee,arguments):
                funobj = self.env.getValue(callee)
                if len(arguments)!= len(funobj.params):
                    self.dragon.error(callee,"extra arguments are given")
                    raise Parameter
                curr_env = Environment(callee.lexeme)
                for i in range(len(funobj.params)):
                    value = self.evalExpression(arguments[i])
                    if self.Typecheck(funobj.params[i][1],value):
                        curr_env.values[funobj.params[i][0].lexeme] = (funobj.params[i][1],value)
                    else :
                        self.dragon.error(callee,"different datatype given")
                        raise TypeError
                self.env.enterBlock(callee)
                self.env.stack.append(curr_env)
                for i in funobj.body.body:
                    try :
                        self.evalStatement(i)
                    except ReturnValue as ret :
                        return ret.value
                    except :
                        exit(-1)
                self.env.exitBlock()
                
                
    def Typecheck(self,vartype, value):
        match vartype:
            case VarType.INT:
                if not isinstance(value,int): return False   
            case VarType.FLOAT:
                if not isinstance(value,float): return False
            case VarType.STRING:
                if not isinstance(value,str): return False
        return True
        
                
    def evalBinary(self,expression):

        # self.env.checkTypeCompatibility(expression.operator, self.evalExpression(expression.left), self.evalExpression(expression.right), expression.operator.lexeme)

        match expression.operator.lexeme:
            case "<":
                return int(self.evalExpression(expression.left)<self.evalExpression(expression.right))
            case ">":
                return int(self.evalExpression(expression.left)>self.evalExpression(expression.right))
            case "<=":
                return int(self.evalExpression(expression.left)<=self.evalExpression(expression.right))
            case ">=":
                return int(self.evalExpression(expression.left)>=self.evalExpression(expression.right))
            case "==":
                return int(self.evalExpression(expression.left)==self.evalExpression(expression.right))
            case "!=":
                return not int(self.evalExpression(expression.left)==self.evalExpression(expression.right))

            case "+":
                return self.evalExpression(expression.left)+self.evalExpression(expression.right)

            case "-":
                # self.env.stringbystring(expression.operator, self.evalExpression(expression.left), self.evalExpression(expression.right), expression.operator.lexeme)
                return self.evalExpression(expression.left)-self.evalExpression(expression.right)
            case "*":
                # self.env.stringbystring(expression.operator, self.evalExpression(expression.left), self.evalExpression(expression.right), expression.operator.lexeme)
                return self.evalExpression(expression.left)*self.evalExpression(expression.right)
            case "/":
                # self.env.stringbystring(expression.operator, self.evalExpression(expression.left), self.evalExpression(expression.right), expression.operator.lexeme)
                return self.evalExpression(expression.left)/self.evalExpression(expression.right)
            case "or":
                return int(self.evalExpression(expression.left) or self.evalExpression(expression.right))
            case "and":
                return int(self.evalExpression(expression.left) and self.evalExpression(expression.right))
