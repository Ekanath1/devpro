import smtplib as s

# This code working fine

ob = s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()
ob.login('ekanathbiradar1999@gmail.com','tznj kjts gkpy mbtw')
subject = 'test python'
body = 'I Love Python'
message = "subject:{}\n\n{}".format(subject,body)
listadd = ['ekanathbiradar551@gmail.com','ekanth@klesnc.org']

ob.sendmail('ekanathbiradar1999@gmail.com',listadd,message)
print('send mail')
ob.quit()