async function sendMessage() {
  const inputEl = document.getElementById("user-input");
  const text = inputEl.value;
  appendMessage("You", text);
  inputEl.value = "";
  
  const res = await fetch("/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({message: text})
  });
  const data = await res.json();
  appendMessage("Bot", data.reply);
}

function appendMessage(sender, text) {
  const msgEl = document.createElement("div");
  msgEl.classList.add("message");
  msgEl.innerHTML = `<strong>${sender}:</strong> ${text}`;
  document.getElementById("messages").appendChild(msgEl);
  msgEl.scrollIntoView();
}
