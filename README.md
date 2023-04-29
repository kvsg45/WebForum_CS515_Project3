# WebForum_CS515_Project3
Creation of Web Forum Using Python

## Venkata Santosh Gouranga Khande vkhande4@stevens.edu
#### GitHub URL: https://github.com/kvsg45/WebForum_CS515_Project3.git

# CS 515: Project 3 - Web Forum 💻

##  ⏰ Estimated hours: 34 hours

| Hours |                 Work                  |
|-------|:-------------------------------------:|
| 2     |    Reading and Understanding flow     |
| 3     |    Planning and Designing the baseline|
| 5     |        Implementing base flow         |
| 10    |       Implementing 5 extensions       |
| 3     |    modification & refactoring code    |
| 5     |   Testing code along with bug fixes   |
| 2     | creating README doc and GitHub set up |
| 4     | Creating Required Shell Scripts       |




##  🧪 Testing

- I started testing parallely while developing. Once, I write any function, I write `doctests` for the function and test the all possible outcomes. It helped me to fix runtime errors during coding phase.
- Once, the base flow was ready, I started testing with various of different arithmetics statements and fixed major of them. This was the overall base flow testing, not just a function or specific use-case. 
- The, I started implementing extensions. I did the testing for the extensions in a same way as base flow. Once, all the extensions were tested, I did base flow testing once again just to make sure it does not affect the original flow. 
- The code was tested for happy cases flow, then I added incomplete statements just to check that it does not fail for that.  I've covered major of corners cases and code was working with expectations of baseline as well as extensions too.

## 🐛 Bugs/Issues

- The latest code has no bugs or issues identified during overall testing.
- Future improvement: The if-else, loops, functions and many things can be added to current codebase.

## 💡 Example of issues/bugs and solution for it

- During testing, I found many of the issues/bugs which were difficult to solve. I've highlighted some below:
1. For unary operation, My code was failing if I've input with negative numbers (unary operation). The fix was a bit time-confusing for me. As the fix took me to change the code. The main issue was because of `-` can be used as subtraction operator as well as represent negative numbers too. Later, I found the fix for it and issue was resolved.
2. Another issue was with post and pre increment/decrement (`++` and `--`). The main reason behind failure was it has to attached with variable or number, not with any other operator or expression. In order to fix it, I need to keep track of prev parsed token. That was a bit difficult to fix when inputs are complex with parenthesis. But, with the help of TA, I found the fix and it worked in the end. 
3. The one issue was with boolean operator when the operator is `!` negate. We might've inputs like `!!!!!!1`. My code was failing for this case at the start. I brainstromed the idea because I was using 2 stacks and I forgot to add a conditions when stack is empty. Later, this fix worked and the inputs with multiple operators passed. 

## Baseline Implementation:


## 🧩 Extensions:
I've implemented 4 extensions. 
Each extension is described as below:
### 1. Op-equals:
- Op-equals extension helps us to evaluate the expressions containing  `+=, -=, *=, /=, %=, ^=, &&=, !!=` operators. 
  - The format for Op-equals is `VAR OP= ARG` means the `op` is applied on `VAR` with argument `ARG`. Usually, all binary operators can be used in Op-equals. 
    - Technically, `x op= y` is equal to `x = x op y`.
      - Refer below example for better understanding and context.
  1. input: 
    ```
    x = 3
    y = 2
    x += 1
    y -= 1
    print x, y
    x *= 2
    y /= 1.5
    print x, y
    ```

   - output: 
    ```
    4.0 1.0
    8.0 0.6666666666666666
    ```
   
    2. input: 
    ```
    x = 2.2
    y = 1.3
    x &&= 0
    y ||= 0
    print x, y
    ```
    
    - output: 
    ```
    0 1
    ```

   3. input: 
    ```
    x = 5
    y = 3
    x += ( y + 1 - 3 * 5)
    print x, y
    y /= ( x - x)
    ```
    
    - output: 
    ```
    -6.0 3.0
    divide by zero
    ```


### 2. Boolean Operators:
- Binary operations extension evaluates the input statements which contain mathematical expressions having `&& (and), || (or), ! (negation)` operators. `&` and `|` are binary operator while `!` is unary operator. 
- The output for any boolean expression would `1` means true or `0` means false. Generally, each non-zero number is treated as `true`. 
- `& (and), | (or)` : supports Op-equals operation too as these are binary operator and updates LHS variable too. 
- The return type for this boolean operator extension would be int, not float as it represent output as binary i.e. true/false. 
- These operators have lower precedence than arithmetic and relational expressions. 
- `|| and &&` are left associative, while `!` is non-associative.
- Test cases for this extension:

    1. input:
    ```
    print 1 && 1, 1 && 0, 1 || 0, !1, !!1, !!!1
    ```
  
    - output: 
    ```
    1 0 1 0 1 0
    ```
  
    2. input:
    ```
    x = -2
    y = 0
    print (x || y) || ( 1 && 1 && 0 && 1 || 1) && y
    print (x || y) || ( 1 && 1 && 0 && 1 || 1) || y
    print (x && y) && ( 1 && 1 && 0 && 1 || 1) || y
    ```
  
    - output:
    ```
    0
    1
    0
    ```

    3. input:
    ```
    x = 1
    x &&= 1
    y ||= 0
    print x, y
    print !x && 4, 3 && !y && x && 5
    ```
  
    - output:
    ```
    1 0
    0 1
    ```
### 3. Comments:
- Comments are used to improve more readability of written code. The parser just ignores the commented part of the input. 
- Comments extension helps us to identify whether the input given is markdown or not.  
- Comments can be done in 2 ways:
  1. Multi-line comments: it starts with `/*` till `*/`. It can start anywhere and end anywhere. All the token content in b/w these are simply ignored as its commented. 
  2. Single-line comments: it starts with `#`. It just comments the current one line only. 
- As per specs, we don't have support for nested comments. Comment can appear anywhere inbetween input token. 
- Test cases for this extension:
    1. input:
    ```
    print 1
    # print 2
    # printing 333
    print 4
    print 5
    /* print 6
    print 7
    print 8
    print 9 */
    print 10
    ```
    
    - output:
    ```
    1.0
    4.0
    5.0
    10.0
    ```
  
    2. input:
    ```
    x = 2 /* assigning value to x
    lets print it 
    now lets print it */ 
    print x
    y = 5 /* assign y to 5 */ + x /* now adding x to it */
    print x, y # printing value
    ```
  
    - output:
    ```
    2.0
    2.0 7.0
    ```

    3. input:
    ```
    x = 1 /* assign value 1 to x
    now print it */ print x
    ```
    - output:
    ```
    parse error
    ```
    - The reason is that there's no newline separating the two statements.
### 4. Relational Operations:
- Relational operations extension evaluates the input statements which contain `'==', '<=', '>=', '!=', '<', '>'` operators.  
- It represents true as `1` and false as `0`. Means the output 1 means the relation holds true for the input.
- Relational operators should be left associative and lower precedence than arithmteic operators.
- Test cases for this extension:

    1. input:
    ```
    x = 1 <= 2
    print 1 == 1, 2 != 2, 5 >= 6, 4 <= 4 < 0, x
    ```

    - ouput:
    ```
    1 0 0 0 1
    ```
  
    2. input:
    ```
    print x < 2 <= 2 < 3, 1 != 1, 1 > 2 <= 4 <= 5 < 8
    ```

    - output:
    ```
    1 0 0
    ```

   3. input:
    ```
    y = 1 << 2
    ```
    - output:
    ```
    parse error
    ```
## 🏃‍Run Guide

- Install python 3 in your machine
- Read README.md file to get more context of the project
- Inputs to the code is given by stdin
   ```shell
   $ python3 bc.py < input_statements.txt
   ```
  Here, input_statements.txt consists bunch of arthemtic statements which is passed to the BC calculator code.

