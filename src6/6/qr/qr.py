# Generates a QR code
# https://github.com/lincolnloop/python-qrcode

import qrcode
from PIL import Image


# Generate QR code
img = qrcode.make("https://youtu.be/oHg5SJYRHA0")

# Save as file
img.save("qr.png", "PNG")
