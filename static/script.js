const chat = document.getElementById("chat");
const input = document.getElementById("question-input");
const sendButton = document.getElementById("send-button");
const clearButton = document.getElementById("clear-chat");

const suggestionButtons = document.querySelectorAll(
    ".suggestion-button"
);


function scrollToBottom() {
    chat.scrollTop = chat.scrollHeight;
}


function createUserMessage(question) {
    const message = document.createElement("div");

    message.className = "message user-message";

    message.innerHTML = `
        <div class="avatar">YOU</div>

        <div class="message-content">
            <strong>You</strong>
            <p></p>
        </div>
    `;

    message.querySelector("p").textContent = question;

    chat.appendChild(message);
    scrollToBottom();
}


function createLoadingMessage() {
    const message = document.createElement("div");

    message.className = "message assistant-message";
    message.id = "loading-message";

    message.innerHTML = `
        <div class="avatar">RM</div>

        <div class="message-content">
            <strong>Real Madrid AI</strong>

            <div class="typing">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;

    chat.appendChild(message);
    scrollToBottom();
}


function removeLoadingMessage() {
    const loadingMessage = document.getElementById(
        "loading-message"
    );

    if (loadingMessage) {
        loadingMessage.remove();
    }
}


function createAssistantMessage(answer, sources = []) {
    const message = document.createElement("div");

    message.className = "message assistant-message";

    const sourcesHtml = sources.length
        ? `
            <details class="sources">
                <summary>
                    View knowledge-base sources
                </summary>

                ${sources.map(source => `
                    <div class="source-item">
                        <strong>
                            Source ${source.number}
                        </strong>

                        <div>
                            ${escapeHtml(source.content)}
                        </div>
                    </div>
                `).join("")}
            </details>
        `
        : "";

    message.innerHTML = `
        <div class="avatar">RM</div>

        <div class="message-content">
            <strong>Real Madrid AI</strong>

            <p>${escapeHtml(answer)}</p>

            ${sourcesHtml}
        </div>
    `;

    chat.appendChild(message);
    scrollToBottom();
}


function createErrorMessage(error) {
    createAssistantMessage(
        `An error occurred: ${error}`
    );
}


function escapeHtml(text) {
    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}


async function sendQuestion(customQuestion = null) {
    const question = (
        customQuestion || input.value
    ).trim();

    if (!question) {
        return;
    }

    createUserMessage(question);

    input.value = "";
    sendButton.disabled = true;

    createLoadingMessage();

    try {
        const response = await fetch("/ask", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                question: question
            })
        });

        const data = await response.json();

        removeLoadingMessage();

        if (!response.ok) {
            throw new Error(
                data.error || "Unknown server error"
            );
        }

        createAssistantMessage(
            data.answer,
            data.sources
        );

    } catch (error) {
        removeLoadingMessage();
        createErrorMessage(error.message);

    } finally {
        sendButton.disabled = false;
        input.focus();
    }
}


sendButton.addEventListener("click", () => {
    sendQuestion();
});


input.addEventListener("keydown", event => {
    if (
        event.key === "Enter" &&
        !event.shiftKey
    ) {
        event.preventDefault();
        sendQuestion();
    }
});


suggestionButtons.forEach(button => {
    button.addEventListener("click", () => {
        const question = button.dataset.question;

        sendQuestion(question);
    });
});


clearButton.addEventListener("click", () => {
    chat.innerHTML = `
        <div class="message assistant-message">
            <div class="avatar">RM</div>

            <div class="message-content">
                <strong>Real Madrid AI</strong>

                <p>
                    Conversation cleared. Ask me anything
                    about Real Madrid.
                </p>
            </div>
        </div>
    `;
});