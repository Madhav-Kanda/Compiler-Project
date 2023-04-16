# Checklist 

### Minimal
<input type="checkbox" checked> A number type and arithmetic.

<input type="checkbox" checked> Let expressions.

<input type="checkbox" checked> A Boolean type, comparisons, and if-else.

<input type="checkbox" checked> Mutable variables.

<input type="checkbox" unchecked> Strings with concatenation and slicing.

<input type="checkbox" checked>A print operation that prints values to screen.

<input type="checkbox" checked> loops

<input type="checkbox" checked> Functions

<input type="checkbox" checked>Lists with operations cons, is-empty?, head, tail.

### Intermediate

<input type="checkbox" checked> Multiple number types such as fractions and integers. Quotient and division are different. Quotient has type (integer, integer) -> integer and division has type (fraction, fraction) -> fraction. An integer can be used wherever a fraction can be used.

<input type="checkbox" unchecked>  Parallel let (See let..and in Ocaml). 

<input type="checkbox" unchecked> An explicit unary boolifying operator. In Perl so x where x has any type produces a Boolean value. For example, if x is a number, it is true when non-zero. If x is a string, it is true when non-empty.

<input type="checkbox" unchecked> Static type checking. The expression (5>3) + 2 should be an error without evaluating anything.

<input type="checkbox" unchecked> for loop to iterate over lists.

<input type="checkbox" checked>Mutable arrays with indexing, appending, popping, concatenation, element assignment.

<input type="checkbox" unchecked>Allow declaration of type of array. For example let xs: Array[int] = [] in ... should prevent xs[0] ← 5/3.

### Advanced

<input type="checkbox" unchecked> Disallow mutable variables to change type. With the binding let mut p = True in ..., the variable p should only be assigned boolean values.

<input type="checkbox" unchecked> Step-by-step debugger for your programming language.

<input type="checkbox" unchecked> User-defined types – records.


<input type="checkbox" unchecked> First-class functions.


### **Extras**

<input type="checkbox" checked> Error Synchronization

<input type="checkbox" checked> Implemented Bytecode without list

<input type="checkbox" checked> Dynamic Data type variables

<input type="checkbox" checked> Resolver pass

<input type="checkbox" checked> Recursive Functions
