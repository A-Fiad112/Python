import os
print(dir(os))
print(dir(os.path))
os.chdir() -> change directory
print(os.getcwd()) -> get current working directory
print(os.listdir()) -> folders and fiels on desktop
os.mkdir('os-demo-2') -> make a folder only
os.makedirs('os-demo-3/a') -> make a folder inside a folder
os.rmdir('os-demo-2') -> delete a folder
os.removedirs('os-demo-3/a') -> delete a folder and inner folder
os.rename('old','new') -> with it's extension
os.stat('demo.txt') -> this get the information of the file
os.walk() -> very useful if u want let say know the folder and inner of this folder and files inner of these folder 
os.path.basename('\temp\test.txt') <- any directory and this is not suppose to be real directory
os.path.exists('\temp\test.txt') <- return true or false 
os.path.isdir('\temp\test.txt') <- return true or false 
os.path.isfile('\temp\test.txt') <- return true or false 
os.path.split('\temp\test.txt') <- return true or false 
os.path.splitext('\temp\test.txt') <- return true or false 
