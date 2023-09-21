
def make_snippet(content):
    # count blank spaces after words, once count reaches 5 replace following words with ...
    blank_space_count = 0
    new_string = []
    for letter in content:
        if blank_space_count >= 5:
            new_long_string = "".join(new_string)
            return new_long_string + "..."
        if letter == " ":
            blank_space_count += 1
            new_string.append(letter)
        else:
            new_string.append(letter)
    return "".join(new_string)


def count_words(text):
    t = ""
    special_char = [',', '!', '?']
    for char in text:
        if char not in special_char:
            t += char
        else:
            pass
    word_list = t.split(" ")
    return len(word_list)


def text_reading_time(text):
    if type(text) is int or text is None:
        raise Exception("Sorry, I can only take a passage of text. Please try again.")
    elif count_words(text) == 1:
        return "I estimate it would take you 0 minute(s) to read this."
    else:
        return f"I estimate it would take you {count_words(text)/200} minute(s) to read this."
    

def grammar_check(text):
    capitalisation = "none"
    full_stop = "none"
    if text[0].isupper():
        capitalisation = "correct"
    if text[-1] == ".":
        full_stop = "correct"
    if "." in text and text[-1] != ".":
        full_stop = "incorrect"
    return f"Capitalisation is: {capitalisation}, full-stop usage is: {full_stop}."


def check_for_todo(text):
    # will try to refactor:
    # happy with this for now!
    if type(text) != str:
        raise Exception("Error: invalid data type, only takes text.")
    return "#TODO" in text


'''
Making a Class called DiaryEntry() which uses some of the above methods, and creates some new ones too.
Exercise for Test Driving a Single-Class Program
'''
class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.count = 0
        self.minute = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        word_list = self.contents.split(" ")
        return len(word_list)

    def reading_time(self, wpm):
        word_list = self.contents.split(" ")
        count = len(word_list)
        return count/wpm

    def reading_chunk(self, wpm, minutes):
        '''
        can't get reading_chunk to work in terms of saving a count of each time its used and using
        that in the slice. Greyed out the two tests related to this in the test file accordingly.
        '''
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        word_list = self.contents.split(" ")
        split_list = []
        split_word = ""
        count = len(word_list)
        forumla = count / wpm
        n = 1
        for word in word_list:
            if n % wpm != 0:
                split_word += word + " "
                n += 1
            else:
                split_word += word + " "
                split_list.append(split_word)
                split_word = ""
                n += 1

        for i, word in enumerate(split_list):
            split_list[i] = word.strip()
            split_list
        
        chunks = "".join(split_list[self.count:minutes])
        self.count += 1
        # self.minute += 1
        print(self.count)
        return chunks
    
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.


'''
Test Drive a Single-Class Function - Challenge
'''

class GrammarStats:
    # accurate = 0
    # num_of_checks = 0 
    def __init__(self):
        self.accurate = 0
        self.num_of_checks = 0
        

    def check(self, text):
        if text[0].isupper() and text[-1] == ".":
            self.num_of_checks += 1
            self.accurate += 1
            return True
        else:
            self.num_of_checks += 1
            return False
    
    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        print(self.accurate)
        print(self.num_of_checks)
        num1 = (self.num_of_checks - self.accurate) / self.num_of_checks
        percentage = 100 - (num1 * 100)
        return percentage