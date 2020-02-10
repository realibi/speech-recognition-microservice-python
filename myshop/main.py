from bottle import route, run, template, request
import speech_recognition as sr
import uuid
import os


@route('/api/index/')
def index():
    return template('index.html')


@route('/api/upload/', method='post')
def upload():
    
    someFile = request.files.get('upload')
    save_path = str(uuid.uuid4()) + '.wav'
    someFile.save(save_path)

    recognizer = sr.Recognizer()

    audioData = sr.AudioFile(save_path)
    with audioData as source:
        audio = recognizer.record(source)

    recognized_text = recognizer.recognize_google(audio, language='ru')
    os.remove(save_path)

    return recognized_text


run(host='localhost', port=1234)