def reverse_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

def remove_duplicates(sentence):
    unique_chars = []
    for char in sentence:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

def find_longest_palindrome(string):
    longest_palindrome = ''
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest_palindrome):
                longest_palindrome = substring
    return longest_palindrome

def capitalize_first_letters(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    capitalized_sentence = ' '.join(capitalized_words)
    return capitalized_sentence

def is_anagram_of_palindrome(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    odd_count = 0
    for count in char_count.values():
        if count % 2 != 0:
            odd_count += 1

    if odd_count > 1:
        return False
    else:
        return True

input_sentence = "Hello world! OpenAI is amazing!"
reversed_sentence = reverse_sentence(input_sentence)
no_duplicates_sentence = remove_duplicates(input_sentence)
longest_palindrome = find_longest_palindrome("babad")
capitalized_sentence = capitalize_first_letters("hello how are you? i'm fine, thank you")
is_anagram_palindrome = is_anagram_of_palindrome("racecar")

print("Frase revertida:", reversed_sentence)
print("Frase sem caracteres duplicados:", no_duplicates_sentence)
print("Substring palíndroma mais longa:", longest_palindrome)
print("Palavras com a primeira letra maiúscula:", capitalized_sentence)
print("É um anagrama de um palíndromo:", is_anagram_palindrome)
