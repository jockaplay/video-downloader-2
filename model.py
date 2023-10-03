from pytube import YouTube
import threading
import time

class Model:
    
    def __init__(self, controller):
        self.controller = controller
        self.semaphore = threading.Semaphore()
        self.title = ''
        self.video_stream = None
    
    def get_title(self):
        return self.title
    
    def _download_video(self, url, path):
        self.video = YouTube(url, on_progress_callback=self.on_progress)
        self.video_stream = self.video.streams.filter(file_extension='mp4').first()
        self.video_stream.download(path)
        
    def thread_download(self, url, path):
        download = threading.Thread(target=self._download_video, args=(url, path))
        download.start()
        self.title = self.video.title
        
    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        downloaded = total_size - bytes_remaining
        percentage = (downloaded / total_size) * 100
        with self.semaphore:
            self.controller.update_bar(str(int(percentage)), percentage)