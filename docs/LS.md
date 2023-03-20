# **Language specifications through examples.**

Language syntax has 2 main components statements and expressions.
Langugage is correct or error free if the program file contains list of error free statements. Also one statement is dependent on other so, program can only be run from top to bottom.

Syntax:

program :

          statement_1

          statement_2

          .......

there are different type of statements - variable declarations, if-else, while-loop, print, expression statements, etc. expression is component of the statement. For example

statement : identifier = expression

so in this case whatever comes after = operator should be expression if its statement then it will give an error.
More specific syntax we will see in below topics.

[1 Variables and data-types](#1)

[2 Variable initialization and assignment](#2)

[3 print statement](#3)

[4 operators](#4)

[5 block statements and Variable scope](#5)

[6 functions](#6)

[7 let expressions](#7)

[8 Project Euler](#8)




**<h2 id="1">Variables and data-types</h2>**
Language supports four types of variables
```
int
float
bool
string
```
for defining statically typed variables you can write below instructions:
```
int integer_variable;
float floatingnumber_variable;
string string_variable;
bool bool_variable;
``` 
we also supports dynamically typed variables you can define it using keyword var.
```
var dynamically_typed_variable;
```
Dynamic typing is a programming language feature where the type of a variable is determined at runtime instead of compile time. In dynamic typing, the data type of a variable can change dynamically during runtime based on the type of value it holds. Some languages, like Python, use dynamic typing instead of static typing.

The primary advantage of dynamic typing is that it makes programming more flexible and easier to use. Since the programmer doesn't have to declare the data type of a variable in advance, they can write code faster and with fewer lines of code. This also allows for more rapid prototyping and experimentation in programming, which can be helpful in the early stages of a project.

Now processors are faster than when C or other languages were written. So, we thought its good to have also dynamically typed variable. tradeoff is that we won't be able to show error at compile-time. 

**<h2 id="2">Variable initialization and assignment</h2>**
```
int a = 1;
int b = 1.5;
float c = 1;
float d = 1.0;
string e = "string variable";
var f = "you can write anything here";
```
a and b both will have value 1. c and d will have value 1.0. and f in this case has string type for now.
```
int a = 5;
a = 6;
```
after run of the programme a will have value 6.
```
int a = 5;
a = "5";
```
this will give you below error
```
[line2] Error at 'a': can't assign to Variable type int
```
if you want this kind of behaviour use below code.
```
var a = 5;
a = "5";
```
**<h2 id="3">print statement</h2>**
you can write print statement as 
```
print {expression}
```
**<h2 id="4">operators</h2>**
Language supports addition, subtraction, multiplication, division, comparison operators, unary negation, and, or operators.
[You can find the order and associativity of the code here.](PARSER.md)

code:
```
int a = 5*3-2+10/6;
var b = 5*3-2+10/6;
string c = "hello"+"world";
bool d = True or False;
bool e = True and True;
bool f = 1==2;
print a;
print b;
print c;
print d;
print e;
print f;
```
output:
```
14
14.666666666666666
helloworld
True
True
False
```
**<h2 id="5">block statements and Variable scope</h2>**
This langugage follows lexical scoping rules. therefore, all variables's scopes will be determined at the compile time. For writing block statements you can write it using brackets.
### If-Else statements (control flow)
code:
```
int a = 6;
if(a==6){
    print "you are in if block";
}
else{
    print "you are in else block";
}
```
output:
```
you are in if block
```
### While loop
code:
```
int a = 5;
int ans = 1;
while(a!=0){
    ans = ans*a;
    a = a-1;
}
print a;
```
output:
```
120
```
### Variable Scope Examples
code:
```
int a = 6;
{
    int a = 5;
    print a;
}
print a;
```
output:
```
5
6
```
code:
```
int b=6;
{
    int a = 7;
}
print a;
```
output:
```
[line5] Error at 'a': Variable is not defined
```
**<h2 id="6">functions</h2>**
function general syntax is:
$return_data_type $function_name(arguments of the form $data_type $arg_name){
    body
    return $value;
}
functions supports recursive calls.
code:
```
int fact(int n){
    if(n==1){
        return n;
    }
    else{
        return n*fact(n-1);
    }
}

print fact(5);
```
output:
```
120
```
**<h2 id="7">let expressions</h2>**
In programming, a let expression is a construct that allows you to bind a value to a variable, typically for a limited scope. The main advantage of using let expressions is that they provide a way to create local variables that are only visible within a specific block of code. This can help to reduce the risk of naming conflicts and make code easier to understand and reason about.

syntax:
let $variable_name = $expression_1 in $expression_2

code:
```
print let a = 5 in a*let a = 6 in 2*a;
```
output:
```
60
```

**<h2 id="8">Project Euler</h2>**

To validate the implementation of our compiler, we wrote the code of 5 problems from Project Euler in our compiler. All of the codes ran without any error being thrown and provided an output as expected. The questions, code and output can be accessed [here.](Euler.md)

