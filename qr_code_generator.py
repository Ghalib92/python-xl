import qrcode

data = input("Enter text or url: ").strip()
name = input("Enter the filename: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color = 'black',back_color = 'white')
image.save(name)
print(f"Qr code saved as{name}")
