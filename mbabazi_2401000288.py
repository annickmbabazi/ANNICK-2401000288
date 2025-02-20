# -*- coding: utf-8 -*-
"""mbabazi 2401000288.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1YVL5wrlfELtsQhhzb1P1NoYLsTrtgskl
"""

offensive_words = [
    "inyenzi", "cockroaches", "kill", "exterminate", "destroy",
    "traitors", "snakes", "rats", "hutu power", "tutsi",
    "ethnic cleansing", "wipe out", "enemy", "revenge",
    "impurity", "traitors", "infiltrators", "parasites"
]
# Function to detect hate speech
def detect_hate_speech(text):
    detected_words = [word for word in offensive_words if word in text.lower()]
    return detected_words

# Example usage
text = "He said very harsh things so much so that the hearts of some people were hurt. He woke up the Hutu, saying that if they do not cut the necks of the Tutsi it will be the Tutsi who will cut theirs. The speech he said made a lot of people worried because he clearly said to send the Tutsis along the Nyabarongo as a shortcut back to their home in Ethiopia.."
hate_words = detect_hate_speech(text)
if hate_words:
    print("Hate speech detected! Offensive words:", hate_words)
else:
    print("No hate speech detected.")