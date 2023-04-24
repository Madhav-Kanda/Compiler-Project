# Checklist 

### Minimal
&#9745; **A number type and arithmetic.**

&#9745; **Let expressions.**

&#9745; **A Boolean type, comparisons, and if-else.**

&#9745; **Mutable variables.**

&#9745; **A print operation that prints values to screen.**

&#9745; **loops**

&#9745; **Functions**

&#9745; **Lists with operations cons, is-empty?, head, tail.**

### Intermediate

&#9745; **Multiple number types such as fractions and integers. Quotient and division are different. Quotient has type (integer, integer) -> integer and division has type (fraction, fraction) -> fraction. An integer can be used wherever a fraction can be used.**

&#9744; Parallel let (See let..and in Ocaml). 

&#9744; An explicit unary boolifying operator. In Perl so x where x has any type produces a Boolean value. For example, if x is a number, it is true when non-zero. If x is a string, it is true when non-empty.

&#9744; Static type checking. The expression (5>3) + 2 should be an error without evaluating anything.

&#9744; for loop to iterate over lists.

&#9745; **Mutable arrays with indexing, appending, popping, concatenation, element assignment.**

&#9744; Allow declaration of type of array. For example let xs: Array[int] = [] in ... should prevent xs[0] ← 5/3.

### Advanced

&#9744; Disallow mutable variables to change type. With the binding let mut p = True in ..., the variable p should only be assigned boolean values.

&#9744; Step-by-step debugger for your programming language.

&#9744; User-defined types – records.

First-class functions.


### **Extras**

&#9745; **Error Synchronization**

&#9745; **Implemented Bytecode**

&#9745; **Dynamic Data type variables**

&#9745; **Resolver pass**

&#9745; **Recursive Functions**

&#9745; **Type Casting**

&#9745; **Dictionary**

