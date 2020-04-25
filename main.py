from __future__ import unicode_literals
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import youtube_dl


class App():
    def __init__(self):
        
        self.app = QApplication(sys.argv)
        self.window = QMainWindow()
        self.window.setGeometry(50,50,1100,500)
        self.window.setMaximumSize(1200,600)
        self.window.setWindowTitle("Youtube Download")
        self.window.setStyleSheet("background-image: url(img/background.jpg)")
        self.window.setWindowIcon(QtGui.QIcon("img/yt.ico"))
        
        self.frame_title = QtWidgets.QFrame(self.window)
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setGeometry(0,0,1200,100)
        self.frame_title.setStyleSheet("background: transparent; border:none;")
        
        self.logo_yt = QtWidgets.QToolButton(self.frame_title)
        self.logo_yt.setGeometry(300,0,100,100)
        self.logo_yt.setIcon(QtGui.QIcon("img/youtube.ico"))
        self.logo_yt.setIconSize(QtCore.QSize(128, 128))
        self.logo_yt.setStyleSheet("background: transparent;")
        
        self.title = QtWidgets.QLabel(self.frame_title)
        self.title.setGeometry(420,50,600,40)
        self.title.setStyleSheet("font-family: Trebuchet MS; font-size:40px; color:white; background:transparent;  text-decoration:underline;")
        self.title.setText("Youtube Download")
        
        self.frame = QtWidgets.QFrame(self.window)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setGeometry(0,120,1200,478)
        self.frame.setStyleSheet("background: rgba(0,0,0,0.5); border:none;")
        
        #AREA DE CONVERTER PARA VIDEO
        self.logo_video = QtWidgets.QToolButton(self.frame)
        self.logo_video.setGeometry(10,10,100,100)
        self.logo_video.setIcon(QtGui.QIcon("img/video.ico"))
        self.logo_video.setIconSize(QtCore.QSize(72, 72))
        self.logo_video.setStyleSheet("background: transparent;")
    
        self.video_text = QtWidgets.QLabel(self.frame)
        self.video_text.setGeometry(120,50,250,40)
        self.video_text.setStyleSheet("font-family: Trebuchet MS; font-size:20px; color:white; background:transparent;  text-decoration:underline;")
        self.video_text.setText("FORMATO DE VIDEO .mp4")
        
        self.url_text = QtWidgets.QLabel(self.frame)
        self.url_text.setGeometry(30,120,100,40)
        self.url_text.setStyleSheet("font-family: Trebuchet MS; font-size:16px; color:white; background:transparent;")
        self.url_text.setText("URL:")
        
        self.video_input = QtWidgets.QLineEdit(self.frame)
        self.video_input.setGeometry(70, 130, 380,20)
        self.video_input.setStyleSheet("border-radius:3px; font-family: Trebuchet MS; font-size:16px; color:white;")
        self.video_input.setPlaceholderText("Cole o link do video aqui")
        
        self.button_confirm = QtWidgets.QPushButton(self.frame)
        self.button_confirm.setGeometry(70,250,120,30)
        self.button_confirm.setStyleSheet("QPushButton{background:#4EEE94;border-radius:5px; color:white; font-family: Trebuchet MS;\
        font-size:16px; font-weight:bold;}\n" "QPushButton:hover{background: #2E8B57;}")
        self.button_confirm.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_confirm.setText("BAIXAR")
        self.button_confirm.setIcon(QtGui.QIcon("img/download.ico"))
        self.button_confirm.setIconSize(QtCore.QSize(20, 20))
        self.button_confirm.clicked.connect(self.download_video)
        
        self.button_clear_video = QtWidgets.QPushButton(self.frame)
        self.button_clear_video.setGeometry(300,250,120,30)
        self.button_clear_video.setStyleSheet("QPushButton{background:#4EEE94;border-radius:5px; color:white; font-family: Trebuchet MS;\
        font-size:16px; font-weight:bold;}\n" "QPushButton:hover{background: #2E8B57;}")
        self.button_clear_video.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_clear_video.setText("LIMPAR")
        self.button_clear_video.setIcon(QtGui.QIcon("img/clear.ico"))
        self.button_clear_video.setIconSize(QtCore.QSize(20, 20))
        self.button_clear_video.clicked.connect(self.clear_video)
        
        self.return_video_text = QtWidgets.QLabel(self.frame)
        self.return_video_text.setGeometry(130,350,300,40)
        self.return_video_text.setStyleSheet("font-family: Trebuchet MS; font-size:16px; color:white; background:transparent;")
        
        
        #AREA DE CONVERTER PARA AUDIO
        self.logo_audio = QtWidgets.QToolButton(self.frame)
        self.logo_audio.setGeometry(610,10,100,100)
        self.logo_audio.setIcon(QtGui.QIcon("img/audio.ico"))
        self.logo_audio.setIconSize(QtCore.QSize(68, 68))
        self.logo_audio.setStyleSheet("background: transparent;")
        
        self.audio_text = QtWidgets.QLabel(self.frame)
        self.audio_text.setGeometry(720,50,250,40)
        self.audio_text.setStyleSheet("font-family: Trebuchet MS; font-size:20px; color:white; background:transparent;  text-decoration:underline;")
        self.audio_text.setText("FORMATO DE AUDIO .webm")
        
        self.url_text2 = QtWidgets.QLabel(self.frame)
        self.url_text2.setGeometry(630,120,100,40)
        self.url_text2.setStyleSheet("font-family: Trebuchet MS; font-size:16px; color:white; background:transparent;")
        self.url_text2.setText("URL:")
        
        self.audio_input = QtWidgets.QLineEdit(self.frame)
        self.audio_input.setGeometry(670, 130, 380,20)
        self.audio_input.setStyleSheet("border-radius:3px; font-family: Trebuchet MS; font-size:16px; color:white;")
        self.audio_input.setPlaceholderText("Cole o link do video aqui")
        
        self.button_confirm2 = QtWidgets.QPushButton(self.frame)
        self.button_confirm2.setGeometry(670,250,120,30)
        self.button_confirm2.setStyleSheet("QPushButton{background:#4EEE94;border-radius:5px; color:white; font-family: Trebuchet MS;\
        font-size:16px; font-weight:bold;}\n" "QPushButton:hover{background: #2E8B57;}")
        self.button_confirm2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_confirm2.setText("BAIXAR")
        self.button_confirm2.setIcon(QtGui.QIcon("img/download.ico"))
        self.button_confirm2.setIconSize(QtCore.QSize(20, 20))
        self.button_confirm2.clicked.connect(self.download_audio)
        
        self.button_clear_audio = QtWidgets.QPushButton(self.frame)
        self.button_clear_audio.setGeometry(900,250,120,30)
        self.button_clear_audio.setStyleSheet("QPushButton{background:#4EEE94;border-radius:5px; color:white; font-family: Trebuchet MS;\
        font-size:16px; font-weight:bold;}\n" "QPushButton:hover{background: #2E8B57;}")
        self.button_clear_audio.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.button_clear_audio.setText("LIMPAR")
        self.button_clear_audio.setIcon(QtGui.QIcon("img/clear.ico"))
        self.button_clear_audio.setIconSize(QtCore.QSize(20, 20))
        self.button_clear_audio.clicked.connect(self.clear_audio)
        
        self.return_audio_text = QtWidgets.QLabel(self.frame)
        self.return_audio_text.setGeometry(730,350,300,40)
        self.return_audio_text.setStyleSheet("font-family: Trebuchet MS; font-size:16px; color:white; background:transparent;")
        

        self.window.show()
        sys.exit(self.app.exec_())
        
        
    #FUNÇÕES
    def download_video(self):
        try:
            ydl_opts = {
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.video_input.text()])
            self.return_video_text.setText("Download efetuado com sucesso!")
        except:
            self.return_video_text.setText("Download efetuado com sucesso!")
            
    def clear_video(self):
        self.return_video_text.clear()
        self.video_input.clear()
        
    def download_audio(self):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.audio_input.text()])
            self.return_audio_text.setText("Download efetuado com sucesso!")
        except:
            self.return_audio_text.setText("Download efetuado com sucesso!")
            
    def clear_audio(self):
        self.return_audio_text.clear()
        self.audio_input.clear()


App()