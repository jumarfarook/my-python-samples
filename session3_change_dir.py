import os

try:
    parentdir = input('Enter the directory to create: ')
    
    if not os.path.isdir(parentdir):
        os.mkdir(parentdir) # create the parent dir
        os.chdir(parentdir) # change directory

        parentdirfullpath = os.getcwd()

        childdirname = os.path.basename(parentdirfullpath) + "_child"
        childdirfullpath = parentdirfullpath + '/' + childdirname
        
        if not os.path.isdir(childdirfullpath):
            os.mkdir(childdirfullpath) # create the child dir
            childdirfile = os.path.basename(childdirfullpath) + ".txt"
            createfile = open(childdirfile, "w")
    
    os.chdir(parentdir) # go to parent directory
    print(os.listdir()) # list the contents of the parent dir

except:
    print ('An exception has occurred')
finally:
    print ('Operation completed successfully')