# geektechstuff
# Python program to check if a file is in a folder and then carry out actions

# libraries to import
# date/time for timestamp
from datetime import datetime
# OS to interact with operating system
import os
# shutil to copy/move file
import shutil
# smtp lib to send email
import smtplib

# variables
file_name = "test.txt"
file_location = os.path.expanduser("~/Desktop/respond_to_file_project/folder_to_check/")
mv_file_name = ""
mv_file_location = os.path.expanduser("~/Desktop/respond_to_file_project/files_that_have_been_found/")
log_file_location = os.path.expanduser("~/Desktop/respond_to_file_project/")
log_value = ""

# settings for email, read from a file called "email_settings" located in same directory as program
from email_settings import smtp_server, port, login_user, login_pass, from_address, to_address
smtpObj = smtplib.SMTP_SSL(smtp_server, port)
smtpObj.login(login_user, login_pass)

# program
os.chdir(file_location)
time_stamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
for filename in os.listdir("."):
        if filename == file_name:
                print("File Found")
                mv_file_name = time_stamp+"_"+file_name
                os.rename(file_name,mv_file_name)
                shutil.move(mv_file_name,mv_file_location)
                print("File moved and renamed", mv_file_name)

                # send email
                email_msg = "File detected, moved and renamed: " +mv_file_name
                email_msg = str(email_msg)
                smtpObj.sendmail(from_address, to_address,
                                'From: FROM_EMAIL_ADDRESS\nSubject: File Detected '+ mv_file_name+'\n\n' + email_msg)
                smtpObj.quit()

                log_value = 1
        else:
                print("No file found matching", file_name)
                log_value = 2

# write to a log file
if log_value == 1:
        os.chdir(log_file_location)
        with open('log_file.txt','a') as filehandle:
                filehandle.write(time_stamp+" File detected"+"\n")
        log_value = ""
elif log_value == 2:
        os.chdir(log_file_location)
        with open('log_file.txt','a') as filehandle:
                filehandle.write(time_stamp+" File not detected"+"\n")
        log_value = ""

