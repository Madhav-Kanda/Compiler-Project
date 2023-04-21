from  Expr import *
from Stmt import *
from StackEnvironment import *
from frames import *
import sys
sys.setrecursionlimit(10000) 

class TypeError(Exception):
    pass

class Parameter(Exception):
    pass

class ReturnValue(Exception):
    def __init__(self,value):
        self.value = value

class Interpreter2:
    
    def __init__(self, statements,dragon):
        self.env = frame(dragon)
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
                for statement in body:
                    self.evalStatement(statement)
            case Print(value):
                final_value = self.evalExpression(value)
                print(final_value)
            case Return(keyword,value):
                value = self.evalExpression(value)
                keyword.lexeme = self.env.getEnvName()
                funobj = self.env.getValue(keyword)
                keyword.lexeme = "return" 
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
                if operator.lexeme=="!": return not self.evalExpression(right)
                if operator.lexeme=="-": 
                    return -1*self.evalExpression(right)
            case Variable(name):
                return self.env.getValue(name)
            case Assign(name,value):
                final_value = self.evalExpression(value)
                self.env.changeValue(name,final_value)
                return final_value
            case Call(callee,arguments):
                funobj = self.env.getValue(callee)
                if len(arguments)!= len(funobj.params):
                    self.dragon.error(callee,"extra arguments or less args are given")
                    raise Parameter
                self.env.enterBlock(callee)
                for i in range(len(funobj.params)):
                    value = self.evalExpression(arguments[i])
                    if self.Typecheck(funobj.params[i][1],value):
                        self.env.stack[-1][funobj.params[i][0].lexeme] = (funobj.params[i][1],value,1)
                    else :
                        self.dragon.error(callee,"different datatype given")
                        raise TypeError
                
                
                for i in funobj.body.body:
                    try :
                        self.evalStatement(i)
                    except ReturnValue as ret :
                        return ret.value
                
            case Let(name, e1, e2):
                value = self.evalExpression(e1)
                self.env.defineValue(name, VarType.DYNAMIC, value)
                c = self.evalExpression(e2)
                return c
            
            case Dictionary(elems):
                return {self.evalExpression(i[0]):self.evalExpression(i[1]) for i in elems} 
            case DictLength(dict):
                d = self.evalExpression(dict)
                return len(d)
            case DictAccess(dict, key):
                d = self.evalExpression(dict)
                k = self.evalExpression(key)
                if k not in d:
                    self.dragon.error(key, "Key not found")
                    raise KeyError
                return d[k] 
            case DictAssign(dict, key, value):
                d = self.evalExpression(dict)
                k = self.evalExpression(key)
                v = self.evalExpression(value)
                d[k] = v
            case DictAdd(dict, key, value):
                d = self.evalExpression(dict)
                k = self.evalExpression(key)
                v = self.evalExpression(value)
                if k in d:
                    self.dragon.error(key, "Key already exists")
                    raise KeyError
                d[k] = v 
            case DictRemove(dict, key):
                d = self.evalExpression(dict)
                k = self.evalExpression(key)
                if k not in d:
                    self.dragon.error(key, "Key not found")
                    raise KeyError
                del d[k] 
            case DictFind(dict, key):
                d = self.evalExpression(dict)
                k = self.evalExpression(key)
                return k in d 
            
            case List(elems):
                return [self.evalExpression(i) for i in elems] 
            case ListLength(list):
                l = self.evalExpression(list)
                return len(l) 
            case ListIsEmpty(list):
                l = self.evalExpression(list)
                return len(l)==0
            case ListAccess(list, index):
                l = self.evalExpression(list)
                i = self.evalExpression(index)
                if i >= len(l):
                    self.dragon.error(index, "Index out of range")
                    raise IndexError 
                return l[i] 
            case ListAssign(list, index, value): 
                l = self.evalExpression(list) 
                i = self.evalExpression(index)
                v = self.evalExpression(value)
                if i >= len(l):
                    self.dragon.error(index, "Index out of range")
                    raise IndexError
                l[i] = v
                return 
            case ListHead(list):
                l = self.evalExpression(list)
                if len(l)==0:
                    self.dragon.error(list, "List is empty")
                    raise IndexError
                return l[0]
            case ListTail(list):
                l = self.evalExpression(list)
                if len(l)==0:
                    self.dragon.error(list, "List is empty")
                    raise IndexError
                return l[1:] 
            case ListSlice(list, start, end, step):
                l = self.evalExpression(list)
                s = self.evalExpression(start)
                e = self.evalExpression(end)

                if step is not None:
                    st = self.evalExpression(step)
                else:
                    st = 1
                
                if s >= len(l):
                    self.dragon.error(start, "Index out of range")
                    raise IndexError
                if e >= len(l):
                    self.dragon.error(end, "Index out of range")
                    raise IndexError
                if st == 0:
                    self.dragon.error(step, "Step cannot be 0")
                    raise IndexError
                
                return l[s:e:st] 
            case ListAppend(list, elem):
                l = self.evalExpression(list)
                e = self.evalExpression(elem)
                l.append(e)
            case ListPop(list):
                l = self.evalExpression(list)
                if len(l)==0:
                    self.dragon.error(list, "List is empty")
                    raise IndexError
                return l.pop() 

                
                
    def Typecheck(self,vartype, value):
        match vartype:
            case VarType.INT:
                if not isinstance(value,int): return False    
            case VarType.BOOL:
                if not isinstance(value,bool): return False 
            case VarType.FLOAT:
                if not isinstance(value,float): return False
            case VarType.STRING:
                if not isinstance(value,str): return False
        return True
        
                
    def evalBinary(self,expression):
        l = self.evalExpression(expression.left)
        r = self.evalExpression(expression.right)
        self.env.checkTypeCompatibility(expression.operator, l, r, expression.operator.lexeme)

        match expression.operator.lexeme:
            case "<":
                return bool(l<r)
            case ">":
                return bool(l>r)
            case "<=":
                return bool(l<=r)
            case ">=":
                return bool(l>=r)
            case "==":
                return bool(l==r)
            case "!=":
                return not bool(l==r)

            case "+":
                return l+r

            case "-":
                self.env.stringbystring(expression.operator, l, r, expression.operator.lexeme)
                return l-r
            case "*":
                self.env.stringbystring(expression.operator, l, r, expression.operator.lexeme)
                return l*r
            case "/":
                self.env.stringbystring(expression.operator, l, r, expression.operator.lexeme)
                if(isinstance(l,int) and isinstance(r,int)): return int(l/r)
                return l/r
            case "%": # modulo operator 
                self.env.stringbystring(expression.operator, l, r, expression.operator.lexeme)
                return l%r 
            case "or":
                return bool(l or r)
            case "and":
                return bool(l and r)
