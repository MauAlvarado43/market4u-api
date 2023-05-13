from app.models import User


def create_info_superadmin( city, cologn, cp, email, firstName, password, lastName, municipality, state, street, telephone, type,company):
    if(type!="ADMIN" or type!="SELLER"):   
        company = None
    
    User.objects.create(
        firstName=firstName,
        city=city,
        cologn=cologn,
        cp=cp,email=email,
        password=password,
        lastName=lastName,
        municipality=municipality,
        state=state,
        street=street,
        telephone=telephone,
        type=type,
        company=company)