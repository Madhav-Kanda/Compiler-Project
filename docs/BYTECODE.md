# **Bytecode**

It is used to represent the bytecode instructions that are generated by the compiler. It contains a list of Instruction objects that represent the individual instructions.

### **Codegen**

The codegen() function is the entry point for the code generator. It takes a list of Stmt objects (statements) as input and generates bytecode instructions based on the statements.

The do_codegen() function is a helper function that is used by codegen() to generate bytecode for individual statements.

The codegen\_() function is another helper function that is used by do_codegen() to generate bytecode for individual expressions.

### **Example**

Let's look at an example. Suppose we have the following code:

```
int a = 10;
int b = 20;

int c = a + b;
```

The corresponding Bytecode output is the following:

```
 ``0 PUSH            value = 10
   1 STORE           id = 2
   2 PUSH            value = 20
   3 STORE           id = 3
   4 LOAD            id = 2
   5 LOAD            id = 3
   6 ADD
   7 STORE           id = 4
   8 HALT
```

Here, the first column represents the instruction pointer. The second column represents the opcode. The third column represents the id/value.

- The first instruction is a PUSH instruction with a value of 10. This pushes the value 10 onto the stack.
- The next instruction is a STORE instruction with an id of 2. This stores the value 10 in the variable a.
- The next instruction is a PUSH instruction with a value of 20. This pushes the value 20 onto the stack.
- The next instruction is a STORE instruction with an id of 3. This stores the value 20 in the variable b.
- The next instruction is a LOAD instruction with an id of 2. This loads the value 10 from the variable a onto the stack.
- The next instruction is a LOAD instruction with an id of 3. This loads the value 20 from the variable b onto the stack.
- The next instruction is an ADD instruction. This adds the two values on the stack and pushes the result onto the stack.
- The next instruction is a STORE instruction with an id of 4. This stores the value 30 in the variable c.
- The next instruction is a HALT instruction. This halts the execution of the bytecode.
