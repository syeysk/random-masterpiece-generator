from random import choice, randint

letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя,'

real_syllables = {'пус', 'ть', 'он', 'зна', 'ет', ',', 'что', 'ес', 'ли', 'по', 'доб' ,'но', 'мне', 'стре', 'ми', 'тся'}
real_words = {'пусть', 'он', 'знает', ',', 'что', 'если', 'подобно', 'мне', 'стремится'}
real_word_combinations = {'пусть', 'он знает', ',', 'что если', 'подобно мне', 'он стремится'}
real_sentences = {'пусть он знает , что если , подобно мне , он стремится'}


def rand_entity(min_length, max_length, alphabet, glue):
    rand_letters = []
    for _ in range(randint(min_length, max_length)):
        rand_letters.append(choice(alphabet))

    return glue.join(rand_letters)


#def rand_entity(min_length, max_length, alphabet):
#    return ''.join(choice(alphabet) for _ in range(randint(min_length, max_length)))

def guess_entities(max_iterations, min_length, max_length, subentities, real_entities, glue=''):
    guessed_entities = set()
    for index_iteration in range(max_iterations):
        entity = rand_entity(min_length, max_length, subentities, glue)
        if entity in real_entities:
            guessed_entities.add(entity)
            if len(guessed_entities) == len(real_entities):
                return True, index_iteration
    
    return False, index_iteration


args_list = [
    (10000000, 1, 5, letters, real_syllables),
    (100000, 1, 3, list(real_syllables), real_words),
    (1000, 1, 2, list(real_words), real_word_combinations, ' '),
    (10000000, 7, 8, list(real_word_combinations), real_sentences, ' '),
]

for args in args_list:
    is_ready, index = guess_entities(*args)
    print(is_ready, index)
    if not is_ready:
        break
