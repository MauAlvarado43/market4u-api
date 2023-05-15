from app.models import User

def create_info_company( city, cologn, company_id, cp, email, firstName, lastName, municipality, password, state, street, telephone, type):
    if(type == "SELLER" or type == "ADMIN"):
        user=User.objects.create(
                        city=city,
                        cologn=cologn,
                        token_verified=True,
                        cp=cp,
                        username=email,
                        email=email,
                        first_name=firstName,
                        last_name=lastName,
                        municipality=municipality,
                        state=state,
                        street=street,
                        telephone=telephone,
                        type=type,
                        company_id=company_id)
        user.set_password(password)
        user.save()