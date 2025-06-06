To record a screen on Ubuntu 
a- Start : Ctrl+Alt+Shift+R 
b- Stop : Ctrl+Alt+Shift+R or on the top right corner you can stop it

You will get .webm inside your home/Videos/Screencasts 

to conver from .webm into gif animation 

$ sudo apt intall ffmpeg    
$ ffmpeg -i input.webm -pix_fmt rgb24 output.gif

to convert from mp4 to gif animation 
$ ffmpeg -i cat.mp4 cat.gif