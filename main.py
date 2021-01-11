# -*- coding: utf-8 -*-
"""
       (`-()_.-=-.
       /66  ,  ,  \
     =(o_/=//_(   /======`
         ~"` ~"~~`        C.E.
         
Created on Wed Jan  6 09:53:47 2021
@author: Chris
Contact :
    Christopher.eaby@gmail.com
"""

from __future__ import unicode_literals
import youtube_dl
from youtubesearchpython import PlaylistsSearch
import tkinter as tk
from zipfile import ZipFile
import glob
import sys
import os

def downloader(artist, album):

    search = PlaylistsSearch(artist + ' ' + album + ' playlist' , limit = 1)
    url = (search.result()['result'][0]['link'])

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
        }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    
    zipObj = ZipFile((artist.strip() + " - " + album.strip()).replace('\n', '') +'.zip', 'w')
    
    for file in glob.glob('*.mp3'):
        zipObj.write(file)
        os.remove(file)
        
    sys.exit(0)
    
gui = tk.Tk()
# sets the title 
gui.title("Album downloader")
# sets the size
gui.geometry("250x130")

txt1 = tk.Text(gui, fg = "white", bg = "purple", height = 1, width = 15)
txt1.grid(row = 4, column = 1)
lbl5 = tk.Label(gui, text = "Artist", justify = tk.CENTER, padx = 30, pady = 10)
lbl5.grid(row = 4, column = 0)
txt2 = tk.Text(gui, fg = "white", bg = "purple", height = 1, width = 15)
txt2.grid(row = 5, column = 1)
lbl6 = tk.Label(gui, text = "Album", justify = tk.CENTER, padx = 30, pady = 10)
lbl6.grid(row = 5, column = 0)
b1 = tk.Button(gui, text = "Download", height = 2, width = 9, command = lambda: downloader(txt1.get("1.0","end"), (txt2.get("1.0","end"))))
b1.grid(row = 6, column = 0)    
    
gui.mainloop()  