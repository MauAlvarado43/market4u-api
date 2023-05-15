from app.models import User, Company

def update_info_superadmin(user_id, city, cologn, company_id, cp, email, firstName, lastName, municipality, state, street, telephone, type, username, password):
    user = User.objects.get(id=user_id)
    if(type == "NORMAL" or type == "SUPERADMIN"):
        user.city=city
        user.cologn=cologn
        user.cp=cp
        user.username=email
        user.email=email
        user.first_name=firstName
        user.last_name=lastName
        user.municipality=municipality
        user.state=state
        user.street=street
        user.telephone=telephone
        user.type=type
        user.company_id=None
        if(password!=''):
            user.set_password(password)
        user.save()
    else:
        user.city=city
        user.cologn=cologn
        user.cp=cp
        user.username=email
        user.email=email
        user.first_name=firstName
        user.last_name=lastName
        user.municipality=municipality
        user.state=state
        user.street=street
        user.telephone=telephone
        user.type=type
        user.company_id=company_id
        if(password!=''):
            user.set_password(password)
        user.save()