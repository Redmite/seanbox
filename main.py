import interface
import keyboard

audioDevices = interface.getAudioDevices()
deviceNum = 0

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '_', '+', '[', ']', '\\', '{', '}', '|', ';', "'", ':', '"', ',', '.', '/', '<', '>', '?','space','backspace']
print(chars)

length = len(audioDevices)

for i in range(length):
    print(audioDevices[i].GetDescription())

def speak(word, audioDevice):
    interface.speak(word, audioDevice)

while True:
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_UP and event.name == 'f4':
        f4 = True
        word = ''
        print(event.name)
        while f4 == True:
            key = keyboard.read_event()
            if key.event_type == keyboard.KEY_DOWN and key.name in chars:
                if key.name == 'space':
                    word += ' '
                    print(key.name)
                    print(word)
                elif key.name == 'backspace':
                    word = word[:-1]
                    print(key.name)
                    print(word)
                else:
                    word += key.name
                    print(key.name)
                    print(word)
            elif key.event_type == keyboard.KEY_UP and key.name == 'f4' or key.name == 'enter':
                f4 = False
                print("end f4")
                interface.speak(word, audioDevices[deviceNum])
    if event.event_type == keyboard.KEY_UP and event.name == 'f6':
        word = ''
        print(event.name)
        word = input('Enter phrase: ')
        print("end f6")
        interface.speak(word, audioDevices[deviceNum])