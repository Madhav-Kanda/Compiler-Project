from TokenType import *
from Expr import *
from Stmt import *


class Parser:
    """
    class for making AST tree for expressions
    """
    
    class ParseError(Exception): # handle errors
        pass
    
    current = 0 
    def __init__(self, tokens, dragon):
        self.tokens = tokens
        self.dragon = dragon
    
    # return head of the root node 
    def parse(self):
        statements = []
        while True: # loop until end of file
            try: 
                # try to parse the file
                while (not self.isAtEnd()) : 
                    statements.append(self.statement())
                
                return statements

            except self.ParseError: 
                # if there is an error in parsing
                # synchronize the parser
                # recovers from the error and continues parsing 
                self.synchronize() 
    
    def statement(self) :
        # implement statements 
        if self.match([TokenType.PRINT]):
            return self.printStatement()
        if self.match([TokenType.IF]):
            return self.ifStatement()
        if self.match([TokenType.WHILE]):
            return self.whileStatement()
        if self.match([TokenType.FOR]):
            return self.forStatement()
        if self.match([TokenType.LEFT_BRACE]):
            return self.blockStatement()
        if self.match([TokenType.INT,TokenType.STRING,TokenType.FLOAT,TokenType.VAR, TokenType.BOOL]):
            return self.declaration()
        if self.match([TokenType.RETURN]):
            return self.returnStatement()
    
        
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
            

    def returnStatement(self):
        keyword = self.previous()
        value = None
        if not self.check(TokenType.SEMICOLON):
            value = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ';' after return value.")
        return Return(keyword, value)
        

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

    # for statement
    def forStatement(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after 'for'")
        
        initializer = None
        if self.match([TokenType.SEMICOLON]):
            initializer = None
        elif self.match([TokenType.INT,TokenType.STRING,TokenType.FLOAT,TokenType.VAR, TokenType.BOOL]):
            initializer = self.varDeclaration(self.previous().type)
        else:
            initializer = self.expressionStatement()
        
        condition = None
        if not self.check(TokenType.SEMICOLON):
            condition = self.expression()
        self.consume(TokenType.SEMICOLON,"Expect ';' after loop condition")
        
        increment = None
        if not self.check(TokenType.RIGHT_PAREN):
            increment = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after for clauses")

        body = self.statement()

        if increment is not None:
            body = Block([body,Expression(increment)])

        if condition is None:
            condition = Literal(True)

        body = While(condition,body)

        if initializer is not None:
            body = Block([initializer,body])

        return body
    
    # expression statement
    def expressionStatement(self):
        expr = self.expression()
        self.consume(TokenType.SEMICOLON, "Expect ; after value")
        return Expression(expr)
    
    
    def declaration(self):
        return self.varDeclaration(self.previous().type)
        

    def function(self, name,type):
        parameters = []
        if not self.check(TokenType.RIGHT_PAREN):
            condition = True
            while condition:
                if len(parameters) >= 255:
                    self.error(
                        token=self.peek(),
                        message="Can't have more than 255 parameters."
                    )
                param_type = None
                l = [TokenType.INT, TokenType.FLOAT, TokenType.STRING,TokenType.VAR, TokenType.BOOL]
                checking = True
                for i in l:
                    if(self.check(i)):
                        match i:
                            case TokenType.INT: param_type = VarType.INT
                            case TokenType.BOOL: param_type = VarType.BOOL
                            case TokenType.FLOAT: param_type = VarType.FLOAT
                            case TokenType.STRING: param_type = VarType.STRING
                            case TokenType.VAR: param_type = VarType.DYNAMIC
                        self.advance()
                        checking = False
                if checking:
                    self.consume(TokenType.INT,message="Expect variable type")
                                           
                param_token = self.consume(
                    type=TokenType.IDENTIFIER, message="Expect parameter name."
                )
                parameters.append((param_token,param_type))
                condition = self.match([TokenType.COMMA])

        self.consume(
            type=TokenType.RIGHT_PAREN, message="Expect ')' after parameters."
        )
        self.consume(
            type=TokenType.LEFT_BRACE, message="Expect '{' before body."
        )
        match type:
            case TokenType.INT: type = VarType.INT
            case TokenType.BOOL: type = VarType.BOOL
            case TokenType.FLOAT: type = VarType.FLOAT
            case TokenType.STRING: type = VarType.STRING
            case TokenType.VAR: type = VarType.DYNAMIC
        body = self.blockStatement()
        return Function(name,type, parameters, body)


    def varDeclaration(self, type):
        name = self.consume(TokenType.IDENTIFIER,"Expect variable name")
        initailizer = None

        if (self.match([TokenType.EQUAL])):
            initailizer = self.expression()

        elif(self.match([TokenType.LEFT_PAREN])) :
            return self.function(name,type)
        
        self.consume(TokenType.SEMICOLON,"expect semicolon")

        
        vartype = None
        match type:
            case TokenType.INT : vartype = VarType.INT
            case TokenType.BOOL : vartype = VarType.BOOL
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
            expr = Binary(expr,operator,right)
        return expr

    #and operator
    def and_(self):
        expr = self.equality()
        while(self.match([TokenType.AND])):
            operator = self.previous()
            right = self.equality()
            expr = Binary(expr,operator,right)
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
                # print(type)
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
        # print(self.tokens[self.current])
        return self.tokens[self.current];
  
    # return previouse token
    def previous(self):
        return self.tokens[self.current - 1];

    def getbehind(self):
        self.current = self.current - 1;
        return self.tokens[self.current];
    

        

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
        if self.match([TokenType.LET]):
            return self.letStatement()
        return self.call()
    
    # parsing the let statement
    # first there should be a let keyword, then we expect a variable name
    # then we expect a "=" sign, then we expect expression 1 followed by
    # "in" followed by expression 2, ending with a semicolon
    def letStatement(self):
        name = self.consume(TokenType.IDENTIFIER,"Expect variable name")
        self.consume(TokenType.EQUAL, "Expect '=' after the variable name")
        e1 = self.expression()
        self.consume(TokenType.IN, "Expect 'in' after expression 1")
        if (self.match([TokenType.LET])):
                e2 = self.letStatement()
        else:
            e2 = self.expression()

        return Let(name, e1, e2)

    def call(self):
        expr = self.primary()
        if self.match([TokenType.LEFT_PAREN]):  
            if(isinstance(expr,Variable)):
                expr = self.finishCall(expr)
            else:
                self.current-=1
                self.consume(TokenType.IDENTIFIER,"expect function name")

        return expr

    def finishCall(self,callee):
        arguments = []
        if not self.check(TokenType.RIGHT_PAREN):   ## If the next token is not a right parenthesis just to handle the case when no arguments present
            while True:
                if len(arguments) >= 255:       ## Keeping track of the maximum limit of the arguments that can be passed based Java's upper limit of the number of arguments
                    self.error(self.peek(),"Can't have more than 255 arguments")
                arguments.append(self.expression())
                if not self.match([TokenType.COMMA]): break     ## If the next token is not a comma then break the loop as no more arguments will be present
        paren = self.consume(TokenType.RIGHT_PAREN,"Expect ')' after arguments")
        return Call(callee.name,arguments)
 
    
    # return leaf node of the tree
    def primary(self):
        if self.match([TokenType.LEFT_SQUARE]): return self.list() 
        if self.match([TokenType.LIST_LENGTH]): return self.list_length()
        if self.match([TokenType.LIST_ISEMPTY]): return self.list_isempty() 
        if self.match([TokenType.LIST_ACCESS]): return self.list_access() 
        if self.match([TokenType.LIST_HEAD]): return self.list_head()
        if self.match([TokenType.LIST_TAIL]): return self.list_tail()
        if self.match([TokenType.LIST_SLICE]): return self.list_slice() 
        if self.match([TokenType.LIST_APPEND]): return self.list_append()
        if self.match([TokenType.LIST_POP]): return self.list_pop()
        if self.match([TokenType.FALSE]) : return Literal(False)
        if self.match([TokenType.TRUE]) : return Literal(True)
        if self.match([TokenType.NIL]) : return Literal(None)
        
        if self.match([TokenType.NUMBER,TokenType.STRING]) : return Literal(self.previous().literal)
        if self.match([TokenType.IDENTIFIER]) : return Variable(self.previous())
        
        if self.match([TokenType.LEFT_PAREN]) : 
            expr = self.expression()
            self.consume(TokenType.RIGHT_PAREN,"Expect ')' after expression")
            return Grouping(expr)
        
        raise self.error(self.peek(), "Expect expression") 

    def list(self):
        elements = []
        if not self.check(TokenType.RIGHT_SQUARE):
            while True:
                elements.append(self.expression()) 
                if not self.match([TokenType.COMMA]): break
        self.consume(TokenType.RIGHT_SQUARE,"Expect ']' after list elements") 
        return List(elements)  
    
    def list_length(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after list length")
        list = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after list")
        return ListLength(list)
    
    def list_isempty(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after list isempty")
        list = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after list")
        return ListIsEmpty(list)
    
    def list_access(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after list index")
        list = self.expression()
        self.consume(TokenType.COMMA,"Expect ',' after list")
        index = self.expression() 
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after index")
        return ListAccess(list,index) 
    
    def list_head(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after list head")
        list = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after list")
        return ListHead(list)

    def list_tail(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after list tail")
        list = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after list")
        return ListTail(list)

    def list_slice(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after list slice")
        list = self.expression()
        self.consume(TokenType.COMMA,"Expect ',' after list")
        start = self.expression()
        self.consume(TokenType.COMMA,"Expect ',' after start index")
        end = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after end index")
        return ListSlice(list,start,end) 

    def list_append(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after list append")
        list = self.expression()
        self.consume(TokenType.COMMA,"Expect ',' after list")
        element = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after element")
        return ListAppend(list,element)
    
    def list_pop(self):
        self.consume(TokenType.LEFT_PAREN,"Expect '(' after list pop")
        list = self.expression()
        self.consume(TokenType.RIGHT_PAREN,"Expect ')' after list")
        return ListPop(list) 
        
        
    def consume(self,type, message):
        if self.check(type) : return self.advance()
        self.dragon.hadError = True 
        raise self.error(self.peek(), message) 
    
    def error(self,token,message):
        self.dragon.error(token,message)
        # return ParseError class to handle error 
        return self.ParseError() 
    
    # synchronizing errors if we got an error don't kill the program try find other errors 
    # to do this if we got error in 1st line skip that line and go to next line
    def synchronize(self): 
        self.advance()
        while(not self.isAtEnd()): # if we are not at end of the file
            if self.previous().type == TokenType.SEMICOLON : return # if we found semicolon return
            
            match self.peek(): 
                case TokenType.CLASS: return
                case TokenType.FUN: return
                case TokenType.VAR: return
                case TokenType.FOR: return
                case TokenType.IF: return
                case TokenType.WHILE: return
                case TokenType.RETURN: return
            
            self.advance() 
