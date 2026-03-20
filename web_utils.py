import webbrowser

def open_google(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return "Opened Google search for more information."