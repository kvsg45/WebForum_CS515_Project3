import secrets
from flask import Flask, request, jsonify
from datetime import datetime
import threading
import re
app = Flask(__name__)

# Name: Gouranga Khande
# CWID: 20008981
# email-id: vkhande4@stevens.edu

lock = threading.Lock()
users = {}
user_id = 0
posts = {}
id = 0

# Extension 1 - Users and user keys
@app.route('/user', methods=['POST'])
def create_user():
    with lock:
        # check if request body is a valid JSON object
        if not request.is_json:
            return jsonify({'err': 'Request body must be a valid JSON object.'}), 400
        
        # check if the name and username fields are present and strings
        name = request.json.get('name')
        if not name or not isinstance(name, str):
            return jsonify({'err': 'Name field is missing or not a string.'}), 400
        
        username = request.json.get('username')
        if not username or not isinstance(username, str):
            return jsonify({'err': 'Username field is missing or not a string.'}), 400
        
        # check if the username is already taken
        for user in users.values():
            if user['username'] == username:
                return jsonify({'err': 'Username is already taken.'}), 400
        
        # generate unique id and key for user
        global user_id
        user_id += 1
        user_key = secrets.token_urlsafe(16)
        
        # add user to dictionary
        users[user_id] = {
            'id': user_id,
            'name': name,
            'key': user_key,
            'username': username
        }
        
        # return user id and key as JSON response
        return jsonify({
            'id': user_id,
            'key': user_key
        }), 200

# Extension 2 - User profiles (needs user)
@app.route('/user/<int:id>', methods=['GET'])
@app.route('/user/<string:username>', methods=['GET'])
def read_user(id=None, username=None):
    with lock:
        if id:
            if id not in users:
                error_message = {'err': 'User not found with id ' + str(id)}
                return jsonify(error_message), 404
            else:
                user_data = {
                    'id': id,
                    'name': users[id]['name'],
                    #'key': users[id]['key'],
                    'username': users[id]['username']
                }
                return jsonify(user_data), 200
        elif username:
            for user_id, user_info in users.items():
                if user_info['username'] == username:
                    user_data = {
                        'id': user_id,
                        'name': user_info['name'],
                        #'key': user_info['key'],
                        'username': user_info['username']
                    }
                    return jsonify(user_data), 200
            error_message = {'err': 'User not found with username ' + username}
            return jsonify(error_message), 404

# Additional Extension for Updating user information
@app.route('/user/<int:id>', methods=['PUT'])
def update_user(id):
    with lock:
        if id in users:
            user = users[id]
            # get updated data from request body
            data = request.json
            # check if user's key matches
            if data.get('key') == user['key']:
                # update metadata
                if data.get('name'):
                    user['name'] = data['name']
                if data.get('username'):
                    # check if the username is same as before
                    if user['username'] == data['username']:
                        pass
                    # check if the username is already taken
                    else:
                        for user_info in users.values():
                            if user_info['username'] == data['username']:
                                return jsonify({'error': 'Username is already taken.'}), 400
                        user['username'] = data['username']

                return jsonify({'message': 'User metadata updated successfully.'}), 200
            else:
                return jsonify({'error': 'Invalid user key.'}), 401
        else:
            return jsonify({'error': 'User not found.'}), 404

# Endpoint #1: create a post with POST /post
@app.route('/post', methods=['POST'])
def create_post():
    with lock:
        try:
            request_data = request.get_json()

            if 'msg' not in request_data or not isinstance(request_data['msg'], str):
                raise ValueError('Request must contain a "msg" field of type string')
            
            key = secrets.token_urlsafe(16)
            timestamp = datetime.utcnow().isoformat()
            
            global id
            id += 1

            if 'user_id' in request_data and 'user_key' in request_data:
                
                user_id = int(request_data['user_id'])
                user_key = request_data['user_key']

                if user_id not in users or users[user_id]['key'] != user_key:
                    raise ValueError('Invalid user credentials')

                # lets get username from user_id
                username = users[user_id]['username']

                post = {
                    'id': id,
                    'msg': request_data['msg'],
                    'key': key,
                    'timestamp': timestamp,
                    'user_id': user_id,
                    'username': username
                }
                posts[id] = post
            elif ('user_id' in request_data and 'user_key' not in request_data) or ('user_id' not in request_data and 'user_key' in request_data):
                raise ValueError('Request must both user_id and user_key :)')
            else:
                post = {
                    'id': id,
                    'msg': request_data['msg'],
                    'key': key,
                    'timestamp': timestamp,
                }
                posts[id] = post
            return jsonify(post), 200

        except ValueError as e:
            error_message = {'err': str(e)}
            return jsonify(error_message), 400

        except Exception as e:
            error_message = {'err': str(e)}
            return jsonify(error_message), 500

# Endpoint #2: read a post with GET /post/{{id}}
@app.route('/post/<int:id>', methods=['GET'])
def read_post(id):
    with lock:
        if id not in posts:
            error_message = {'err': 'Post not found with id ' + str(id)}
            return jsonify(error_message), 404
        else:
            post = posts[id]
            read_check=list(post.keys())
            if read_check.__contains__("user_id") and read_check.__contains__("username"):
                post_data = {
                    'id': post['id'],
                    'msg': post['msg'],
                    'timestamp': post['timestamp'],
                    "user_id": post["user_id"],
                    "username": post["username"]
                }
            else:
                post_data = {
                    'id': post['id'],
                    'msg': post['msg'],
                    'timestamp': post['timestamp'],
                }
            return jsonify(post_data), 200
        
# Endpoint #3: delete a post with DELETE /post/{{id}}/delete/{{key}}
@app.route('/post/<int:id>/delete/<string:key>', methods=['DELETE'])
def delete_post(id, key):
    with lock:
        if id not in posts:
            error_message = {'err': 'Post not found with id ' + str(id)}
            return jsonify(error_message), 404
        elif posts[id]['key'] != key:
            error_message = {'err': 'Key does not match for post with id ' + str(id)}
            return jsonify(error_message), 403
        else:
            post = posts.pop(id)
            post_check=list(post.keys())
            if post_check.__contains__("user_id") and post_check.__contains__("username"):
                post_data = {
                    'id': post['id'],
                    'key': post['key'],
                    'timestamp': post['timestamp'],
                    'user_id': post['user_id'],
                    'username': post['username']
                }
            else:
                post_data = {
                    'id': post['id'],
                    'key': post['key'],
                    'timestamp': post['timestamp'],
                }
            return jsonify(post_data), 200

# Extension 3 - Date- and time-based range queries
@app.route('/posts', methods=['GET'])
def get_posts():
    with lock:
        # check if request body is a valid JSON object
        if not request.is_json:
            return jsonify({'err': 'Request body must be a valid JSON object.'}), 400
        
        # check if the name and username fields are present and strings
        start_time_str = request.json.get('start_date_time')
        end_time_str = request.json.get('end_date_time')
        if not start_time_str and not end_time_str:
            return jsonify({'err': 'Start date time and End Date time fields are missing. Please include "start_date_time" and "end_date_time" '}), 400
        if (start_time_str and not isinstance(start_time_str, str)) or (end_time_str and not isinstance(end_time_str, str)):
            return jsonify({'err': 'Both fields should be strings'}), 400
        
        try:
            if(start_time_str and end_time_str):
                start_time = datetime.fromisoformat(start_time_str)
                end_time = datetime.fromisoformat(end_time_str)
            elif(start_time_str and not end_time_str):
                start_time = datetime.fromisoformat(start_time_str)
            elif(end_time_str and not start_time_str):
                end_time = datetime.fromisoformat(end_time_str)
        except ValueError:
            return jsonify({'err': 'Please follow the correct Date - Time ISO8601 format - YYYY-MM-DDTHH:MM:SS.ssssss or YYYY-MM-DD .'}), 400
        
        if(start_time_str and end_time_str):
            if start_time>end_time:
                return jsonify({'err': 'Start time cannot be ahead of End time. Please correct the time.'}), 400   
           
        
        # Filter posts based on timestamp range
        filtered_posts = []
        for post in posts:
            
            post_time = datetime.fromisoformat(posts[post]['timestamp'])
            if start_time_str and end_time_str:
                if start_time <= post_time <= end_time:
                    return_post=posts[post]
                    del return_post['key']
                    filtered_posts.append(return_post)
            elif start_time_str:
                if start_time <= post_time:
                    return_post=posts[post]
                    del return_post['key']
                    filtered_posts.append(return_post)
            elif end_time_str:
                if post_time <= end_time:
                    return_post=posts[post]
                    del return_post['key']
                    filtered_posts.append(return_post)               
        
        if len(filtered_posts)==0:
            return "No posts are created in the given timeframe"
        else:
            return jsonify(filtered_posts)

# Extension 4 - User-based range queries
@app.route('/posts/user/<string:username>', methods=['GET'])
def get_posts_by_user(username):
    with lock:
        # Filter posts based on user
        username_list=list(users.values())
        username_list_names=[x['username'] for x in username_list]
        if not isinstance(username, str):
            return jsonify({'err': 'username should be in string format'}), 400
        if username not in username_list_names:
            return jsonify({'err': 'No username found: ' + username + ' Please enter correct username'}), 400
        filtered_posts = []
        for post in posts.values():
            if list(post.keys()).__contains__("username"):
                if post['username'] == username:
                    return_post=post
                    del return_post['key']
                    filtered_posts.append(return_post)  
        
        # Return filtered posts as JSON
        return jsonify(filtered_posts)

# Extension 5 - Fulltext search
@app.route('/posts/search', methods=['GET'])
def search_posts():
    with lock:
        
        # check if request body is a valid JSON object
        if not request.is_json:
            return jsonify({'err': 'Request body must be a valid JSON object.'}), 400
        
        # Get search from request json
        query = request.json.get('query')
        
        if not query or isinstance(query,int):
            return jsonify({'err': 'Missing query field or query is not a string. Please correct it!'}), 400
        
        # Search posts based on fulltext search
        matched_posts = []
        for post in posts:
            if re.search(query, posts[post]['msg'], re.IGNORECASE):
                return_post=posts[post]
                del return_post['key']
                matched_posts.append(return_post)  
        
        if len(matched_posts)==0:
            return "No Matched posts with the query"
        else:
        # Return matched posts as JSON
            return jsonify(matched_posts)
