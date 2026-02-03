import subprocess
import sys
import time
import json
import random


def play():
    global mpv

    width = 854
    height =480
    

    mpv = subprocess.Popen(
        ["mpv","--title=SakugaClip","--prefetch-playlist=yes" ,f"--geometry={width}x{height}", f"--playlist={playlist}"],
        stdout=subprocess.DEVNULL,  
        stderr=subprocess.DEVNULL 
        )



def main():
    global playlist

    file = "info.jsonl"

    playlist = "playlist.txt"

    data = []

    size = 250

    with open(file , "r") as f :

        for line in f :

            data.append(json.loads(line.strip()))

    with open(playlist,"w") as f :

        samples = random.sample(data,size)
        

        for sample in samples :

            link = sample["link"]

            f.write(link + "\n")

    play()


if __name__ == "__main__":
    try :
        main()
    except :
        mpv.terminate()

