# easy code
# import qrcode 
# img= qrcode.make("www.google.com")
# img.save("new_google.png")

#complex code

import qrcode 
from PIL import Image

qr= qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4)
qr.add_data("www.google.com")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="blue")
img.save("google.png")