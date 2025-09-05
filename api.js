//Pequena tela de login


function login() {
    const username = document.getElementById('username').value;

    if (username) {
        localStorage.setItem('username', username);
        document.getElementById('loginContainer').style.display = 'none';
        document.getElementById('chatContainer').style.display = 'block';
        document.getElementById('welcomeMessage').innerText = `Welcome, ${username}!`;
        loadMessages();
        connectWebSocket();
        fetchOnlineUsers();
        setInterval(fetchOnlineUsers, 5000); // Atualiza a lista de usuários online a cada 5 segundos
    } else {
        alert('Please enter a username.');
    }
}

//Tela de chat
function sendMessage() {
    const messageInput = document.getElementById('messageInput');
    const message = messageInput.value.trim();
    const username = localStorage.getItem('username');
    if (message && username) {
        const msgData = { username, message };
        socket.send(JSON.stringify(msgData));
        messageInput.value = '';
        appendMessage(msgData);
        saveMessage(msgData);
        fetchOnlineUsers(); // Atualiza a lista de usuários online após enviar uma mensagem
    }
}

function appendMessage({ username, message }) {
    const messagesDiv = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${username}:</strong> ${message}`;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function loadMessages() {
    fetch('/api/messages')
        .then(response => response.json())
        .then(data => {
            data.forEach(appendMessage);
        }
        )
        .catch(error => console.error('Error loading messages:', error));
}

function saveMessage(msgData) {
    fetch('/api/messages', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(msgData)
    }).catch(error => console.error('Error saving message:', error));
}

let socket;
function connectWebSocket() {
    socket = new WebSocket(`ws://${window.location.host}`);
    socket.onmessage = function (event) {
        const msgData = JSON.parse(event.data);
        appendMessage(msgData);
        saveMessage(msgData);
        fetchOnlineUsers(); // Atualiza a lista de usuários online ao receber uma mensagem
    };
    socket.onclose = function () {
        console.log('WebSocket closed, reconnecting...');
        setTimeout(connectWebSocket, 1000);
    };
    socket.onerror = function (error) {
        console.error('WebSocket error:', error);
        socket.close();
    };
}

function fetchOnlineUsers() {
    fetch('/api/online-users')
        .then(response => response.json())
        .then(data => {
            const onlineUsersDiv = document.getElementById('onlineUsers');
            onlineUsersDiv.innerHTML = '<strong>Online Users:</strong><br>' + data.join('<br>');
        })
        .catch(error => console.error('Error fetching online users:', error));
}
document.getElementById('loginButton').addEventListener('click', login);
document.getElementById('sendButton').addEventListener('click', sendMessage);
document.getElementById('messageInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

window.onload = function () {
    if (localStorage.getItem('username')) {
        login();
    }
};
//Configurações do vscode
