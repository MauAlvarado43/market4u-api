from app.models import User, Company

def update_info_normal(user_id, email, firstName, password, lastName, type, company_id):
    user = User.objects.get(id=user_id)
    user.email = email
    user.username = email
    user.first_name = firstName
    user.last_name = lastName
    user.type = type
    user.company = Company.objects.get(id=company_id)
    if(password != ''):
            user.set_password(password)
    user.save()