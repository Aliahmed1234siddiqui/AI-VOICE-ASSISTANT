import webbrowser


#  this function for Open Websites
def open_website(command):
    """Open a website based on user input."""
    sites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "my mail":"https://mail.google.com/mail/u/0/#inbox",
        "my github":"https://github.com/Aliahmed1234siddiqui",
        "my portfolio":"https://ali-siddiqui-portfolio.web.app/",
    }
    for key, url in sites.items():
        if key in command:
            webbrowser.open(url)
            return f"Opening {key}..."
    return "Website not found."
