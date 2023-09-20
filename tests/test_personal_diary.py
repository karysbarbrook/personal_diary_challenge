'''
Design
A function called make_snippet that takes a string as an argument and returns the 
first five words and then a '...' if there are more than that.
'''

import pytest
from lib.personal_diary import *


'''
Complete and now redundant: Test that make_snippet() counts number of blank spaces in string.
'''
# def test_make_snippet_blank_space_counter():
#     assert make_snippet("hello my name is Karys") == 4


'''
Given a string is 5 or less words, function make_snippet() returns the same string.
'''
def test_make_snippet_5_or_less_words_is_same_string():
    assert make_snippet("hello my name is Karys") == "hello my name is Karys"



'''
Given that a string is more than 5 words, make_snippet() returns the first 5 words and "..." to replace any words after it.
'''
def test_make_snippet_more_than_5_words_replaced_with_dots():
    assert make_snippet("hello my name is Karys nice to meet you") == "hello my name is Karys ..."
    assert make_snippet("The thing about bees is that their wing to body ratio is very uneven.") == "The thing about bees is ..."


'''
Design
A function called count_words that takes a string as an argument and returns the 
number of words in that string.
'''

'''
Completed and now redundant: Test that function count_words() can take the input of a string and return a list of all the words in that string.
'''
# def test_count_words_returns_list_of_words():
#     assert count_words("hello nice to meet you") == ["hello", "nice", "to", "meet", "you"]

'''
Completed and now redundant: Given that a character is not a letter, or the character is a special character (, ! ?) do not include in word_list.
'''
# def test_count_words_special_characters_omitted_from_word_list():
#     assert count_words("hello, nice to meet you!") == ["hello", "nice", "to", "meet", "you"]

'''
Test that function count_words() returns a number equal to the amount of words inside word_list.
'''
def test_count_words_returns_number_of_words():
    assert count_words("hello nice to meet you") == 5


'''Design
Takes a text input and outputs an estimate of reading time for that text, assuming the user can read
    200 words a minute.
'''

def test_empty_string_equals_0():
    assert text_reading_time("") == "I estimate it would take you 0 minute(s) to read this."


def test_data_type_int_throws_error():
    with pytest.raises(Exception) as e:
        text_reading_time(45)
    error_message = str(e.value)
    assert error_message == "Sorry, I can only take a passage of text. Please try again."


def test_data_type_none_throws_error():
    with pytest.raises(Exception) as e:
        text_reading_time(None)
    error_message = str(e.value)
    assert error_message == "Sorry, I can only take a passage of text. Please try again."


def test_200_words_equals_1_minute():
    assert text_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed massa turpis, maximus ac urna nec, mollis dictum metus. Proin eu enim pulvinar, condimentum nisi et, vehicula est. Etiam vel elementum sem. Maecenas id efficitur neque, vitae sollicitudin libero. Donec iaculis vehicula iaculis. Duis eget mollis risus, quis convallis nulla. Nam elit justo, pellentesque vel dui in, rhoncus lacinia ante. Cras diam quam, sagittis eu rutrum nec, pretium vel massa. Cras vel lacinia ante. Quisque eu eros nec diam maximus congue. Vestibulum id ligula est. Maecenas suscipit, neque at sollicitudin tempor, orci purus fermentum nisi, sit amet maximus justo sapien in lectus. Duis velit elit, tristique sed urna sed, dictum dapibus lacus. Nulla et nisi in lacus accumsan tincidunt. Aliquam venenatis quam erat. In quam urna, facilisis ut aliquet eu, vestibulum et ex. Sed id aliquet metus, vitae maximus neque. Duis ut orci magna. Phasellus varius tortor nec lorem sollicitudin, vel egestas lorem tempus. Integer quis erat id dolor ultricies posuere eu ac turpis. Fusce eros leo, suscipit at libero auctor, finibus pharetra augue. Vivamus et tellus et mauris pulvinar laoreet in congue elit. Nam commodo blandit turpis, et iaculis risus cursus sed. Aliquam id molestie lorem. Nam vitae dictum nisi.") == "I estimate it would take you 1.0 minute(s) to read this."

def test_100_words_equals_half_minute():
    assert text_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sit amet libero id enim imperdiet dapibus non ut augue. Proin eget hendrerit neque, nec sodales nibh. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus ultricies egestas porta. Fusce imperdiet tortor tortor, ac molestie orci lacinia sit amet. Cras et mi neque. Vivamus varius mauris tellus, sit amet placerat quam venenatis ut. Nunc sed lectus lectus. Praesent sit amet erat arcu. Duis mollis tellus nisl, et lobortis nunc sollicitudin at. Morbi sodales vestibulum dui, ut semper purus cursus a. Aliquam tincidunt euismod dolor, pharetra mattis diam interdum eget.") == "I estimate it would take you 0.5 minute(s) to read this."



'''
Design

Takes a sentence input, and checks the text starts with a capital letter and ends with a '.'
'''

def test_no_capital_letter_or_full_stop():
    assert grammar_check("i am going to the park today") == "Capitalisation is: none, full-stop usage is: none."

def test_correct_capital_letter_no_full_stop():
    assert grammar_check("I am going to the park today") == "Capitalisation is: correct, full-stop usage is: none."

def test_no_capital_letter_correct_full_stop():
    assert grammar_check("i am going to the park today.") == "Capitalisation is: none, full-stop usage is: correct."

def test_correct_capital_letter_and_full_stop():
    assert grammar_check("I am going to the park today.") == "Capitalisation is: correct, full-stop usage is: correct."

def test_incorrect_full_stop():
    assert grammar_check("I am. going to the park today") == "Capitalisation is: correct, full-stop usage is: incorrect."


'''
Design
As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.
'''

def test_todo_is_in_text():
    assert check_for_todo("This is my new #TODO for today.") == True

def test_todo_not_in_text():
    assert check_for_todo("This is my new task for today.") == False

def test_incorrect_data_type():
    with pytest.raises(Exception) as e:
        check_for_todo(100)
    error_message = str(e.value)
    assert error_message == "Error: invalid data type, only takes text."