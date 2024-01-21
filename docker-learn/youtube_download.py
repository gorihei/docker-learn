import sys, re, os
from yt_dlp import YoutubeDL

args = sys.argv
urls = []
for i, arg in enumerate(args):
    if i == 0: continue
    if re.match('https?://[\w/:%#\$&\?\(\)~\.=\+\-]+', arg):
        urls.append(arg)
    else:
        print(f'invalid url:{arg}')
        exit(1)

print('download target urls:')
for url in urls:
    print(f'   {url}')

ydl_options = {
    'outtmpl' : f'{os.getcwd()}{os.path.sep}video{os.path.sep}%(title)s.%(ext)s'
}

with YoutubeDL(ydl_options) as ydl:
    result = ydl.download(urls)