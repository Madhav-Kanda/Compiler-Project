from Environment import Environment


class Callable:
    def call(self, interpreter, arguments):
        pass

    def arity(self):
        pass


class Func(Callable):
    def __init__(self, name, parameters, body,closure):
        self.name = name
        self.parameters = parameters
        self.body = body
        self.closure = closure

    def call(self, interpreter, arguments):
        environment = Environment(self.closure)
        [
            environment.define(param.lexeme, arg)
            for param, arg in zip(self.parameters, arguments)
        ]

        interpreter.execute_block(
            statements=self.body, environment=environment
        )

    def arity(self):
        return len(self.parameters)

    def to_string(self):
        return f"<fn {self.name.lexeme}>"