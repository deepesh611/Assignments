def find_first(grammar, symbol, calculated_first_sets):
    first_set = set()

    if symbol in calculated_first_sets:
        return calculated_first_sets[symbol]

    if symbol.islower() or symbol == 'ε':
        first_set.add(symbol)
    else:
        for production in grammar[symbol]:
            if production[0].islower() or production[0] == 'ε':
                first_set.add(production[0])
            else:
                first_set.update(find_first(grammar, production[0], calculated_first_sets))

    calculated_first_sets[symbol] = first_set
    return first_set


def find_follow(grammar, symbol, calculated_follow_sets, calculated_first_sets):
    if symbol in calculated_follow_sets:
        return calculated_follow_sets[symbol]

    follow_set = set()
    if symbol == 'S':
        follow_set.add('$')

    for non_terminal, productions in grammar.items():
        for production in productions:
            if symbol in production:
                index = production.index(symbol)
                if index < len(production) - 1:
                    next_symbol = production[index + 1]
                    if next_symbol.islower() or next_symbol == 'ε':
                        follow_set.add(next_symbol)
                        
                    else:
                        follow_set.update(find_first(grammar, next_symbol, calculated_first_sets))
                        if 'ε' in find_first(grammar, next_symbol, calculated_first_sets):
                            follow_set.update(find_follow(grammar, non_terminal, calculated_follow_sets, calculated_first_sets))      
                else:
                    if non_terminal != symbol:
                        follow_set.update(find_follow(grammar, non_terminal, calculated_follow_sets, calculated_first_sets))

    calculated_follow_sets[symbol] = follow_set
    return follow_set





grammar = {
        'S': ['AB', 'BC'],
        'A': ['aA', 'ε'],
        'B': ['bB', 'c'],
        'C': ['cC', 'd']
}

calculated_first_sets = {}
calculated_follow_sets = {}

for non_terminal in grammar.keys():
        find_first(grammar, non_terminal, calculated_first_sets)
        find_follow(grammar, non_terminal, calculated_follow_sets, calculated_first_sets)

print("\nFirst Sets:")
for non_terminal, first_set in calculated_first_sets.items():
        print(f"First({non_terminal}) = {first_set}")

print("\nFollow Sets:")
for non_terminal, follow_set in calculated_follow_sets.items():
        print(f"Follow({non_terminal}) = {follow_set}")

