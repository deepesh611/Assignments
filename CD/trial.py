# LL(1) Parser for the grammar:
# E -> E + T | T
# T -> T * F | F
# F -> ( E ) | id

# Function to parse E non-terminal
def E():
    T()
    while lookahead == '+':
        match('+')
        T()

# Function to parse T non-terminal
def T():
    F()
    while lookahead == '*':
        match('*')
        F()

# Function to parse F non-terminal
def F():
    global lookahead
    if lookahead == '(':
        match('(')
        E()
        match(')')
    elif lookahead.isalnum():
        match(lookahead)
    else:
        error()

# Function to match the lookahead token
def match(expected):
    global lookahead
    if lookahead == expected:
        lookahead = next_token()
    else:
        error()

# Function to get the next token
def next_token():
    global position
    position += 1
    if position < len(input_str):
        return input_str[position]
    else:
        return ''

# Function to handle syntax errors
def error():
    print("Syntax error at position", position)
    exit(1)

# Main function
if __name__ == "__main__":
    input_str = input("Enter an arithmetic expression: ")
    position = 0
    lookahead = input_str[position]

    # Start parsing
    E()

    # If parsing is successful, print success message
    if lookahead == '':
        print("Parsing successful!")
    else:
        error()
