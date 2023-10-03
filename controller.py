from model import Model
from view import View

class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model(self)
    
    def main(self):
        self.view.main()
        
    def download(self):
        self.model.thread_download(self.view.URL.get(), '.')
        if self.model.title != '':
            self.view.Video_name.set(self.model.title)
            self.view.download_feedback(True)
    
    def update_bar(self, text, percent): 
        self.view.progress_update(text, percent)
        
if __name__ == "__main__":
    controller = Controller()
    controller.main()