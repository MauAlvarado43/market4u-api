from app.models import User

def create_info_company( company_id, email, firstName, lastName, password, type):
        user=User.objects.create(
                        token_verified=True,
                        username=email,
                        email=email,
                        first_name=firstName,
                        last_name=lastName,
                        type=type,
                        company_id=company_id)
        user.set_password(password)
        user.save()