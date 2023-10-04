from model import Model
from view import View

class Controller:
    def __init__(self):
        self.view = View(self)
        self.model = Model(self)
    
    def main(self):
        self.view.main()
        
    def download_video(self):
        self.model.select_video(self.view.URL.get())
        if self.model.get_title() != '':
            self.view.Video_name.set(f'{self.model.get_title()}')
            self.model.thread_download_video('.')
            self.view.download_feedback(True)
            
    def download_audio(self):
        self.model.select_video(self.view.URL.get())
        if self.model.get_title() != '':
            self.view.Video_name.set(f'{self.model.get_title()}')
            self.model.thread_download_music('.')
            self.view.download_feedback(True)
    
    def update_bar(self, percent): 
        self.view.progress_update(percent)
        
    def converting(self, is_converting):
        if is_converting:
            self.view.status_feedback('Convertendo...')
        else:
            self.view.status_feedback('Download completo!', '#5b5')
            self.view.btn0.configure(state='normal')
            self.view.btn1.configure(state='normal')
            
        
if __name__ == "__main__":
    controller = Controller()
    controller.main()