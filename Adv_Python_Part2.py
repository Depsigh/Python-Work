import os
import shutil 

os.mkdir('copy_slides')

#Finds files in ~/Downloads with the file extension .pptx or .ppt.
print(shutil.which('.ptx'))
print(shutil.which())


#Copies these files into the current working directory.

print('Before:', os.lisdir('copy_slides'))
shutil.copy('.ptx', 'copy_slides')
print ('After', os.listdir("copy_slides"))

#Im not really sure about this function nor am i sure how to get it to run.