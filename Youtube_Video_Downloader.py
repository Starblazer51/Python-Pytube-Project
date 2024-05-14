#!/usr/bin/env python
# coding: utf-8

# In[24]:


from pytube import YouTube
from pytube import Playlist
import customtkinter as ctk
import os
from customtkinter import CTkButton
from customtkinter import CTkFrame
from customtkinter import CTkEntry


# In[25]:


def single_dl(root, video_url):
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        dl_dir = get_download()
        stream.download(output_path=dl_dir)
        kill_switch(root)
    except:
        print("video url invalid")


# In[26]:


def get_download():
    target_dir = os.path.expanduser("~")
    dl_dir = os.path.join(target_dir, "Downloads")
    return dl_dir


# In[27]:


def playlist_dl(playlist_utl):
    try:
        obj_list = Playlist(playlist_url)
        print(f'downloading playlist {obj_list.title}')
        dl_dir = get_download()
        for video in obj_list.videos:
            stream = video.streams.get_highest_resolution()
            stream.download(output_path=dl_dir)
    except:
        print("playlist url invalid")
    


# In[28]:


def kill_switch(root):
    root.destroy()
    root.quit()
    


# In[29]:


def forget(root):
    widgets = root.winfo_children()
    for widget in widgets:
        widget.destroy()


# In[30]:


def go_back(root):
    forget(root)
    dl_gui(root)


# In[31]:


def dl_bridge(root, dl_type):
    forget(root)
        
    if dl_type == 0:
        root.title("YT Single Download")
        single_url = CTkEntry(root, placeholder_text = "Enter url here")
        single_url.pack()
        CTkButton(root, text="submit", command=lambda: single_dl(root, single_url.get())).pack(padx=0, pady=10)
        CTkButton(root, text="back", command=lambda: go_back(root)).pack(padx=0, pady=50)
    elif dl_type == 1:
        root.title("YT Playlist Download")
        playlist_url = CTkEntry(root, placeholder_text = "Enter url here")
        playlist_url.pack()
        CTkButton(root, text="submit", command=lambda: playlist_dl(root, playlist_url.get())).pack(padx=0, pady=10)
        CTkButton(root, text="back", command=lambda: go_back(root)).pack(padx=0, pady=50)
    
    


# In[32]:


def dl_gui(root):
    
    root.title("YT Video Downloader")
    root.geometry("300x250")

    CTkButton(root, text="Single Download", command=lambda: dl_bridge(root, 0)).pack(padx=0, pady=0)
    CTkButton(root, text="Playlist Download", command=lambda: dl_bridge(root, 1)).pack(padx=0, pady=50)
    CTkButton(root, text="Quit", command=lambda: kill_switch(root)).pack(padx=0, pady=10)


# In[33]:


def main():
    root = ctk.CTk()
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("dark-blue")
    
    dl_gui(root)

    root.mainloop()
main()


# In[ ]:




