# Written by Eric Martin for COMP9021


'''
Checks whether a word can be generated from a starting symbol
by a context free grammar, represented by a dictionnary
whose keys are the nonterminals and for each nonterminal N,
the value associated with N is the set of productions of N,
one of which is possibly ε (the empty production).

A character is a nonterminal symbol iff it is an uppercase letter.

If ε is not one of the starting symbol's productions, then it is added
as such by eliminate_ε() in case the empty string can be generated.
Whether this is the case or not, eliminate_ε() removes all productions
of ε by nonterminals different to the starting symbol, possibly adding
other productions to generate the same language.
That allows one to guarantee that a nonempty word w belongs to the
generated language iff it can be generated thanks to a sequence
of productions consisting of words no longer than w.
'''


def eliminate_ε(rules, starting_symbol):
    '''
    >>> rules = {'S': {'SS', '(S)', '()'}}
    >>> eliminate_ε(rules, 'S') == rules
    True
    
    >>> rules = {'S': {'bSbb', 'A'}, 'A': {'aA', 'ε'}}
    >>> eliminate_ε(rules, 'S') == {'S': {'', 'A', 'bbb', 'bSbb'},
    ...                            'A': {'aA', 'a'}}
    True
    '''
    # We look for the set S1 of all symbols producing ε,
    # then for the set S2 of all symbols producing a sequence
    # of symbols in S1, then for the set S3 of all symbols
    # producing a sequence of symbols in the union of S1 with S2...
    # If starting_symbol eventually shows up, 
    # then ε is added to starting_symbol's productions
    # in case it is not already recorded as such.
    symbols_leading_to_ε = {'ε'}
    search_more = True
    while search_more:
        search_more = False
        for nonterminal in rules.keys() - symbols_leading_to_ε:
            if any(set(production) <= symbols_leading_to_ε for production in rules[nonterminal]):
                if nonterminal == starting_symbol:
                    rules[starting_symbol].add('ε')
                    search_more = False
                    break
                symbols_leading_to_ε.add(nonterminal)
                search_more = True
    new_rules = {}
    for nonterminal in rules:
        new_productions = set()
        for production in rules[nonterminal] - {'ε'}:
            # In production, an occurrence of a nonterminal P
            # is either kept or eliminated (doubling the number of
            # derived productions) in case 'ε' can be produced from P.
            # For instance, if X can produce 'ε' but Y cannot, then
            # the production aaXbYaX will give rise to the productions:
            # - aaXbYaX
            # - aabYaX
            # - aaXbYa
            # - aabYa
            productions = {''}
            for symbol in production:
                if symbol in rules and 'ε' in rules[symbol]:
                    productions = productions.union(word + symbol for word in productions)
                else:
                    productions = {word + symbol for word in productions}
            new_productions = new_productions.union(productions)
        new_rules[nonterminal] = new_productions
        # If the grammar can generate the empty string,
        # then '' is one of the productions of starting_symbol;
        # it is removed from all other productions, if any.
        if nonterminal != starting_symbol:
            new_rules[nonterminal] -= {''}
    return new_rules

def can_generate_with_no_ε(word, rules, starting_symbol):
    '''
    >>> rules = {'S': {'SS', '(S)', '()'}}
    >>> can_generate_with_no_ε('()', rules, 'S')
    True
    >>> can_generate_with_no_ε('(())', rules, 'S')
    True
    >>> can_generate_with_no_ε('()()', rules, 'S')
    True
    >>> can_generate_with_no_ε('(()())', rules, 'S')
    True
    >>> can_generate_with_no_ε('((())())(((())))', rules, 'S')
    True
    >>> can_generate_with_no_ε('(', rules, 'S')
    False
    >>> can_generate_with_no_ε('())', rules, 'S')
    False

    >>> rules = {'S': {'', 'A', 'bbb', 'bSbb'}, 'A': {'aA', 'a'}}
    >>> can_generate_with_no_ε('', rules, 'S')
    True
    >>> can_generate_with_no_ε('bbb', rules, 'S')
    True
    >>> can_generate_with_no_ε('aa', rules, 'S')
    True
    >>> can_generate_with_no_ε('babb', rules, 'S')
    True
    >>> can_generate_with_no_ε('bbbbbb', rules, 'S')
    True
    >>> can_generate_with_no_ε('bbaaabbbb', rules, 'S')
    True
    >>> can_generate_with_no_ε('bbbaaaaaabbbbbb', rules, 'S')
    True
    >>> can_generate_with_no_ε('bbbbb', rules, 'S')
    False
    >>> can_generate_with_no_ε('bbabbbbb', rules, 'S')
    False
    >>> can_generate_with_no_ε('bbabbbba', rules, 'S')
    False
    '''
    if word == '':
        return '' in rules[starting_symbol]
    rules[starting_symbol] -= {''}
    generated_bigrams = {('', starting_symbol)}
    seen_bigrams = generated_bigrams
    while generated_bigrams:
        bigram = generated_bigrams.pop()
        # bigram is a pair of the form (w_1, w_2)
        # where all symbols in w_1 are terminals.
        # - If w_2 is of the form tw where t is a terminal symbol,
        #   then (w_1, w_2) is replaced by (w_1t, w).
        # - Otherwise, if w_1 is not an initial segment of word,
        #   then (w_1, w_2) is dumped.
        # - Otherwise, if w_2 is empty, then either w_1 is word
        #   and word is known to have been generated, or (w_1, w_2) is dumped.
        # - Otherwise, w_2 is of the form Nw where N is a nonterminal symbol,
        #   and (w_1, w_2) is replaced by all pairs of the form
        #   (w_1, w'w) where w' can be produced from N and w_1w'w is
        #   not longer than word.
        while bigram[1] and not bigram[1][0].isupper():
            bigram = bigram[0] + bigram[1][0], bigram[1][1: ]
        if not word.startswith(bigram[0]):
            continue
        if not bigram[1]:
            if len(bigram[0]) == len(word):
                return True
            continue
        for pattern in rules[bigram[1][0]]:
            new_bigram = bigram[0], pattern + bigram[1][1: ]
            if len(new_bigram[0]) + len(new_bigram[1]) <= len(word):
                if new_bigram not in seen_bigrams:
                   generated_bigrams.add(new_bigram)
                seen_bigrams.add(new_bigram)
    return False

def can_generate(word, rules, starting_symbol):
    '''
    >>> rules = {'S': {'SS', '(S)', '()'}}
    >>> can_generate('()', rules, 'S')
    True
    >>> can_generate('(())', rules, 'S')
    True
    >>> can_generate('()()', rules, 'S')
    True
    >>> can_generate('(()())', rules, 'S')
    True
    >>> can_generate('((())())(((())))', rules, 'S')
    True
    >>> can_generate('(', rules, 'S')
    False
    >>> can_generate('())', rules, 'S')
    False

    >>> rules = {'S': {'bSbb', 'A'}, 'A': {'aA', 'ε'}}
    >>> can_generate('', rules, 'S')
    True
    >>> can_generate('bbb', rules, 'S')
    True
    >>> can_generate('aa', rules, 'S')
    True
    >>> can_generate('babb', rules, 'S')
    True
    >>> can_generate('bbbbbb', rules, 'S')
    True
    >>> can_generate('bbaaabbbb', rules, 'S')
    True
    >>> can_generate('bbbaaaaaabbbbbb', rules, 'S')
    True
    >>> can_generate('bbbbb', rules, 'S')
    False
    >>> can_generate('bbabbbbb', rules, 'S')
    False
    >>> can_generate('bbabbbba', rules, 'S')
    False
    '''
    return can_generate_with_no_ε(word, eliminate_ε(rules, starting_symbol), starting_symbol)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
