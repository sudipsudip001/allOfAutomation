@echo off
set current_dir=%~dp0
set file_name=conda_runner.py
set full_path=%current_dir%%file_name%
python "%full_path%" %*
@REM pause