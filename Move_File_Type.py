#geektechstuff
#Python to move particular file types

#Requires OS and shutil modules
import os
import shutil

#title
print('')
print('GeekTechStuff presents the file type mover')
print('')
print('')

#Uses os to use user input to set the working directory
location = input('Folder that contains the files')
copy_location = ''
os.chdir(location)
file_type = input('Which file type? e.g. jpeg')
file_type = '.'+file_type
print('You want to check: '+location+' for a file type of '+file_type)

#giving user the option to get out if needed
cont = input('Is this correct? Y or N: ')
cont = str.lower(cont)

if cont == 'n':
    print('Ending now, no further action')

elif cont == 'y':
    print('Continuing the program!')
    print('')
    copy_location = input('Where should the files go?: ')
    print('')
    for filename in os.listdir('.'):
        if filename.endswith(file_type):
            copy_location = copy_location+filename
            print('Moving ' + filename + ' to ' + copy_location)
            shutil.move(filename, copy_location)


else:
    print('You were given two choices and managed to mess it up. This is why computers will one day rule the world!')



