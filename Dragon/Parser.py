from TokenType import *
from Expr import *


class Parser:
    
    class ParseError(Exception):
        pass
    
    current =0 
    def __init__(self, tokens):
        self.tokens = tokens
        
    def parse(self):
        try:
            x = self.expression()
            return x
        except :
            return None
                
    def expression(self):
        return self.equality()
    
    def equality(self):
        expr = self.comparison()
        while(self.match([TokenType.BANG_EQUAL,TokenType.EQUAL_EQUAL])):
            operator = self.previous()
            right = self.comparison()
            expr = Binary(expr,operator,right)
            
        return expr
    
    def match(self, types):
        for type in types:
            if self.check(type):
                self.advance()
                return True
        
        return False
    
    def check(self, type):
        if(self.isAtEnd()): return False
        return self.peek().type == type;
    
    def advance(self):
        if not self.isAtEnd(): self.current+=1
        return self.previous()
    
    def isAtEnd(self) :
        return self.peek().type == TokenType.EOF;
    
    def peek(self) :
        return self.tokens[self.current];
  
    def previous(self):
        return self.tokens[self.current - 1];

    def comparison(self):
        expr = self.term()
        
        while(self.match([TokenType.GREATER,TokenType.GREATER_EQUAL,TokenType.LESS,TokenType.LESS_EQUAL])):
            operator = self.previous()
            right = self.term()
            expr = Binary(expr,operator,right)
            
        return expr
    
    def term(self):
        expr = self.factor()
        while self.match([TokenType.MINUS, TokenType.PLUS]):
            operator = self.previous()
            right = self.factor()
            expr = Binary(expr, operator, right)
        return expr
    
    def factor(self):
        expr = self.unary()
        while(self.match([TokenType.SLASH,TokenType.STAR])):
            operator = self.previous()
            right = self.unary()
            expr = Binary(expr,operator,right)
            
        return expr
    
    def unary(self):
        if( self.match([TokenType.BANG,TokenType.MINUS])):
            operator = self.previous()
            right = self.unary()
            return Unary(operator,right)
        return self.primary()
    
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