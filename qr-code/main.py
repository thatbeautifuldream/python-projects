# qr code generator in python
import qrcode
data = "https://milind.bio.link"
img = qrcode.QRCode(version=1, box_size=10, border=4)
img.add_data(data)
img.make(fit=True)
img.make_image(fill_color="black", back_color="white")
img.save("qr-code.png")