# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def reading_time(text)"
    """Calculates reading time from a string
    
    Parameters:
        text: the text from which speed is calculated from in the form of a string

    Returns "Your text will take {x} minute/s to read" where x is a number to 1 dp and minutes is a string

    Side effects: None

    """
    pass

    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty string
It responds with "No text present"
"""
reading_time("") => "No text present"

"""
Given a list of 200 words
It returns a calculated reading time of 1 minute
"""
reading_time(200-word-string) => "Your text will take 1.0 minute/s to read"

"""
Given a list of 400 words
It returns a calculated reading time of 2 minutes
"""
reading_time(400-word-string) => "Your text will take 2.0 minute/s to read"

"""
Given a list of 100 words
It returns a calculated reading time of 0.5 minutes
"""
reading_time(100-word-string) => "Your text will take 0.5 minute/s to read"


```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


Ensure all test function names are unique, otherwise pytest will ignore them!
