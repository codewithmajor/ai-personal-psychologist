async function sendMessage() {
    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    const userText = input.value.trim();
    if (userText === "") return;

    const userDiv = document.createElement("div");
    userDiv.className = "user";
    userDiv.innerText = userText;
    chatBox.appendChild(userDiv);
    input.value = "";

    const response = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText })
    });

    const data = await response.json();

    const botDiv = document.createElement("div");
    botDiv.className = "bot";
    botDiv.innerText = data.reply;
    chatBox.appendChild(botDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}
