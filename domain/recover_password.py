from app.models import User
from django.utils import timezone
from datetime import timedelta
from django.utils.crypto import get_random_string
from rest_framework import status
import domain.utils.http_codes as codes
from domain.create_user import send_mail_token


def send_token_password(email):

    if not User.objects.filter(email=email).exists():
        return status.HTTP_401_UNAUTHORIZED, None

    user = User.objects.get(email=email)

    if not user.token_verified:
        return status.HTTP_200_OK, user.token

    token = get_random_string(length=32)
    user.token = token
    user.save()

    subject_html_mail = "[Martket4U] Restablecimiento de contraseña"
    preheader_html_mail = (
        "Al parecer has olvidado tu contraseña. No te preocupes recuperala ahora mismo"
    )
    title_html_mail = f"Restablecimiento de contraseña"
    body_html_mail = """
    Hace poco hemos recibido una solicitud de restablecimiento de la 
    contraseña de su cuenta. Para restablecer su contraseña solo presiona 
    el bóton de abajo.
    """
    name_button = "Recupera tu contraseña"
    path = "restore_password"

    send_mail_token(
        subject_html_mail,
        preheader_html_mail,
        title_html_mail,
        body_html_mail,
        name_button,
        path,
        email,
        token
    )

    return status.HTTP_200_OK, None


def restore_password(token, new_password):

    user = User.objects.get(token=token)

    if not user:
        return status.HTTP_401_UNAUTHORIZED
    
    user.set_password(new_password)
    user.save()

    return status.HTTP_200_OK

