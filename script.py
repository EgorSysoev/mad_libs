import re
import collections

# The list of words we are going to replace in the file.
wordsToReplace = ['ADJECTIVE', 'NOUN', 'ADVERB', 'VERB']


def get_word_value(word):
    """
    The function to get the value for the word.
    :param word: the string
    :return: the string of the user input
    """
    word_val = str(input(f'Enter an {word.lower()}\n'))
    return word_val


def create_re_for_words(list_of_words):
    """
    The function created the list of RE objects for the specified list of strings.
    :param list_of_words: the list of words we are looking for
    :return: the list of RE objects for each word
    """
    return [re.compile(rf'\b{word}\b') for word in list_of_words]


if __name__ == "__main__":
    # Get the content of the file.
    with open('/home/egor/dev/python/mad_libs/test.txt', 'r') as f:
        content = f.read()

    # The dictionary and the ordered dictionary of matched words from the file and their position in the text.
    wordsDict = {i.start(): i.group() for pattern in
                 create_re_for_words(wordsToReplace) for i in pattern.finditer(content)}
    orderedWordList = collections.OrderedDict(sorted(wordsDict.items()))

    # Replace the words in the text with the user's input.
    for theWord in orderedWordList.values():
        content = content.replace(theWord, get_word_value(theWord), 1)

    # Save the new content to the file.
    with open('/home/egor/dev/python/mad_libs/result.txt', 'w') as f:
        f.write(content)
        print('The modified string was saved to the file.\n')

    print(content)
