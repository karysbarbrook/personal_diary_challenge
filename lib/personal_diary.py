
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