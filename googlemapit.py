import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    address = "https://www.google.com/maps/search/" + ('+'.join(sys.argv[1:]))
    print(address)
    print(sys.argv[0])
    webbrowser.open(address)
else:
    address = "https://www.google.com/maps/search/" + pyperclip.paste()
    webbrowser.open(address)