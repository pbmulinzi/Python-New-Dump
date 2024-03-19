#Car Game
Command = ""
while True:
    Command = input('>').lower()
    if Command == 'start':
        print('Car started...Ready to go!')
    elif Command == 'stop':
        print('Car Stopped.')
    elif Command == "help":
        print("""
Start - Car started.
Stop - Car Stopped.
Quit - quit game.
              """)
    elif Command == "quit":
        break
    else:
        print("I don't understand that...")
        break
else:
    print("")
