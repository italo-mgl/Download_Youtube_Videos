import PySimpleGUI as sg
from pytube import YouTube
import os


sg.theme("Dark Blue 16")

l1 = sg.Titlebar("Youtube Download", None, "red", "white")
l2 = sg.Text("URL")
l3 = sg.Input(size=(50, 1), key="url")
l5 = sg.Button("Download MP3")
l6 = sg.Button("Download MP4")

interface = [[l1],[l2],[l3],[l5],[l6]]

janela = sg.Window("Window", interface)


while True:
    evento, valor = janela.read()

    if valor == sg.WIN_CLOSED:

            if valor == sg.WIN_CLOSED:

        break
    
    elif evento == "Download MP4":
        link = janela["url"].get()
        video = YouTube(link)
        stream = video.streams.get_highest_resolution()
        stream.download("Downloads")
        print("Download completado!")
    elif evento == "Download MP3":
        link = janela["url"].get()
        video = YouTube(link)
        stream = video.streams.get_audio_only()
        stream.download("Downloads")
        print("Download completado!")
    janela.close()
    exit()
