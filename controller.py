from model import Model
from view import View

class Controller:
    def __init__(self):
        self.view = View()
        self.model = Model()
    
    def main(self):
        self.view.main()

if __name__ == "__main__":
    controller = Controller()
    controller.main()