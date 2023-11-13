from PyQt6.QtWidgets import QMainWindow, QTextEdit,QLineEdit, QPushButton, QApplication
import sys

from backend import Chatbot

import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.my_chatbot = Chatbot()  # This should be placed in class level

        self.setMinimumSize(700, 500)

        # Add chat area widget
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # Add the input field widget

        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)

        self.input_field.returnPressed.connect(self.send_message) # An improvement. Msg is sent when a enter key is pressed as an alternative to send button
        # This will send message after the enter key is pressed, not before. That's why send_message function is used here without parenthesis-meaning that it should not be excecuted/called immediately.
        # Add the button

        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)

        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        # my_chatbot = Chatbot() # This should be placed in class level
        user_input = self.input_field.text().strip() # double check text()
        print(user_input)
        self.chat_area.append(f"<p style='color:#333333>Question: {user_input}</p>")
        self.input_field.clear()

        # THE FOLLOWING TWO LINES SHOULD BE PLACED IN A THREADING TO GET SOME TIME BREAK BETWEEN QUESTION AND ANSWER:
        # response = self.my_chatbot.get_response(user_input)
        # self.chat_area.append(f"<p style='color:#333333, background-color: #E9E9E9'>Response: {response}</P>")

        # THREADING:-
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.my_chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333, background-color: #E9E9E9'>Response: {response}</P>")




app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())