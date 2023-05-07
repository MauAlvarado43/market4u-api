import os
import random
from datetime import timedelta
from rest_framework import status

from django.conf import settings
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.html import strip_tags

from domain.utils.http_codes import CODE_421_INVALID_CODE
from app.celery import send_mail_async
from app.models import User, File

HTML_TEMPLATE = """

<!DOCTYPE html>
<html>
  <head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <style type="text/css">
      /* FONTS */
      @media screen {{
        @font-face {{
          font-family: "Lato";
          font-style: normal;
          font-weight: 400;
          src: local("Lato Regular"), local("Lato-Regular"),
            url(https://fonts.gstatic.com/s/lato/v11/qIIYRU-oROkIk8vfvxw6QvesZW2xOQ-xsNqO47m55DA.woff)
              format("woff");
        

        @font-face {{
          font-family: "Lato";
          font-style: normal;
          font-weight: 700;
          src: local("Lato Bold"), local("Lato-Bold"),
            url(https://fonts.gstatic.com/s/lato/v11/qdgUG4U09HnJwhYI-uK18wLUuEpTyoUstqEm5AMlJo4.woff)
              format("woff");
        }}

        @font-face {{
          font-family: "Lato";
          font-style: italic;
          font-weight: 400;
          src: local("Lato Italic"), local("Lato-Italic"),
            url(https://fonts.gstatic.com/s/lato/v11/RYyZNoeFgb0l7W3Vu1aSWOvvDin1pK8aKteLpeZ5c0A.woff)
              format("woff");
        }}

        @font-face {{
          font-family: "Lato";
          font-style: italic;
          font-weight: 700;
          src: local("Lato Bold Italic"), local("Lato-BoldItalic"),
            url(https://fonts.gstatic.com/s/lato/v11/HkF_qI1x_noxlxhrhMQYELO3LdcAZYWl9Si6vvxL-qU.woff)
              format("woff");
        }}
      }}

      /* CLIENT-SPECIFIC STYLES */
      body,
      table,
      td,
      a {{
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
      }}
      table,
      td {{
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
      }}
      img {{
        -ms-interpolation-mode: bicubic;
      }}

      /* RESET STYLES */
      img {{
        border: 0;
        height: auto;
        line-height: 100%;
        outline: none;
        text-decoration: none;
      }}
      table {{
        border-collapse: collapse !important;
      }}
      body {{
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
      }}

      /* iOS BLUE LINKS */
      a[x-apple-data-detectors] {{
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
      }}

      /* MOBILE STYLES */
      @media screen and (max-width: 600px) {{
        h1 {{
          font-size: 32px !important;
          line-height: 32px !important;
        }}
      }}

      /* ANDROID CENTER FIX */
      div[style*="margin: 16px 0;"] {{
        margin: 0 !important;
      }}
    </style>
  </head>
  <body
    style="
      background-color: #f4f4f4;
      margin: 0 !important;
      padding: 0 !important;
    "
  >
    <!-- HIDDEN PREHEADER TEXT -->
    <div
      style="
        display: none;
        font-size: 1px;
        color: #fefefe;
        line-height: 1px;
        font-family: 'Lato', Helvetica, Arial, sans-serif;
        max-height: 0px;
        max-width: 0px;
        opacity: 0;
        overflow: hidden;
      "
    >
      {preheader}
    </div>

    <table border="0" cellpadding="0" cellspacing="0" width="100%">
      <!-- LOGO -->
      <tr>
        <td bgcolor="#519FA5" align="center">
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="max-width: 600px"
          >
            <tr>
              <td
                align="center"
                valign="top"
                style="padding: 40px 10px 40px 10px"
              >
                <a href="{site_url}" target="_blank">
                  <img
                    alt="Logo"
                    src="https://i.ibb.co/Rb2DkqH/Logo.jpg"
                    style="
                      display: block;
                      width: 30%;
                      font-family: 'Lato', Helvetica, Arial, sans-serif;
                      color: #ffffff;
                      font-size: 18px;
                    "
                    border="0"
                  />
                </a>
              </td>
            </tr>
          </table>

        </td>
      </tr>
      <!-- HERO -->
      <tr>
        <td bgcolor="#519FA5" align="center" style="padding: 0px 10px 0px 10px">
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="max-width: 600px"
          >
            <tr>
              <td
                bgcolor="#ffffff"
                align="center"
                valign="top"
                style="
                  padding: 40px 20px 20px 20px;
                  border-radius: 4px 4px 0px 0px;
                  color: #111111;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 48px;
                  font-weight: 400;
                  letter-spacing: 4px;
                  line-height: 48px;
                "
              >
                <h1 style="font-size: 40px; font-weight: 400; margin: 0">
                  {title}
                </h1>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <!-- COPY BLOCK -->
      <tr>
        <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px">
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="max-width: 600px"
          >
            <!-- COPY -->
            <tr>
              <td
                bgcolor="#ffffff"
                align="left"
                style="
                  padding: 20px 30px 40px 30px;
                  color: #666666;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 18px;
                  font-weight: 400;
                  line-height: 25px;
                "
              >
                <p style="margin: 0">
                  {body}
                </p>
              </td>
            </tr>
            <!-- BULLETPROOF BUTTON -->
            <tr>
              <td bgcolor="#ffffff" align="left">
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td
                      bgcolor="#ffffff"
                      align="center"
                      style="padding: 20px 30px 60px 30px"
                    >
                      <table border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td
                            align="center"
                            style="border-radius: 3px"
                            bgcolor="#FC4B08"
                          >
                            <p
                              style="
                                padding-left: 20px;
                                padding-right: 20px;
                                font-size: 20px;
                                color: white;
                                font-family: Helvetica, Arial, sans-serif;
                              "
                              >{verification_code}
                            </p>
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <!-- COPY -->
            <tr>
              <td
                bgcolor="#ffffff"
                align="left"
                style="
                  padding: 0px 30px 20px 30px;
                  color: #666666;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 18px;
                  font-weight: 400;
                  line-height: 25px;
                "
              >
                <p style="margin: 0">
                </p>
              </td>
            </tr>
            <!-- COPY -->
            <tr>
              <td
                bgcolor="#ffffff"
                align="left"
                style="
                  padding: 0px 30px 40px 30px;
                  border-radius: 0px 0px 4px 4px;
                  color: #666666;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 18px;
                  font-weight: 400;
                  line-height: 25px;
                "
              >
                <p style="margin: 0">Saludos,<br />Market4U</p>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr style="height: 50px;"></tr>
    </table>
  </body>
</html>


"""

HTML_TEMPLATE_TOKEN = """
  <!DOCTYPE html>
<html>
  <head>
    <title></title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <style type="text/css">
      /* FONTS */
      @media screen {{
        @font-face {{
          font-family: "Lato";
          font-style: normal;
          font-weight: 400;
          src: local("Lato Regular"), local("Lato-Regular"),
            url(https://fonts.gstatic.com/s/lato/v11/qIIYRU-oROkIk8vfvxw6QvesZW2xOQ-xsNqO47m55DA.woff)
              format("woff");
        
        @font-face {{
          font-family: "Lato";
          font-style: normal;
          font-weight: 700;
          src: local("Lato Bold"), local("Lato-Bold"),
            url(https://fonts.gstatic.com/s/lato/v11/qdgUG4U09HnJwhYI-uK18wLUuEpTyoUstqEm5AMlJo4.woff)
              format("woff");
        }}
        @font-face {{
          font-family: "Lato";
          font-style: italic;
          font-weight: 400;
          src: local("Lato Italic"), local("Lato-Italic"),
            url(https://fonts.gstatic.com/s/lato/v11/RYyZNoeFgb0l7W3Vu1aSWOvvDin1pK8aKteLpeZ5c0A.woff)
              format("woff");
        }}
        @font-face {{
          font-family: "Lato";
          font-style: italic;
          font-weight: 700;
          src: local("Lato Bold Italic"), local("Lato-BoldItalic"),
            url(https://fonts.gstatic.com/s/lato/v11/HkF_qI1x_noxlxhrhMQYELO3LdcAZYWl9Si6vvxL-qU.woff)
              format("woff");
        }}
      }}
      /* CLIENT-SPECIFIC STYLES */
      body,
      table,
      td,
      a {{
        -webkit-text-size-adjust: 100%;
        -ms-text-size-adjust: 100%;
      }}
      table,
      td {{
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
      }}
      img {{
        -ms-interpolation-mode: bicubic;
      }}
      /* RESET STYLES */
      img {{
        border: 0;
        height: auto;
        line-height: 100%;
        outline: none;
        text-decoration: none;
      }}
      table {{
        border-collapse: collapse !important;
      }}
      body {{
        height: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        width: 100% !important;
      }}
      /* iOS BLUE LINKS */
      a[x-apple-data-detectors] {{
        color: inherit !important;
        text-decoration: none !important;
        font-size: inherit !important;
        font-family: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
      }}
      /* MOBILE STYLES */
      @media screen and (max-width: 600px) {{
        h1 {{
          font-size: 32px !important;
          line-height: 32px !important;
        }}
      }}
      /* ANDROID CENTER FIX */
      div[style*="margin: 16px 0;"] {{
        margin: 0 !important;
      }}
    </style>
  </head>
  <body
    style="
      background-color: #f4f4f4;
      margin: 0 !important;
      padding: 0 !important;
    "
  >
    <!-- HIDDEN PREHEADER TEXT -->
    <div
      style="
        display: none;
        font-size: 1px;
        color: #fefefe;
        line-height: 1px;
        font-family: 'Lato', Helvetica, Arial, sans-serif;
        max-height: 0px;
        max-width: 0px;
        opacity: 0;
        overflow: hidden;
      "
    >
      {preheader}
    </div>
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
      <!-- LOGO -->
      <tr>
        <td bgcolor="#519FA5" align="center">
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="max-width: 600px"
          >
            <tr>
              <td
                align="center"
                valign="top"
                style="padding: 40px 10px 40px 10px"
              >
                <a href="{site_url}" target="_blank">
                  <img
                    alt="Logo"
                    src="https://i.ibb.co/Rb2DkqH/Logo.jpg"
                    style="
                      display: block;
                      width: 30%;
                      font-family: 'Lato', Helvetica, Arial, sans-serif;
                      color: #ffffff;
                      font-size: 18px;
                    "
                    border="0"
                  />
                </a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <!-- HERO -->
      <tr>
        <td bgcolor="#519FA5" align="center" style="padding: 0px 10px 0px 10px">
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="max-width: 600px"
          >
            <tr>
              <td
                bgcolor="#ffffff"
                align="center"
                valign="top"
                style="
                  padding: 40px 20px 20px 20px;
                  border-radius: 4px 4px 0px 0px;
                  color: #111111;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 48px;
                  font-weight: 400;
                  letter-spacing: 4px;
                  line-height: 48px;
                "
              >
                <h1 style="font-size: 40px; font-weight: 400; margin: 0">
                  {title}
                </h1>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <!-- COPY BLOCK -->
      <tr>
        <td bgcolor="#f4f4f4" align="center" style="padding: 0px 10px 0px 10px">
          <table
            border="0"
            cellpadding="0"
            cellspacing="0"
            width="100%"
            style="max-width: 600px"
          >
            <!-- COPY -->
            <tr>
              <td
                bgcolor="#ffffff"
                align="left"
                style="
                  padding: 20px 30px 40px 30px;
                  color: #666666;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 18px;
                  font-weight: 400;
                  line-height: 25px;
                "
              >
                <p style="margin: 0">
                  {body}
                </p>
              </td>
            </tr>
            <!-- BULLETPROOF BUTTON -->
            <tr>
              <td bgcolor="#ffffff" align="left">
                <table width="100%" border="0" cellspacing="0" cellpadding="0">
                  <tr>
                    <td
                      bgcolor="#ffffff"
                      align="center"
                      style="padding: 20px 30px 60px 30px"
                    >
                      <table border="0" cellspacing="0" cellpadding="0">
                        <tr>
                          <td
                            align="center"
                            style="border-radius: 3px"
                            bgcolor="#FC4B08"
                          >
                            <a
                              href="{verify_url}"
                              target="_blank"
                              style="
                                font-size: 20px;
                                font-family: Helvetica, Arial, sans-serif;
                                color: #ffffff;
                                text-decoration: none;
                                padding: 15px 25px;
                                border-radius: 2px;
                                border: 1px solid #000000;
                                display: inline-block;
                              "
                              >{name_button}</a
                            >
                          </td>
                        </tr>
                      </table>
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <!-- COPY -->
            <tr>
              <td
                bgcolor="#ffffff"
                align="left"
                style="
                  padding: 0px 30px 0px 30px;
                  color: #666666;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 18px;
                  font-weight: 400;
                  line-height: 25px;
                "
              >
                <p style="margin: 0">
                  Si eso no funcionó, copia y pega el siguiente link en tu 
                  navegador: 
                </p>
              </td>
            </tr>
            <!-- COPY -->
            <tr>
              <td
                bgcolor="#ffffff"
                align="left"
                style="
                  padding: 20px 30px 20px 30px;
                  color: #666666;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 18px;
                  font-weight: 400;
                  line-height: 25px;
                "
              >
                <p style="margin: 0">
                  <a
                    href="{verify_url}"
                    target="_blank"
                    style="color: #7d35e8"
                    >{verify_url}</a
                  >
                </p>
              </td>
            </tr>
            <!-- COPY -->
            <tr>
              <td
                bgcolor="#ffffff"
                align="left"
                style="
                  padding: 0px 30px 20px 30px;
                  color: #666666;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 18px;
                  font-weight: 400;
                  line-height: 25px;
                "
              >
                <p style="margin: 0">
                </p>
              </td>
            </tr>
            <!-- COPY -->
            <tr>
              <td
                bgcolor="#ffffff"
                align="left"
                style="
                  padding: 0px 30px 40px 30px;
                  border-radius: 0px 0px 4px 4px;
                  color: #666666;
                  font-family: 'Lato', Helvetica, Arial, sans-serif;
                  font-size: 18px;
                  font-weight: 400;
                  line-height: 25px;
                "
              >
                <p style="margin: 0">Saludos,<br />Market4U</p>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr style="height: 50px;"></tr>
    </table>
  </body>
</html>
"""

def send_mail(subject, preheader, title, body, verification_code, to_email):

    html_message = HTML_TEMPLATE.format(
        preheader=preheader,
        site_url=os.getenv("CLIENT_URL"),
        title=title,
        body=body,
        verification_code=verification_code,
    )
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER

    send_mail_async.delay(
        subject, plain_message, from_email, [to_email], html_message=html_message
    )

def send_mail_token(subject, preheader, title, body, button_name, path, to_email, token):
    verify_url = f"{os.getenv('CLIENT_URL')}/{path}/{token}"

    html_message = HTML_TEMPLATE_TOKEN.format(
        preheader=preheader,
        site_url=os.getenv("CLIENT_URL"),
        title=title,
        body=body,
        verify_url=verify_url,
        name_button=button_name
    )
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER

    send_mail_async.delay(
        subject, plain_message, from_email, [to_email], html_message=html_message
    )


def registry(first_name, last_name, email, password):
    token = get_random_string(length=32)

    if User.objects.filter(email=email).exists():
        return {"status": status.HTTP_401_UNAUTHORIZED, "token": None}

    else:
        code = "".join([str(random.randint(0, 9)) for _ in range(5)])
        photo = File.objects.get(pk=10001)
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=email,
            type="NORMAL",
            token=token,
            token_verified=False,
            photo=photo,
            code=int(code)
        )

        user.set_password(password)
        user.save()
    
    subject_html_mail = "[Market4U] Verificación de correo"
    preheader_html_mail = "¡Estamos encantados de tenerte aquí! Prepárate para sumergirte en tu nueva cuenta."
    title_html_mail = f"!Bienvenido {first_name}!"
    body_html_mail = """
        Estamos emocionados de que comiences. Primero, necesitas
        confirmar tu cuenta. Este es tu código de verificación.
    """
    verification_code = code
  
    send_mail(
        subject_html_mail,
        preheader_html_mail,
        title_html_mail,
        body_html_mail,
        verification_code,
        email
    )
    
    return {"status": status.HTTP_200_OK, "token": token}


def registry_verify(token, code):
    user = User.objects.get(token=token)

    if not user:
        return status.HTTP_400_BAD_REQUEST

    if int(code) == user.code:
        user.token_verified = True
        user.save()
    else:
        return CODE_421_INVALID_CODE
    
    return status.HTTP_200_OK


def registry_generate(token):
    
    user = User.objects.get(token=token)

    if not user:
        return status.HTTP_400_BAD_REQUEST

    new_code = "".join([str(random.randint(0, 9)) for _ in range(5)])
  
    user.code = new_code
    user.save()

    subject_html_mail = "[Market4U] Re-verificación de correo"
    preheader_html_mail = (
        "¡Has solicitado un nuevo correo! Prepárate para empezar a comprar."
    )
    title_html_mail = f"!Hola {user.first_name}!"
    body_html_mail = """
        Hace poco hemos recibido una solicitud de restablecimiento de código. Para verificar su cuenta solo ingresa este código.
    """
    verification_code = new_code

    send_mail(
        subject_html_mail,
        preheader_html_mail,
        title_html_mail,
        body_html_mail,
        verification_code,
        user.email
    )
    return status.HTTP_200_OK
