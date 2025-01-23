
f = open(r'./input.txt', 'r')                   # make sure that you gave given the right path of the input file
input_string = f.read()
word = ''
input_string = input_string

index = 0
tokens = 0
string = 0

digits = []
identifiers = []
keyword_present = []
function_present = []
operator_present = []
separator_present = []

separators = ['(', ')', '{', '}', '[', ']', ',', ';']
operators = ['+', '-', '*', '/', '%', '=', '>', '<', '>=', '<=', '==', '!=','&']
keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum', 'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short', 'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned','void', 'volatile', 'while']


while True:
    try:
        if input_string[index] == '#':
            for i in input_string[index+1:]:
                index += 1
                if i == '\n':
                    break
            
        
        elif input_string[index] in input_string:
            if input_string[index].isalpha() or input_string[index].isdigit():
                word += input_string[index]
                if input_string[index+1] == '(':
                    if word not in function_present:
                        function_present.append(word)
                    tokens += 1
                    word = ''
                                   
                elif input_string[index+1] == ' ' or input_string[index+1] in operators or input_string[index+1] in separators:
                    if word in keywords:
                        # print(word, 'is a keyword')
                        if word not in keyword_present:
                            keyword_present.append(word)
                        tokens += 1
                        word = ''
                    else:
                        # print(word, 'is an identifier')
                        if word not in identifiers:
                            identifiers.append(word)
                        tokens +=1
                        word = ''
            
            # for excluding comments
            elif input_string[index] == r'/':
                if input_string[index+1] == r'*':
                    for i in input_string[index+1:]:
                        index += 1
                        if i == r'/':
                            break
                elif input_string[index+1] == r'/':
                    for i in input_string[index+1:]:
                        index += 1
                        if i == '\n':
                            break
            
            elif input_string[index] in operators:
                # print(input_string[index], 'is an operator')
                if input_string[index] not in operator_present:
                    operator_present.append(input_string[index])
                    tokens += 1
            
            elif input_string[index] in separators:
                # print(input_string[index], 'is a separator')
                if input_string[index] not in separator_present:
                    separator_present.append(input_string[index])
                tokens += 1
            
            elif input_string[index] == '"':
                word += input_string[index]
                for i in input_string[index+1:]:
                    word += i
                    index += 1
                    if i == '"':
                        # print(word, 'is a string')
                        string += 1
                        tokens += 1
                        word = ''
                        break 
            
            # else: 
            #     try:
            #         if input_string[index].isdigit():
            #             word += input_string[index]
                        
            #             if input_string[index+1] == ' ' or input_string[index+1] in operators or input_string[index+1] in separators:
            #                 # print(word, 'is a digit')
                            
            #                 if word not in digits:
            #                     digits.append(word)
            #                 tokens += 1
            #                 word = ''
            #     except:
            #         pass
                           
            index += 1
    except:
        break
    

print('\nTotal number of keywords: ', len(keyword_present))
print('Keywords Present: ', keyword_present,'\n')    

# print('Total number of digits: ', len(digits))
# print('Digits Present: ', digits,'\n')

print('Total number of functions: ', len(function_present))
print('Functions Present: ', function_present,'\n')

print('Total number of identifiers: ', len(identifiers))
print('Identifiers Present: ', identifiers,'\n')

print('Total number of operators: ', len(operator_present))
print('Operators Present: ', operator_present,'\n')

print('Total number of separators: ', len(separator_present))
print('Separators Present: ', separator_present)

print('\nTotal number of strings: ', string)

print('\nTotal number of Tokens: ', tokens)
        
   

