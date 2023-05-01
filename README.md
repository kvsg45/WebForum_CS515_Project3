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

### Endpoint - 1 (Creation of Post with POST/post):

- I started testing this endpoint in postman application. once the shell script runs, we need to test in postman with the generated IP address from the terminal. using this local IP address: "http://127.0.0.1:5000/post" as required
- According to the designed code, the user need to give a JSON object as input which contains the following elements below:
    1. msg : The message user want to post
    2. user_id : The ID of the user
    3. user_key : The secret key of the user
- Example:
```
{
    "msg":"Hi",
    "user_id":"3",
    "user_key":"6Y3i9iqvKN0ZlejeekVJsg"
}

```
- The above mentioned fields must be given for creating any post. 
- Any of the fields missing will give raise to ValueError. If the user_key is incorrect or does not match with uder_id, it returns Invalid Credentials
- Instructions to test this Endpoint:
- Give the post details as below in postman:
```
{
    "msg":"XXX", #message of the user
    "user_id":"<int:id>", #User id
    "user_key":"<string:key>" #Secret Key of the User
}

```
- Testcases:

1. Case - 1
```
{
    "msg":"Hi From Test case 1",
    "user_id":"5",
    "user_key":"xExsCETjGbDD6X4uWnS8DA"
}

Output

{
    "id": 14,
    "key": "lD8ZO3hgMGnrf2YRtQS7Nw",
    "msg": "Hi From Test case 1",
    "timestamp": "2023-04-30T04:04:01.147144",
    "user_id": 5,
    "username": "rohith10"
}
```
2. Case - 2
```
{
    "msg":"Hi From Test case 2",
    "user_id":"3",
    "user_key":"xExsCETjGbDD6X4uWnS8DA"
}

Output

{
    "err": "Invalid user credentials"
}
```
3. Case - 3
```
{
    "msg":"Hi From Test case 3",
    "user_id":"5"
}

Output

{
    "err": "Request must contain \"user_id\" and \"user_key\" fields"
}
```
4. Case - 4
```
{
    "user_id":"5",
    "user_key":"xExsCETjGbDD6X4uWnS8DA"
}

Output

{
    "err": "Request must contain a \"msg\" field of type string"
}
```
5. Case - 5
```
{
    "msg":1234,
    "user_id":"5",
    "user_key":"xExsCETjGbDD6X4uWnS8DA"
}

Output

{
    "err": "Request must contain a \"msg\" field of type string"
}
```
Case - 6
```
{
    "msg":"Hi from Test case 6",
    "user_id":5,
    "user_key":"xExsCETjGbDD6X4uWnS8DA"
}

Output

{
    "id": 16,
    "key": "I6n4_fO7nGw44dfj_nXYjA",
    "msg": "Hi from Test case 6",
    "timestamp": "2023-04-30T04:12:02.911529",
    "user_id": 5,
    "username": "rohith10"
}
```
- All operations which are implemented successfully return the code 200 and which are invalid and failed returned the code 400

### Endpint - 2 (read a post with GET /post/{{id}}):

- We need to test in postman with the generated IP address from the terminal. using this local IP address: "http://127.0.0.1:5000/post" as required. This is same for all extensions hereby.
- To get a post we need to give "id" of the post in postman with the following IP Address format: "http://127.0.0.1:5000/post/\<int:id>"
1. Test case - 1
    "http://127.0.0.1:5000/post/4"
Output:
```
{
    "id": 4,
    "msg": "There is a pigeon in the classroom!!",
    "timestamp": "2023-04-30T00:48:12.138526",
    "user_id": 2,
    "username": "hari45"
}

```
2. Test case - 2
    input: "http://127.0.0.1:5000/post/20"
Output:
```
{
    "err": "Post not found with id 20"
}
```
Hence, this is the Endpoint 2 implementation

### Endpoint - 3: delete a post with DELETE /post/{{id}}/delete/{{key}}

- This endpoint is designed to delete a post with the respective post id and secret key of the post.
- The Input URL should be of the form "/post/<int:id>/delete/<string:key>" where id = post's id and key = post's key
- If the post id and key do not match, it raises error and returns the code 403
- If there is no ID present in the input URL, it raises error and returns the code 404

1. Test case - 1
    Input: http://127.0.0.1:5000/post/3/delete/7GepPrRYI5BCWNBSlwA0FA
Output:
```
{
    "id": 3,
    "key": "7GepPrRYI5BCWNBSlwA0FA",
    "timestamp": "2023-04-30T00:47:54.156596",
    "user_id": 2,
    "username": "hari45"
}
```
2. Test case - 2
    Input: http://127.0.0.1:5000/post/5/delete/s43gm_t_5xiQABp6ePbxkQ
Output:
```
{
    "err": "Key does not match for post with id 5"
}
```
3. Test case - 3
    Input: http://127.0.0.1:5000/post/15/delete/s43gm_t_5xiQABp6ePbxkQ
Output:
```
{
    "err": "Key does not match for post with id 15"
}
```

- Hence all the required cases are implemented for this extension

## 🧩 Extensions:

### Extension - 1 (Users and user keys)

- This Extension allows us to create new users by giving "name" and "username" values in JSON input.
- The given input is valid only when the above 2 values are given and also the username should be unique and do not match with the other usernames already present.
- The input URL in the postman given is: "http://127.0.0.1:5000/post" and the type of request is POST
- Given input must be JSON and error handling is done for the extension
- The ouput field contains JSON object containing 2 fields i.e., "id" and "key"
1. Test Case - 1
```
{
    "name":"Ramya",
    "username":"rvalukul"
}

Output

{
    "id": 5,
    "key": "aegyAG96mUCs9NrBgdyEnw"
}
```
2. Test Case - 2
```
{
    "name":"Arun"
}

Output

{
    "err": "Username field is missing or not a string."
}
```
3. Test Case - 3
```
{
    "username":"apjabdul"
}

Output

{
    "err": "Name field is missing or not a string."
}
```
4. Test Case - 4
```
"name":"Khande",
"username":"khand45"

Output

{
    "err": "Request body must be a valid JSON object."
}
```
5. Test Case - 5
```
{
    "name":9872,
    "username":"khand45"
}

Output:

{
    "err": "Name field is missing or not a string."
}
```
6. Test Case - 6
```
{
    "name":"Ramesh",
    "username":"rvalukul"
}

Output:

{
    "err": "Username is already taken."
}
```

### Extension - 2 User profiles (needs user)

- This Extension enables us to get user information by giving the user id in the Input URL or by giving the username
- The input URL is of the format "http://127.0.0.1:5000/user/\<int:id>" or "http://127.0.0.1:5000/user/\<string:username>"
- The given id or username is validated if present in the data stored dictionaries.
- The output is JSON with the following fields in it: "id", "name", "key", "username"
1. Test case - 1
Input: http://127.0.0.1:5000/user/2
```
{
    "id": 2,
    "key": "zxwjNIfXhGNXMjzE6FewEw",
    "name": "Hari",
    "username": "hari18"
}
```
2. Test case - 2
Input: http://127.0.0.1:5000/user/5
```
{
    "id": 5,
    "key": "aegyAG96mUCs9NrBgdyEnw",
    "name": "Ramya",
    "username": "rvalukul"
}
```
3. Test case - 3
Input: http://127.0.0.1:5000/user/20
```
{
    "err": "User not found with id 20"
}
```
4. Test case - 4
Input: http://127.0.0.1:5000/user/kvsg45
```
{
    "id": 1,
    "key": "FYPjgf_UNOvsYj9_VsimjA",
    "name": "Gouranga",
    "username": "kvsg45"
}
```
5. Test case - 5
Input: http://127.0.0.1:5000/user/gouranga
```
{
    "err": "User not found with username gouranga"
}
```
Hence the Implementation of Extension 2 is completed successfully.


### Extension - 3 Date- and time-based range queries

- This extension enables us to search posts within 2 different timestamps.
- In the input JSON, we need to give "start-time-str" and "end-time-str" values
- Posts which are created and present in the given timeframe are returned as JSON objects
1. Test case - 1
```
{
    "start_date_time":"2023-05-01"
}

Output:

[
    {
        "id": 1,
        "key": "4bdve3WIls--UJWmCMjbNQ",
        "msg": "Hello How are you everyone!",
        "timestamp": "2023-05-01T20:10:29.588142"
    },
    {
        "id": 2,
        "key": "iqX3qyxTBJQZzMKcEC5P2A",
        "msg": "Excited to meet you all",
        "timestamp": "2023-05-01T20:10:51.223520"
    },
    {
        "id": 3,
        "key": "h1fCdPDL6NO8sAs2YniV2g",
        "msg": "Hi Speaker!",
        "timestamp": "2023-05-01T20:11:19.338812",
        "user_id": 1,
        "username": "kvsg45"
    },
    {
        "id": 4,
        "key": "K48srGgmhhVaM4cRCHDh3g",
        "msg": "We are good",
        "timestamp": "2023-05-01T20:11:25.867823",
        "user_id": 1,
        "username": "kvsg45"
    },
    {
        "id": 5,
        "key": "ITelg6T7GppMRi--qceQZA",
        "msg": "How is your day",
        "timestamp": "2023-05-01T20:11:34.607039",
        "user_id": 1,
        "username": "kvsg45"
    },
    {
        "id": 6,
        "key": "PIPXA744zEpPjiVYmc1neA",
        "msg": "Wasuppp!!",
        "timestamp": "2023-05-01T20:11:46.609029",
        "user_id": 2,
        "username": "rvalukul"
    },
    {
        "id": 7,
        "key": "tzdrFozNOd5HlWlkGnD5Mw",
        "msg": "Let's go to NYC!!",
        "timestamp": "2023-05-01T20:12:05.827136",
        "user_id": 3,
        "username": "hari20"
    }
]
```
2. Test case - 2
```
{
    "end_date_time":"2023-05-01T20:11:33"
}

Output:

[
    {
        "id": 1,
        "key": "4bdve3WIls--UJWmCMjbNQ",
        "msg": "Hello How are you everyone!",
        "timestamp": "2023-05-01T20:10:29.588142"
    },
    {
        "id": 2,
        "key": "iqX3qyxTBJQZzMKcEC5P2A",
        "msg": "Excited to meet you all",
        "timestamp": "2023-05-01T20:10:51.223520"
    },
    {
        "id": 3,
        "key": "h1fCdPDL6NO8sAs2YniV2g",
        "msg": "Hi Speaker!",
        "timestamp": "2023-05-01T20:11:19.338812",
        "user_id": 1,
        "username": "kvsg45"
    },
    {
        "id": 4,
        "key": "K48srGgmhhVaM4cRCHDh3g",
        "msg": "We are good",
        "timestamp": "2023-05-01T20:11:25.867823",
        "user_id": 1,
        "username": "kvsg45"
    }
]
```
3. Test Case 3

```
{
    "start_date_time":"2023-05-01T20:10:30",
    "end_date_time":"2023-05-01T20:11:20"
}

Output:

[
    {
        "id": 2,
        "key": "iqX3qyxTBJQZzMKcEC5P2A",
        "msg": "Excited to meet you all",
        "timestamp": "2023-05-01T20:10:51.223520"
    },
    {
        "id": 3,
        "key": "h1fCdPDL6NO8sAs2YniV2g",
        "msg": "Hi Speaker!",
        "timestamp": "2023-05-01T20:11:19.338812",
        "user_id": 1,
        "username": "kvsg45"
    }
]
```
4. Test Case 4

```
{
    "start_date_time":"2023-05-02",
    "end_date_time":"2023-05-01"
}

Output:

{
    "err": "Start time cannot be ahead of End time. Please correct the time."
}

```
5. Test Case 5

```
{
    "start_date_time":"2023/04/28",
    "end_date_time":"2023-05-01"
}

Output

{
    "err": "Please follow the correct Date - Time ISO8601 format - YYYY-MM-DDTHH:MM:SS.ssssss or YYYY-MM-DD ."
}
```
6. Test Case 6
```
{
    "start_date_time":"2023-04-28",
    "end_date_time":"2023-05-01"
}

Output

No posts are created in the given timeframe

```

- Hence these are the test cases for the Date Time based search extension

### Extension - 4 User-based range queries

- This Extension enables us get posts based on the username given
- It Returns all the posts made by the user and the given username must be string
- username is given in the input url and no JSON input is required
- We will be using 'GET' method for this extension

1. Test Case - 1
    Input: http://127.0.0.1:5000/posts/user/kvsg45
Output
```
[
    {
        "id": 3,
        "key": "h1fCdPDL6NO8sAs2YniV2g",
        "msg": "Hi Speaker!",
        "timestamp": "2023-05-01T20:11:19.338812",
        "user_id": 1,
        "username": "kvsg45"
    },
    {
        "id": 4,
        "key": "K48srGgmhhVaM4cRCHDh3g",
        "msg": "We are good",
        "timestamp": "2023-05-01T20:11:25.867823",
        "user_id": 1,
        "username": "kvsg45"
    },
    {
        "id": 5,
        "key": "ITelg6T7GppMRi--qceQZA",
        "msg": "How is your day",
        "timestamp": "2023-05-01T20:11:34.607039",
        "user_id": 1,
        "username": "kvsg45"
    }
]
```
2. Test Case - 2
    Input: http://127.0.0.1:5000/posts/user/gouranga
Output:
```
{
    "err": "No username found: gouranga Please enter correct username"
}
```
3. Test Case - 3
    Input: http://127.0.0.1:5000/posts/user/hari20
Output:
```
[
    {
        "id": 7,
        "key": "tzdrFozNOd5HlWlkGnD5Mw",
        "msg": "Let's go to NYC!!",
        "timestamp": "2023-05-01T20:12:05.827136",
        "user_id": 3,
        "username": "hari20"
    }
]
```
Hence the necessary test cases are successfully implemented

### Extension - 5 Full Text Search

- This Extension enables us to search for the posts which contain given input query.
- Using regex we match for a pattern and return any posts if present
- It returns "No posts with given input query" if there are no matches
- "GET" method is used in this extension

1. Test Case - 1
```
{
    "value":"Hi"
}

Output

{
    "err": "Missing query field or query is not a string. Please correct it!"
}
```
2. Test Case - 2
```
{
    "query":"Hi"
}

Output

[
    {
        "id": 3,
        "key": "h1fCdPDL6NO8sAs2YniV2g",
        "msg": "Hi Speaker!",
        "timestamp": "2023-05-01T20:11:19.338812",
        "user_id": 1,
        "username": "kvsg45"
    }
]
```
3. Test Case - 3
```
{
    "query":"was"
}

Output

[
    {
        "id": 6,
        "key": "PIPXA744zEpPjiVYmc1neA",
        "msg": "Wasuppp!!",
        "timestamp": "2023-05-01T20:11:46.609029",
        "user_id": 2,
        "username": "rvalukul"
    }
]
```
4. Tesr Case - 4
```
{
    "query":"hari"
}

Output

No Matched posts with the query
```
- Hence this extension is implemented with no errors, the given input query is validated by ignosring case of the query and the message. 



## 🐛 Bugs/Issues:


## 💡 Example of issues/bugs and solution for it:


## 📖 Summaries of the tests performed:


## 🏃‍Run Guide

- Install python 3 in your machine
- Read README.md file to get more context of the project
- Inputs to the code is given by stdin
   ```shell
   $ python3 bc.py < input_statements.txt
   ```
  Here, input_statements.txt consists bunch of arthemtic statements which is passed to the BC calculator code.

