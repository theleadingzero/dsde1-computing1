
# Week 2 Exercises

# Tuesday - The Command Line

Go to [this site to download a zip file](https://github.com/veltman/clmystery) and the instructions to play the game. It is a text-based game to help you get comfortable navigating around the command line. Yes, you could easily cheat! But the point is to use the game to make learning these commands more fun. Could you give boring exercises if you prefer.

Can work on your own or in pairs.

# Thursday - Python Data Types and Scripting

This week is about getting comfortable with the building blocks of Python and how to start constructing a new program.

We'll start with working in the interactive python shell. 

1. Open the terminal within VS Code and type:

```python
python
```

2. You have now started an interactive session in Python. Go through the below exercises inside the interactive shell.

3. When you want to end a session, either type the following line or type together the CTRL button with D:

```python
exit()
```


## Printing Variables

1. Type in the code to compute `10 + 5`, `3 - 99`, and `5.5 * 3.2`

2. Notice that the answer is printed immediately. Now save each answer in a variable:

```python
a = 10+5
b = 3-99
c = 5.5.*3.2
```
3. Nothing prints immediately. Now type:

```python
a
```

The value held by `a` is now printed.

The value held by `a` is now printed.

4. Try typing:

```python
print(b)
```

This is an alternative way to print and the way you print when writing code in a saved file (which you'll do later).



## Number Datatypes

Numbers are either represented as whole numbers (integers or `int`) or as numbers with a fractional part or decimal point (`float`). 

Most of the operators are what you would expect - add with `+` and multiply with `*`. Note that division with `/` will always give an answer as a `float` and `//` will give an `int` which is the mathematical floor of the result of the division. You can use the `type( )` function to see the datatype of a variable.

1. Type in and run the code below to see some examples.


```python
type(100 * 8)
type(0.6 + 4)
```

You can find more information in the [Python docs](https://docs.python.org/3.6/tutorial/introduction.html).

2. Compare the output from `9/3` `9/3.` `9//3` and `9//2` and check their data types.


## Creating Variables

Like in other programming languages, you can create a variable that has a name and holds a value. What is different about Python is that you don't need to say what kind of data the variable is holding. Python will just note the data type you've used. For example, in Arduino or another C-language you would write:

```C
int number = 47;
```

But in Python you would write:

```python
number = 47
```

Note a couple differences. First there isn't `int` in front of the Python variable, but there also isn't a `;` at the end.

```python
# A longer example (this is a comment, not code)
apples = 3
oranges = 8
fruit = apples + oranges
print(fruit)
```

1. Create two variables `width` and `height` with two different values, then calculate the area (`width * height`) and store it in a new variable called `area`. Finally print the value held in `area`.



## Strings

Strings are text and need to be within pairs of `' '` or `" "`. More details can be found in the [Python Docs](https://docs.python.org/3.6/tutorial/introduction.html#strings). It's just best to stick with a single style and not mix both `' '` and `" "` in the same code. For Computing-1 we'll choose to use `' '` for all strings.

You can concatenate strings with the `+`. Try it out. 

1. Create two variables that each store a string - `'hello'` and `'world'`, then combine them into a new variable called `sentence` that prints `hello world`. 

__HINT:__ You'll need to add a space somewhere.


Longer strings that span multiple lines can be contained by a pair of three double quotes. 

2. Add another line of text to the below variable `long_string` and print the result.


```python
long_string = """
This is my very long string.
It can even contain line breaks.
"""
```

## Booleans

A Boolean datatype can only hold one of two possible values: `True` and `False`.

```python
# Two different Boolean variables
# Also, lines that start with # are comments
# These aren't interpreted by the Python interpreter
truth = True
lies = False
```

A Boolean comparison like `>` or `<=` generates a Boolean value. 

1. Try typing in the following code into the interactive shell.

```python
4>6
5==5
10<=20
```

2. Change the above code so that they each print ```False```.

## Errors

It's helpful to read the error messages that Python outputs when it comes across an error. You can read more about error messages in the [Python Docs](https://docs.python.org/3.6/tutorial/errors.html)

1. Run the below code and read what the error message says is going wrong, then fix the code so that it no longer causes an error.


```python
a = 123
print(A)
```


```python
4 + '32'
```


```python
answer = 42
print answer
```


## Importing modules

There are a large number of modules included in Python that can give you additional functionality. The [`math` module](https://docs.python.org/3/library/math.html) is one of them. 

```python
import math
print(math.e)
```

1. Go to the [module documentation](https://docs.python.org/3/library/math.html) and find out how to finish the code below.

```python
import math

radius = 5

# Calculate the area of the circle using the variable radius
# Hint: you don't need to type out pi, it is included in the math module
area = 

```

2. Using functions from the `math` module, use code to solve the following equations:

    y = 2 + sin(x) when x = 3

    y = log(x-3) + 2(x+4) when x = 5


3. You can 'tab complete' inside of the interacive Python shell. Type `math.c` and hit 'tab' twice quickly to see all the functions within `math` that start with the letter c. 

4. You can view the help documentation for a function directly in the terminal. For example `help(math.floor)` shows the documentation for the floor function. The 'Q' key quits the help interface and returns you to the interactive Python terminal. Find and view the help documentation for taking the square root of a number.


## Saving Code in Python Files

Note that importing modules only lasts for a single session of the interactive shell. If you leave the session by typing `exit()` and then start a new session with `python`, you will have to re-import any modules you want to use. All the previous variables you had created in earlier sessions will also be erased. This is a good feature - it means you know you are starting from a clean slate whenever you start a new interactive shell session.

However, when you want to start building up more complicated code, you don't want to type it all out each time. Instead you can save your code in a text file ending with `.py`. This indicates is Python code.

1. Inside of VS Code create a new file (you can do that from the File menu). Type the following code:

```python
message = 'If this has printed, you have run the code successfully.'
print(message)
```

2. Save the file as `firstProgram.py`. You can save it wherever you'd like on your computer, but keep track of where that is as you'll need to use the command line to get there.

3. In the terminal in VS Code, use `cd` to move to the same folder as where you saved `firstProgram.py`.

4. Run the code by typing `python firstProgram.py`

5. Instead of starting the interactive Python shell, the Python interpreter will run the Python code in your file and then return to the command line when all the code has been run. 

__HINT:__ If at any point the code seems to be stuck and isn't ending, you can type `CTRL` + `c` to quit the running code.


## Getting Input Interactively From The Command Line

1. Read the [Python documentation on the `input()` function](https://docs.python.org/3/library/functions.html#input). 

2. Modify your Python code in `firstProgram.py` so that it asks the user to enter a message and then prints the message again for the user. The interaction would look like this:

```
$ python firstProgram.py
$ What is your message? This is my message.
$ This is my message.
```

## Stretch Exercise: Number Guessing Game

Building on the Python code asking for a message and then printing it again, write a program that asks the user to guess a number between 1 and 10. The program then prints whether the number is equal to the random number generated by the code. So it then prints `True` and ends the program if the input number is equal to the random number. If it is not equal to the number generated by the code, it prints `False` and ends the program.

As a starting point, try writing code to match this pseudocode (a mix between natural language and generic technical language):

```
    1. Prompt user for input
    2. Generate a random number
    3. Compare generated number to input
    4. Print result
```

As data read in by `input()` is always saved as a `string`, here is some code to help you convert the input number into an `int` (this is called casting something as an integer).

```python
guess = input()
guess = int(guess)
```

__HINT 1:__ Look through the `random` module for useful ways to generate a random number.

__HINT 2:__ You don't need to use `if` statements - we haven't learned how to use them in Python yet. Think about how you can use a Boolean variable in a clever way with the `==` comparator.