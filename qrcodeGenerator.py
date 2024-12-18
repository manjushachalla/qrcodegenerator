import qrcode
qr=qrcode.QRCode(
    version=5,
    box_size=5,
    border=2
)
name=input("enter your name:")
age=int(input("enter your age:"))
email=input("enter your email:")
data={'Name':name,"Age":age,'E-mail':email}
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image()
img.save("detailsqr.png")
img.show()