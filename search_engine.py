import webbrowser
website = input("Search website: ")

if website == "google":
    google = input("search: ")
    webbrowser.open("https://www.google.com/search?q=" + google)