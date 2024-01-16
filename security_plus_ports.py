import tkinter as tk
from tkinter import messagebox
import random

# Define the quiz questions, choices, and answers
quiz = {
    "What port is commonly used for HTTP?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for HTTPS?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 3389"],
        "answer": "C"
    },
    "What port is commonly used for SSH?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 3389"],
        "answer": "A"
    },
    "What port is commonly used for RDP?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 3389"],
        "answer": "D"
    },
    "What port is commonly used for SMTP?": {
        "choices": ["A. 25", "B. 80", "C. 443", "D. 3389"],
        "answer": "A"
    },
    "What port is commonly used for DNS?": {
        "choices": ["A. 22", "B. 80", "C. 53", "D. 3389"],
        "answer": "C"
    },
    "What port is commonly used for FTP control?": {
        "choices": ["A. 22", "B. 21", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for FTP data transfer?": {
        "choices": ["A. 20", "B. 80", "C. 443", "D. 3389"],
        "answer": "A"
    },
    "What port is commonly used for Telnet?": {
        "choices": ["A. 23", "B. 80", "C. 443", "D. 3389"],
        "answer": "A"
    },
    "What port is commonly used for POP3?": {
        "choices": ["A. 22", "B. 110", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for IMAP?": {
        "choices": ["A. 22", "B. 80", "C. 143", "D. 3389"],
        "answer": "C"
    },
    "What port is commonly used for LDAP?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 389"],
        "answer": "D"
    },
    "What port is commonly used for DHCP?": {
        "choices": ["A. 67 and 68", "B. 80", "C. 443", "D. 3389"],
        "answer": "A"
    },
    "What port is commonly used for TACACS+?": {
        "choices": ["A. 22", "B. 49", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for Kerberos?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 88"],
        "answer": "D"
    },
    "What port is commonly used for SNMP?": {
        "choices": ["A. 22", "B. 161 and 162", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for LDAPS?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 636"],
        "answer": "D"
    },
    "What port is commonly used for FTPS?": {
        "choices": ["A. 22", "B. 990", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for IMAPS?": {
        "choices": ["A. 22", "B. 80", "C. 993", "D. 3389"],
        "answer": "C"
    },
    "What port is commonly used for POP3S?": {
        "choices": ["A. 22", "B. 995", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for RADIUS?": {
        "choices": ["A. 22", "B. 1812 and 1813", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for Diameter (RADIUS)?": {
        "choices": ["A. 22", "B. 80", "C. 3868", "D. 3389"],
        "answer": "C"
    },
    "What port is commonly used for SRTP?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 5004"],
        "answer": "D"
    },
    "What port is commonly used for L2TP?": {
        "choices": ["A. 22", "B. 1701", "C. 443", "D. 3389"],
        "answer": "B"
    },
    "What port is commonly used for PPTP?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. 1723"],
        "answer": "D"
    },
    "What port is commonly used for PPP?": {
        "choices": ["A. 22", "B. 80", "C. 443", "D. N/A"],
        "answer": "D"
    }
}

# Get a list of questions and shuffle them to ensure randomness
questions = list(quiz.keys())
random.shuffle(questions)

def check_answer(question, user_answer, window):
    if user_answer.get() == quiz[question]["answer"]:
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Sorry, the correct answer is {quiz[question]['answer']}.")

    window.destroy()
    if questions:  # Check if there are still questions left in the quiz
        start_quiz()

def start_quiz():
    if questions:  # Check if there are still questions left in the quiz
        question = questions.pop()  # Pop a question from the quiz

        # Create a new window for the question
        window = tk.Toplevel(root)
        window.title(question)

        # Add the question to the window
        question_label = tk.Label(window, text=question)
        question_label.pack()

        # Add the choices to the window
        user_answer = tk.StringVar()
        for choice in quiz[question]["choices"]:
            rb = tk.Radiobutton(window, text=choice, variable=user_answer, value=choice[0])
            rb.pack()

        # Add a submit button to the window
        submit_button = tk.Button(window, text="Submit", command=lambda: check_answer(question, user_answer, window))
        submit_button.pack()

# Create the root window
root = tk.Tk()
root.title("Quiz")

# Add a start button to the root window
start_button = tk.Button(root, text="Start Quiz", command=start_quiz)
start_button.pack()

# Start the tkinter event loop
root.mainloop()
