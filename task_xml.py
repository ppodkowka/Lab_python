import xml.sax
import xml.etree.ElementTree as ET


class SongHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.artist = ""
        self.year = ""
        self.album = ""


    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "song":
            print("Song:")
            title = attributes["title"]
            print("Title:", title)

     # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "artist":
             print("Artist:", self.artist)
        elif self.CurrentData == "year":
             print("Year:", self.year)
        elif self.CurrentData == "album":
             print("Album:", self.album)
        self.CurrentData = ""

    def Characters(self, content):
        if self.CurrentData == "artist":
            self.artist = content
        elif self.CurrentData == "year":
            self.year = content
        elif self.CurrentData == "album":
            self.album = content


if __name__ == '__main__':
    parser = xml.sax.make_parser()  # creating an XMLReader
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)  # turning off namespaces
    Handler = SongHandler()
    parser.setContentHandler(Handler)  # overriding default ContextHandler
    parser.parse(r"C:\Users\ppodk\OneDrive\Pulpit\programowanie\Lab_Python\iksemel")

    mytree = ET.parse(r"C:\Users\ppodk\OneDrive\Pulpit\programowanie\Lab_Python\iksemel")
    myroot = mytree.getroot()

    print(myroot)

    for artists in myroot.iter("artist"):
        artists.text = "some artist"
    mytree.write('output.xml')
