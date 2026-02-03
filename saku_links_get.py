import requests
from bs4 import BeautifulSoup
import json


def read_write(gharad,file,info=None):

    if gharad == "write" :

        with open(file , "a") as f :
            f.write(json.dumps(info) + "\n")

    elif gharad == "read" :

        with open(file , "r") as f :

            for line in f :

                data = json.loads(line.strip())

                print(data)





def parse(rep):

    file = "info.jsonl"

    hit = 0

    soup = BeautifulSoup(rep.text,"xml")

    posts = soup.find_all("post")

    for post in posts :

        url = post.get("file_url")

        score = post.get("score") ; score = int(score)

        size = post.get("file_size") ; size = int(size)

        tag = post.get("tags")

        image = post.get("preview_url")

        if score > 300 and size > 5000000 and ".mp4" in url:

            hit +=1

            video = {"link" : url , "score" : score ,} 

            with open(file , "a") as f :

                f.write(json.dumps(video) + "\n")

    print(f"{hit} good videos")




def main() :



    for page in range(1,1764) :

        base_url = f"https://www.sakugabooru.com/post.xml?page={page}&limit=100"

        rep = requests.get(base_url)

        liest = parse(rep)

        print(base_url)



if __name__ == "__main__":
    main()