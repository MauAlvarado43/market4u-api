from app.models import User, Company

def update_info_superadmin(user_id, company_id, email, firstName, lastName, type, username, password):
    user = User.objects.get(id=user_id)
    if(type == "NORMAL" or type == "SUPERADMIN"):
        user.username=email
        user.email=email
        user.first_name=firstName
        user.last_name=lastName
        user.type=type
        user.company_id=None
        if(password!=''):
            user.set_password(password)
        user.save()
    else:
        user.username=email
        user.email=email
        user.first_name=firstName
        user.last_name=lastName
        user.type=type
        user.company_id=company_id
        if(password!=''):
            user.set_password(password)
        user.save()