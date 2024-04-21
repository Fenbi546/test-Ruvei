# напиши здесь код основного приложения и первого экрана
class MainWin (QWidget):
    def _init__(self):
        super().-_init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()