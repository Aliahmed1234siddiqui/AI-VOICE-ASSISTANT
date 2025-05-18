import wikipedia

# ✅ Function 4: Wikipedia Search
def search_wikipedia(command):
    """Search Wikipedia for a topic."""
    topic = command.replace("wikipedia", "").strip()
    try:
        summary = wikipedia.summary(topic, sentences=2)
        return summary
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find any information on that."
