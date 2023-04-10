class Token:
    """
    it has all reqired information to represent 1 token
    (type, lexeme, literal, line)
    """
    
    def __init__(self, type, lexeme, literal, line):
        self.type = type
        self.lexeme = lexeme
        self.literal = literal
        self.line = line
        
        
    def strConversion(self):
        return self.type + " " + self.lexeme + " " + self.literal
    
    
    
    