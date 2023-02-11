from TokenType import *
from Expr import *
from Stmt import *


class Parser:
    """
    class for making AST tree for expressions
    """
    
    class ParseError(Exception):
        pass
    
    current =0 
    def __init__(self, tokens, dragon):
        self.tokens = tokens
        self.dragon = dragon
    
    # return head of the root node 
    def parse(self):
        statements = []
        while(not self.isAtEnd()) :
            statements.append(self.statement())
        return statements
            
    
    def statement(self) :
        # implement statements 
        if self.match([TokenType.PRINT]):
            return self.printStatement()
        if self.match([TokenType.IF]):
            return self.ifStatement()
        if self.match([TokenType.WHILE]):
            return self.whileStatement()
        if self.match([TokenType.LEFT_BRACE]):
            return self.blockStatement()
        if self.match([TokenType.INT,TokenType.STRING,TokenType.FLOAT,TokenType.VAR]):
            return self.declaration()
        
        return self.expressionStatement()
    
    def blockStatement(self):
        ans = Block(body = [])
        check =  self.match([TokenType.RIGHT_BRACE])
        while not check and not self.isAtEnd():
            ans.body.append(self.statement())
            check =  self.match([TokenType.RIGHT_BRACE])
        if not check :
            self.consume(TokenType.RIGHT_BRACE, "Expected '}'")
        return ans
            
        

    # print statement
    def printStatement(self):
        value = self.expression()
        self.consume(TokenType.SEMICOLON,"Expect ';' after value")
        return Print(value)
    
    # if statement
    def ifStatement(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after 'if'")
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after condition")
        thenBranch = self.statement()
        elseBranch = None

        if self.match([TokenType.ELSE]):
            elseBranch = self.statement()
        
        return If(condition,thenBranch,elseBranch)

    # while statement
    def whileStatement(self):
        
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after 'while'")
        condition = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after condition")
        body = self.statement()

        return While(condition,body)
    
    # expression statement
    def expressionStatement(self):
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ; after value")
        return Expression(expr)
    
    
    def declaration(self):
        return self.varDeclaration(self.previous().type)
        
    def varDeclaration(self, type):
        name = self.consume(TokenType.IDENTIFIER,"Expect variable name")
        initailizer = None
        if (self.match([TokenType.EQUAL])):
            initailizer = self.expression()
        
        self.consume(TokenType.SEMICOLON,"expect semicolon")
        vartype = None
        match type:
            case TokenType.INT : vartype = VarType.INT
            case TokenType.STRING : vartype = VarType.STRING
            case TokenType.FLOAT : vartype = VarType.FLOAT
            case TokenType.VAR : vartype = VarType.DYNAMIC
        return Var(name,vartype,initailizer)
    
    def assignment(self):

        expr = self.or_()
        if self.match([TokenType.EQUAL]):
                equals = self.previous()
                value = self.assignment()
                
                if isinstance(expr,Variable):
                    name = expr.name
                    return Assign(name,value)
                
                self.error(equals, "Invalid assignment target")

            
        return expr
        
    # or operator
    def or_(self):
        expr = self.and_()
        while(self.match([TokenType.OR])):
            operator = self.previous()
            right = self.and_()
            expr = Logical(expr,operator,right)
        return expr

    #and operator
    def and_(self):
        expr = self.equality()
        while(self.match([TokenType.AND])):
            operator = self.previous()
            right = self.equality()
            expr = Logical(expr,operator,right)
        return expr
            
    # parse the expression and return root of AST
    def expression(self):
        return self.assignment()
    
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
        if self.match([TokenType.IDENTIFIER]) : return Variable(self.previous())
        
        if self.match([TokenType.LEFT_PAREN]) : 
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN,"Expect ')' after expression")
            return Grouping(expr)
        # print(self.previous())
        raise self.error(self.peek(), "Expect expression")
        
    def consume(self,type, message):
        if self.check(type) : return self.advance()
        self.dragon.hadError = True
        raise self.error(self.peek(), message)
    
    def error(self,token,message):
        self.dragon.error(token,message)
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