from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import csv


def _switch_tabs(driver):
	for handle in driver.window_handles:
	    driver.switch_to_window(handle)


def _check_completion_status(driver):
	finished = raw_input('Have the projects finished duplicating? (Y/N): ')	
	if finished.lower() == 'y':	
		driver.close()
	else:
		finished = raw_input('Have the projects finished duplicating? (Y/N): ')


# TODO: Handle error handling for password input
def _check_for_page_timeout(driver):
	error_check = driver.find_element_by_id('error_message_box')
	if not error_check:
		print 'greenlight'
	

def _digest_csv_data(driver):
	file_to_open = raw_input('Please provide the full name of the file: ')	
	with open(file_to_open) as csvfile:
		print 'in the open'
		reader = csv.DictReader(csvfile)
		for row in reader:
			if len(row['Name']) > 5:				
				driver.implicitly_wait(60)
				driver.find_element_by_id('pot_action_menu').click()
				driver.find_element_by_id('duplicate_project').click() 
				student_name_field = driver.find_element_by_id('duplicate_object_name_input')
				student_name_field.send_keys(row['Name'])
				driver.find_element_by_id('duplicate_object_dialog_submit').click()
				print 'creating user: ' + row['Name']
				driver.implicitly_wait(60)			
				# _check_for_page_timeout(driver)							
	
	driver.implicitly_wait(60)
	_check_completion_status(driver)


def _duplicate_template_for_student():
	# This should be the url of the opened project for duplication
	get_url = raw_input('Please provide the url where the projects will live: ')
	driver = webdriver.Firefox()	
	driver.get(get_url)
	driver.find_element_by_id('google_auth_button').click()

	_switch_tabs(driver)	

	get_user_name = raw_input('Please provide your username (email address): ')
	username = driver.find_element_by_name('Email')	
	username.send_keys(get_user_name)	
	driver.find_element_by_id('next').click()

	get_passwd = raw_input('Please provide your password: ')
	passwd = driver.find_element_by_name('Passwd')
	passwd.send_keys(get_passwd)
	driver.find_element_by_id('signIn').click()
	print 'we are logging in'

	_switch_tabs(driver)		
	_digest_csv_data(driver)


if __name__ == '__main__':
	_duplicate_template_for_student()	
else:	
	print 'These methods are private'


