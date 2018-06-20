import os

# Change working directory
def change_working_directory():
    os.chdir(os.path.join("C:\\Users\\darrylweimers\\Desktop",'TestFile'))

# Write to custom directory
def write_to_directory(path,fileName,lines):
    previousDirectory = os.getcwd()
    os.chdir(path)
    fileWrite = open(fileName,'w+')
    fileWrite.writelines(lines)
    os.chdir(previousDirectory)

def write_to_directory(path,newfileName,lines):
    fileWrite = open(os.path.join(path,newfileName), 'w')
    fileWrite.writelines(lines)


# List files under directory
def execute(callback,srcPath,dstPath):
    # Change directory
    os.chdir(srcPath)
    # Update files and save it in a new directory
    for fileName in os.listdir(os.getcwd()):    # List files in directory
        if os.path.isfile(fileName):
            # Open file
            fileRead = open(fileName,'r+')
            # Read all lines
            lines = fileRead.readlines()
            # Update lines
            updatedLines = []
            for line in lines:
                updatedLines.append(callback(line))
            # Write updated file into a new directory
            if not os.path.exists(dstPath):
                os.mkdir(dstPath)
            write_to_directory(dstPath,fileName,updatedLines)
            #write_to_directory(dstPath,fileName, updatedLines)




