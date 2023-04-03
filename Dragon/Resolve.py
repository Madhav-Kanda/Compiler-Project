from TokenType import *
from Expr import *
from Stmt import *
from Environment import *
from StackEnvironment import *

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
            match expression:
                case Binary(left,operator,right):
                    re1 = resolveExpression(left)
                    re2 = resolveExpression(right)
                case Variable(name):
                    expression.name.lexeme = (expression.name.lexeme,self.env.getValue(name))
                    print(name.lexeme, self.id)
                case Let(name, e1, e2):
                    self.env.enterBlock()
                    self.id+=1
                    re1 = resolveExpression(e1)
                    print(name.lexeme, self.id)
                    name.lexeme = (name.lexeme, self.id)
                    re2 = resolveExpression(e2)
                    self.id-=1
                    self.env.exitBlock()
                case Grouping(expression):
                    resolveExpression(expression)
                case Assign(name,value):
                    resolveExpression(value)
                case Call(callee,arguments):
                    resolveExpression(callee)
                    for argument in arguments:
                        resolveExpression(argument)
                        
        def resolveStatement(statement):
            match statement:
                case Block(body):
                    self.env.enterBlock()
                    self.id+=1
                    self.resolve(statement.body)
                    self.id-=1
                    self.env.exitBlock()
              
        
            
        for statement in statements:
            match statement:
                case Expression(expression):
                    resolveExpression(expression)
                case Var(name,type,initializer):
                    name2 = name
                    name2.type = VarType.INT
                    self.env.defineValue(name2,VarType.INT,self.id)
                    print(name.lexeme, self.id)
                    resolveExpression(initializer)
                case Block(body):
                    self.env.enterBlock()
                    self.id+=1
                    self.resolve(statement.body)
                    self.id-=1
                    self.env.exitBlock()
                        
                case Print(value):
                    resolveExpression(value)
                case If(condition,thenBranch,elseBranch):
                    resolveExpression(condition)
                    resolveStatement(thenBranch)
                    if elseBranch:
                        resolveStatement(elseBranch)
                case While(condition,body):
                    resolveExpression(condition)
                    resolveStatement(body)
                case Function(name,type,params,body):
                    self.env.enterBlock()
                    for param in params:
                        resolveExpression(param)
                    # self.id+=1
                    resolveStatement(body)
                    # self.id-=1
                    self.env.exitBlock()
                case Return(keyword,value):
                    resolveExpression(value)
            
                




