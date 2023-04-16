# **VM**

This is a simple virtual machine (VM) designed to execute bytecode instructions. It has support for basic arithmetic operations, variables, and function calls.

**The VM class has four attributes:**

**1. bytecode:** an instance of the ByteCode class representing the bytecode to be executed.

**2. ip:** an integer representing the current instruction pointer.

**3. data:** a list of Literal objects representing the virtual machine stack.

**4. currentFrame:** an instance of the Frame class representing the current frame.

**The VM class has three methods:**

**1. load:** This method takes a ByteCode object as an argument and sets it as the current bytecode for the virtual machine.

**2. restart:** This method resets the virtual machine by setting the instruction pointer to 0 and clearing the data stack.

**3. run:** This method executes the bytecode instructions. It uses a switch statement to execute the instructions based on the opcode. It also uses a while loop to execute the instructions until the end of the bytecode is reached. The instructions that can be exectuted can be found in the [Instructions](INSTRUCTIONS.md) section.
