"""Count words in file."""

def tokenize(filename):
    
    file = open(filename)
    words =[]

    for line in file:
        for word in line.split():
            word= word.strip(" .,( "  ' [ ' " ").lower()
            words.append(word)

    return words

def word_count(words):
    
    dictionary = {}
    
    for word in words:
        dictionary[word] = dictionary.get(word, 0) + 1
    
    return dictionary

def print_word_counts(dictionary):
    
    for key, value in dictionary.items():
        print(f"{key} : {value}")
    
ls = tokenize('twain.txt')
counter = word_count(ls)
print_word_counts(counter)