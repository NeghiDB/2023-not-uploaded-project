import os

#path folder would be searched for
path='C:/Users/Nosa/Desktop/'

#input any character present in the file name, the longer the input, the more accurate it would be
y = input('Enter the name of the files you want to delete: ')

#check the specified path for the file name characters presence
files = [i for i in os.listdir(path) if os.path.isfile(os.path.join(path,i)) and y in i]
print(files)

#for console demonstration only so you could see the number of files
y = int(len(files))
print(y)

#for loop to ensure that each of the items in the list are deleted one at a time before the loop ends
for i in range(len(files)):
    os.remove('C:\\Users\\NOSA\\Desktop\\'+ files[i])