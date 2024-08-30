# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     app.run(debug=True)

# from flask import Flask, jsonify, request, send_from_directory
# from flask_swagger_ui import get_swaggerui_blueprint
# import os

# app = Flask(__name__)

# # Initialize in-memory database (list of to-do items)
# todos = []

# # Swagger UI setup
# SWAGGER_URL = '/swagger'
# API_URL = '/static/swagger.json'
# swagger_ui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,
#     API_URL,
#     config={'app_name': "Flask Todo API"}
# )
# app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# # Serve the Swagger JSON file
# @app.route('/static/swagger.json')
# def swagger_json():
#     file_path = os.path.join('static', 'swagger.json')
#     if not os.path.isfile(file_path):
#         return jsonify({'error': 'Swagger JSON file not found', 'file_path': file_path}), 404
#     return send_from_directory('static', 'swagger.json')

# # Route to get all to-do items
# @app.route('/todos', methods=['GET'])
# def get_todos():
#     return jsonify(todos)

# # Route to add a new to-do item
# @app.route('/todos', methods=['POST'])
# def add_todo():
#     if not request.json or 'todo' not in request.json:
#         return jsonify({'error': 'Bad request', 'message': 'Missing "todo" field'}), 400

#     todo = request.json['todo']
#     if not isinstance(todo, str) or not todo.strip():
#         return jsonify({'error': 'Bad request', 'message': '"todo" must be a non-empty string'}), 400

#     new_todo = {'id': len(todos) + 1, 'task': todo}
#     todos.append(new_todo)
#     return jsonify({'message': 'Todo added!', 'todo': new_todo}), 201

# # Route to update a to-do item by ID
# @app.route('/todos/<int:todo_id>', methods=['PUT'])
# def update_todo(todo_id):
#     todo = next((item for item in todos if item['id'] == todo_id), None)
#     if not todo:
#         return jsonify({'error': 'Not Found', 'message': 'Todo not found'}), 404

#     if not request.json or 'task' not in request.json:
#         return jsonify({'error': 'Bad request', 'message': 'Missing "task" field'}), 400

#     task = request.json['task']
#     if not isinstance(task, str) or not task.strip():
#         return jsonify({'error': 'Bad request', 'message': '"task" must be a non-empty string'}), 400

#     todo['task'] = task
#     return jsonify({'message': 'Todo updated!', 'todo': todo})

# # Route to delete a to-do item by ID
# @app.route('/todos/<int:todo_id>', methods=['DELETE'])
# def delete_todo(todo_id):
#     global todos
#     todo = next((item for item in todos if item['id'] == todo_id), None)
#     if not todo:
#         return jsonify({'error': 'Not Found', 'message': 'Todo not found'}), 404

#     todos = [item for item in todos if item['id'] != todo_id]
#     return jsonify({'message': 'Todo deleted!'})

# # if __name__ == '__main__':
# #     app.run(debug=True)

# if __name__ == '__main__':
#     app.run()


from flask import Flask, jsonify, request, send_from_directory, render_template
from flask_swagger_ui import get_swaggerui_blueprint
from flask_frozen import Freezer
import os

app = Flask(__name__)

# Initialize in-memory database (list of to-do items)
todos = []

# Swagger UI setup
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={'app_name': "Flask Todo API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Serve the Swagger JSON file
@app.route('/static/swagger.json')
def swagger_json():
    file_path = os.path.join('static', 'swagger.json')
    if not os.path.isfile(file_path):
        return jsonify({'error': 'Swagger JSON file not found', 'file_path': file_path}), 404
    return send_from_directory('static', 'swagger.json')

# Route to get all to-do items
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# Route to add a new to-do item
@app.route('/todos', methods=['POST'])
def add_todo():
    if not request.json or 'todo' not in request.json:
        return jsonify({'error': 'Bad request', 'message': 'Missing "todo" field'}), 400

    todo = request.json['todo']
    if not isinstance(todo, str) or not todo.strip():
        return jsonify({'error': 'Bad request', 'message': '"todo" must be a non-empty string'}), 400

    new_todo = {'id': len(todos) + 1, 'task': todo}
    todos.append(new_todo)
    return jsonify({'message': 'Todo added!', 'todo': new_todo}), 201

# Route to update a to-do item by ID
@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Not Found', 'message': 'Todo not found'}), 404

    if not request.json or 'task' not in request.json:
        return jsonify({'error': 'Bad request', 'message': 'Missing "task" field'}), 400

    task = request.json['task']
    if not isinstance(task, str) or not task.strip():
        return jsonify({'error': 'Bad request', 'message': '"task" must be a non-empty string'}), 400

    todo['task'] = task
    return jsonify({'message': 'Todo updated!', 'todo': todo})

# Route to delete a to-do item by ID
@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todo = next((item for item in todos if item['id'] == todo_id), None)
    if not todo:
        return jsonify({'error': 'Not Found', 'message': 'Todo not found'}), 404

    todos = [item for item in todos if item['id'] != todo_id]
    return jsonify({'message': 'Todo deleted!'})

# Frozen-Flask setup
freezer = Freezer(app)

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    freezer.freeze()
    app.run(debug=True)

