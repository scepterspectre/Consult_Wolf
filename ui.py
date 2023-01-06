import openai
from apscheduler.schedulers.blocking import BlockingScheduler
from PyQt6.QtWidgets import QApplication, QComboBox
import sys
import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
# Extract the OpenAI API key and the MongoDB connection string from the configuration file
openai.api_key = os.getenv("openai_api_key")

app = QApplication(sys.argv)

# Create a dictionary mapping question types to prompts
question_types = {
    "Random": "Randomly select a year only between 1990 and 2022. Select a specific large multi-national corporation that faced a pressing issue in that time period and display a specific scenario with context. Then, present a specific problem for skilled consultants to solve.",
    "Financial": "Select a specific company in the financial sector and a specific year between 1990 and 2022. Describe a scenario in which the company is facing a pressing financial issue and present a problem for skilled consultants to solve.",
    "Marketing": "Select a specific company in the consumer goods sector and a specific year between 1990 and 2022. Describe a scenario in which the company is facing a pressing marketing issue and present a problem for skilled consultants to solve.",
    "Operations": "Select a specific company in the manufacturing sector and a specific year between 1990 and 2022. Describe a scenario in which the company is facing a pressing operations issue and present a problem for skilled consultants to solve.",
    "Human Resources": "Select a specific company in any sector and a specific year between 1990 and 2022. Describe a scenario in which the company is facing a pressing human resources issue and present a problem for skilled consultants to solve."
}


def generate_question(question_text_widget, question_type_combo_box):
    # Get the selected question type
    question_type = question_type_combo_box.currentText()

    # Use the appropriate prompt for the selected question type
    prompt = question_types[question_type]

    # Use the ChatGPT API to generate a question based on the prompt and display it in the given widget
    try:
        completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1,
                                               stop=None, temperature=0.5)
    except openai.api_services.api_service.ApiException:
        print("Error: OpenAI API request failed. Please check your API key and try again.")
        exit()
    message = completions.choices[0].text
    question_text_widget.setText(message)


def grade_thought_process(thought_process, follow_up_questions_text_widget):
    # Check if the thought process is less than seven words
    if len(thought_process.split()) < 7:
        follow_up_questions_text_widget.setText("Please elaborate ")
    else:
        # Use the ChatGPT API to generate follow-up questions and display them in the given widget
        prompt = "Ask three follow-up questions based on the user's thought process stated previously and suggest more optimal apporaches to this problem: " + thought_process
        try:
            completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1,
                                                   stop=None, temperature=0.5)
        except openai.api_services.api_service.ApiException:
            print("Error: OpenAI API request failed. Please check your API key and try again.")
            exit()
        follow_up_questions = completions.choices[0].text
        follow_up_questions_text_widget.setText(follow_up_questions)


def grade_answer(final_answer, feedback_text_widget):
    # Check if the final answer is less than seven words
    if len(final_answer.split()) < 7:
        feedback_text_widget.setText("Please elaborate ")
    else:
        # Use the ChatGPT API to generate feedback and display it in the given widget
        prompt = "Analyze the user's final answer in terms of real life plausibilty and the overall pros and cons of their solution: " + final_answer
        try:
            completions = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=1024, n=1,
                                                   stop=None, temperature=0.5)
        except openai.api_services.api_service.ApiException:
            print("Error: OpenAI API request failed. Please check your API key and try again.")
            exit()
        feedback = completions.choices[0].text
        feedback_text_widget.setText(feedback)


def reset(question_text, thought_process_text, follow_up_questions_text, answer_text, feedback_text):
    question_text.setText('')
    thought_process_text.setText('')
    follow_up_questions_text.setText('')
    answer_text.setText('')
    feedback_text.setText('')