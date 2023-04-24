# Checklist 

### Minimal
**A number type and arithmetic.**

**Let expressions.**

**A Boolean type, comparisons, and if-else.**

**Mutable variables.**

**A print operation that prints values to screen.**

**loops**

**Functions**

**Lists with operations cons, is-empty?, head, tail.**

### Intermediate

**Multiple number types such as fractions and integers. Quotient and division are different. Quotient has type (integer, integer) -> integer and division has type (fraction, fraction) -> fraction. An integer can be used wherever a fraction can be used.**

Parallel let (See let..and in Ocaml). 

An explicit unary boolifying operator. In Perl so x where x has any type produces a Boolean value. For example, if x is a number, it is true when non-zero. If x is a string, it is true when non-empty.

Static type checking. The expression (5>3) + 2 should be an error without evaluating anything.

for loop to iterate over lists.

**Mutable arrays with indexing, appending, popping, concatenation, element assignment.**

Allow declaration of type of array. For example let xs: Array[int] = [] in ... should prevent xs[0] ← 5/3.

### Advanced

Disallow mutable variables to change type. With the binding let mut p = True in ..., the variable p should only be assigned boolean values.

Step-by-step debugger for your programming language.

User-defined types – records.

First-class functions.


### **Extras**

**Error Synchronization**

**Implemented Bytecode**

**Dynamic Data type variables**

**Resolver pass**

**Recursive Functions**

**Type Casting**

**Dictionary**

