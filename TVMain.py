from TVLogic import *

def main():
    application = QApplication([])
    window = Television()
    window.setGeometry(0, 0, 400, 400)
    window.show()
    application.exec()

if __name__ == '__main__':
    main()