import pyttsx3, PyPDF2

pdfreader = PyPDF2.PdfReader(open('hello.pdf', 'rb'))

speaker = pyttsx3.init()

for page_num in range(len(pdfreader.pages)):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'hello.mp3')
speaker.runAndWait()

speaker.stop()

if __name__ == '__main__':
    pass