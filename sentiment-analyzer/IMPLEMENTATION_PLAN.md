# How I Built the Sentiment Analyzer (My Process)

When I decided to build this Sentiment Analyzer, I didn't want to just copy-paste code. I wanted to treat it like a real, professional project. 

To keep myself organized, I broke the work down into five main phases. Here is the exact roadmap I followed to take this from an idea to a fully functioning, dynamic web app.

## Phase 1: Getting the Core AI Working
*My first goal was to just get Python to understand text sentiment.*

- [x] **Set up my workspace:** Created a clean virtual environment and a `requirements.txt` file so the project is easy to share.
- [x] **Picked my tools:** Decided on `TextBlob` for the heavy lifting since it's great for getting started with NLP, and `Flask` to eventually serve it to the web.
- [x] **Wrote the brain (`analyzer.py`):** 
  - I created a function that takes in a string of text and spits out a polarity score (is it positive or negative?) and a subjectivity score (is it a fact or an opinion?).
  - Wrote a quick script to test it out in my terminal to make sure the math actually made sense before I bothered building a website for it.

## Phase 2: Building the API
*Once the Python script worked, I needed a way for a website to talk to it.*

- [x] **Set up Flask (`app.py`):** Wrote the barebones server code.
- [x] **Created the endpoint:** Built a `POST /analyze` route. The idea is that the frontend will send a JSON package with text, and this route will return the sentiment data.
- [x] **Handled edge cases:** Added some error catching. If someone sends an empty string, the server politely tells them to actually type something instead of just crashing.

## Phase 3: The Frontend Basics
*Time to make it visible in the browser.*

- [x] **Set up Jinja2 (`templates/base.html`):** Instead of dumping all my HTML into one file, I created a master template. It holds all my `<head>` tags, my fonts (I went with 'Outfit'), and my Bootstrap CDN links. 
- [x] **Built the UI (`templates/index.html`):** Created the text box and a layout for the results using Bootstrap's grid system so it wouldn't look terrible on my phone.

## Phase 4: Making it Look Awesome (UI/UX)
*It worked, but it felt a bit boring. I wanted it to feel premium and alive.*

- [x] **Added Glassmorphism (`static/style.css`):** I gave the main card a frosted glass effect (`backdrop-filter: blur`) so it looks super modern.
- [x] **Real-Time Typing:** I hated having to click an "Analyze" button. I wrote some JavaScript to analyze the text *while* you type. I added a 500ms "debounce" so it only asks the server for the sentiment after you pause typing for half a second.
- [x] **Mood Ring Background:** This is my favorite part. I wrote a script that changes the background CSS variables based on the mood of the text. Positive text turns the background green, negative turns it red. 
- [x] **Smooth Number Counters:** Instead of the scores just snapping to new numbers instantly, I wrote an animation loop in JS so the numbers visibly count up and down.

## Phase 5: Wrapping it Up
*Making it ready for the world to see.*

- [x] **Wrote the Docs:** Put together a solid `README.md` explaining what the project is, how to run it, and what I learned.
- [x] **Documented the Process:** Wrote this very document to show my work!
- [ ] **Next steps:** Deploy it to the internet and maybe upgrade the AI model.
