import youtube_dl as yt
import time as t
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def downloadVideo(result, url, ydl):
    print(f'''Video found! Title: {result['title']}
Would you like to download this video as an MP3? [Y/N]''')
    downloadConfirm = input().upper()
    while downloadConfirm not in ["Y", "N"]:
        downloadConfirm = input("Unknown option, please type Y or N and press ENTER.").upper()
    if downloadConfirm == "Y":
        print("Starting download!")
        ydl.download([url])
        print("Video downloaded!")

def downloadPlaylist(result, url, ydl):
    print(f'''Playlist found! Title: {result['entries'][0]['playlist_title']}
Would you like to download this playlist as an MP3? [Y/N]''')
    downloadConfirm = input().upper()
    while downloadConfirm not in ["Y", "N"]:
        downloadConfirm = input("Unknown option, please type Y or N and press ENTER.").upper()
    if downloadConfirm == "Y":
        print("Starting download!")
        ydl.download([url])
        print("Playlist downloaded!")

def download(url):
    ydl = yt.YoutubeDL({'outtmpl' : '/downloads/%(title)s.mp3'})
    with ydl:
        result = ydl.extract_info(url,
                                  download=False)
        clear()
        if 'entries' in result:
            downloadPlaylist(result, url, ydl)
        else:
            downloadVideo(result, url, ydl)

def intro():
    print(r''' __   __  _______  __   __  _______  _______  __   __  _______  _______ 
|  | |  ||       ||  | |  ||       ||       ||  |_|  ||       ||       |
|  |_|  ||   _   ||  | |  ||_     _||   _   ||       ||    _  ||___    |
|       ||  | |  ||  |_|  |  |   |  |  | |  ||       ||   |_| | ___|   |    ___  __ __
|_     _||  |_|  ||       |  |   |  |  |_|  ||       ||    ___||___    | _ / - \/ // /
  |   |  |       ||       |  |   |  |       || ||_|| ||   |     ___|   |(_) .__/\_, /   _________________
  |___|  |_______||_______|  |___|  |_______||_|   |_||___|    |_______| /_/   /___/   /github.com/buxx0/ ''')
    t.sleep(3)

def main():
    done = False
    while not done:
        intro()
        clear()
        url_input = input("Please paste the URL of the video/playlist you'd like to download as an MP3:\n")
        download(url_input)
        download_again = input("Would you like to download another playlist/video? [Y/N]\n").upper()
        while download_again not in ["Y", "N"]:
            download_again = input("Unknown option, please type Y or N and press ENTER.").upper()
        if download_again == "N":
            clear()
            print("Thank you for using YouToMp3!\nClosing in 3 seconds...")
            done = True
            t.sleep(3)

main()