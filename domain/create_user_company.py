from app.models import User, File

def create_info_company( company_id, email, firstName, lastName, password, type):
        photo = File.objects.get(pk=10001)
        user=User.objects.create(
                        token_verified=True,
                        username=email,
                        email=email,
                        first_name=firstName,
                        last_name=lastName,
                        type=type,
                        state = "NS",
                        photo=photo,
                        company_id=company_id)
        user.set_password(password)
        user.save()