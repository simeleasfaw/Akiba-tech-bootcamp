def clean_text(text):
    text = text.lower()

    punctuation = ".,!?;:"

    for char in punctuation:
        text = text.replace(char, "")

    return text

def count_words(text):
    words = clean_text(text).split()
    return len(words)


def count_characters(text):
    count = 0

    for char in clean_text(text):
        if char != " ":
            count += 1

    return count

def count_vowels_consonants(text):
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in clean_text(text):
        if char in vowels:
            vowel_count += 1
        elif char.isalpha():
            consonant_count += 1

    return vowel_count, consonant_count


def find_longest_word(text):
    words = clean_text(text).split()
    longest_length = 0
    longest_words = []

    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_words = [word]

        elif len(word) == longest_length:
            longest_words.append(word)

    return longest_words


def word_frequency(text):
    words = clean_text(text).split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


def find_repeated_words(text):
    frequency = word_frequency(text)
    repeated = []

    for word, count in frequency.items():
        if count > 1:
            repeated.append(word)

    return repeated

def five_most_frequent(text):
    frequency = word_frequency(text)

    sorted_words = sorted(
        frequency.items(),
        key=lambda item: item[1],
        reverse=True
    )

    return sorted_words[:5]

text = input("Enter a paragraph: ")

vowels, consonants = count_vowels_consonants(text)

print("\n----- TEXT ANALYSIS -----")
print("Total words:", count_words(text))
print("Characters (excluding spaces):", count_characters(text))
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Longest word:", find_longest_word(text))
print("Word frequency:", word_frequency(text))
print("Repeated words:", find_repeated_words(text))
print("Top five frequent words:", five_most_frequent(text))
