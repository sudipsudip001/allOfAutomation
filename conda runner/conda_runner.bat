@echo off
set current_dir=%~dp0
set file_name=conda_runner.py
set full_path=%current_dir%%file_name%

@rem to list the virtual environments
call conda env list

@rem take the environment names rom the user.
set /p var="Which environment to select? (Press Enter to select the default environment)"

@rem to open the mentioned python file
python3 "%full_path%" %var% %*

@rem pause