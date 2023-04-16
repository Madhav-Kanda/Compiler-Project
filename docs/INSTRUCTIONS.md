# **INSTRUCTIONS**

This file contains the instructions for the stack VM. We have implemented the following instructions:

**1. PUSH(val):** This instruction pushes a literal value onto the top of the data stack.

**2. CALL():** This instruction performs a function call by creating a new frame and setting the instruction pointer (ip) to the entry point of the called function.

**3. RETURN():** This instruction returns from a function call by restoring the previous frame and setting the ip to the return address.

**4. UMINUS():** This instruction performs the unary minus operation on the top of the data stack.

**5. ADD():** This instruction pops the top two values from the data stack and pushes their sum onto the stack.

**6. SUB():** This instruction pops the top two values from the data stack and pushes their difference onto the stack.

**7. MUL():** This instruction pops the top two values from the data stack and pushes their product onto the stack.

**8. DIV():** This instruction pops the top two values from the data stack and pushes their quotient onto the stack.

**9. EXP():** This instruction pops the top two values from the data stack and pushes the result of raising the first value to the power of the second value onto the stack.

**10. EQ():** This instruction pops the top two values from the data stack and pushes a boolean value indicating whether they are equal onto the stack.

**11. NE():** This instruction pops the top two values from the data stack and pushes a boolean value indicating whether they are not equal onto the stack.

**12. LT():** This instruction pops the top two values from the data stack and pushes a boolean value indicating whether the first value is less than the second value onto the stack.

**13. GT()** This instruction pops the top two values from the data stack and pushes a boolean value indicating whether the first value is greater than the second value onto the stack.

**14. LE():** This instruction pops the top two values from the data stack and pushes a boolean value indicating whether the first value is less than or equal to the second value onto the stack.

**15. GE():** This instruction pops the top two values from the data stack and pushes a boolean value indicating whether the first value is greater than or equal to the second value onto the stack.

**16. JMP(label):** This instruction jumps to the specified label.

**17. JMP_IF_FALSE(label):** This instruction pops the top value from the data stack and jumps to the specified label if it is false.

**18. JMP_IF_TRUE(label):** This instruction pops the top value from the data stack and jumps to the specified label if it is true.

**19. NOT():** This instruction performs the logical not operation on the top of the data stack.

**20. DUP():** This instruction duplicates the top value on the data stack.

**21. POP():** This instruction removes the top value from the data stack.

**22. LOAD(localID):** This instruction loads the value of the specified local variable onto the data stack.

**23. STORE(localID):** This instruction stores the top value from the data stack into the specified local variable.

**24. HALT():** This instruction stops the execution of the program and returns the last value on the data stack.

**25. PUSHFN():** This instruction pushes the target offset of a function onto the data stack. The target offset is obtained from a label object associated with the function ID. The label object is stored in a dictionary mapping function IDs to their target offsets. The function ID is also appended to a list of function IDs. The instruction increments the instruction pointer (ip) by 1.
