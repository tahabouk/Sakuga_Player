import subprocess
import sys
import time
import json
import random

file = "info.jsonl"

playlist = "playlist.txt"

playlist_size = 250 


def play(playlist):

    width = 854
    height =480
    

    mpv = subprocess.Popen(
        ["mpv","--title=SakugaClip","--prefetch-playlist=yes" ,f"--geometry={width}x{height}", f"--playlist={playlist}"],
        stdout=subprocess.DEVNULL,  
        stderr=subprocess.DEVNULL 
        )



def main():

    data = []

    with open(file , "r") as f :

        for line in f :

            data.append(json.loads(line.strip()))

    with open(playlist,"w") as f :

        samples = random.sample(data,playlist_size)
        

        for sample in samples :

            link = sample["link"]

            f.write(link + "\n")

    play(playlist)


if __name__ == "__main__":
    main()

