from xmlrpc.client import Boolean


class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """

        
        return input_str[::-1]

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """
        check_vowel = False

        if character.lower() in ('a','e','i','o','u'):
            check_vowel = True 

        elif character.upper()  in ('A','E','I','O','U'):
            check_vowel = True
        else:
            check_vowel = False


        return check_vowel

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """

        longest = max(sentence.split(), key = len)
       
        return longest


    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        len_list = []
        words = text.split(" ")
        for i in range(0,len(words)):
            len_list.append(len(words[i]))

        return len_list