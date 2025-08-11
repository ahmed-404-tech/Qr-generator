import qrcode

def createQr(back, fill, data):
    qr = qrcode.QRCode(version=2, box_size=10, border=2)
    qr.add_data(data)

    qr.make(fit=True)
    qr.make_image(back_color=back, fill_color=fill).save("qr.png")
