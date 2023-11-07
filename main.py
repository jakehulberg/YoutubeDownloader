#!/usr/bin/env python3

from pytube import YouTube
url = input("Youtube URL: ")

my_video = YouTube(url)

print(my_video.title)

print(my_video.thumbnail_url)

my_video = my_video.streams.get_highest_resolution()

my_video.download('/Users/jakehulberg/Desktop/Youtube_Downloads')
