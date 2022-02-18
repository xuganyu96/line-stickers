import requests
from apnggif import apnggif
from linestickers.htmlparse import LineStickerParser

def fetch_to_file(path, url):
    """Given url, write the resposne to the path"""
    r = requests.get(url)
    with open(path, "wb") as f:
        f.write(r.content)


if __name__ == "__main__":
    r = requests.get("https://store.line.me/stickershop/product/18307594/en")
    parser = LineStickerParser()

    parser.feed(r.text)

    for sticker_id, url in parser.sticker_urls.items():
        path = f"./{sticker_id}.png"
        fetch_to_file(path, url)
        apnggif(path)

