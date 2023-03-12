# FTP-Downloader
This is a simple personal project to automatically download files from an FTP server. Currently, I am using this to run backups of a game server for my friends and I.

To use this program, there must be a .env file in the working directory named **ConnectionDetails.env**. This will hold the details for the FTP server that the program will use.
The parameters are:
* HOST - The IP address/domain name for the FTP server
* PORT - The port number to use
* USER - The username to login to the server
* PASSWORD - The password to login to the server
* SOURCE - The folder on the FTP server to download
* DESTINATION - Where to place the downloaded files on the local machine

A sample connection file is included, **ConnectionDetails_Sample.env**.

When ran, the **FTPDownloader.py** script will read in the connection file, connect to the FTP server using the provided credentials, download all files from the source
directory, compress them all into a single zip file, and delete the uncompressed files. 

Also included is a batch file I use to run this from the Windows task scheduler, **RunDownloader.bat**.
