import qrcode

counter = 25
data = input("what data do you want to put in the qr-code: ")

name = input("what would you like to name the file: ")

qr = qrcode.QRCode(version=3, box_size=25, border=2.5)
qr.add_data(data)

qr.make(fit=True)

    # Choose random fill and background colors until they are different

img = qr.make_image(fill_color="black", back_color="white")

img.save(name + ".png")