// frontend/app.js
// Handles sending messages to the FastAPI backend and rendering chat messages on the page.

// Adjust this to match where your backend is running.
const BACKEND_URL = "http://127.0.0.1:8000/chat";

const chatWindow = document.getElementById("chat-window");
const chatForm = document.getElementById("chat-form");
const userInput = document.getElementById("user-input");

/**
 * Append a message bubble to the chat window.
 * role: "user" | "bot" | "meta"
 */
function addMessage(text, role = "bot") {
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("message", role);
    messageDiv.textContent = text;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

/**
 * Show a temporary "typing" indicator from the bot.
 */
function showTypingIndicator() {
    const indicator = document.createElement("div");
    indicator.classList.add("message", "meta");
    indicator.id = "typing-indicator";
    indicator.textContent = "AI is thinking...";
    chatWindow.appendChild(indicator);
    chatWindow.scrollTop = chatWindow.scrollHeight;
}

/**
 * Remove the typing indicator if it exists.
 */
function removeTypingIndicator() {
    const indicator = document.getElementById("typing-indicator");
    if (indicator) {
        indicator.remove();
    }
}

/**
 * Handle form submission: send user message to backend and display response.
 */
chatForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const message = userInput.value.trim();
    if (!message) return;

    // Show user message
    addMessage(message, "user");

    // Clear input and disable send button temporarily
    userInput.value = "";
    userInput.disabled = true;
    chatForm.querySelector(".send-button").disabled = true;

    // Show typing indicator
    showTypingIndicator();

    try {
        const response = await fetch(BACKEND_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message }),
        });

        if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        removeTypingIndicator();

        // Add bot response
        addMessage(data.reply, "bot");

        // If crisis was detected, emphasize this in the UI
        if (data.is_crisis) {
            addMessage(
                "If you are in immediate danger, please contact your local emergency number or a crisis helpline right now.",
                "meta"
            );
        }
    } catch (error) {
        removeTypingIndicator();
        addMessage("Sorry, something went wrong while connecting to the server. Make sure the backend is running!", "meta");
        console.error(error);
    } finally {
        userInput.disabled = false;
        chatForm.querySelector(".send-button").disabled = false;
        userInput.focus();
    }
});
