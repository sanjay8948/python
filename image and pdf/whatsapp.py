from selenium import webdriver
driver = webdriver.chrome()
driver.get('https://web.whatsapp.com/')

name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = input('Enter the count ')
input('Enter anything after scanning the QR code')
