from TokenType import *
from Expr import *
from Stmt import *
from Environment import *
from StackEnvironment import *
import copy

class Resolve:

    def __init__(self, statements, dragon):
        self.dragon = dragon
        self.statements = statements
        self.id = 1
        self.env = StackEnvironment(dragon)

    def resolvii(self):
        return self.resolve(self.statements) 

    def resolve(self, statements):
        
        def resolveExpression(expression):
            t = expression
            match expression:
                case Binary(left,operator,right):
                    re1 = resolveExpression(expression.left)
                    re2 = resolveExpression(expression.right)
                case Variable(name):
                    expression.name.lexeme = (expression.name.lexeme,self.env.getValue(name))
                case Let(name, e1, e2):
                    self.env.enterBlock()
                    self.id+=1
                    re1 = resolveExpression(expression.e1)
                    dummy = copy.copy(expression)
                    self.env.defineValue(dummy.name,VarType.INT,self.id)
                    expression.name.lexeme = (name.lexeme, self.id)
                    re2 = resolveExpression(expression.e2)
                    self.env.exitBlock()
                case Grouping(expression):
                    resolveExpression(t.expression)
                case Assign(name,value):
                    resolveExpression(expression.value)
                    expression.name.lexeme = (expression.name.lexeme,self.env.getValue(name))
                case Call(callee,arguments):
                    # print(self.env.stack[0])
                    expression.callee.lexeme = (expression.callee.lexeme,self.env.getValue(callee))
                    for i in range(len(arguments)):
                        resolveExpression(expression.arguments[i])
                case List(elements):
                    for i in expression.elements:
                        resolveExpression(i)
                case ListLength(list):
                    resolveExpression(expression.list)
                case ListIsEmpty(list):
                    resolveExpression(expression.list)
                case ListAccess(list,index):
                    resolveExpression(expression.list)
                    resolveExpression(expression.index)
                case ListHead(list):
                    resolveExpression(expression.list)
                case ListTail(list):
                    resolveExpression(expression.list)
                case ListSlice(list,start,end):
                    resolveExpression(expression.list)
                    resolveExpression(expression.start)
                    resolveExpression(expression.end)
                    resolveExpression(expression.step)
                case ListAppend(list,element):
                    resolveExpression(expression.list)
                    resolveExpression(expression.element)
                case ListPop(list):
                    resolveExpression(expression.list)
                    
                    
                    

              
        
            
        for statement in statements:
            match statement:
                case Expression(expression):
                    resolveExpression(statement.expression)
                case Var(name,type,initializer):
                    name2 = copy.copy(name)
                    resolveExpression(statement.initializer)
                    self.id+=1
                    self.env.defineValue(name2,VarType.INT,self.id)
                    statement.name.lexeme = (name.lexeme,self.id)
                case Block(body):
                    self.env.enterBlock()
                    self.resolve(statement.body)
                    self.env.exitBlock()
                        
                case Print(value):
                    resolveExpression(statement.value) 
                case If(condition,thenBranch,elseBranch):
                    resolveExpression(statement.condition)
                    self.resolve(statement.thenBranch.body)
                    if elseBranch:
                        self.resolve(statement.elseBranch.body)
                case While(condition,body):
                    resolveExpression(statement.condition)
                    self.resolve(statement.body.body)
                case Function(name,type,params,body):
                    name2= copy.copy(name)
                    self.id+=1
                    statement.name.lexeme = (name.lexeme,self.id)
                    self.env.defineValue(name2,VarType.INT,self.id)
                    self.env.enterBlock()
                    for ind in range(len(params)):
                        self.id+=1
                        temp = copy.copy(params[ind][0])
                        self.env.defineValue(temp,VarType.INT,self.id)
                        statement.params[ind][0].lexeme = (params[ind][0].lexeme, self.id)
                    self.resolve(statement.body.body)
                    self.env.exitBlock()
                case Return(keyword,value):
                    resolveExpression(statement.value)
            
                




