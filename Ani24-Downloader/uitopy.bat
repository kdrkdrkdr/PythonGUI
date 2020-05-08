
pyside2-uic.exe .\ui.ui -o .\ui.py



echo if __name__ == "__main__": >> ui.py
echo     import sys >> ui.py
echo     app = QApplication(sys.argv) >> ui.py
echo     form = QMainWindow() >> ui.py
echo     ui = Ui_MainWindow() >> ui.py
echo     ui.setupUi(form) >> ui.py
echo     form.show() >> ui.py
echo     sys.exit(app.exec_()) >> ui.py
