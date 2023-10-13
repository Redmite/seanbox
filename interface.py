import win32com.client as wincom

voiceService = wincom.Dispatch("SAPI.SpVoice")

voices = voiceService.GetVoices()
for i in range(voices.Count):
    print(voices.Item(i).GetDescription())

voiceService.Rate = 3

voiceService.Voice = voices.Item(1)

def speak(text, audioDevice):

    voiceService.AudioOutput = audioDevice

    voiceService.Speak(text)
def getAudioDevices():

    audioDevices = voiceService.GetAudioOutputs()

    return audioDevices