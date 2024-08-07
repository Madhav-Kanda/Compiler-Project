# **Dragon: Python-based Compiler**

## **Project Overview**

A Python-based compiler that can handle the complete compilation process, including lexical analysis, parsing, semantic analysis, and optimization. While also supporting a variable "var" that enhances the programming capabilities.

The target language for our compiler will be a high-level programming language in our project we are calling it Dragon, and we are evaluating with and without bytecode generation. Output given by parser can be run on variety of platforms. Our compiler will support advanced features such as error handling, making it suitable for both academic and commercial use.

In addition to its technical capabilities, our compiler also have a user-friendly interface, allowing even non-technical users to easily compile their code and run their programs. This  makes our compiler accessible to a wider range of users, and provide an excellent learning opportunity for anyone interested in compilers and computer languages. 

## **Getting Started**

### **Step 1: Clone the repository**

The first step is to clone the repository to your local machine. To do this, you'll need to have Git installed. Once you have Git installed, open up your terminal and run the following command:

```
git clone https://github.com/Syntax-Sorcerers/Compiler-Project.git
```

### **Step 2: Running the code**

Ensure that the python version is 3.10 or above. For running the code type the following command in the terminal:

```
python dragon.py ${relative-path}
```

Here ${relative-path} is the path of the .txt file containing the code to be executed relative to the Dragon folder (The present working directory being the dragon folder).

### **Step 3: Testing the compiler (Optional)**

To test the various aspects of the language and the compiler, we have provided a set of test cases in the test folder. To run the test cases, run the following command in the terminal:

```
python automated_test_runner.py
```

### ** Installing compiler as a command line tool**

To do this you just need to add this repository to user environment path and after that you can invoke compiler by typing dragon for example

```
dragon test.txt
```

## **Checklist for our language**

[Checklist](docs/Checklist.md)



## **Language specifications**

[Language features and examples](docs/LS.md)

## **Architecture**

For this project, we are using python 3.10. We will write all the features of our language and construct a parse tree. We will generate bytecode from parse-tree and also build VM for running bytecode. So, our compiler is a python application that can be run on any machine already installed python.

## **Documentations of different layers of the compiler**

[Scanner](docs/SCANNER.md) - tokenizing user given text file.

[Parser](docs/PARSER.md) - making AST tree for compiler.

[Interpreter](docs/INTERPRETER.md) - evaluating AST tree.

[Environment](docs/ENVIRONMENT.md) - data structure for binding value to its variables.

[Bytecode](docs/BYTECODE.md) - generating bytecode from AST tree.

[Resolver](docs/RESOLVER.md) - resolving variable and function references.

[VM](docs/VM.md) - virtual machine for running bytecode.

[VM Instructions](docs/INSTRUCTIONS.md) - instructions for VM.

[Checklist](docs/Checklist.md) - Tasks completed in the project.

## **Reference**

[Crafting Interpreter](https://craftinginterpreters.com/contents.html) - Robert Nystrom
