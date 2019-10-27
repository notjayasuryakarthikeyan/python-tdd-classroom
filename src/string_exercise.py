class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """
        reverse_str = ""
        for char_of_str in input_str[::-1]:
            reverse_str += char_of_str

        return reverse_str

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        english_vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        if character in english_vowel:
            return True

        return False

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """
        longest_word = ""
        max_length = 0
        word = ""

        for index_of_each_char in range(len(sentence)):
            char_of_sentence = sentence[index_of_each_char]
            if char_of_sentence != ' ':
                word = word + char_of_sentence

            if char_of_sentence == ' ' or index_of_each_char == len(sentence)-1:
                if max_length < len(word):
                    max_length = len(word)
                    longest_word = word
                word = ""

        return longest_word

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        word = ""
        word_length_list = []
        for index_of_each_char in range(len(text)):
            char_of_text = text[index_of_each_char]
            if char_of_text != ' ':
                word = word + char_of_text

            if char_of_text == ' ' or index_of_each_char == len(text) - 1:
                word_length_list.append(len(word))
                word = ""

        return word_length_list
