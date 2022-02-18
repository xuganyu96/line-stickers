from html.parser import HTMLParser
import json


class LineStickerParser(HTMLParser):
    sticker_urls = {}  # maps ID to URL

    @staticmethod
    def get_animation_url(attr):
        """Given a list of attributes such as the input to handle_starttag's
        attrs, return a dictionary that maps data-preview.id to
        data-preview.id.animationUrl. If "data-preview" is not present, return
        an empty dictionary
        """
        for attr in attr:
            if attr[0] == "data-preview":
                data_preview = json.loads(attr[1])
                return {data_preview["id"]: data_preview["animationUrl"]}
        return {}

    def handle_starttag(self, tag, attrs):
        if tag == "li":
            self.sticker_urls.update(self.get_animation_url(attrs))
            

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

