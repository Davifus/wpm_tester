import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        #Program Title
        self.setWindowTitle("WPM Tester")

        #layout
        self.setLayout(qtw.QVBoxLayout())

        #label
        myLabel = qtw.QLabel("Type Here")

        #label font changes
        myLabel.setFont(qtg.QFont('Georgia', 24))

        self.layout().addWidget(myLabel)

        #text box
        myEntry = qtw.QTextEdit(self, 
                                lineWrapMode = qtw.QTextEdit.FixedColumnWidth, 
                                lineWrapColumnOrWidth = 35, placeholderText = "Type Here" 
                                )


        myEntry.setObjectName('text_box')
        """ myEntry.setText('') #this set what auto fill in textbox """
        self.layout().addWidget(myEntry)
        
        #button
        myButton = qtw.QPushButton("Start", clicked = lambda: populate())
        self.layout().addWidget(myButton)

        def populate(): #this will change the text into a paragraph/sentence
            myLabel.setText(f'This is sentence you must copy to the text box')

        self.show()



app = qtw.QApplication([])
mw = MainWindow()

app.exec_()


#######features#######
""" 
EASY
- Timer for when you press start
- a number indicator that shows current wpm
- separate tab that shows the last 10 attempts 
- when you finish it a pop will show of the stats 

DIFFICULT
- redo button to retry the same prompt
- reset button to get a new prompt
- highlights red when you mispelled/extra space & etc
- keyboard picture that highlight depending where you press on the key
- convert this into a website?
"""
#IMPORTANT DONT DELETE USED FOR CONVERTING PYQT INTO PY FILE TO EDIT
#pyuic5 -x WPM.ui -o WPM.py