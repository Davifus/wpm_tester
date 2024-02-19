from PyQt5 import QtCore, QtGui, QtWidgets
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("Georgia")
        MainWindow.setFont(font)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.promptTitle = QtWidgets.QLabel(self.centralwidget)
        self.promptTitle.setGeometry(QtCore.QRect(140, 30, 511, 81))
        
        font = QtGui.QFont()
        font.setFamily("Georgia")
        font.setPointSize(36)
        
        self.promptTitle.setFont(font)
        self.promptTitle.setObjectName("promptTitle")

        self.prompt = ""
        #start button
        self.loadPrompt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.load())
        self.loadPrompt.setGeometry(QtCore.QRect(330, 230, 91, 31))
        self.loadPrompt.setObjectName("loadPrompt")
        
        #reset button 
        self.redoPrompt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.reset())
        self.redoPrompt.setGeometry(QtCore.QRect(430, 230, 91, 31))
        self.redoPrompt.setObjectName("redoPrompt")
        
        #new button 
        self.newPrompt = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.new())
        self.newPrompt.setGeometry(QtCore.QRect(230, 230, 91, 31))
        self.newPrompt.setObjectName("redoPrompt")
        
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 280, 531, 201))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.textChanged.connect(self.checkUserInput)
        
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 100, 531, 111))
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setPlaceholderText("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setHtml("")  
        
        
        self.start_time = None
        self.total_words_typed = 0
        self.currentWPM = QtWidgets.QLabel(self.centralwidget)
        self.currentWPM.setGeometry(QtCore.QRect(210, 510, 120, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentWPM.setFont(font)
        self.currentWPM.setObjectName("currentWPM")
        self.textEdit.textChanged.connect(self.updateWPM)
        
        
        self.currentAcc = QtWidgets.QLabel(self.centralwidget)
        self.currentAcc.setGeometry(QtCore.QRect(320, 510, 160, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentAcc.setFont(font)
        self.currentAcc.setObjectName("currentAcc")
        self.textEdit.textChanged.connect(self.updateAccuracy)
        
        #timer
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.showTime)
        self.count = 0
        self.flag = False
        self.currentTimer = QtWidgets.QLabel(self.centralwidget)
        self.currentTimer.setGeometry(QtCore.QRect(480, 510, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.currentTimer.setFont(font)
        self.currentTimer.setObjectName("currentTimer")
        
        
        #highlight
        self.textEdit.textChanged.connect(self.checkUserInput)  # Connect textChanged signal to checkUserInput

        # Set initial style for prompt textEdit_2
        self.textEdit_2.setStyleSheet(
            "background-color: lightgray; color: gray;"  # Style to highlight prompt text
        )
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
    
    
    #calculates the time
    def showTime(self):
        if self.flag:
            self.count += 1
            text = str(self.count // 10)
        
            self.currentTimer.setText(f"Timer: {text}")
            
    #enable the timer to start
    def Start(self):
        self.flag = True
        self.timer.start(100)
    
    #reset timer,acc, and wpm
    def reset(self):
        self.timer.stop()
        self.count = 0
        self.flag = False
        self.start_time = None
        self.textEdit.clear()
        self.currentWPM.setText("WPM: 0")
        self.currentAcc.setText("Accuracy: 100.00%")
        self.currentTimer.setText("Timer: 0")
        self.textEdit.setReadOnly(False)
        
    #reset timer,acc, and wpm
    def new(self):
        self.timer.stop()
        self.count = 0
        self.flag = False
        self.start_time = None
        self.textEdit.clear()
        self.currentWPM.setText("WPM: 0")
        self.currentAcc.setText("Accuracy: 100.00%")
        self.currentTimer.setText("Timer: 0")
        self.textEdit.setReadOnly(False)
        self.pickPrompt()
        self.textEdit_2.setText(self.prompt)
        

    #temp prompt & eventually use database
    def pickPrompt(self):
        prompts = [
        "My mama always said life was like a box of chocolates. You never know what you're gonna get.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "The way to get started is to quit talking and begin doing.",
        ]
        
        self.prompt = random.choice(prompts)
        
    
    
    #stop timer based of completed attempt
    def checkUserInput(self):
        length = len(self.prompt)
        
        # Start the timer when the user types the first character
        if len(self.textEdit.toPlainText()) == 1:
            self.Start()
        
        # Stop the timer when the user completes typing the prompt
        if len(self.textEdit.toPlainText()) == length:
            self.timer.stop()
            self.textEdit.setReadOnly(True)
        self.updatePromptInTextEdit2()
        
    
    def updatePromptInTextEdit2(self):
        user_text = self.textEdit.toPlainText()
        prompt_text = self.prompt[:len(user_text)]  # Extract the portion of the prompt that matches user input

        # Highlight the prompt text by setting different styles
        prompt_html = f'<span style="color: gray;">{prompt_text}</span>'  # Apply gray color to prompt text
        remaining_html = self.prompt[len(user_text):]  # Get the remaining unprompted text

        # Combine the highlighted prompt text and remaining unprompted text
        combined_html = prompt_html + remaining_html
        self.textEdit_2.setHtml(combined_html)

            
    #accuracy of user input
    def updateAccuracy(self):
        user_text = self.textEdit.toPlainText()
        
        incorrect_characters = sum(1 for prompt_char, user_char in zip(self.prompt, user_text) if prompt_char != user_char)
        accuracy = 100 - (incorrect_characters / len(self.prompt) * 100)

        self.currentAcc.setText(f"Accuracy: {accuracy:.2f}%")
        
    #calculate the word per minute
    def updateWPM(self):
        text = self.textEdit.toPlainText()
        words_typed = len(text.split())
        
        # Only calculate WPM if there's some text and the timer is running
        if words_typed > 0 and self.flag:
            if not self.start_time:
                self.start_time = QtCore.QTime.currentTime()
            else:
                elapsed_time = self.start_time.elapsed() / 1000 / 60  # Convert milliseconds to minutes
                wpm = (words_typed / elapsed_time) if elapsed_time > 0 else 0  # Calculate WPM only if time elapsed is non-zero
                self.currentWPM.setText(f"WPM: {wpm:.2f}")

    #populating the empty box with a prompt
    def load(self): #future pull from a database of paragraph and sentences
        if self.textEdit_2.toPlainText().strip() == "":
            self.pickPrompt()
            self.textEdit_2.setText(self.prompt)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "WPM Tester"))
        self.promptTitle.setText(_translate("MainWindow", "TEST YOUR FINGERS"))
        self.loadPrompt.setText(_translate("MainWindow", "Start")) 
        self.redoPrompt.setText(_translate("MainWindow", "Reset"))
        self.newPrompt.setText(_translate("MainWindow", "New"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Type here"))
        self.currentWPM.setText(_translate("MainWindow", f"WPM: 0"))
        self.currentAcc.setText(_translate("MainWindow", "Accuracy: 100.00%"))
        self.currentTimer.setText(_translate("MainWindow", f"Timer: {self.count}"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
    
    
    
#######features#######
""" 
DIFFICULT
- separate tab that shows the last 10 attempts 
- highlights red when you mispelled/extra space & etc
- keyboard picture that highlight depending where you press on the key
- connect to db for prompt
- convert this into a website?

DONE
- Timer starts when you press start
- Prompt populates when you press start
- Accuracy is tracked during typing
- Timer stop when you finished typing
- a number indicator that shows current wpm
- redo button to retry the same prompt
    - reset wpm,acc,timer, and user input box and make it read only until reset
- reset button to get a new prompt
    - reset prompt to new prompt, wpm,acc,timer, and user input box
"""


#IMPORTANT DONT DELETE USED FOR CONVERTING PYQT INTO PY FILE TO EDIT
#pyuic5 -x WPM.ui -o WPM.py
