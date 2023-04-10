from TokenType import *
from Expr import *
from Stmt import *
from instructions import *
from VM import *

class ByteCode:
    insns: list[Instruction]

    def __init__(self):
        self.insns = []

    def label(self):
        return Label(-1)

    def emit(self, instruction):
        self.insns.append(instruction)

    def emit_label(self, label):
        label.target = len(self.insns)


def codegen(statements):
    code = ByteCode()
    do_codegen(statements, code)
    code.emit(I.HALT())
    return code


def do_codegen (statements, code):
    for statement in statements:
        codegen_(statement, code)

def codegen_(statement, code):
    ops = {
        TokenType.PLUS: I.ADD(),
        TokenType.MINUS: I.SUB(),
        TokenType.STAR: I.MUL(),
        TokenType.SLASH: I.DIV(),
        TokenType.BANG_EQUAL: I.NE(),
        TokenType.EQUAL_EQUAL: I.EQ(),
        TokenType.GREATER: I.GT(),
        TokenType.GREATER_EQUAL: I.GE(),
        TokenType.LESS: I.LT(),
        TokenType.LESS_EQUAL: I.LE(),
    }

    match statement:

        case Expression(expression):
            codegen_(expression, code) 
        case Binary(left, operator, right):
            codegen_(left, code)
            codegen_(right, code)
            code.emit(ops[operator.type]) 
        case Literal(value):
            code.emit(I.PUSH(value))    
        case Variable(name):
            code.emit(I.LOAD(name.lexeme[1]))
        case Var(token, type, initializer):
            codegen_(initializer, code)
            code.emit(I.STORE(token.lexeme[1]))
        case Assign(name, value):
            codegen_(value, code)
            code.emit(I.STORE(name.lexeme[1]))
        case Grouping(expression):
            codegen_(expression, code)
        case Unary(operator, right):
            codegen_(right, code)
            if operator.type == TokenType.MINUS:
                code.emit(I.NEG())
            elif operator.type == TokenType.BANG:
                code.emit(I.NOT())
        case Block(body):
            for s in body:
                codegen_(s, code)
        case Let(name, e1, e2):
            codegen_(e1, code)
            code.emit(I.STORE(name.lexeme[1]))
            codegen_(e2, code)
        case If(cond, iftrue, iffalse):
            E = code.label()
            F = code.label()
            codegen_(cond, code)
            code.emit(I.JMP_IF_FALSE(F))
            codegen_(iftrue, code)
            code.emit(I.JMP(E))
            code.emit_label(F)
            codegen_(iffalse, code)
            code.emit_label(E)
        case While(cond, body):
            B = code.label()
            E = code.label()
            code.emit_label(B)
            codegen_(cond, code)
            code.emit(I.JMP_IF_FALSE(E))
            codegen_(body, code)
            code.emit(I.JMP(B))
            code.emit_label(E)
            code.emit(I.PUSH(None))
        case _:
            pass




