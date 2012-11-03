def load(row, directory):
	return Painting( row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], directory + row[13], row[14] )

class Painting:
	def __init__( self, author, title, year, genre, collection, location, latitude, longitude, width, height, area, image, imageURL, filePath, notes ):
		self.author = author
		self.title = title
		self.year = year
		self.genre = genre
		self.collection = collection
		self.location = location
		self.latitude = latitude
		self.longitude = longitude
		self.width = width
		self.height = height
		self.area = area
		self.image = image
		self.imageURL = imageURL
		self.filePath = filePath
		self.notes = notes

		self.data = None
