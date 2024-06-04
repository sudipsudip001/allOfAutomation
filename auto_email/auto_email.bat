@echo off
set /P email=Enter the email of receiver:
set /P subject=Enter the subject:
set /P message=Enter the message:
echo %email% > id.txt
echo %subject% > subject.txt
echo %message% > message.txt

set current_dir=%~dp0
set file_name=auto_email.py
set full_path=%current_dir%%file_name%
python "%full_path%" %*

pause