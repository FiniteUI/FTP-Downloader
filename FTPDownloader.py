import dotenv
import ftplib
import os
from datetime import datetime
import zipfile
import shutil

def cloneDirectory(directory, destination, ftp):
    #get file list
    ftp.cwd(directory)
    files = ftp.nlst()

    for f in files:
        dest = os.path.join(destination, f)
        file = directory + '/' + f

        #check if file is file or directory
        x = ftp.sendcmd(f'MLST {file}')
        if 'type=dir' in x:
            dir = True
        else:
            dir = False

        if dir:
            #if directory, go process that directory
            os.makedirs(dest)
            cloneDirectory(file, dest, ftp)    
        else:
            #if file, download it
            print("Downloading file [" + file + ']...')
            ftp.retrbinary("RETR " + file, open(dest, 'wb').write)

def zipfolder(foldername, target_dir):            
    zipobj = zipfile.ZipFile(foldername + '.zip', 'w', zipfile.ZIP_DEFLATED)
    rootlen = len(target_dir) + 1
    for base, dirs, files in os.walk(target_dir):
        for file in files:
            fn = os.path.join(base, file)
            zipobj.write(fn, fn[rootlen:])

#load credentials
dotenv.load_dotenv('ConnectionDetails.env')

#login to FTP server
server = ftplib.FTP(os.getenv('HOST'))
server.login(os.getenv('USER'), os.getenv('PASSWORD'))

#now build new download location
folderName = datetime.strftime(datetime.today(), "%Y-%m-%d-%H-%M-%S")
destination = os.path.join(os.getenv('DESTINATION'), folderName)

print(f"Running FTP Downloader for FTP Server [{os.getenv('HOST')}] and source folder [{os.getenv('SOURCE')}] to destination [{destination}]...")

#now download the files
cloneDirectory(os.getenv('SOURCE'), destination, server)

#log out of FTP
server.quit()
print("FTP Download complete.")

#now zip folder and delete original
print(f"Zipping up folder [{destination}]...")
zipfolder(destination, destination)

print(f"Zip file [{zip}] created. Deleting source folder [{destination}]...")
shutil.rmtree(destination)

print("Process complete.")

	