import sys
from Scanner import Scanner
from Token import *
from TokenType import *
from Parser import *
from ASTPrinter import *
from Interpreter import *
from Interpreter2 import *
from Resolve import *
from Interpreter import *
from VM import *
from bytecode import *


class Dragon:
    """
    Language class it has 2 type of running conventions run through file 
    and run through prompt. it includes error reporting methods. Basically
    input and what compiler want to suggest to a user/programmer
    """
    
    def __init__(self):
        self.hadError = False    
        
    def runFile(self,path):
        file = open(path,mode='r')
        all_of_it = file.read()
        file.close()
        self.run(all_of_it)
        if self.hadError : exit(-1)
        
    def runPrompt(self):        
        while True:
            print(">> ")
            line = input()
            if line == None : break
            self.run(line)
            self.hadError = False
            
    def run(self,source):
        try:
            scanner = Scanner(source,self)
        except:
            exit(-1)
        tokens = scanner.scanTokens()
        parse = Parser(tokens, self)
        statements = parse.parse()
        resolver = Resolve(statements,self)
        resolver.resolvii()
        statements = resolver.statements


        bytecode = codegen(statements)
        # print_bytecode(bytecode)

        with open ("bytecode_output.txt", "w") as f:
            for i in bytecode.insns:
                f.write(str(i) + "\n")
            f.close()

        v = VM()
        v.load(bytecode)
        v.execute()
        
        # if self.hadError : 
        #     return
        # try :
        #     interpreter = Interpreter2(statements,self)
        #     interpreter.interprete()
        # except:
        #     print("working")
        #     exit(-1)
        # interpreter = Interpreter2(statements,self)
        # interpreter.interprete()
        
            
    def error(self,line : int, message):
        self.report(line, "", message)
        
    def error(self,token : Token,message):
        if token.type == TokenType.EOF:
            self.report(token.line, "at end", message)
        else :
            self.report(token.line, " at '"+ token.lexeme +"'", message)
        
    def report(self,line, where, message):
        print("[line" + str(line) + "] Error" + str(where) + ": " + message)
        self.hadError = True
    
    def rint(self,statement):
        match statement:
            case Expression(expression):
                self.erint(expression)
            case Var(token,type,initializer):
                print(token.lexeme)
                self.erint(initializer)
            case If(condition, thenBranch, elseBranch):
                self.erint(condition)
                self.rint(thenBranch)
                if elseBranch:
                    self.rint(elseBranch)
            case While(condition,body):
                self.erint(condition)
                self.rint(body)
            case Block(body):
                for i in body:
                    self.rint(i)
            case Print(value):
                self.erint(value)
            case Function(name,type,params,body):
                print(name.lexeme)
                for i in params:
                    print(i[0].lexeme)
                self.rint(body)
            case Return(keyword,value):
                self.erint(value)
    
    def erint(self,expressio):
        match expressio:
            case Grouping(expression):
                self.erint(expression)
            case Unary(operator,right):
                self.erint(right)
            case Variable(name):
                print(name.lexeme)
            case Assign(name,value):
                print(name.lexeme)
                self.erint(value)
            case Let(name,e1,e2):
                print(name.lexeme)
                self.erint(e1)
                self.erint(e2)
            case Call(callee,arguments):
                print(callee.lexeme)
                for i in arguments:
                    self.erint(i)
            case Binary(left,operator,right):
                self.erint(left)
                self.erint(right)
                
        
        
        
def main():
    drag = Dragon()
    if len(sys.argv)>2:
        print("more than 2 arguments are not allowed")
        
    elif len(sys.argv)==2:
        drag.runFile(sys.argv[1])
        
    else:
        drag.runPrompt()
    
if __name__ == "__main__":
    main()