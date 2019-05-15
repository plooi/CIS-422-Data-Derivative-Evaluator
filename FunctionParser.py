

chars_in_number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
symbols = ["+", "-", "*", "/", "^", "(", ")"]
def main():
    print(convert_to_ast("199999 + sin(1)"))
def convert_to_ast(text):
    tokens = tokenize(text)
    tree = create_tree(tokens)
def tokenize(text):
    tokens = []
    i = 0
    current_token = ""
    while i < len(text):
        if text[i] in chars_in_number:
            while i < len(text):
                if text[i] in chars_in_number:current_token += text[i]
                else: break
                i += 1
            tokens.append(current_token)
            current_token = ""
        elif text[i].isalpha():
            while i < len(text):
                if text[i].isalpha():current_token += text[i]
                else: break
                i += 1
            tokens.append(current_token)
            current_token = ""
        elif text[i] in symbols:
            current_token += text[i]
            i += 1
            tokens.append(current_token)
            current_token = ""
        elif text[i] == ' ':
            i += 1
        else:
            raise InvalidCharacterException(text[i])
        
    return tokens
TOKEN_TYPE_WORD = 1
TOKEN_TYPE_SYMBOL = 2
TOKEN_TYPE_NUMBER = 3
def token_type(token_string):
    if len(token_string) == 0:
        raise Exception("Error: Token string is empty string")
    if token_string[0].isalpha():
        return TOKEN_TYPE_WORD
    elif token_string[0] in symbols:
        return TOKEN_TYPE_SYMBOL
    elif token_string[0] in chars_in_number:
        return TOKEN_TYPE_NUMBER
    else:
        raise Exception("Invalid token: " + token_string)
PLUS_MINUS_ORDER = 1
MULT_DIV_ORDER = 2
EXPONENT_ORDER = 3
def get_symbol_order(symbol):
    if symbol == "+" or symbol == "-":
        return PLUS_MINUS_ORDER
    elif symbol == "*" or symbol == "/":
        return MULT_DIV_ORDER
    elif symbol == "^":
        return EXPONENT_ORDER
    else:
        raise Exception("Invalid symbol " + str(symbol))
def create_tree(tokens):
    print(tokens)#
    if len(tokens) == 1:
        if token_type(tokens[0]) == TOKEN_TYPE_WORD or token_type(tokens[0]) == TOKEN_TYPE_NUMBER:
            node = SyntaxNode()
            if token_type(tokens[0]) == TOKEN_TYPE_WORD:
                node.func = lambda inp: tokens[0]
            else:
                node.func = lambda inp: int(tokens[0])
    i = 0
    index_of_first_operator = -1
    order_of_first_operator = None
    first_operator = None
    while i < len(tokens):
        if tokens[i] == "(":
            i = find_close(tokens, i)
        elif token_type(tokens[i]) == TOKEN_TYPE_SYMBOL:
            order = get_symbol_order(tokens[i])
            if order_of_first_operator == None or order_of_first_operator < order:
                order_of_first_operator = order
                index_of_first_operator = i
                first_operator = tokens[i]
        i += 1
    if index_of_first_operator == -1:
        return create_tree(tokens[1:-1])
    else:
        node = SyntaxNode()
        node.func = get_function(first_operator)
        node.inputs = [create_tree(tokens[0:index_of_first_operator]), create_tree(tokens[index_of_first_operator+1])]
        return node
def get_function(operator):
    return {
    "+" : lambda inp: inp[0] + inp[1],
    "-" : lambda inp: inp[0] - inp[1],
    "*" : lambda inp: inp[0] * inp[1],
    "/" : lambda inp: inp[0] / inp[1],
    "*" : lambda inp: inp[0] ** inp[1]
    }[operator]
    
def find_close(tokens, i):
    i += 1
    while i < len(tokens):
        if tokens[i] == "(":
            i = find_close(tokens, i)
        elif tokens[i] == ")":
            return i+1
        i += 1
    raise Exception("Unmatched parenthases at token index " + str(i) + " in " + str(tokens))
class SyntaxNode:
    def __init__(self):
        self.func = lambda inputs: 0
        self.inputs = []
class InvalidCharacterException(Exception):
    def __init__(self, invalid_char):
        self.invalid_char = invalid_char
    def __str__(self):
        return "Invalid character: '" + self.invalid_char + "'"
if __name__ == "__main__": main()
