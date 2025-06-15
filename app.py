from flask import Flask, request, jsonify, render_template
from transformers import pipeline

app = Flask(__name__)

# Load a small GPT-2 text-generation pipeline (downloads ~500 MB once)
generator = pipeline("text-generation", model="gpt2")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    # Generate a continuation of the user input
    outputs = generator(
        user_msg,
        max_length=len(user_msg.split()) + 20,
        num_return_sequences=1,
        do_sample=True,
        top_p=0.9
    )
    bot_msg = outputs[0]["generated_text"][len(user_msg):].strip()
    return jsonify({"reply": bot_msg})

if __name__ == "__main__":
    app.run(debug=True)
