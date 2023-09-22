# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## ------------------ EXERCISES ----------------------

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my tasks
I want a program that I can add todo tasks to and see a list of them.

As a user
So that I can focus on tasks to complete
I want to mark tasks as complete and have them disappear from the list.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class TodoTaskTracker():
    # User-facing properties:
    #   n/a

    def __init__(self):
        # Parameters:
        #   n/a
        self.list = []
        # Side effects:
        #   n/a
        pass # No code here yet

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the task to self.list
        pass # No code here yet

    def display_tasks(self):
        # Returns:
        #   List containing all added tasks
        # Side-effects:
        #   Throws an exception if no task is set
        pass # No code here yet

    def task_completed(self, task):
        # Parameters:
        # task: string representing a single task
        # Returns:
        # An f-string that confirms task is completed and shows updated list with task removed
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given one task is added to the task list,
display_tasks() presents a list of all the current incomplete tasks.

"""
tasks = TodoTaskTracker()
task1.add("Wash the dishes")
tasks.display_tasks() => ["Wash the dishes"]

"""
Given multiple tasks are added to the task list,
display_tasks() presents a list of all the current incomplete tasks,
"""
tasks = TodoTaskTracker()
tasks.add("Wash the dishes")
tasks.add("Mow the lawn")
tasks.add("Make dinner at 7pm")
tasks.display_tasks() => ["Wash the dishes", "Mow the lawn", "Make dinner at 7pm"]

"""
Given a task in the list is input into task_completed(),
It returns an f-string saying task has been completed and the updated list with that task removed.
"""
tasks = TodoTaskTracker()
tasks.add("Wash the dishes")
tasks.add("Mow the lawn")
tasks.add("Make dinner at 7pm")
tasks.task_completed("Mow the lawn") => "Task: Mow the lawn has been completed. Checking it off your list... current todo list now: ['Wash the dishes', 'Make dinner at 7pm']"

'''
Given there are no tasks in the task list when calling display_tasks(),
It throws an error.
'''
tasks = TodoTaskTracker()
tasks.display_tasks() => "You have no tasks to display."

'''
Given that a user tries to complete a task that is not in their task list,
It throws an error.
'''
tasks = TodoTaskTracker()
tasks.task_completed() => "Task does not exist in your list."

'''
Given that a user tries to add a task that already exists in the list,
It throws an error.
'''
tasks = TodoTaskTracker()
tasks.add("Wash the dishes")
tasks.add("Wash the dishes") => "You've already added this task to your list."

'''
Given that a user tries to check off a task, but their input uses some capital letters or is all lowercase,
task_completed() converts that input so it is not case sensitive and the user can easily modify their tasks.
'''
tasks = TodoTaskTracker()
tasks.add("Mow the lawn")
tasks.task_completed("mow the lawn") => "Task: Mow the lawn has been completed. Checking it off your list... current todo list now: ['Wash the dishes', 'Make dinner at 7pm']"




```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

``` python

def test_display_one_task_correct():
    tasks = TodoTaskTracker()
    tasks.add("Wash the dishes")
    assert tasks.display_tasks() == ["Wash the dishes"]

def test_display_multiple_tasks_correct():
    tasks = TodoTaskTracker()
    tasks.add("Wash the dishes")
    tasks.add("Mow the lawn")
    tasks.add("Make dinner at 7pm")
    assert tasks.display_tasks() == ["Wash the dishes", "Mow the lawn", "Make dinner at 7pm"]

def test_task_checklist_works():
    tasks = TodoTaskTracker()
    tasks.add("Wash the dishes")
    tasks.add("Mow the lawn")
    tasks.add("Make dinner at 7pm")
    assert tasks.task_completed("Mow the lawn") == "Task: Mow the lawn has been completed. Checking it off your list... current todo list now: ['Wash the dishes', 'Make dinner at 7pm']"

def test_error_when_no_tasks_to_display():
    tasks = TodoTaskTracker()
    with pytest.raises(Exception) as e:
        tasks.display_tasks()
    error_message = str(e.value)
    assert error_message == "You have no tasks to display."

def test_error_when_task_does_not_exist():
    tasks = TodoTaskTracker()
    with pytest.raises(Exception) as e:
        tasks.task_completed()
    error_message = str(e.value)
    assert error_message == "Task does not exist in your list."

def test_error_when_trying_to_add_task_that_already_exists():
    tasks = TodoTaskTracker()
    tasks.add("Wash the dishes")
    with pytest.raises(Exception) as e:
        tasks.add("Wash the dishes")
    error_message = str(e.value)
    assert error_message == "You've already added this task to your list."

def test_task_completed_is_not_case_sensitive():
    tasks = TodoTaskTracker()
    tasks.add("Mow the lawn")
    assert tasks.task_completed("mow the lawn") == "Task: Mow the lawn has been completed. Checking it off your list... current todo list now: ['Wash the dishes', 'Make dinner at 7pm']"

```
## -------- CHALLENGE ------------

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker():
    # User-facing properties:
    #   n/a

    def __init__(self):
        # Parameters:
        #  n/a
        self.music_list = []
        # Side effects:
        #   n/a
        pass # No code here yet

    def add(self, music):
        # Parameters:
        #   string representing singular music track
        # Returns:
        #  none
        # Side-effects
        #   music is added to self.music_list
        pass # No code here yet

    def display_tracks(self):
        # Parameters:
        # n/a
        # Returns:
        #  list of music the user has listened to. 
        # Side-effects:
        #   n/a
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a user adds multiple tracks they've listened to,
display_tracks() will return a list of all of them.

"""
tracking_music = MusicTracker()
tracking_music.add("Queen: Don't Stop Me Now")
tracking_music.add("Adele: Rolling In The Deep")
tracking_music.add("Nothing But Thieves: Impossible")
tracking_music.display_tracks() => ["Queen: Don't Stop Me Now", "Adele: Rolling In The Deep", "Nothing But Thieves: Impossible"]


"""
Given that a user tries to enter a number (or simply not a string),
It throws an error.

"""
tracking_music = MusicTracker()
tracking_music.add(236) => "Error: can only take text."



"""
Given that the user tries to display their listening list when they haven't added any music,
It throws an error.
"""
tracking_music = MusicTracker()
tracking_music.display_tracks() => "No track listening record available. Try adding some songs first."


"""
Given that the user tries to add a track they've already listened to,
It throws an error.
"""
tracking_music = MusicTracker()
tracking_music.add("Queen: Don't Stop Me Now")
tracking_music.add("Queen: Don't Stop Me Now") => "You've already added this song to your listening record."
# note: may want to allow users to add a song multiple times so it shows how many times they listened to that
# track, however as this class currently does not track number of listens, feels unnecessary for now.



```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

``` python

def test_multiple_tracks_display_correct():
    tracking_music = MusicTracker()
    tracking_music.add("Queen: Don't Stop Me Now")
    tracking_music.add("Adele: Rolling In The Deep")
    tracking_music.add("Nothing But Thieves: Impossible")
    assert tracking_music.display_tracks() == ["Queen: Don't Stop Me Now", "Adele: Rolling In The Deep", "Nothing But Thieves: Impossible"]

def test_correct_data_type():
    tracking_music = MusicTracker()
    with pytest.raises(Exception) as e:
        tracking_music.add(236)
    error_message = str(e.value)
    assert error_message == "Error: can only take text."

def test_error_when_empty_list_displayed():
    tracking_music = MusicTracker()
    with pytest.raises(Exception) as e:
        tracking_music.display_tracks()
    error_message = str(e.value)
    assert error_message == "No track listening record available. Try adding some songs first."

def test_error_when_adding_song_already_added():
    tracking_music = MusicTracker()
    tracking_music.add("Queen: Don't Stop Me Now")
    with pytest.raises(Exception) as e:
        tracking_music.add("Queen: Don't Stop Me Now")
    error_message = str(e.value)
    assert error_message == "You've already added this song to your listening record."




```