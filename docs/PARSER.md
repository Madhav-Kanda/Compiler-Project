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
| `or`| left |
| `and` | left |

language supports ifelse statements, expression statements, while statements, variable declaration statements.

## **Use of parser class**

class Parser contains 1 function that can be called to use functionality of the parser. this function will return list of statements. this statements will be used by interpreter to evaluate expressions and statements. All the errors related to syntax will be reported by parser. Type checking and runtime errors won't be reported by parser.


## **Synchronising errors**
synchrnoize() function is declared so that if we got an error, we don't kill the program and try finding other errors . 
To do this if we got error in a particular line, we skip that line and go to next line. 
This functions is called in parse() function whenever an exception is thrown. It helps recover from the error and continue parsing. 

## Test Examples
### test - 1 
```
int a = 
print(a);
```
**Output** 
```
[line2] Error at 'print': Expect expression
```
**Explanation** <br>
There is no expression after variable 'a' declaration 

<br>

### test - 2 
```
int a = 5
int b = 6;
print(a) 
```
**Output**
```
[line2] Error at 'int': expect semicolon
[line3] Errorat end: Expect ';' after value
```

**Explanation** <br>
There is no semicolon after variable 'a' declaration, so it expects a semicolon before line2. <br>
Parsing is continued, and another error after print statement is encounterd. There is no semicolon. 

<br>

### test - 3
```
int a = +5 - 4
print(a);
```
**Output**
```
[line1] Error at '+': Expect expression
```

**Explanation** <br>
Gives only one error of 'expect expression' and not of semicolon meaning once error encountered in a statement, that statement is skipped and pointer is moved to the next statement for parsing. 
