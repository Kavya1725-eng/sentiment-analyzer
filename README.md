# 🧠 Sentiment Analyzer

Hey there!Welcome to my Sentiment Analyzer project. 

I built this web app to dive deeper into Natural Language Processing (NLP) and see how machines understand human emotion. You can type in any text, and the app will tell you whether the emotional tone is Positive, Negative, or Neutral in real-time. 



##  What it does

- **Real-Time Feedback:** No need to hit a submit button. Just start typing, and the app analyzes your text on the fly. I used a JavaScript "debounce" trick so it doesn't overload the server while you type.
- **Mood Ring Background:** I had some fun with the UI! The background shapes and colors actually react to what you're typing. If you type something happy, the background turns a soft green. Type something angry, and it shifts to red.
- **Smooth Animations:** The polarity and subjectivity scores count up and down smoothly instead of just snapping to the new numbers. 
- **API Ready:** I built a `/analyze` endpoint, so if I ever want to connect this to another app, the backend is ready to go.

##  How I built it

| Part | What I used |
|------|-------------|
| **Backend** | Python 3 and Flask |
| **The "Brain"** | TextBlob (for the NLP magic) |
| **Frontend** | HTML, CSS, JavaScript, and Bootstrap 5 |
| **Templating** | Jinja2 |
| **Design Vibe** | Glassmorphism, custom CSS animations |

##  How to run it locally

Want to try it out on your own machine? It's pretty easy to set up.

### You'll need:
- Python 3.8 or newer
- pip

### Setup steps:

```bash
# 1. Clone this repo
git clone https://github.com/YOUR_USERNAME/sentiment-analyzer.git
cd sentiment-analyzer

# 2. Set up a virtual environment so we don't mess with your global Python
python -m venv venv

# On Windows, turn it on like this:
venv\Scripts\activate
# On Mac/Linux, do this instead:
# source venv/bin/activate

# 3. Install the required libraries
pip install -r requirements.txt

# 4. Download the language data that TextBlob needs to understand words
python -m textblob.download_corpora

# 5. Start the server!
python app.py
```

Once it's running, just open up your browser and go to `http://127.0.0.1:5000`.

## 📡 Using the API

If you just want to hit the API, you can send a POST request to `/analyze`.

**Send this:**
```json
{
  "text": "I absolutely love this project!"
}
```

**Get this back:**
```json
{
  "label": "Positive",
  "polarity": 0.8,
  "subjectivity": 0.6,
  "emoji": "😊",
  "text": "I absolutely love this project!"
}
```

## 📚 What I learned from this

This was a really fun project, and I learned a ton of practical skills:
- How to extract sentiment (polarity) and opinionation (subjectivity) from raw text.
- How to build a modern, glass-style UI that doesn't just sit there, but actually reacts to user input.
- How to debounce JavaScript events so my server doesn't catch on fire when someone types really fast.
- How to structure a Flask project properly with Jinja2 templates.

## 🔮 What's next?

I'm not totally done with this yet. Here's what I want to add in the future:
- [ ] Swap out TextBlob for a HuggingFace transformer model to make the AI even smarter.
- [ ] Add a feature to upload a CSV file and analyze a bunch of texts at once.
- [ ] Host it live on the web using Render or Railway.







