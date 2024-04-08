from objects.lexer import Lexer
from objects.interpreter import Interpreter
from objects.parser import Parser


def main():
    while True:
        try:
            text = input('Введіть вираз (або "exit" для виходу): ')
            if text.lower() == "exit":
                print("Вихід із програми.")
                break
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            result = interpreter.interpret()

            print(f"Результат: {result}")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
