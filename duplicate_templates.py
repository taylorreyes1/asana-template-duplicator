from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv

# TODO: Handle error handling for password input
def _switch_tabs(driver):
	for handle in driver.window_handles:
	    driver.switch_to_window(handle)


def _check_completion_status():
	finished = raw_input('Have the projects finished duplicating? (Y/N): ')	
	if finished.lower() == 'y':	
		driver.close()
	else:
		finished = raw_input('Have the projects finished duplicating? (Y/N): ')


def _duplicate_template_for_student():
	# This should be the url of the opened project for duplication
	get_url = raw_input('Please provide the url where the projects will live: ')
	driver = webdriver.Firefox()	
	driver.get(get_url)
	driver.find_element_by_id('google_auth_button').click()

	_switch_tabs(driver)	

	username = driver.find_element_by_name('Email')	

	username.send_keys('geoff.boss@hackreactor.com')	
	driver.find_element_by_id('next').click()

	get_passwd = raw_input('Please provide your password: ')
	passwd = driver.find_element_by_name('Passwd')
	passwd.send_keys(get_passwd)
	driver.find_element_by_id('signIn').click()
	print 'we are logging in'

	_switch_tabs(driver)		

	with open('testing_new_names.csv') as csvfile:
		print 'in the open'
		reader = csv.DictReader(csvfile)
		for row in reader:
			if len(row['Name']) > 5:				
				driver.implicitly_wait(40)
				driver.find_element_by_id('pot_action_menu').click()
				driver.find_element_by_id('duplicate_project').click() 
				student_name_field = driver.find_element_by_id('duplicate_object_name_input')
				student_name_field.send_keys(row['Name'])
				driver.find_element_by_id('duplicate_object_dialog_submit').click()
				print 'creating user: ' + row['Name']
				driver.implicitly_wait(40)										
	
	driver.implicitly_wait(60)
	_check_completion_status()
	
if __name__ == '__main__':
	try:
		_duplicate_template_for_student()	
	except Exception, e:
		print e	


