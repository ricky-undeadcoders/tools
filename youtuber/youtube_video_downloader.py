#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=UXyHf_SpUUI')
# print vars(yt)
print('got content')
# print yt.vid_info
mooky = yt.streams.all()
print('got video')
# print yt.video_id
# print yt.watch_url
#
# print mooky[0]
mooky[0].download('E:\\Performance Media')

print('all done')
