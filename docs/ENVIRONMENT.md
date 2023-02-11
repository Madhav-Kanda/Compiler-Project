# **Environment**

## **Class and Attributes**
`StackEnvironment` class contains all required functionality to define variable, and change value of variable. it also get value of the variable based on lexical scoping. Shadowing of variable is also allowed. 

**Attributes**
`stack` - list of object Environment
`dragon` - object of class Dragon to report errors.

## **Language specifications**
Dragon supports lexical scoping. Errors related to defining variables. Typeerrors while assigning values will be reported by this class. 

**Example**
```
var a = 5;
if(a==5){
    var a = 6;
    print a;
}
print a;
```
here variable in if condition refers to variable a which value is 5. In if body prints statement's expression a refers to a whose value is 6. After if body variable a declared in the if body will be removed from environment. So, code will output
```
6
5
```  
