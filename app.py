from flask import Flask, request, render_template
from textblob import TextBlob
import nltk

nltk.download('punkt')
nltk.download('stopwords')

app = Flask(__name__)

# Expanded list of biased, offensive, and harmful words
bias_keywords = [
    "idiot", "moron", "dumb", "stupid", "loser", "freak", "trash", "worthless", "disgusting", "useless",
    "b*tch", "sl*t", "wh*re", "gold-digger", "homewrecker", "nagging", "hysterical", "stay in the kitchen",
    "fat", "whale", "skeleton", "anorexic", "obese",
    "cripple", "ret**d", "special case", "psycho", "loony",
    "burn in hell", "your religion is fake", "infidel", "god hates you", "blasphemer",
    "nice rack", "bend over", "send nudes", "you’d look better without clothes", "sit on my lap",
    "kill yourself", "you should die", "go jump off a bridge", "hope you get hurt", "someone should end you",
    "no one likes you", "you have no friends", "you’ll die alone", "go rot", "ugly af",
    "brain-dead", "no iq", "window-licker", "dumber than a rock", "caveman",
    "boomer", "fossil", "old hag", "wrinkly", "grandpa", "grandma",
    "simp", "beta male", "virgin", "cuck", "weakling",
    "bossy", "drama queen", "emotional", "overly sensitive", "cat lady",
    "go back to your country", "you don’t belong here", "immigrant scum", "foreign trash", "speak english",
    "snowflake", "soy boy", "karen", "chad", "npc",
    "stfu", "gtfo", "lmfao", "fml", "wtf",
    "f**k", "sh*t", "a**hole", "d**k", "b**tard",
    "i want to die", "life is pointless", "no one cares about me", "i hate myself", "i should just disappear"
]

def detect_bias(text):
    blob = TextBlob(text.lower())
    for word in bias_keywords:
        if word in blob.words:
            return f"⚠️ Bias Detected: The text contains harmful or offensive words like '{word}'."
    return "✅ No Bias Detected: The text appears neutral."

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        user_input = request.form["text"]
        result = detect_bias(user_input)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)