from dataclasses import dataclass
from typing import List
from Token import Token
from TokenType import TokenType
import Expr


class AstPrinter:
    def print(self, expr):
        return expr.accept(self)

    def visit_binary_expr(self, expr: Expr.Binary) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.left, expr.right)

    def visit_grouping_expr(self, expr: Expr.Grouping) -> str:
        return self.parenthesize("group", expr.expression)

    def visit_literal_expr(self, expr: Expr.Literal) -> str:
        if expr.value is None:
            return "nil"
        return str(expr.value)

    def visit_unary_expr(self, expr: Expr.Unary) -> str:
        return self.parenthesize(expr.operator.lexeme, expr.right)

    def parenthesize(self, name: str, *exprs: Expr) -> str:
        parts = []
        parts.append("(")
        parts.append(name)
        for expr in exprs:
            parts.append(" ")
            parts.append(expr.accept(self))
        parts.append(")")
        return "".join(parts)


def main():
    expression = Expr.Binary(
        Expr.Unary(Token(TokenType.MINUS, "-", None, 1),Expr.Literal(123)),
        Token(TokenType.STAR, "*", None, 1),
        Expr.Grouping(Expr.Literal(45.67)))

    print(AstPrinter().print(expression))

main()