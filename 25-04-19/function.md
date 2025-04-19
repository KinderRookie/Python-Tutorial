# Function

Functions are reusable blocks of code that perform a specific task. They help organize code, reduce repetition, and improve readability.

## 1. Defining a Function

Use the `def` keyword to define a function.

```python
def greet():
    print("Hello, world!")
```

Calling the function
```python
greet()
```

## 2. Arguments of a function
Argument(=parameter) is value that we can pass through function. A function can get mutiple arguments and perform specific job using passed arguments. 

Example
---
```Python
def add_two_numbers(num1, num2):
    print("Number1: ", num1)
    print("Number2: ", num2)

    result = num1 + num2

    return result
```

```Python
result = add_two_numbers(3, 8)
print(result)
```
*OUTPUT*

Number1: 3  
Number2: 8  
11
---

Instead of repeating same blocks of codes, make blocks into function so that we can reuse afterwards!



    

