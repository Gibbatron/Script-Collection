## This Python script performs the following:
## - opens a Firefox page
## - opens Twitter
## - logs into Twitter
## - Searches for a person
## - opens that persons profile


from selenium import webdriver

import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Create instance webdriver
browser = webdriver.Firefox()
browser.get('https://twitter.com/i/flow/login') #should take you straight to the login pop-up box
print("Website loaded")

# Lets user see and also load the elemen. Code pauses the script for 2 seconds
time.sleep(2)

# Locate the login button   
#login = browser.find_elements(By.XPATH, '//*[@id="doc"]/div[1]/div/div[1]/div[2]/a[3]')
#login = browser.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[3]/a/div')
#above line was through inspecting the login button and copying the XPath

# Using the click function which is similar to a click in the mouse
#login[0].click()

#print("Login button located on Twitter")

# Locate the username field
#user = browser.find_elements(By.XPATH, '//*[@id="login-dialog-dialog"]/div[2]/div[2]/div[2]/form/div[1]/input')
#user = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
#user = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[1]')
#user = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]')

#// means start from the root of the HTML document.
# looks for an <input> tag with name attribute as 'text'
user = browser.find_element(By.XPATH, '//input[@name="text"]')

# click on the username field to select it
#user[0].click()

#print("Username field located")

# Enter the username
#user[0].send_keys('Gibbzyy')
user.send_keys('USERNAME')

print("Username entered")

# Locate and click on the next button
#next = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
next = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
next.click()

print("Next button located & clicked")
time.sleep(2)
# find the password field and click it
#password = browser.find_elements(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password = browser.find_elements(By.XPATH, '//input[@name="password"]')
#password.click()

print("Password field located")

# Read password from a password.txt file (for added security)
with open('password.txt', 'r') as myfile:
    Password = myfile.read().replace('\n', '')
#user.send_keys(Password)
#password.send_keys(Password)
password[0].send_keys(Password)

print("Password entered")

#locate and click log in button
LOG = browser.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/button/div')
LOG.click()
print("Logged in successfully")
time.sleep(5)



#Find the search bar, click it, and search for Tommy Tangs profile (my favourite bioinformatician)

elem = browser.find_element(By.XPATH, '//input[@aria-label="Search query"]')
elem.click()

elem.send_keys("@tangming2005")

#using keys to send special KEYS,i.e. the enter key
elem.send_keys(Keys.RETURN)

print("Search done")
time.sleep(2)

#open Tommys twitter profile (should be the top entry on the page)
tommy = browser.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/section/div/div/div[3]/div/div/button/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]')
tommy.click()

#closing browser
browser.close()


