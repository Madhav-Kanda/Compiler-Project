import sys
from Scanner import Scanner
from Token import *
from TokenType import *
from Parser import *
from ASTPrinter import *
from Interpreter import *
from Resolve import *
from Environment import *

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
        statements2 = statements

        statements2 = Resolve(statements2, self)
        statements2.resolvii()
        if self.hadError : return
        try :
            interpreter = Interpreter(statements,self)
            interpreter.interprete()
        except:
            exit(-1)
        
            
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