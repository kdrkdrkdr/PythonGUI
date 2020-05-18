
pyside2-uic.exe .\main_ui.ui -o .\ani24ui.py



echo if __name__ == "__main__": >> ani24ui.py
echo     import sys >> ani24ui.py
echo     app = QApplication(sys.argv) >> ani24ui.py
echo     form = QMainWindow() >> ani24ui.py
echo     ui = Ui_MainWindow() >> ani24ui.py
echo     ui.setupUi(form) >> ani24ui.py
echo     form.show() >> ani24ui.py
echo     sys.exit(app.exec_()) >> ani24ui.py
