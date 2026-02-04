import requests
from bs4 import BeautifulSoup
import json

file = "info.jsonl"

# Returns a list of the links that are in the file
def available_links():

    ava_links = []

    with open (file , "r") as f :

        for line in f :

            data = json.loads(line.strip())

            ava_links.append(data["link"])


    return ava_links

# Parses the xml response and writes the best links based on popularity 
def parse(rep):

    ava_links = available_links()

    hit = 0

    soup = BeautifulSoup(rep.text,"xml")

    posts = soup.find_all("post")

    for post in posts :

        url = post.get("file_url")

        score = post.get("score") ; score = int(score)

        size = post.get("file_size") ; size = int(size)

        tag = post.get("tags")

        image = post.get("preview_url")

        if score > 300 and size > 5000000 and ".mp4" in url and url not in ava_links  :

            hit +=1

            video = {"link" : url , "score" : score ,} 

            with open(file , "a") as f :

                f.write(json.dumps(video) + "\n")

    print(f"{hit} good videos")

# You could run it to add only new links to the file
def main() :

    for page in range(1,1764) :

        base_url = f"https://www.sakugabooru.com/post.xml?page={page}&limit=100"

        rep = requests.get(base_url)

        liest = parse(rep)

        print(base_url)


if __name__ == "__main__":
    main()