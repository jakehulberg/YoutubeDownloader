#!/usr/bin/env python3

from pytube import YouTube
url = input("Youtube URL: ")

my_video = YouTube(url)

print(my_video.title)

my_video = my_video.streams.get_highest_resolution()

my_video.download('/Users/jakehulberg/Desktop/Youtube_Downloads')

url2 = input ("2nd Youtube URL: ")

my_video2 = YouTube(url)

print(my_video2.title)


my_video2 = my_video2.streams.get_highest_resolution()

M_video2.download('/Users/jakehulberg/Desktop/Youtube_downloads')
