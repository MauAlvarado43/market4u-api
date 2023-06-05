from django.shortcuts import get_object_or_404
from django.core.files.storage import FileSystemStorage
from cfdiclient import Fiel, Autenticacion
from app.models import File

def validate_keys(fiel_cer, fiel_key, fiel_pass):

    fs = FileSystemStorage()

    file_cer = get_object_or_404(File, pk=fiel_cer)
    file_key = get_object_or_404(File, pk=fiel_key)

    cer = fs.open(file_cer.name, 'rb').read()
    key = fs.open(file_key.name, 'rb').read()

    try:

        fiel = Fiel(cer, key, fiel_pass)
        token = Autenticacion(fiel).obtener_token()

        if token is not None: 
            return True

    except Exception as e:
        pass

    return False