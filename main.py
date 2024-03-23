from os import link
from pytube import YouTube

global moin  

def main():
    global yt
    print("Bitte gib den Link ein :)")
    link = str(input())
    yt=YouTube(link)
    del link
    print("Bitte wähle zwischen Musik und Video!")
    global mode
    mode = str(input())

def Download_Music():
    stream = yt.streams.get_by_itag(251).download()

def Download_Video():     
    stream = yt.streams.get_by_itag(137).download()

def Restart():
    print("Möchtest du noch einmal etwas herunterladen?Ja/Nein")
    neustart = str(input())
    if neustart == "Ja":
        main()
        download()
    else:
        print("Ich wünsche einen angenehmen Tag :)")

def download():
    if mode == "Video":
        Download_Video()
        print("Download abgeschlossen")
        Restart()    
    elif mode == "Musik":
        Download_Music()
        print("Download abgeschlossen")
        Restart()
    else:
        print("Du kannst nur zwischen video und musik auswählen")
        Restart()

main()
download()
