import os.path

def load(row, directory):
    if os.path.isfile(directory + row[0]):
        return Painting(**{
            'filePath':   directory + row[0],
            'id':         row[1],
            'title':      row[2],
            'year':       row[3],
            'genre':      row[4],
            'height':     row[5],
            'width':      row[6],
            'area':       row[7],
            'materials':  row[8],
            'collection': row[9],
            'img_width':  row[10],
            'img_height': row[11],
            'img_ratio':  row[12]
        })
    else:
        raise IOError

class Painting:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.title = kwargs['title']
        self.year = kwargs['year']
        self.genre = kwargs['genre']
        self.collection = kwargs['collection']
        self.width = kwargs['width']
        self.height = kwargs['height']
        self.area = kwargs['area']
        self.filePath = kwargs['filePath']

        self.data = None

    def __repr__(self):
        return self.year
