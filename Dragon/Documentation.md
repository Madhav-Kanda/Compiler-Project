## Lexical Analysis

A program written in Dragon is read by Scanner.py. The code which is the input is divided into tokens for further use.
Below documentation shows how the scanner.py scans the file and divides into tokens based on keywords, identifier, 
number or string. 

#### Allowed Keywords:
    and      class     else     false     for     if
    nil      or        return   super     this    true
    var      while     let      in        int     bool
    float    mute      fun
                
#### Some common nuances:
    1. Not a token:
          Whitespace: ' '
          Raw string: '\r'
          Tab:        '\t'
    2. A token:
          Newline:    '\n'
     
#### Comments:
     Comments start with '//' and all text after this is ignored till the end of the comment or till the
     end of a line. Comments are ignored by the syntax.
     
#### Whitespace:
     Whitespace is ignored as a token by the scanner but it is used to separate tokens. For Ex: ab is one
     token but a b are two separate tokens.
     
#### Delimiters:
    (       )       {       }       ,       .
    ;       !       =         

#### Operators:
    -       +       *       /       <       >
    
#### Identifiers supported
     1. Strings
     2. Numbers
     3. Keywords
     4. Miscellaneous Identifiers

## Expressions:
    1. Binary:
       Takes two expressions and gives a single expression. 
       Ex: + (Addition operator),
           - (Subtration operator),
           * (Multiplication operator) and 
           / (Division operator).
       
    2. Grouping:
       Contains a single Expression.
       
    3. Literal:
       Contains the variable types currently allowed in the language.
       Ex: boolean(bool), integer(int) and floating point(float).
       
    4. Unary:
       Takes a single expression and returns a single expression. 
       Ex: + (greater than zero indicator)
           - (less than zero indicator)
           ++ (increment by one)
           -- (decrement by one)
           ! (complement, reverts the value of a boolean variable)
  
  ## Statements:
     1. Expression
     2. Var
  
  ## Parsing:
     
     1. Var Declaration:
        Assign the respective variables to their datatypes from the tokens 
        obtained after scanning/lexing. Currently supports int, string, float
        and dynamic.
     2. Assignment:
        Assigns the value after the equals-to (=) operator to the variable type 
        before it.
     3. or_:
        Checks for and_(and) operator first. If not found, the while loop checks 
        for multiple "or's" and assigns it to a Logical binding defined in 
        "Expr.py". If and_(and) operator is found it goes to the and_ function.
     4. and_: 
        Assigns the value after the equals-to (=) operator to the variable type 
        before it. Then the while loop checks for multiple "and's" and assigns 
        it to a Logical binding defined in "Expr.py."
     5. Comparison:
        Returns the expression for greater-than, less-than, greater and lesser operators.
     6. Term:
        Parses plus and minus signs expressions.
     7. Factor:
        Parses multiplication and division expressions.
     8. Unary:
        Parses unary operators like ! and -.
     9. Error: 
        Returns all the errors if any in the program.
 

## Printing the AST Tree

    To convert the implemented AST tree into a string representing nesting structure of the tree, 
    we can use the AstPrinter from ASTPrinter class. Given an AST tree of the form:
    
   <img width="125" alt="image" src="https://user-images.githubusercontent.com/76394914/215323892-aad3c54b-a9e6-4842-ac66-9d4f4c4771c0.png">

     We will convert it to produce (*(-123)(group 45.67))
         
### Implementation
    We have implemented the ASTPrinter class. Upon calling its prin function, it calls the correponding accept method of each
    expression. This accept function further calls the visit_ method corresponding to its type. In visit_ method's implementation, 
    the literal are directly converted to the string whereas in other expressions we call the parenthesize() helper method. It 
    takes name and list of subexpressions and wraps them all in paranthesis. This returns the string expression to be printed.
    
