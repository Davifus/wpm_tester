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
- separate tab that shows the last 10 attempts 
- reset button to get a new prompt
    - reset prompt to new prompt, wpm,acc,timer, and user input box

DIFFICULT
- highlights red when you mispelled/extra space & etc
- keyboard picture that highlight depending where you press on the key
- convert this into a website?

DONE
- Timer starts when you press start
- Prompt populates when you press start
- Accuracy is tracked during typing
- Timer stop when you finished typing
- a number indicator that shows current wpm
- redo button to retry the same prompt
    - reset wpm,acc,timer, and user input box and make it read only until reset
"""


#IMPORTANT DONT DELETE USED FOR CONVERTING PYQT INTO PY FILE TO EDIT
#pyuic5 -x WPM.ui -o WPM.py