# **Interpreter**

## **1. Typechecking**

Whenever we are evaluating a binary expression, the `checktypecompatibility` function will check the type of both the left as well as the right expression.

If the type matches, then the operation is compatible.

But let say if you try to operate a `+` between an *integer* and a *string*, then the function will raise a type error.

## **Some test case examples** 

### Test - 1 
```
print(1 < 2)
```
**Output** 
```
True
```
**Explanation** <br>
the left operand is 1 (*integer*), the right operand is also an *integer*. So, they are type compatible, hence *True* is printed by the interpreter.

<br>

### Test - 2 
```
int a = 5;
var b = "hello";
print(a + b);
```
**Output**
```
[line3] Error at '+': <class 'int'> and <class 'str'> are incompatible with the operator +
```

**Explanation** <br>
The type of a is an *integer*, where as the type of b is a *string*, so if anyone tries to operate a plus sign between an integer and a string, the interpreter will consider it as a `type` error, and will generate an `incompatibility` error.

<br>

### Test - 3
```
int a = 5;
float b = 2.7;
print(a*b);
```
**Output**
```
13.5
```

**Explanation** 
The interpreter allows to operate *integers* and *floating point* numbers. Hence, in the above test case, it doesn't show a error. Instead, it prints the correct value of the multiplication *i.e.* 13.5
<br><br>

## **2. Invalid operations over strings**
If we try to subtract, multiply or divide 2 strings, then the interpreter will give error. 

This has been handled by the `stringbystring` function. It checks for the type of both the operands, if they both are strings and any one of the above mentioned operations are performed, then it will raise an error.

## **Some test case examples** 

### Test - 1 
```
var a = "s";
var b = "t";
print(a/b);
```
**Output** 
```
[line3] Error at '/': <class 'str'> and <class 'str'> are incompatible with the particular operation /
```
**Explanation** <br>
Both the operands are string, and we try to divide them which is illogical, hence, the interpreter generates an error.

<br>

### Test - 2 
```
var a = "hello ";
var b = "world";
print(a + b);
```
**Output**
```
hello world
```

**Explanation** <br>
Both the operands of are of type *string*, but the operation is *plus* meaning concatenation. Hence, the interpreter considers this as valid and allows this.

<br>




