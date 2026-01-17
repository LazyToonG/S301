class Music:
    def __init__(self, id, title, artist, path, length):
        self.id = id
        self.title = title
        self.artist = artist
        self.path = path
        self.length = int(length) if length else 0
