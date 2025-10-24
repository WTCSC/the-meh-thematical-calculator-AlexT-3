## Meh-Thematical Calculator
### Alexandria Tuell
> This program is an unenthusiastic calculator that is able to complete basic math operations including addition, subtraction, multiplication, and division while outputting sarcastic messages.

#### Requirements:
* Python3

### Testing:
There are several test functions to make sure that addition, subtraction, multiplication, and division instances all work properly. To ensure that your functions are working properly, navigate to the project directory and execute `pytest`.
The code should look like this if all functions are working properly:
```
============================================================================================== test session starts ==============================================================================================
platform linux -- Python 3.12.3, pytest-7.4.4, pluggy-1.4.0
rootdir: /home/tuella@CSGP.EDU/Projects/the-meh-thematical-calculator-AlexT-3
collected 9 items                                                                                                                                                                                               

test_calculator.py .........                                                                                                                                                                              [100%]

=============================================================================================== 9 passed in 0.01s ===============================================================================================
```


#### Startup and usage:
Within the terminal, type in the command `python3 mehth.py`
The program will first ask you to give it 2 numbers. Then, it asks for the operation you would like to calculate the numbers with. 
```
Ugh, it's you. Welcome to meh-culator I guess.
Give me your first number.4
Okay now I need your second number.9
What operation do you want? (+, -, *, /)*
```
The program then outputs the solution to your equation.
```
 Your total is 36.0 . Is that all or are you gonna keep bothering me?
```
