import requests
from bs4 import BeautifulSoup
import urllib3
import csv


def main():
    file1 = open('aqitems.txt', 'r')
    Lines = file1.readlines()
    count = 0
    name = ""
    items = []
    for line in Lines:
        name = line.strip()
        url = "https://classic.wowhead.com/search?" + \
            urllib3.request.urlencode({'q': name})
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        # f = open("output.txt", "a")
        # f.write(r.text)
        # f.close()
        image = soup.find("link",  rel="image_src")
        link = soup.find("meta",  property="og:url")
        if image:
            image = image.attrs["href"]
        if not image:
            image = soup.find("meta",  property="og:image")
            image = image.attrs["content"]
        items.append({
            # 'image': imagealt.attrs["content"],
            'image': image,
            'link': link.attrs["content"],
            'name': name
        })
        print("Done "+name)

    with open('output.csv', 'w', newline='') as csvfile:
        fieldnames = ['image', 'link', 'name']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for data in items:
            writer.writerow(data)


if __name__ == "__main__":
    main()
