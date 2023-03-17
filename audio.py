# import pyttsx3,PyPDF2

# #Replace file.pdf' with path to your PDF file (i.e. /Desktop/Contracts/file.pdf)

# pdfreader = PyPDF2.PdfReader(open('E:\AES.pdf','rb'))
# reader = pyttsx3.init()

# for page in range(pdfreader.numPages):   

#     text = pdfreader.getPage(page).extractText()

#     legible_text = text.strip().replace('\n',' ')

#     print(legible_text)

#     reader.say(legible_text)

#     reader.save_to_file(legible_text,'file.mp3')

#     reader.runAndWait()

# reader.stop()

# Fetch Everyday News
# pip install newspaper3k
# Grammer Fixer
# pip install language-tool-python
import language_tool_python as Grammer
fixer = Grammer.LanguageTool('en-US')
text=input ('Enter the text')
scan = fixer.check(text)
for result in scan:
    print("result:",result)
    print("Correction: " + fixer.correct(text))
    print("")