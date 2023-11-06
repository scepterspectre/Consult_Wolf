"Final Code 1/5"

from PyQt6.QtWidgets import QApplication, QWidget, QFrame, QPushButton, QTextEdit, QLabel, QFileDialog, \
    QVBoxLayout, QHBoxLayout, QComboBox, QSizePolicy
from PyQt6.QtGui import QPixmap, QFont, QIcon, QColor, QPalette
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve

import sys
import ui

# Create the main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Consult Wolf')
window.setGeometry(100, 100, 800, 600)

# Create the introduction screen
intro_screen = QWidget()
intro_screen.setWindowTitle('Introduction')
intro_screen.setGeometry(100, 100, 800, 600)

intro_screen.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #95A3A6);")

# Create a label to display the introduction text
intro_label = QLabel(intro_screen)
intro_label.setText(
    "Consult Wolf is a game that helps you practice your consulting skills. \n In each round, you'll be presented with a problem and you'll have to come up with a solution. \n Are you ready to give it a try?")
intro_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

# Create a button to continue to the main game
play_button = QPushButton("Play Now", intro_screen)
play_button.clicked.connect(intro_screen.close)  # Close the introduction screen when the button is clicked

# Create a vertical layout to hold the intro_label and play_button widgets
layout = QVBoxLayout()

# Add the intro_label and play_button widgets to the layout
layout.addWidget(intro_label)
layout.addWidget(play_button)

# Set the layout of the intro_screen to be the vertical layout
intro_screen.setLayout(layout)

# Set the spacing between the widgets to 20 pixels
layout.setSpacing(20)

# Show the introduction screen
intro_screen.show()

# Wait for the introduction screen to be closed before showing the main game screen
intro_screen.closeEvent = lambda _: window.show()

# Create a QLabel widget and set its size to the size of the window
label = QLabel(window)
label.setGeometry(0, 0, window.width(), window.height())

# Create the widgets
question_type_combo_box = QComboBox()
question_type_combo_box.addItems(
    ui.question_types.keys())  # Populate the combo box with the keys of the question_types dictionary
question_type_combo_box.setCurrentIndex(0)  # Set the current index to the index of the default value
question_type_combo_box.currentIndexChanged.connect(
    lambda: ui.generate_question(question_text, question_type_combo_box))  # Handle the currentIndexChanged signal

question_label = QLabel("Question:")
question_text = QTextEdit()
generate_button = QPushButton("Generate")
generate_button.clicked.connect(
    lambda: ui.generate_question(question_text, question_type_combo_box))  # Handle the clicked signal
thought_process_label = QLabel("Your Initial Thoughts:")
thought_process_text = QTextEdit()
grade_thought_process_button = QPushButton("Grade Thought Process")
grade_thought_process_button.clicked.connect(lambda: ui.grade_thought_process(thought_process_text.toPlainText(),
                                                                              follow_up_questions_text))  # Handle the clicked signal
follow_up_questions_label = QLabel("Our Follow-Up Questions:")
follow_up_questions_text = QTextEdit()
answer_label = QLabel("Your Answer:")
answer_text = QTextEdit()
grade_answer_button = QPushButton("Grade Answer")
grade_answer_button.clicked.connect(
    lambda: ui.grade_answer(answer_text.toPlainText(), feedback_text))  # Handle the clicked signal
feedback_label = QLabel("Our Final Feedback:")
feedback_text = QTextEdit()
reset_button = QPushButton("Reset")  # Create the reset button

# Set the font of the labels and buttons to a modern sans-serif font
font = QFont("Tahoma", 12)
question_label.setFont(font)
generate_button.setFont(font)
thought_process_label.setFont(font)
grade_thought_process_button.setFont(font)
follow_up_questions_label.setFont(font)
answer_label.setFont(font)
grade_answer_button.setFont(font)
feedback_label.setFont(font)
reset_button.setFont(font)  # Set the font of the reset button

# Set the text color of the labels and buttons to #5A5A5A
question_label.setStyleSheet("color: #FFFFFF")
generate_button.setStyleSheet("color: #FFFFFF")
thought_process_label.setStyleSheet("color: #FFFFFF")
grade_thought_process_button.setStyleSheet("color: #FFFFFF")
follow_up_questions_label.setStyleSheet("color: #FFFFFF")
answer_label.setStyleSheet("color: #FFFFFF")
grade_answer_button.setStyleSheet("color: #FFFFFF")
feedback_label.setStyleSheet("color: #FFFFFF")
reset_button.setStyleSheet("color: #FFFFFF")  # Set the text color of the reset button

question_card = QFrame()
question_card_layout = QVBoxLayout()

# Add the combo box and the question text widget to the layout
question_card_layout.addWidget(question_type_combo_box)
question_card_layout.addWidget(question_label)
question_card_layout.addWidget(question_text)
question_card_layout.addWidget(generate_button)
question_card.setLayout(question_card_layout)

# Create a vertical layout for the answer card
answer_card = QFrame()
answer_card_layout = QVBoxLayout()
answer_card_layout.addWidget(thought_process_label)
answer_card_layout.addWidget(thought_process_text)
answer_card_layout.addWidget(grade_thought_process_button)
answer_card_layout.addWidget(follow_up_questions_label)
answer_card_layout.addWidget(follow_up_questions_text)
answer_card_layout.addWidget(answer_label)
answer_card_layout.addWidget(answer_text)
answer_card_layout.addWidget(grade_answer_button)
answer_card_layout.addWidget(feedback_label)
answer_card_layout.addWidget(feedback_text)
answer_card_layout.addWidget(reset_button)
answer_card.setLayout(answer_card_layout)

# Create a horizontal layout for the main window
layout = QHBoxLayout()
layout.addWidget(question_card)
layout.addWidget(answer_card)
window.setLayout(layout)

reset_button.clicked.connect(
    lambda: ui.reset(question_text, thought_process_text, follow_up_questions_text, answer_text, feedback_text))

# Set the size policy of the combo box to fixed to prevent it from resizing when the window is resized
question_type_combo_box.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

# Set the size policy of the combo box to fixed to prevent it from resizing when the window is resized
question_type_combo_box.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
# Set the read-only property of the text boxes to true to prevent the user from manually editing them
question_text.setReadOnly(True)
thought_process_text.setReadOnly(False)
follow_up_questions_text.setReadOnly(True)
feedback_text.setReadOnly(True)

# Set the window background to a linear gradient that transitions
window.setStyleSheet("background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #95A3A6, stop: 1 #3E5559);")

# Run the main loop
sys.exit(app.exec())
