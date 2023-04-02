from Token import Token
from TokenType import TokenType

class Scanner :  
    
    
    keywords = {"and": TokenType.AND,
                "class" : TokenType.CLASS,
                "else" : TokenType.ELSE,
                "false": TokenType.FALSE,
                "for" : TokenType.FOR,
                "if": TokenType.IF,
                "nil" : TokenType.NIL,
                "or" : TokenType.OR,
                "return": TokenType.RETURN,
                "super" : TokenType.SUPER,
                "this" : TokenType.THIS,
                "true": TokenType.TRUE,
                "var" : TokenType.VAR,
                "while" : TokenType.WHILE,
                "let" : TokenType.LET,
                "in" : TokenType.IN,
                "int" : TokenType.INT,
                "bool" : TokenType.BOOL,
                "float" : TokenType.FLOAT,
                "mute" : TokenType.MUTE,
                "fun" : TokenType.FUN,
                "print": TokenType.PRINT,
                "string" : TokenType.STRING,
                "access" : TokenType.LIST_ACCESS, 
                "slice" : TokenType.LIST_SLICE,
                "append" : TokenType.LIST_APPEND,
                "pop" : TokenType.LIST_POP, 
                }  
    def __init__(self, source,dragon,tokens=[], start=0, current=0, line=1):
        self.source = source
        self.tokens = tokens
        self.start = start
        self.current = current
        self.line = line
        self.dragon = dragon
    
    def scanTokens(self):
        while not self.isAtEnd():
            self.start = self.current
            self.scanToken()
        self.tokens.append(Token(TokenType.EOF, "", None, self.line))
        return self.tokens
    
    def isAtEnd(self):
        return self.current >= len(self.source)
    
    def advance(self):
        self.current += 1
        return self.source[self.current - 1]
    
    
    def addToken(self, type, literal=None):
        text = self.source[self.start:self.current]
        self.tokens.append(Token(type, text, literal, self.line))
        

    def scanToken(self):
        c = self.advance()
        match c:
            case '(': 
                self.addToken(TokenType.LEFT_PAREN) 
            case ')': 
                self.addToken(TokenType.RIGHT_PAREN) 
            case '[':  # for list
                self.addToken(TokenType.LEFT_SQUARE)
            case ']':  # for list 
                self.addToken(TokenType.RIGHT_SQUARE) 
            case '{': 
                self.addToken(TokenType.LEFT_BRACE)
            case '}': 
                self.addToken(TokenType.RIGHT_BRACE)
            case ',': 
                self.addToken(TokenType.COMMA)
            case '.': 
                self.addToken(TokenType.DOT)
            case '-': 
                self.addToken(TokenType.MINUS)
            case '+': 
                self.addToken(TokenType.PLUS)
            case ';': 
                self.addToken(TokenType.SEMICOLON)
            case '*': 
                self.addToken(TokenType.STAR)
            case '!':
                self.addToken(TokenType.BANG_EQUAL if self.match('=') else TokenType.BANG)
            case '=':
                self.addToken(TokenType.EQUAL_EQUAL if self.match('=') else TokenType.EQUAL)
            case '<':
                self.addToken(TokenType.LESS_EQUAL if self.match('=') else TokenType.LESS)
            case '>':
                self.addToken(TokenType.GREATER_EQUAL if self.match('=') else TokenType.GREATER)
            case '/':
                if(self.match('/')):
                    while (self.peek() != '\n' and not self.isAtEnd()): self.advance()
                else:
                    self.addToken(TokenType.SLASH)
            
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass
            case '\n': 
                self.line+=1
            case '"':
                self.string()
            case _:
                if self.isDigit(c):
                    self.number()
                elif self.isAlpha(c):
                    self.identifier()
                else:   
                    self.dragon.error(self.line, "Unexpected character.")
    
    def identifier(self):
        while self.isAlphaNumeric(self.peek()): self.advance()
        text = self.source[self.start:self.current]
        type = None
        if text in self.keywords:
            type = self.keywords[text]
        else :
            type = TokenType.IDENTIFIER
        self.addToken(type)
    
    def number(self):
        while self.isDigit(self.peek()): self.advance()
        check = False
        if self.peek() == '.' and self.isDigit(self.peekNext()):
            check = True
            self.advance()
            while self.isDigit(self.peek()): self.advance()
        
        if check : self.addToken(TokenType.NUMBER, float(self.source[self.start:self.current]))
        else : self.addToken(TokenType.NUMBER, int(self.source[self.start:self.current]))
    
    def string(self):
        while self.peek() != '"' and not self.isAtEnd():
            if self.peek() == '\n': self.line+=1
            self.advance()
        
        if self.isAtEnd():
            self.dragon.error(self.line, "Unterminated string.")
            return
        
        self.advance()
        
        value = self.source[self.start+1:self.current-1]
        self.addToken(TokenType.STRING, value)
    
    def match(self, expected):
        if (self.isAtEnd()): return False
        if self.source[self.current] != expected: return False
        self.current += 1
        return True

    def peek(self):
        if self.isAtEnd(): return '\0'
        return self.source[self.current]
    
    def peekNext(self):
        if self.current + 1 >= len(self.source): return '\0'
        return self.source[self.current + 1]
    
    def isAlpha(self, c):
        return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z') or c == '_'
    
    def isAlphaNumeric(self, c):
        return self.isAlpha(c) or self.isDigit(c)
    
    def isDigit(self, c):
        return c >= '0' and c <= '9'
    
    
from dragon import Dragon
