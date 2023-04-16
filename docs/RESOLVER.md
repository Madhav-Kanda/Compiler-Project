**<h2 id="9">Resolver</h2>**

The convention for scoping for Dragon is Lexical Scoping. Resolver provides a convenient way to resolve variable names and values in a set of statements and expressions. It plays an important role as it helps to ensure that variable names and values are correctly resolved according to Lexical Scoping or the construct of the scoping as defined in a language. 

**Class Structure**
Class named is Resolve. It initiliases the id's to the variables to be 1. Resolvii calls resolve function which has two functions for expressions and statements namely resolveExpression and resolveStatement.

**ID increment**
For assigning the ids to the variables and to get Lexical Scoping, id variable is increased if we enter a function, nested LET, different params and variables.

**Binding Change**
For any variable, in any expression or statement, the binding of the variable is changed as follows: <br>
Before: a <br>
After: (a,id)

**Features**

The Variable Resolution Tool provides a wide range of features for resolving variable names and values in statements and expressions, including:


I. Expressions:
1. Resolving binary operators: Calls resolveExpression on left and right operands.
2. Resolving variable names: The main action of resolver happens here. Ex: The binding of variable "a" will change as (a, 1), if 1 is the id assigned to it.
So a->(a,1)
3. Resolving let expressions:
Resolver action is performed by incrementing id on entering the block. Here the variable is resolved according to the above explaination in Resolving variable names.
4. Resolving grouping expressions
5. Resolving assign statements
6. Resolving function calls: Resolver action performed as per binding name ->(binding name, id)
7. Resolving list operations, including access, length, isEmpty, head, tail, slice, append, and pop

II. Statements:
1. Var:
On seeing a variable, id is incremented by 1 so different ids are assigned each time. Resolver action is performed again according to same construct.

2. Block: 
Enter and exit the block and resolve body in between.

3. Print
4. If:
Resolve the condition, resolve "then branch", then checks for else branch.
5. While: 
Evaluate the condition, the resolve the body.
6. Function:
id is again incremented on entering the function. Binding is changed. For each param, id is assigned and incremented for each param. The binding is changed for each param. Then body is resolved and we exit the block. 
7. Return

The tool uses a stack-based environment to keep track of variable mappings, which helps to ensure that variable values are correctly resolved and scoped according to the programming language's rules.


**Interpreter** <br>
Yes, we have a second interpreter! You might be wondering why? If you revisit the above documentation, you might have come across the change in binding from a to (a,id). Now in the old interpreter, it was able to interpret based on the var name a alone but to process (a,id) is not possible. Hence the change.

The major reasons for interpreter2 are:

1. Usage of Frames over Stack Environment. Interpreter1 uses Stack Environment whereas Interpreter2 uses Frames. Because of this change, we only need to change our block or environment when we enter a function. Earlier we used to append a new dictionary which was our environment to the Stack in Nested Let, Function, Entering a Block. But now only for functions do we change it.

2. Interpreter2 interprets by accessing the id. Lexical scoping is thus achieved.

The entire code for interpreter2 is almost similar to interpreter just the change is in the way of accessing the binding for the variables. 


