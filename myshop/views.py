from django.shortcuts import render
from django.http import HttpResponse
import os
from .forms import UploadFileForm
import uuid
from django.core.files.storage import FileSystemStorage
import speech_recognition as sr


def index(request):
    return render(request, 'index.html')

def recognize(request):
    someFile = request.FILES['upload']
    save_path = str(uuid.uuid4()) + '.wav'
    fs = FileSystemStorage()
    
    fs.save(save_path, someFile)

    recognizer = sr.Recognizer()

    audioData = sr.AudioFile(save_path)
    with audioData as source:
        audio = recognizer.record(source)

    recognized_text = recognizer.recognize_google(audio, language='ru')
    os.remove(save_path)

    return HttpResponse(recognized_text)