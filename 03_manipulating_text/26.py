
# *ex5 - Create a program that reads a sentence from the keyboard and shows:
# *   How many times the letter "A" appears
# *   In which position it first appears
# *   In which position it appears last

sentence = str(input('Enter a sentence: ')).upper().strip()

print(f'\nThe letter A appears  {sentence.count("A")} times in the sentence.')
print(f'The first letter A appeared at position {sentence.find("A")+1}')
print(f'The last letter A appeared at position {sentence.rfind("A")+1}')
