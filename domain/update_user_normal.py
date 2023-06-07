from app.models import User, Company

def update_info_normal(user_id, email, firstName, password, lastName, type,company):
    user = User.objects.get(id=user_id)
    user.email = email
    user.first_name = firstName
    user.last_name = lastName
    user.type = type
    user.company = Company.objects.get(id=company)
    if(password != ''):
            user.set_password(password)
    user.save()