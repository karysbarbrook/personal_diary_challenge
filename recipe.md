# {{PROBLEM}} Function Design Recipe



Copy this into a `recipe.md` in your project and fill it out.

## EXERCISE 1

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def text_reading_time(text):
    """takes a text input and outputs an estimate of reading time for that text, assuming the user can read
    200 words a minute.

    Parameters: (list all parameters and their types)
        text: a string containing words

    Returns: (state the return value and its type)
        an f-string containing an int value of the number of minutes it would take to read the text

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text containing 200 words
It returns an f-string with an int value of 1
"""
text_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed massa turpis, maximus ac urna nec, mollis dictum metus. Proin eu enim pulvinar, condimentum nisi et, vehicula est. Etiam vel elementum sem. Maecenas id efficitur neque, vitae sollicitudin libero. Donec iaculis vehicula iaculis. Duis eget mollis risus, quis convallis nulla. Nam elit justo, pellentesque vel dui in, rhoncus lacinia ante. Cras diam quam, sagittis eu rutrum nec, pretium vel massa. Cras vel lacinia ante. Quisque eu eros nec diam maximus congue. Vestibulum id ligula est. Maecenas suscipit, neque at sollicitudin tempor, orci purus fermentum nisi, sit amet maximus justo sapien in lectus. Duis velit elit, tristique sed urna sed, dictum dapibus lacus. Nulla et nisi in lacus accumsan tincidunt. Aliquam venenatis quam erat. In quam urna, facilisis ut aliquet eu, vestibulum et ex. Sed id aliquet metus, vitae maximus neque. Duis ut orci magna. Phasellus varius tortor nec lorem sollicitudin, vel egestas lorem tempus. Integer quis erat id dolor ultricies posuere eu ac turpis. Fusce eros leo, suscipit at libero auctor, finibus pharetra augue. Vivamus et tellus et mauris pulvinar laoreet in congue elit. Nam commodo blandit turpis, et iaculis risus cursus sed. Aliquam id molestie lorem. Nam vitae dictum nisi.") => "I estimate it would take you 1 minute(s) to read this."

"""
Given an empty string
It returns an f-string with an int value of 0
"""
text_reading_time("") => "I estimate it would take you 0 minute(s) to read this."

"""
Given a text containing 100 words
It returns an f-string with an int value of 0.5
"""
text_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sit amet libero id enim imperdiet dapibus non ut augue. Proin eget hendrerit neque, nec sodales nibh. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus ultricies egestas porta. Fusce imperdiet tortor tortor, ac molestie orci lacinia sit amet. Cras et mi neque. Vivamus varius mauris tellus, sit amet placerat quam venenatis ut. Nunc sed lectus lectus. Praesent sit amet erat arcu. Duis mollis tellus nisl, et lobortis nunc sollicitudin at. Morbi sodales vestibulum dui, ut semper purus cursus a. Aliquam tincidunt euismod dolor, pharetra mattis diam interdum eget.") => "I estimate it would take you 0.5 minute(s) to read this."


"""
Given a None or an int value
It throws an error
"""
text_reading_time(None/int) => throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

def test_empty_string_equals_0():
    assert text_reading_time("") == "I estimate it would take you 0 minute(s) to read this."


def test_data_type_not_string_throws_error():
    with pytest.raises(Exception) as e:
        text_reading_time(45)
    assert str(e.value) == "Sorry, I can only take a passage of text, not numbers. Please try again."
    with pytest.raises(Exception) as e:
        text_reading_time(None)
    assert str(e.value) == "Error: no text identified. Please try again."


def test_200_words_equals_1_minute():
    assert text_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed massa turpis, maximus ac urna nec, mollis dictum metus. Proin eu enim pulvinar, condimentum nisi et, vehicula est. Etiam vel elementum sem. Maecenas id efficitur neque, vitae sollicitudin libero. Donec iaculis vehicula iaculis. Duis eget mollis risus, quis convallis nulla. Nam elit justo, pellentesque vel dui in, rhoncus lacinia ante. Cras diam quam, sagittis eu rutrum nec, pretium vel massa. Cras vel lacinia ante. Quisque eu eros nec diam maximus congue. Vestibulum id ligula est. Maecenas suscipit, neque at sollicitudin tempor, orci purus fermentum nisi, sit amet maximus justo sapien in lectus. Duis velit elit, tristique sed urna sed, dictum dapibus lacus. Nulla et nisi in lacus accumsan tincidunt. Aliquam venenatis quam erat. In quam urna, facilisis ut aliquet eu, vestibulum et ex. Sed id aliquet metus, vitae maximus neque. Duis ut orci magna. Phasellus varius tortor nec lorem sollicitudin, vel egestas lorem tempus. Integer quis erat id dolor ultricies posuere eu ac turpis. Fusce eros leo, suscipit at libero auctor, finibus pharetra augue. Vivamus et tellus et mauris pulvinar laoreet in congue elit. Nam commodo blandit turpis, et iaculis risus cursus sed. Aliquam id molestie lorem. Nam vitae dictum nisi.") == "I estimate it would take you 1 minute(s) to read this."


def test_100_words_equals_half_minute():
    assert text_reading_time("Lorem ipsum dolor sit amet, consectetur adipiscing elit. In sit amet libero id enim imperdiet dapibus non ut augue. Proin eget hendrerit neque, nec sodales nibh. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus ultricies egestas porta. Fusce imperdiet tortor tortor, ac molestie orci lacinia sit amet. Cras et mi neque. Vivamus varius mauris tellus, sit amet placerat quam venenatis ut. Nunc sed lectus lectus. Praesent sit amet erat arcu. Duis mollis tellus nisl, et lobortis nunc sollicitudin at. Morbi sodales vestibulum dui, ut semper purus cursus a. Aliquam tincidunt euismod dolor, pharetra mattis diam interdum eget.") == "I estimate it would take you 0.5 minute(s) to read this."




```


## EXERCISE 2

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable
sentence-ending punctuation mark.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def grammar_check(text):
    """takes a sentence input, and checks the text starts with a capital letter and ends with a '.'

    Parameters: (list all parameters and their types)
        text: a string containing words

    Returns: (state the return value and its type)
        Two strings: one stating whether there is capitalisation at the start of the sentence, and 
        another stating whether there is a full stop at the end of the sentence.

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a sentence with no capital letter at the start and no full stop at the end
It returns two strings stating each one is not grammatically correct
"""
grammar_check("i am going to the park today") => "No capitalisation." "No full-stop at the end of the sentence."

"""
Given a sentence with correct capitalisation, but no full-stop
It returns two strings stating one is grammatically correct, and the other one isn't.
"""
grammar_check("I am going to the park today") => "Correct capitalisation." "No full-stop at the end of the sentence."

"""
Given a sentence with no capitalisation, and correct full-stop
It returns two strings stating one is grammatically correct, and the other one isn't.
"""
grammar_check("i am going to the park today.") => "No capitalisation." "Correct use of full-stop at the end of the sentence."


"""
Given a sentence with both correct capitalisation and correct full-stop
It returns two strings stating each one is grammatically correct.
"""
grammar_check("I am going to the park today.") => "Correct capitalisation." "Correct use of full-stop at the end of the sentence."


"""
Given a sentence with a full stop, in a location anywhere but the end of the sentence
It returns a string stating incorrect usage of the full-stop.
"""
grammar_check("I am. going to the park today") => "Correct capitalisation." "Incorrect usage of a full-stop: it should be placed at the end of a sentence."
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

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



```

## CHALLENGE

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def check_for_todo(text):
    """


    Parameters: (list all parameters and their types)
        text: a string containing text

    Returns: (state the return value and its type)
        returns True or False

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects


    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given that the text includes the substring #TODO
It returns True
"""
check_for_todo("This is my new #TODO for today.") => True

"""
Given that the text does not include the substring #TODO
It returns False
"""
check_for_todo("This is my new task for today.") => False

"""
Given that the input of the 'text' argument is any data type other than string
It throws an error
"""
# could be more specific and check each data type, e.g. int, Boolean, etc. but for now will leave as is.
check_for_todo(79) => "Error: invalid data type, only takes text."

"""

"""


"""

"""


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

```python

# my test file already has imported pytest

def test_todo_is_in_text():
    assert check_for_todo("This is my new #TODO for today.") == True

def test_todo_not_in_text():
    assert check_for_todo("This is my new task for today.") == False

def test_incorrect_data_type():
    with pytest.raises(Exception) as e:
        check_for_todo(100)
    error_message = str(e.value)
    assert error_message == "Error: invalid data type, only takes text."



```