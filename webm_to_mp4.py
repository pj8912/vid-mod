from moviepy.editor import *
from moviepy.video.fx.all import *

#video file
clip = VideoFileClip("Screencast from 15-03-23 12:32:24 PM IST.webm")

#newname
newname = "output.mp4"
clip.write_videofile(newname)
print("New VideoFile: ", newname, "created!!")

