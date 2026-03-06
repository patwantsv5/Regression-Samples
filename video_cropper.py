from moviepy.editor import VideoFileClip

# use regression env
# video cropping tool, just put start and end. I WILL NOT USE MICROSLOP CLIPCHAMP I HATE MICROSLOP

per = "16%"
vid = VideoFileClip(f"video_data/{per}.mp4")
s = 7
e = 27

clipped = vid.subclip(s, e)
clipped.write_videofile(f"video_cropped/{per}_cropped.mp4")
