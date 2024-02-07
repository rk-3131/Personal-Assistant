import webbrowser

# Path to Brave executable
brave_path = 'C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe'  # Example path, adjust as necessary
# C:\Program Files\BraveSoftware\Brave-Browser\Application
# Register Brave browser with the webbrowser module
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))

# Open a URL in the Brave browser
webbrowser.get('brave').open('https://www.google.com')