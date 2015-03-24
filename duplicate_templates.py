from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

# TODO: Handle error handling for password input
def switch_tabs(driver):
	for handle in driver.window_handles:
	    driver.switch_to_window(handle)

def duplicate_template_for_student():
	driver = webdriver.Firefox()
	driver.get("https://app.asana.com/0/21372080955173/21372080955173")
	driver.find_element_by_id('google_auth_button').click()

	switch_tabs(driver)	

	username = driver.find_element_by_name('Email')
	passwd = driver.find_element_by_name('Passwd')

	username.send_keys('geoff.boss@hackreactor.com')
	get_passwd = raw_input('Please provide your password: ')

	passwd.send_keys(get_passwd)
	driver.find_element_by_id('signIn').click()
	print 'we are logging in'

	switch_tabs(driver)		

	with open('testing_names.csv') as csvfile:
		print 'in the open'
		reader = csv.DictReader(csvfile)
		for row in reader:
			if len(row['Name']) > 5:
				driver.implicitly_wait(5)
				driver.find_element_by_id('pot_action_menu').click()
				driver.find_element_by_id('duplicate_project').click() 
				student_name_field = driver.find_element_by_id('duplicate_object_name_input')
				student_name_field.send_keys(row['Name'])
				driver.find_element_by_id('duplicate_object_dialog_submit').click()
				print 'creating user: ' + row['Name']
				driver.implicitly_wait(5)						

	print 'we hit the end of the loop'
	driver.implicitly_wait(15)
	driver.close()


duplicate_template_for_student()	
# new_student_name = raw_input('What is the students name: ')

# student_name_field.send_keys(new_student_name)
# driver.find_element_by_id('duplicate_object_dialog_submit').click()

# new_user = driver.find_element_by_xpath('//span[contains(.,' + '"' + new_student_name + '"' + ')]')
# new_user = driver.find_elements_by_xpath("//span[contains(text(), " + "'" + new_student_name + "'" + ")]")
# new_user = driver.find_element(By.XPATH, "//span[contains(text(), " + "'" + new_student_name + "'" + ")]")

# driver.implicitly_wait(15)
# for i in new_user:
# 	print i

# new_user.click()
# print 'we clickin'
# driver.find_element_by_id('project_members_button').click()
# driver.find_element_by_id('project_members_button/add_user').click()

# new_student_email = raw_input('Enter email address:' )
# driver.find_element_by_id('project_members_button/add_user').send_keys(new_student_email)

# add_new_user = driver.find_elements_by_xpath("//div[contains(text(), 'Add Member')]")
# # add_new_user = driver.find_element_by_xpath('//div[contains(.,'Add Member')]')
# add_new_user.click()

