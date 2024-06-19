import qrcode

#Taking UPI ID As a input
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the payment URL based on the UPI ID and the payment app
#You can modify these URLs based on the payment apps you want to support

phonepe_upr = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_upr = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_upr = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#Create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_upr)
paytm_qr = qrcode.make(paytm_upr)
google_pay_qr = qrcode.make(google_pay_upr)


#Save the QR code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')


#Display the QR codes 
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

