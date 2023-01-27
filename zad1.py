# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = 'котлеты абвгдеёж иерусалим, где  жаба ежабв ?'

def deleteWord(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return ' '.join(text)

print(deleteWord(text))