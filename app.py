from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for to-do items
todos = [
    {"id": 1, "task": "Learn Flask", "done": False},
    {"id": 2, "task": "Build a CI/CD pipeline", "done": False}
]

@app.route('/')
def home():
    return "Welcome to the To-Do List App!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    new_todo = request.json
    new_todo["id"] = len(todos) + 1
    todos.append(new_todo)
    return jsonify(new_todo), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo["id"] != todo_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
