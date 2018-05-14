from pytube import YouTube
from os import path, mkdir

url_list = [
    #('URL_string', 'Name to save as'),
    # ('https://www.youtube.com/watch?v=XhWvz4dK4ng', 'The AST and me'),
    ]
dest_dir =  '/Users/ayeager/Desktop/PyCon2018YouTube'

def clean_title(title):
    """make the title file_name friendly"""
    for char in ['\\', '/', '(', ')', '{', '}', '%', '<', '>']:
        title.replace(char, '_')
    return title

# do work
if not path.exists(dest_dir):
    mkdir(dest_dir)  # make sure the directory exists
print(f'{len(url_list)} videos to download.  Starting...')
vid_ct = 1
for target_url, user_name in url_list:
    print(f'starting video # {vid_ct}')
    yt = YouTube(target_url)
    stream = yt.streams.filter(file_extension='mp4').first()
    f_name = user_name or clean_title(yt.title)
    stream.download(output_path=dest_dir, filename=f_name)
    print(f'video {vid_ct} complete')
    vid_ct += 1








