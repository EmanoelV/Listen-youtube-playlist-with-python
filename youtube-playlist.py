import pafy
import vlc
from time import sleep
import keyboard
from colored import attr, fg
cyan = fg('cyan')
red = fg('red')
res = attr('reset')

url = "PUT_YOUR_YOUTUBE_PLAYLIST_URL_HERE"
playlist = pafy.get_playlist(url) # Extracts playlist information

for music in playlist['items']:
    url_video = "https://www.youtube.com/watch?v=" + music['playlist_meta']['encrypted_id'] # Extrai o link de cada vídeo da playlist
    video = pafy.new(url_video)
    audio = video.getbestaudio() # Extracts only the audio from the videos
    playurl = audio.url

    print(music['playlist_meta']['title'] + f' - {red}' + music['playlist_meta']['duration'] + f'{res}')

    # Below is the standard media reproduction of the python-vlc library
    Instance = vlc.Instance()
    player = Instance.media_player_new()
    Media = Instance.media_new(playurl)
    Media.get_mrl()
    player.set_media(Media)
    player.play()
    sleep(3)
    while player.is_playing():
        key = keyboard.read_key() # Detects the pressed key
        if key == 'page up':
            print(f'{cyan}-next{res}')
            break
    player.stop()
