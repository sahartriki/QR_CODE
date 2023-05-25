import qrcode

QR=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=50, border=1)
link=input("link ? : ")
QR.add_data(link)
img = QR.make_image(fill_color="black" , back_color="white")
name=input("Qr code name? : ")
img.save(name+".png", 'PNG')