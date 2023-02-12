# **Scanner**

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

  ## **Use of Scanner class**

        Scanner is the first stage of a compiler. It scans the entire code and divides the code into Tokens. These tokens
        are then stored in a list made available for the Parser to work upon them for semantic analysis. It is here 
        where the first differentiation is done on the basis of keywords, comments, whitespaces, operators and the 
        most important which is expressions. 
