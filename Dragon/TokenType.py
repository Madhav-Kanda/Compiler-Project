from enum import Enum

class TokenType(Enum):
    # single character tokens
    LEFT_PAREN = 0
    RIGHT_PAREN = 1 
    LEFT_BRACE =2 
    RIGHT_BRACE =3
    COMMA =4 
    DOT = 5
    MINUS =6
    PLUS = 7 
    SEMICOLON =8 
    SLASH =9 
    STAR = 10
    EOF = 43
    
    # One or two character tokens.
    BANG = 11 
    BANG_EQUAL = 12
    EQUAL = 13 
    EQUAL_EQUAL = 14
    GREATER = 15 
    GREATER_EQUAL = 16
    LESS = 17
    LESS_EQUAL = 18
    
    # Literals.
    IDENTIFIER = 19
    STRING = 20
    NUMBER = 21
    
    # Keywords.
    AND = 22
    CLASS = 23
    ELSE = 24 
    FALSE = 25
    FOR = 27
    IF = 28
    NIL = 29
    OR = 30
    LET = 31 # print is not in our language (different from Lox)
    RETURN = 32
    SUPER = 33
    THIS = 34
    TRUE = 35
    IN = 36 # for let x = 3 in x*x this type of instructions in required 
    WHILE  = 37
    VAR = 38
    INT = 39
    BOOL = 40
    FLOAT = 41
    MUTE = 42
    FUN = 43
    PRINT = 44