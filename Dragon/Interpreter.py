from  Expr import *
from Stmt import *
from StackEnvironment import *

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
            case Logical(left,operator,right):
                left_value = self.evalExpression(left)
                if operator.lexeme == "or":
                    if left_value: return left_value
                else:
                    if not left_value: return left_value
                return self.evalExpression(right)
                
    def evalBinary(self,expression):
        
        match expression.operator.lexeme:
            case "<":
                return self.evalExpression(expression.left)<self.evalExpression(expression.right)
            case ">":
                return self.evalExpression(expression.left)>self.evalExpression(expression.right)
            case "<=":
                return self.evalExpression(expression.left)<=self.evalExpression(expression.right)
            case ">=":
                return self.evalExpression(expression.left)>=self.evalExpression(expression.right)
            case "==":
                return self.evalExpression(expression.left)==self.evalExpression(expression.right)
            case "!=":
                return not self.evalExpression(expression.left)==self.evalExpression(expression.right)
            case "+":
                return self.evalExpression(expression.left)+self.evalExpression(expression.right)
            case "-":
                return self.evalExpression(expression.left)-self.evalExpression(expression.right)
            case "*":
                return self.evalExpression(expression.left)*self.evalExpression(expression.right)
            case "/":
                return self.evalExpression(expression.left)/self.evalExpression(expression.right)
                