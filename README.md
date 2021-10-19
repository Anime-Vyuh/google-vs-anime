## Google Voice Machine vs Anime Voice Actors

### Requirements
- `gTTS` : Google Text to Speech
- `playsound` : To Play the sound, that is saved by gTTS
- `Tkinter` : To Create GUI Application
- `Pygame` : To Play the Dialouges

### Example to convert  Voice into Japanese

```
from gtts import gTTS

dialog = "Baka"
#voice in Japanese Janguage
voice=gTTS(text=dialog, lang='ja',slow=False)
voice.save('{}.mp3'.format(dialog))

```
### Play Characters Dialouge Using Pygame

```
pygame.mixer.init()
pygame.mixer.music.load('song path')
pygame.mixer.music.play(loops=1)
```

[Check the Article](https://animevyuh.org/google-vs-anime-voice)
