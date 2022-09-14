from datetime import datetime

from flask import Flask, request, render_template

import json

app = Flask(__name__)


def load_chat():
    with open("chat.json", "r") as json_file:
        data = json.load(json_file)
        return data["messages"]


all_messages = load_chat()


def save_chat():
    data = {"messages": all_messages}
    with open("chat.json", "w") as json_file:
        json.dump(data, json_file)


@app.route("/chat")
def display_chat():
    return render_template("form.html")


@app.route("/")
def index_page():
    return "Welcome to our <b>Messenger</b>"


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@app.route("/send_message")
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    save_chat()
    return "Ok"


def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M"),
    }
    all_messages.append(new_message)


app.run(host="0.0.0.0", port=80)
