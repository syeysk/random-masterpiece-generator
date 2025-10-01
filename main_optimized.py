from random import choice, randint

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя,'

real_syllables = tuple(tuple(i) for i in ('пус', 'ть', 'он'))
real_words = (
    (real_syllables[0], real_syllables[1]),
    (real_syllables[2],),
)
real_word_combinations = (
    (real_words[0],),
    (real_words[1],),
)
real_sentences = (
    (real_word_combinations[0], ),
)


def rand_entity(min_length, max_length, alphabet):
    rand_letters = []
    for _ in range(randint(min_length, max_length)):
        rand_letters.append(choice(alphabet))

    return tuple(rand_letters)


#def rand_entity(min_length, max_length, alphabet):
#    return choice(alphabet) for _ in range(randint(min_length, max_length))

def guess_entities(max_iterations, subentities, real_entities):
    min_length, max_length = 0, 0
    _subentities = {}
    for key, subentity in enumerate(subentities):
        _subentities[subentity] = key
    
    _real_entities = set()
    for entity in real_entities:
        length = len(entity)
        if length > max_length:
            max_length = length
            if min_length == 0:
                min_length = length
        elif length < min_length:
            min_length = length

        _entity = []
        for subentity in entity:
            _entity.append(_subentities[subentity])
        
        _real_entities.add(tuple(_entity))
    
    #print('  ', subentities)
    #print('  ', real_entities)
    print('  ', _subentities)
    print('  ', _real_entities)

    guessed_entities = set()
    _subentities_list = list(_subentities.values())
    for index_iteration in range(max_iterations):
        entity = rand_entity(min_length, max_length, _subentities_list)
        if entity in _real_entities:
            guessed_entities.add(entity)
            if len(guessed_entities) == len(_real_entities):
                return True, index_iteration
    
    return False, index_iteration


args_list = [
    (10000000, letters, set(real_syllables)),
    (100000, real_syllables, set(real_words)),
    (1000, real_words, set(real_word_combinations)),
    (1000000, real_word_combinations, set(real_sentences)),
]

for args in args_list:
    is_ready, index = guess_entities(*args)
    print(is_ready, index)
    if not is_ready:
        break

print()
