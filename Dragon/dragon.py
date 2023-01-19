import sys
import Scanner
import TokenType
import Token

class Dragon:
    """
    Language class it has 2 type of running conventions run through file 
    and run through prompt. it includes error reporting methods. Basically
    input and what compiler want to suggest to a user/programmer
    """
    
    hadError = False
    
    def __init__(self):
        pass
    
    def runFile(path):
        file = open(path,mode='r')
        all_of_it = file.read()
        file.close()
        Dragon.run(all_of_it)
        if Dragon.hadError : exit(-1)
        
    def runPrompt():        
        while True:
            print(">> ")
            line = input()
            if line == None : break
            Dragon.run(line)
            Dragon.hadError = False
            
    def run(self,source):
        scanner = Scanner()
        tokens = scanner.scanTokens()
        
        for token in tokens:
            print(token)
            
    def error(line, message):
        Dragon.report(line, "", message)
        
    def report(line, where, message):
        print("[line" + line + "] Error" + where + ": " + message)
        Dragon.hadError = True
        
def main():
    if sys.argv>2:
        print("more than 2 arguments are not allowed")
        
    elif sys.argv==2:
        Dragon.runFile(sys.argv[1])
        
    else:
        Dragon.runPrompt()
    