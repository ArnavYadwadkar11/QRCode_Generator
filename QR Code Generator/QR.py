import pyqrcode
import png
from pyqrcode import QRCode
s = "www.google.org"
url = pyqrcode.create(s)
url.svg('abc.svg', scale=8)
url.png('myqr.png', scale=6)