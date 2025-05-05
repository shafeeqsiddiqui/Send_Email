import smtplib as s 

ob = s.SMTP('SMTP.gmail.com', 587)
ob.ehlo()
ob.starttls()
ob.login("sshafeeqsiddiqui@gmail.com", "********")
subject="Email testing Python "
body = "I LOVE PYTHON"
msg = "subject:{}\n\n{}".format(subject, body)
list_add=['sidshafeeq1@gmail.com',
      'sshafeeq@student.iul.ac.in']

ob.sendmail("sshafeeqsiddiqui@gmail.com", list_add, msg)
print("send mail")
ob.quit()