def is_anagrams():
    word_1 = list(input('Please enter a word: ').lower())
    word_2 = list(input('Please enter a word: ').lower())
    word_1.sort()
    word_2.sort()

    return 'ANAGRAMS' if word_1 == word_2 else 'NOT ANAGRAMS'

print(is_anagrams())
