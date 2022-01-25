import os
import io
import qrcode
import info

print("IP: {}".format(info.my_ip))
print("PORT: {}".format(info.PORT))

link = 'http://{}:{}'.format(info.my_ip, info.PORT)

qr = qrcode.QRCode()
qr.add_data(link)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print("Link gerado: ")
print(f.read())

os.system("python3.10 -m http.server {}".format(info.PORT))