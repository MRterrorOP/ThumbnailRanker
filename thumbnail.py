from pytube import YouTube

# YouTube video URL
video_url = "https://youtu.be/nPHFjkCYJm8?feature=shared"

# Create a YouTube object
yt = YouTube(video_url)

# Get the thumbnail URL
thumbnail_url = yt.thumbnail_url

print("Thumbnail URL:", thumbnail_url)
