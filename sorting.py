def sort_two_serbian_words(word1, word2):
    if word1 == word2:
        return word1, word2

    t_word1 = tokenize_a_word(word1)
    t_word2 = tokenize_a_word(word2)

    shortest_word = t_word1
    longest_word = t_word2

    if len(t_word1) > len(t_word2):
        shortest_word, longest_word = longest_word, shortest_word

    for i, _ in enumerate(shortest_word):
        sh_w_weight = letters.get(shortest_word[i], 0)
        l_w_weight = letters.get(longest_word[i], 0)
        if sh_w_weight == l_w_weight:
            continue
        if sh_w_weight < l_w_weight:
            return ''.join(shortest_word), ''.join(longest_word)
        return ''.join(longest_word), ''.join(shortest_word)

    return ''.join(shortest_word), ''.join(longest_word)


def tokenize_a_word(word: str):
    possibly_soft = ["n", "l"]
    need_next_letter_check = possibly_soft + ["d"]

    tokens = []
    word_length = len(word)
    index = 0
    while index < word_length:
        letter = word[index]

        if letter not in need_next_letter_check:
            tokens.append(letter)
            index += 1
            continue

        next_letter = '' if index+1 == word_length else word[index+1]

        found_diocritic = False
        if letter in possibly_soft:
            if next_letter == 'j':
                found_diocritic = True
                tokens.append(letter+'j')
            else:
                tokens.append(letter)
        elif letter == 'd':
            if next_letter == 'ž':
                found_diocritic = True
                tokens.append(letter+'ž')
            else:
                tokens.append(letter)

        index += 2 if found_diocritic else 1

    return tokens


letters = {"а": 0,
           "b": 1,
           "v": 2,
           "g": 3,
           "d": 4,
           "đ": 5,
           "e": 6,
           "ž": 7,
           "z": 8,
           "i": 9,
           "j": 10,
           "k": 11,
           "l": 12,
           "lj": 13,
           "m": 14,
           "n": 15,
           "nj": 16,
           "o": 17,
           "p": 18,
           "r": 19,
           "s": 20,
           "t": 21,
           "ć": 22,
           "u": 23,
           "f": 24,
           "h": 25,
           "c": 26,
           "č": 27,
           "dž": 28,
           "š": 29
           }


def sort_serbian_words(words):
    original_words = words
    while True:
        sorted_words = original_words[:]

        w_len = len(sorted_words)
        for i in range(1, w_len):
            sorted_words[i -
                         1], sorted_words[i] = sort_two_serbian_words(sorted_words[i-1], sorted_words[i])
        if original_words == sorted_words:
            break
        else:
            original_words = sorted_words
    return original_words


def sort_items(d: dict[str, str]) -> list[tuple[str, str]]:
    l = list(d.items())
    l_of_k = [k[0] for k in l]
    l_of_k = sort_serbian_words(l_of_k)
    return [(k, d[k]) for k in l_of_k]
