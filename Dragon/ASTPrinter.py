from dataclasses import dataclass
from Token import Token
from TokenType import TokenType
import Expr


class AstPrinter:
    def prin(expr):
        return expr.accept()

    def visit_binary_expr( expr: Expr.Binary) -> str:
        return AstPrinter.parenthesize(expr.operator.lexeme, [expr.left, expr.right])

    def visit_grouping_expr(expr: Expr.Grouping) -> str:
        return AstPrinter.parenthesize("group", [expr.expression])

    def visit_literal_expr( expr: Expr.Literal) -> str:
        return str(expr.value)

    def visit_unary_expr( expr: Expr.Unary) -> str:
        return AstPrinter.parenthesize(expr.operator.lexeme, [expr.right])

    def parenthesize( name: str, exprs) -> str:
        parts = []
        parts.append("(")
        parts.append(name)
        for expr in exprs:
            parts.append(" ")
            parts.append(expr.accept())
        parts.append(")")
        # print(parts)
        return "".join(parts)


# def main():
#     e1 = Expr.Unary(Token(TokenType.MINUS, "-", None, 1),Expr.Literal(123))
#     expression = Expr.Binary(
#         e1,
#         Token(TokenType.STAR, "*", None, 1),
#         Expr.Grouping(Expr.Literal(45.67)))

#     print(AstPrinter.prin(expression))

    
