

import qrcode
import matplotlib.pyplot as plt
from google.colab import files

upi_id = input("Enter your UPI ID: ")

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')  
google_pay_qr.save('google_pay_qr.png')

plt.imshow(phonepe_qr)
plt.axis('off')
plt.title('PhonePe QR Code')
plt.show()

plt.imshow(paytm_qr)
plt.axis('off')
plt.title('Paytm QR Code')
plt.show()

plt.imshow(google_pay_qr)
plt.axis('off')
plt.title('Google Pay QR Code')
plt.show()

files.download('phonepe_qr.png')
files.download('paytm_qr.png')
files.download('google_pay_qr.png')
