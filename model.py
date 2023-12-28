from pytube import YouTube
import moviepy.editor as mp
import threading
import sys
import re
import os

class Model:
    # link test: https://www.youtube.com/watch?v=BHrVmYr9qbg / https://www.youtube.com/watch?v=pZaagWrjEzg
    def __init__(self, controller):
        self.controller = controller
        self.semaphore = threading.Semaphore()
        self.title = ''
        self.music_type = [False, '']
    
    def get_title(self):
        return self.title
    
    def select_video(self, url):
        self.video = YouTube(url, on_progress_callback=self._on_progress, on_complete_callback=self._on_complete)
        self.title = self.video.title
    
    def _download_video(self, path):
        self.video_stream = self.video.streams.filter(file_extension='mp4').first()
        self.video_stream.download(path, skip_existing=False)
        
    def thread_download_video(self, path):
        download = threading.Thread(target=self._download_video, args=(path))
        download.start()
                
    def thread_download_music(self, path):
        download = threading.Thread(target=self._download_video, args=(path))
        download.start()
        self.music_type = [True, path]
        
    def _on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        downloaded = total_size - bytes_remaining
        percentage = (downloaded / total_size) * 100
        with self.semaphore:
            self.controller.update_bar(percentage)
            
    def _on_complete(self, stream, chunk):
        if self.music_type[0]:
            path = self.music_type[1]
            for file in os.listdir(path):
                if re.search('mp4', file) and file.split(".")[0] == self.get_title():
                    with open("output.txt", "wt") as output:
                        sys.stdout = output
                        sys.stderr = output
                        mp4_path = os.path.join(path, file)
                        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
                        self.controller.converting(True)
                        new_file = mp.AudioFileClip(mp4_path)
                        new_file.write_audiofile(mp3_path)
                    os.remove(file)
                    os.remove('output.txt')
                    self.controller.converting(False)