#!/usr/bin/env python3

from pytube import YouTube

url = input("Youtube URL: ")
folder = "Youtube_downloads"

my_video = YouTube(url)

print(my_video.title)

my_video = my_video.streams.get_highest_resolution()

my_video.download('/Users/jakehulberg/Desktop/' + folder)

url2 = input ("2nd Youtube URL: ")

my_video2 = YouTube(url2)

print(my_video2.title)


my_video2 = my_video2.streams.get_highest_resolution()

my_video2.download('/Users/jakehulberg/Desktop/' + folder)

url3 = input ("3rd Youtube URL: ")

my_video3 = YouTube(url3)

print(my_video3.title)


my_video3 = my_video3.streams.get_highest_resolution()

my_video3.download('/Users/jakehulberg/Desktop/' + folder)

url4 = input ("4rth Youtube URL: ")

my_video4 = YouTube(url3)

print(my_video4.title)


my_video4 = my_video4.streams.get_highest_resolution()

my_video4.download('/Users/jakehulberg/Desktop/' + folder)