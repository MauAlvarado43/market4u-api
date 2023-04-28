from app.models import User
from django.utils import timezone
from datetime import timedelta
from django.utils.crypto import get_random_string
from rest_framework import status
import domain.utils.http_codes as codes
from domain.create_user import send_mail, DURATION_MINUTES_TOKEN


def send_token_password(email):
    if not User.objects.filter(email=email).exists():
        return status.HTTP_401_UNAUTHORIZED

    user = User.objects.get(email=email)
    if not user.token_verified:
        return codes.CODE_420_TOKEN_NOT_VERIFIED

    expiration_date = timezone.now() + timedelta(minutes=DURATION_MINUTES_TOKEN)
    token = get_random_string(length=32)

    user.verify_token = token
    user.verify_token_expiration = expiration_date
    user.save()

    subject_html_mail = "[Fantasy] Recuperación de cuenta"
    preheader_html_mail = (
        "Al parecer has olvidado tu contraseña. No te preocupes recuperala ahora mismo"
    )
    title_html_mail = f"Recuperación de cuenta"
    body_html_mail = """
    Hace poco hemos recibido una solicitud de restablecimiento de la 
    contraseña de su cuenta. Para restablecer su contraseña solo presiona 
    el bóton de abajo.
    """
    name_button = "Recupera tu contraseña"
    path = "restore_password"

    send_mail(
        subject_html_mail,
        preheader_html_mail,
        title_html_mail,
        body_html_mail,
        name_button,
        path,
        email,
        token,
    )

    return status.HTTP_200_OK


def restore_password(token, new_password):
    if not User.objects.filter(verify_token=token).exists():
        return status.HTTP_401_UNAUTHORIZED

    user = User.objects.get(verify_token=token)
    if timezone.now() <= user.verify_token_expiration:
        user.set_password(new_password)
        user.verify_token = ""
        user.save()
        return status.HTTP_200_OK

    else:
        return codes.CODE_421_TOKEN_EXPIRED
