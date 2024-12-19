from ftplib import FTP


ftp_host = 'host ip'  
ftp_user = 'your user'      
ftp_pass = 'your password'        


local_file = 'path/to/file.txt'
remote_file = 'remote_file.txt'   


ftp = FTP(ftp_host)
ftp.login(ftp_user, ftp_pass)


with open(local_file, 'rb') as f:
    ftp.storbinary(f"STOR {remote_file}", f)


ftp.quit()

