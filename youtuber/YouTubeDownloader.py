from pytube import YouTube
from os import path, mkdir
import asyncio

url_list = [
            # 'https://www.youtube.com/watch?v=AQsZsgJ30AE',
            # 'https://www.youtube.com/watch?v=q42hCs2E4So',
            # 'https://www.youtube.com/watch?v=WXkhJ92-fsY',
            # 'https://www.youtube.com/watch?v=Jd8ulMb6_ls',
            # 'https://www.youtube.com/watch?v=zJ9z6Ge-vXs',
            # 'https://www.youtube.com/watch?v=FjojZxDZscQ',
            # 'https://www.youtube.com/watch?v=NyNUYYI-Pdg',
            # 'https://www.youtube.com/watch?v=lk6FGg5RzAk',
            # 'https://www.youtube.com/watch?v=cxTXJ3N91s0',
            # 'https://www.youtube.com/watch?v=q42hCs2E4So',
    # 'https://www.youtube.com/watch?v=ePZDoRg8oNY',
    'https://www.youtube.com/watch?v=Cj9xCnRg1VE'
]
dest_dir = 'C:\\Users\\Ricky\\Desktop\\PyConVideos'


def clean_title(title):
    """make the title file_name friendly"""
    for char in ['\\', '/', '(', ')', '{', '}', '%', '<', '>']:
        title.replace(char, '_')
    return title


async def download_video(url):
    # do work
    print(f'starting video # {url}')
    if not path.exists(dest_dir):
        mkdir(dest_dir)  # make sure the directory exists
    yt = YouTube(url)
    f_name = clean_title(yt.title)
    print(f'title: {f_name}')
    stream = yt.streams.filter(file_extension='mp4').first()
    stream.download(output_path=dest_dir, filename=f_name)
    yt.streams.filter(file_extension='mp4').first().download(output_path=dest_dir, filename=f_name)
    print(f'video {url}, {f_name} complete')


import random
async def this(id):
    print(f'starting{id}')
    pt = random.randint(1,10)
    await asyncio.sleep(pt)
    print(f'finished time in {pt}')


async def download_videos():
    try:
        coroutines = [asyncio.ensure_future(download_video(target_url)) for target_url in url_list]
        # coroutines = [asyncio.ensure_future(this(target_url)) for target_url in range(20)]
        await asyncio.gather(*coroutines)
    except Exception as e:
        print(f'fatal error {e}')

    # coroutines = [download_video(target_url) for target_url in url_list]
    # completed, pending = await asyncio.wait(coroutines)


if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    event_loop.run_until_complete(download_videos())
    event_loop.close()



''''

from pytube import YouTube
from os import path, mkdir
import asyncio

url_list = ['https://www.youtube.com/watch?v=AQsZsgJ30AE',
            'https://www.youtube.com/watch?v=q42hCs2E4So',
            'https://www.youtube.com/watch?v=WXkhJ92-fsY',
            'https://www.youtube.com/watch?v=Jd8ulMb6_ls',
            'https://www.youtube.com/watch?v=zJ9z6Ge-vXs',
            'https://www.youtube.com/watch?v=FjojZxDZscQ',
            'https://www.youtube.com/watch?v=NyNUYYI-Pdg',
            'https://www.youtube.com/watch?v=lk6FGg5RzAk',
            'https://www.youtube.com/watch?v=cxTXJ3N91s0',
            'https://www.youtube.com/watch?v=XKoK9wJjSqY',
            'https://www.youtube.com/watch?v=q42hCs2E4So',
]
dest_dir = 'C:\\Users\\Ricky\\Desktop\\PyConVideos'


def clean_title(title):
    """make the title file_name friendly"""
    for char in ['\\', '/', '(', ')', '{', '}', '%', '<', '>']:
        title.replace(char, '_')
    return title


async def download_video(url):
    # do work
    if not path.exists(dest_dir):
        mkdir(dest_dir)  # make sure the directory exists
    yt = YouTube(url)
    f_name = clean_title(yt.title)
    print(f'starting video # {url} {f_name}')
    stream = yt.streams.filter(file_extension='mp4').first()
    stream.download(output_path=dest_dir, filename=f_name)
    return f'video {url}, {f_name} complete'


async def download_videos():
    coroutines = [download_video(target_url) for target_url in url_list]
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())

if __name__ == "__main__":
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(download_videos())
    except Exception as e:
        print(f'fatal error {e}')

'''