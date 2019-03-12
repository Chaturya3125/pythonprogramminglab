import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='gchaturyar@gmail.com'
receiver='derrendsouza36@gmail.com'
msg="hii"
s.login(sender,'chaturya@63')
s.sendmail(sender,receiver,msg)
print("msg sent successfully")
s.quit()
	
