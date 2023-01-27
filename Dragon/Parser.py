from TokenType import *
from Expr import *


class Parser:
    """
    class for making AST tree for expressions
    """
    
    class ParseError(Exception):
        pass
    
    current =0 
    def __init__(self, tokens):
        self.tokens = tokens
    
    # return head of the root node 
    def parse(self):
        try:
            x = self.expression()
            return x
        except :
            return None
                
    # parse the expression and return root of AST
    def expression(self):
        return self.equality()
    
    # parse equality operator
    def equality(self):
        expr = self.comparison()
        while(self.match([TokenType.BANG_EQUAL,TokenType.EQUAL_EQUAL])):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr,operator,right)
            
        return expr
    
    # if match with given types return True
    def match(self, types):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        
        return False
    
    # check current token is particular type or not
    def check(self, type):
        if(self.isAtEnd()): return False
        return self.peek().type == type;
    
    #  return current token and increase pointer by 1
    def advance(self):
        if not self.isAtEnd(): self.current+=1
        return self.previous()
    
    # check if pointer is at end of the code file 
    def isAtEnd(self) :
        return self.peek().type == TokenType.EOF;
    
    # returns current token
    def peek(self) :
        return self.tokens[self.current];
  
    # return previouse token
    def previous(self):
        return self.tokens[self.current - 1];

    # grammar non terminal comparison return expression with comparision operator as root if exists
    def comparison(self):
        expr = self.term()
        
        while(self.match([TokenType.GREATER,TokenType.GREATER_EQUAL,TokenType.LESS,TokenType.LESS_EQUAL])):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr,operator,right)
            
        return expr
    
    # grammar non terminal comparison return expression with (+,-) operator as root if exists
    def term(self):
        expr = self.factor()
        while self.match([TokenType.MINUS, TokenType.PLUS]):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        return expr
    
    # grammar non terminal comparison return expression with (/,*) operator as root if exists
    def factor(self):
        expr = self.unary()
        while(self.match([TokenType.SLASH,TokenType.STAR])):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr,operator,right)
            
        return expr
    # grammar non terminal comparison return expression with (!,-) operator as root if exists
    def unary(self):
        if( self.match([TokenType.BANG,TokenType.MINUS])):
            operator = self.previous()
            right = self.unary()
            return Unary(operator,right)
        return self.primary()
    # return leaf node of the tree
    def primary(self):
        if self.match([TokenType.FALSE]) : return Literal(False)
        if self.match([TokenType.TRUE]) : return Literal(True)
        if self.match([TokenType.NIL]) : return Literal(None)
        
        if self.match([TokenType.NUMBER,TokenType.STRING]) : return Literal(self.previous().literal)
        
        if self.match([TokenType.LEFT_PAREN]) : 
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN,"Expect ')' after expression")
            return Grouping(expr)
        
        raise self.error(self.peek(), "Expect expression")
        
    def consume(self,type, message):
        if self.check(type) : return self.advance()
        
        raise self.error(self.peek(), message)
    
    def error(self,token,message):
        dragon.Dragon.error(token,message)
        return self.ParseError()
    # synchronizing errors if we got an error don't kill the program try find other errors 
    # to do this if we got error in 1st line skip that line and go to next line
    def synchronize(self):
        self.advance()
        while(not self.isAtEnd()):
            if self.previous().type == TokenType.SEMICOLON : return
            
            match self.peek():
                case TokenType.CLASS: return
                case TokenType.FUN: return
                case TokenType.VAR: return
                case TokenType.FOR: return
                case TokenType.IF: return
                case TokenType.WHILE: return
                case TokenType.RETURN: return
            
            self.advance()
            
import dragon