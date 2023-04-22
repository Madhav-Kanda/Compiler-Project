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
    LEFT_SQUARE = 47
    RIGHT_SQUARE = 48
    LIST_ACCESS = 49 # for list indexing 
    LIST_SLICE = 50 # for list slicing 
    LIST_APPEND = 51 # for list appending 
    LIST_POP = 52 # for list popping 
    LIST_LENGTH = 53 # for list length 
    LIST_ISEMPTY = 54 # for list empty or not 
    LIST_HEAD = 55 # for list head
    LIST_TAIL = 56 # for list tail
    MODULO = 57 # for modulo (%) operator 
    LIST_ASSIGN = 58 # for list assignment 
    COLON = 59 # for dictionary
    DICT_ACCESS = 60 # for dictionary indexing 
    DICT_LENGTH = 61 # for dictionary length
    DICT_ASSIGN = 62 # for dictionary assignment
    DICT_ADD = 63 # for dictionary adding
    DICT_REMOVE = 64 # for dictionary removing
    DICT_FIND = 65 # for dictionary finding 

    
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
    STRING_ACCESS = 66
    STRING_SLICE = 67
    STRING_LENGTH = 68
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
    FUN = 45
    PRINT = 44
    DYNAMIC = 46
    UMINUS = 58 # for unary minus operator
    NUMSTR = 99
    STRNUM = 100