from model import Model
from view import View

class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model(self)
    
    def main(self):
        self.view.main()
        
    def download(self):
        self.model.select_video(self.view.URL.get())
        if self.model.get_title() != '':
            self.view.Video_name.set(f'{self.model.get_title()}')
            self.model.thread_download('.')
            self.view.download_feedback(True)
    
    def update_bar(self, percent): 
        self.view.progress_update(percent)
        
if __name__ == "__main__":
    controller = Controller()
    controller.main()