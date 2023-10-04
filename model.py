from pytube import YouTube
import threading

class Model:
    # link test: https://www.youtube.com/watch?v=BHrVmYr9qbg
    def __init__(self, controller):
        self.controller = controller
        self.semaphore = threading.Semaphore()
        self.title = ''
    
    def get_title(self):
        return self.title
    
    def select_video(self, url):
        self.video = YouTube(url, on_progress_callback=self._on_progress)
        self.title = self.video.title
    
    def _download_video(self, path):
        self.video_stream = self.video.streams.filter(file_extension='mp4').first()
        self.video_stream.download(path, skip_existing=False)
        
    def thread_download(self, path):
        download = threading.Thread(target=self._download_video, args=(path))
        download.start()
        
    def _on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        downloaded = total_size - bytes_remaining
        percentage = (downloaded / total_size) * 100
        with self.semaphore:
            self.controller.update_bar(percentage)