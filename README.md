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




##  🧪 Testing the Baseline (3 Endpoints) and Extensions (5):

# Endpoint - 1 (Creation of Post with POST/post):

-I started testing this endpoint in postman application. once the shell script runs, we need to test in postman with the generated IP address from the terminal. using this local IP address: "http://127.0.0.1:5000/post" as required
-According to the designed code, the user need to give a JSON object as input which contains the following elements below:
1. msg : The message user want to post
2. user_id : The ID of the user
3. user_key : The secret key of the user
-Example:
```
{
    "msg":"Hi",
    "user_id":"3",
    "user_key":"6Y3i9iqvKN0ZlejeekVJsg"
}

```
-The above mentioned fields must be given for creating any post. 
-Any of the fields missing will give raise to ValueError. If the user_key is incorrect or does not match with uder_id, it returns Invalid Credentials
-Instructions to test this Endpoint:
-Give the post details as below in postman:
```
{
    "msg":"XXX", #message of the user
    "user_id":"<int:id>", #User id
    "user_key":"<string:key>" #Secret Key of the User
}

# Endpint - 2 (read a post with GET /post/{{id}}):






## 🐛 Bugs/Issues


## 💡 Example of issues/bugs and solution for it



## Baseline Implementation:


## 🧩 Extensions:
I've implemented 5 extensions. 
Each extension is described as below:

### 1. Users and user keys:
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


### 2. User profiles (needs user):
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
### 3. Date- and time-based range queries
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
### 4. User-based range queries (needs user)
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
    

### 4. User-based range queries (needs user):


### 5. Fulltext search:


## 🏃‍Run Guide

- Install python 3 in your machine
- Read README.md file to get more context of the project
- Inputs to the code is given by stdin
   ```shell
   $ python3 bc.py < input_statements.txt
   ```
  Here, input_statements.txt consists bunch of arthemtic statements which is passed to the BC calculator code.

