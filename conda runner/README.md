14th May, 2024
These two files(conda_runner.py and conda_runner.bat) can run anaconda prompt in any directory using scripting. The only problem is it isn't much robust as it should be. Maybe it will be improved in the future IDK.

The problem is that with each windows reboot or restart the size of right click magically increases or decreases for some reasons. Because of this the clicks aren't accurate and when the click aren't accurate, it's not possible to do what we originally intended that was to automate clicks and enter messages as well. So, everytime I open the script the size of right-click's prompt caused me to rechange the coordinates again in order to adjust the clicks. This clearly isn't efficient.

I don't want to tinker too much into the windows security to change this setting cause it might be a possible option to prevent unwanted scripting that could otherwise harm my PC. I might have to look at other ways of scripting to make my system more robust and efficient.

For now, I've just created another script to type in the texts for me. This way half the script is half as efficient as it previously was although if we were to really quantize it, the efficiency that it brings would probably be about 40%. It's just my personal opinion and 'feel'. I would soon have to find a solution to it to make my life easier. That's it for this today.



17th May, 2024

Yeah, I finally made it work as it should. The key ingredient was to use 'windows' key instead of the mouse pointer to click at the windows tab. Then you type in commands and hit enter at your will. Also I've used 'os' library to get the directory name from the user and 'time' library to get the current working time.