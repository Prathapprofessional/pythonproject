document.addEventListener('DOMContentLoaded', function() {
    const todosList = document.getElementById('todos');
    const todoInput = document.getElementById('todo-input');
    const addButton = document.getElementById('add-button');

    // Function to fetch todos from the backend
    function fetchTodos() {
        fetch('https://your-flask-app-url/todos')
            .then(response => response.json())
            .then(data => {
                todosList.innerHTML = '';
                data.forEach(todo => {
                    const li = document.createElement('li');
                    li.textContent = todo.task;
                    todosList.appendChild(li);
                });
            })
            .catch(error => console.error('Error fetching todos:', error));
    }

    // Function to add a new todo
    function addTodo() {
        const newTodo = todoInput.value;
        if (newTodo.trim() === '') {
            alert('Please enter a todo.');
            return;
        }
        fetch('http://localhost:5000/todos', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ todo: newTodo })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Todo added:', data);
            fetchTodos(); // Refresh the todo list
            todoInput.value = ''; // Clear the input field
        })
        .catch(error => console.error('Error adding todo:', error));
    }

    // Event listeners
    addButton.addEventListener('click', addTodo);

    // Initial fetch of todos
    fetchTodos();
});
