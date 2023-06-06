from app.models import User, File

def create_info_superadmin( company_id, email, firstName, lastName, password, type):
    photo = File.objects.get(pk=10001)
    if(type == "NORMAL" or type == "SUPERADMIN"):
        user = User.objects.create(
                        city="", 
                        cologn="", 
                        cp=0, 
                        username=email,
                        email=email, 
                        first_name=firstName, 
                        last_name=lastName, 
                        municipality="", 
                        state="NS", 
                        street="", 
                        telephone="", 
                        type=type, 
                        photo=photo,
                        token_verified=True)
        user.set_password(password) 
        user.save()
    elif(type == "SELLER" or type == "ADMIN"):
        user=User.objects.create(
                        city="",
                        cologn="",
                        token_verified=True,
                        cp=0,
                        photo=photo,
                        username=email,
                        email=email,
                        first_name=firstName,
                        last_name=lastName,
                        municipality="",
                        state="NS",
                        street="",
                        telephone="",
                        type=type,
                        company_id=company_id)
        user.set_password(password)
        user.save()