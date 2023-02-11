# **Parser**
## **class and attributes** 

It contains **Parser** class its attributes are tokens and dragon

`tokens` - list of class Token 

`dragon` - object of dragon class

We will make parse tree from list of tokens. Scanner doesn't make sure that token sequence is correct or not. these syntax errors will be shown by this class. dragon attribute is necessary to report any errors.

## **Language specifications needed for Parser**

Dragon language is sequence of statements. Statements uses expression to complete purpose of the user. Language supports below operators. Operators precedence is decreaseing from top to bottom.

| Operators | Associativity |
| --- | --- |
| `!` , `- unary` | right |
| `*` , `/` | left |
| `+` , `-` | left |
| `<=` , `>=` , `<`, `>`  | no |
| `!=` , `==` | no |
| `=` | right |

language supports ifelse statements, expression statements, while statements, variable declaration statements.

## **Use of parser class**

class Parser contains 1 function that can be called to use functionality of the parser. this function will return list of statements. this statements will be used by interpreter to evaluate expressions and statements. All the errors related to syntax will be reported by parser. Type checking and runtime errors won't be reported by parser.

