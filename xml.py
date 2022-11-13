import xml.sax
import xml.etree.ElementTree as ET


class SongHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.artist = ""
        self.year = ""
        self.album = ""

    # Call when an element starts
    def startElement(self, tagName, attributes):
        self.CurrentData = tagName
        if tagName == 'song':
            print('---Song---')
            title = attributes['title']
            print('Title:', title)

     # Call when an elements ends
    def endElement(self, tagName):
        if tagName == 'artist':
             print('Artist:', self.artist)
        elif tagName == 'year':
             print('Year:', self.year)
        elif tagName == 'album':
             print('Album:', self.album)
        self.CurrentData = ''

    def characters(self, content):
        if self.CurrentData == 'artist':
            self.artist = content
        elif self.CurrentData == 'year':
            self.year = content
        elif self.CurrentData == 'album':
            self.album = content


if __name__ == '__main__':
    handler = SongHandler()
    xml.sax.parse(r"C:\Users\ppodk\OneDrive\Pulpit\programowanie\Lab_Python\example.xml",handler)

    mytree = ET.parse(r"C:\Users\ppodk\OneDrive\Pulpit\programowanie\Lab_Python\example.xml")
    myroot = mytree.getroot()
    print(myroot)
    #changing name of artist to "some artist"
    for artists in myroot.iter("artist"):
        artists.text = "some artist"
    mytree.write('output.xml')
