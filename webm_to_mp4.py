from moviepy.editor import *
from moviepy.video.fx.all import *

#video file
clip = VideoFileClip("FILENAME")

#newname
newname = "output.mp4"
clip.write_videofile(newname)
print("New VideoFile: ", newname, "created!!")

