from app.models import User, Company

def update_info_normal(user_id, city, cologn, cp, email, firstName, password, lastName, municipality, state, street, telephone, type,company):
    user = User.objects.get(id=user_id)
    user.city = city
    user.cologn = cologn
    user.cp = cp
    user.email = email
    user.first_name = firstName
    user.last_name = lastName
    user.municipality = municipality
    user.state = state
    user.street = street
    user.telephone = telephone
    user.type = type
    user.company = Company.objects.get(id=company)
    if(password != ''):
            user.set_password(password)
    user.save()