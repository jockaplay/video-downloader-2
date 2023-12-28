import customtkinter as ctk
import tkinter as tk

class View(ctk.CTk):
    
    PAD = 20
    
    def __init__(self, controller):
        super().__init__()
        self.title('Video Downloader')
        self.controller = controller

        self.URL = tk.StringVar()
        self.Video_name = tk.StringVar()
        
        self._main_frame()
        self._entry_frame()
        self._status_frame()
        self._buttons_frame()
        self._progressbar_frame()
        
        self._config_window()
       
    def main(self):
        self.mainloop()
     
    def _main_frame(self):
        self.frame_1 = ctk.CTkFrame(self, fg_color='#fff')
        self.frame_1.pack(expand=True, fill='both')
        
    def _entry_frame(self):
        self.frame_2 = ctk.CTkFrame(self.frame_1, fg_color='#fff')
        self.frame_2.pack(fill='x', padx=self.PAD, pady=self.PAD)
        self._make_entry()
        
    def _make_entry(self):
        self.lbl = ctk.CTkLabel(self.frame_2, text='URL do video: ', fg_color='#fff', text_color="#101010")
        self.lbl.pack(side='left')
        self.entry = ctk.CTkEntry(self.frame_2, placeholder_text="Insira o link do video aqui...",
                                  placeholder_text_color="#a5a5a5", fg_color='#fff', text_color="#101010")
        self.entry.pack(expand=True, fill='x', side='left')
        self.folder = ctk.CTkButton(self.frame_2, text="local", state='disabled')
        self.folder.pack(side='left')
    
    def _status_frame(self):
        self.status_frame = ctk.CTkFrame(self.frame_1, fg_color='#fff')
        self.status_frame.pack(fill='both', padx=self.PAD, expand=True)
        self._status()

    def _status(self):
        self.lbl_status = ctk.CTkLabel(self.status_frame, text=f'', fg_color='#fff')
        self.lbl_status.pack(side='top')
    
    def _progressbar_frame(self):
        self.frame_3 = ctk.CTkFrame(self.frame_1, fg_color='#fff')
        self.frame_3.pack(fill='x', padx=self.PAD)
        
    def _make_progress_bar(self):
        self.pb = ctk.CTkProgressBar(self.frame_3, mode='determinate', bg_color='#fff')
        self.pb.set(0)
        self.pb.pack(fill='x', side='bottom')
        self.dlLabel = ctk.CTkLabel(self.frame_3, text="Fazendo o download... 1%", text_color='#101010')
        self.dlLabel.pack(side='bottom')
    
    def _buttons_frame(self):
        self.frame_button = ctk.CTkFrame(self.frame_1, fg_color='#fff')
        self.frame_button.pack(fill='x', padx=self.PAD, pady=self.PAD, side='bottom')
        self._make_buttons()
        
    def _make_buttons(self):
        self.btn0 = ctk.CTkButton(self.frame_button, text='Video', bg_color='#fff',
                                  command=self._download_video)
        self.btn0.pack(fill='x', pady=self.PAD//4)
        self.btn1 = ctk.CTkButton(self.frame_button, text='Música', bg_color='#fff',
                                  command=self._download_music)
        self.btn1.pack(fill='x')
    
    def _download_video(self):
        self.URL.set(self.entry.get())
        self.controller.download_video()
        
    def _download_music(self):
        self.URL.set(self.entry.get())
        self.controller.download_audio()       
        
    def download_feedback(self, validate: bool):
        if validate:
            self.btn0.configure(state='disabled')
            self.btn1.configure(state='disabled')
            self.Video_name.set(f'{self.Video_name.get()}')
            self.status_feedback(self.Video_name.get())
            self._make_progress_bar()
        else:
            self.status_feedback('Link Inválido.')
        
    def status_feedback(self, message:str, color:str='#000'):
        self.lbl_status.configure(text=f'{message}', text_color=color)
        
    def progress_update(self, percent: float):
        self.pb.set(percent/100)
        self.status_feedback(f'{self.Video_name.get()}')
        self.dlLabel.configure(text=f'Fazendo o download... {str(int(percent))}%')
        if (percent/100) == 1:
            self._close_progress_bar()
            self.status_feedback('Download completo.', '#5b5')
                
    def _close_progress_bar(self):
        self.pb.destroy()
        self.dlLabel.destroy()
    
    def _config_window(self):
        width = 560
        height = 320
        self.geometry(f'{width}x{height}')
        self.update()
        
        width = self.winfo_width()
        height = self.winfo_height()
        
        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight() - height) // 2
        
        self.geometry(f'{width}x{height}+{x_offset}+{y_offset}')
        self.resizable(False, False)