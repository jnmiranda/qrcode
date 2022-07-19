import pyqrcode
import png

s = "https://www.youtube.com/watch?v=c65yR7FWJsM"

#Generate QR code
url = pyqrcode.create(s)

#Create and save the png file naming "myqr.png"
url.png("myqr.png", scale = 6)