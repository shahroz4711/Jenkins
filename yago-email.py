import yagmail

# Replace with your email credentials and recipient
yag = yagmail.SMTP('coursesinfo9@gmail.com', 'ubgdmmxzdycfheew')
contents = "ki hal aa thk hu "

yag.send('iamok73727@gmail.com', 'Hi I am Shahroz', contents)

print("email has been sent")
