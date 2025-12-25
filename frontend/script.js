function sendMessage() {
    const input = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");

    const userText = input.value.trim();
    if (userText === "") return;

    // Show user message
    const userDiv = document.createElement("div");
    userDiv.className = "user";
    userDiv.innerText = userText;
    chatBox.appendChild(userDiv);

    input.value = "";

    // Safety check
    if (userText.toLowerCase().includes("suicide") ||
        userText.toLowerCase().includes("kill myself")) {

        const alertDiv = document.createElement("div");
        alertDiv.className = "bot";
        alertDiv.innerText =
            "I’m really sorry you’re feeling this way. If you are in danger, please contact emergency services or a suicide helpline immediately.";
        chatBox.appendChild(alertDiv);
        return;
    }

    // Temporary AI response (dummy)
    const botDiv = document.createElement("div");
    botDiv.className = "bot";
    botDiv.innerText =
        "Thank you for sharing. Would you like to try a short breathing exercise?";
    chatBox.appendChild(botDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}
