def isnegative(numb):
    '''
    >>> from solutions import isnegative
    >>> type(isnegative(0))
    <class 'bool'>
    >>> isnegative(4)
    False
    >>> isnegative(0)
    False
    >>> isnegative(-6)
    True
    ''' 
    return numb < 0

def count_evens(numbs):
    '''
    >>> from solutions import count_evens
    >>> type(count_evens([1, 2, 3]))
    <class 'int'>
    >>> count_evens([1, 2, 3])
    1
    >>> count_evens([4, 6, 8, 10, 12])
    5
    >>> count_evens([1, 3, 5, 7, 9])
    0
    >>> count_evens([])
    0
    >>> count_evens([3, 2])
    1
    '''
    count = 0 
    for x in numbs:
        if x % 2 == 0:
            count += 1
    return count

def increment_odds(numbs):
    '''
    >>> from solutions import increment_odds
    >>> type(increment_odds([1, 2, 3]))
    <class 'list'>
    >>> increment_odds([1, 2, 3])
    [2, 2, 4]
    >>> increment_odds([2, 2, 1, 4, 5])
    [2, 2, 2, 4, 6]
    >>> increment_odds([])
    []
    >>> increment_odds([0, 1])
    [0, 2]
    '''
    for x in range(len(numbs)):
       if numbs[x] % 2 == 1:
            numbs[x] = numbs[x] + 1
    return numbs

def average(numbs):
    '''
    >>> from solutions import average
    >>> type(average([1, 2, 3]))
    <class 'float'>
    >>> average([1, 2, 3])
    2.0
    >>> average([4, 6, 8, 10, 12])
    8.0
    >>> average([1, 2])
    1.5
    '''
    return sum(numbs)/len(numbs)

def name_to_dict(full_name):
    '''
    >>> from solutions import name_to_dict
    >>> type(name_to_dict('Ada Lovelace'))
    <class 'dict'>
    >>> name_to_dict('Ada Lovelace')
    {'first_name': 'Ada', 'last_name': 'Lovelace'}
    >>> name_to_dict('Marie Curie')
    {'first_name': 'Marie', 'last_name': 'Curie'}
    '''
    new_list = []
    new_list = full_name.split(" ")
    new_dict = {}
    new_dict["first_name"] = new_list[0]
    new_dict["last_name"] = new_list[1]
    return new_dict

def name_to_dict(name):
    new_list = name.split(" ")
    first = new_list[0]
    last = new_list[1]
    return {
        "first_name": first,
        "last_name": last
    }


def capitalize_names(dict_names):
    '''
    >>> from solutions import capitalize_names
    >>> names = []
    >>> names.append({'first_name': 'ada', 'last_name': 'lovelace'})
    >>> names.append({'first_name': 'marie', 'last_name': 'curie'})
    >>> names
    [{'first_name': 'ada', 'last_name': 'lovelace'}, {'first_name': 'marie', 'last_name': 'curie'}]
    >>> type(names)
    <class 'list'>
    >>> capitalize_names(names)
    [{'first_name': 'Ada', 'last_name': 'Lovelace'}, {'first_name': 'Marie', 'last_name': 'Curie'}]
    >>> type(capitalize_names(names))
    <class 'list'>
    '''
    for x in dict_names:
        x['first_name'] =(x['first_name'].capitalize())
        x['last_name'] =(x['last_name'].capitalize())
    return dict_names

def count_vowels(word):
    '''
    >>> from solutions import count_vowels
    >>> type(count_vowels('codeup'))
    <class 'int'>
    >>> count_vowels('codeup')
    3
    >>> count_vowels('abcde')
    2
    >>> count_vowels('why')
    0
    '''
    count = 0 
    for x in word:
        if x.lower() in "aeiou":
            count += 1
    return count


def analyze_word(word):
    '''
    >>> from solutions import analyze_word
    >>> type(analyze_word('codeup'))
    <class 'dict'>
    >>> analyze_word('codeup')
    {'word': 'codeup', 'n_letters': 6, 'n_vowels': 3}
    >>> analyze_word('abcde')
    {'word': 'abcde', 'n_letters': 5, 'n_vowels': 2}
    >>> analyze_word('why')
    {'word': 'why', 'n_letters': 3, 'n_vowels': 0}
    '''
    dict_word = {}
    dict_word["word"] = word
    dict_word["n_letters"] = len(word)
    dict_word["n_vowels"] = count_vowels(word)
    return dict_word

    return {
        "word" : word,
        "n_letters" : len(word),
        "n_vowels" : count_vowels(word)
    }