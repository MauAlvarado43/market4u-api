# Generated by Django 3.2.18 on 2023-05-08 05:12

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('active', models.BooleanField(default=False)),
                ('type', models.CharField(choices=[('SUPERADMIN', 'SUPERADMIN'), ('ADMIN', 'ADMIN'), ('SELLER', 'SELLER'), ('NORMAL', 'NORMAL')], max_length=64)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('cp', models.IntegerField(default=0)),
                ('municipality', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(choices=[('NS', 'NS'), ('AGUASCALIENTES', 'AGUASCALIENTES'), ('BAJA CALIFORNIA', 'BAJA CALIFORNIA'), ('BAJA CALIFORNIA SUR', 'BAJA CALIFORNIA SUR'), ('CAMPECHE', 'CAMPECHE'), ('COAHUILA', 'COAHUILA'), ('COLIMA', 'COLIMA'), ('CHIAPAS', 'CHIAPAS'), ('CHIHUAHUA', 'CHIHUAHUA'), ('DURANGO', 'DURANGO'), ('CIUDAD DE MEXICO', 'CIUDAD DE MEXICO'), ('GUANAJUATO', 'GUANAJUATO'), ('GUERRERO', 'GUERRERO'), ('HIDALGO', 'HIDALGO'), ('JALISCO', 'JALISCO'), ('MEXICO', 'MEXICO'), ('MICHOACAN', 'MICHOACAN'), ('MORELOS', 'MORELOS'), ('NAYARIT', 'NAYARIT'), ('NUEVO LEON', 'NUEVO LEON'), ('OAXACA', 'OAXACA'), ('PUEBLA', 'PUEBLA'), ('QUERETARO', 'QUERETARO'), ('QUINTANA ROO', 'QUINTANA ROO'), ('SAN LUIS POTOSI', 'SAN LUIS POTOSI'), ('SINALOA', 'SINALOA'), ('SONORA', 'SONORA'), ('TABASCO', 'TABASCO'), ('TAMAULIPAS', 'TAMAULIPAS'), ('TLAXCALA', 'TLAXCALA'), ('VERACRUZ', 'VERACRUZ'), ('YUCATAN', 'YUCATAN'), ('ZACATECAS', 'ZACATECAS')], max_length=64)),
                ('cologn', models.CharField(blank=True, max_length=100)),
                ('telephone', models.CharField(blank=True, max_length=100)),
                ('token', models.CharField(blank=True, max_length=40)),
                ('token_verified', models.BooleanField(default=False)),
                ('code', models.IntegerField(default=0)),
            ],
            options={
                'db_table': '_user',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='buyer_carts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '_cart',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': '_category',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('common_name', models.CharField(blank=True, max_length=100)),
                ('rfc', models.CharField(blank=True, max_length=20)),
                ('cp', models.IntegerField(default=0)),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.CharField(blank=True, max_length=100)),
                ('active', models.BooleanField(default=False)),
                ('municipality', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(choices=[('NS', 'NS'), ('AGUASCALIENTES', 'AGUASCALIENTES'), ('BAJA CALIFORNIA', 'BAJA CALIFORNIA'), ('BAJA CALIFORNIA SUR', 'BAJA CALIFORNIA SUR'), ('CAMPECHE', 'CAMPECHE'), ('COAHUILA', 'COAHUILA'), ('COLIMA', 'COLIMA'), ('CHIAPAS', 'Chiapas'), ('CHIHUAHUA', 'CHIHUAHUA'), ('DURANGO', 'DURANGO'), ('CIUDAD DE MEXICO', 'CIUDAD DE MEXICO'), ('GUANAJUATO', 'GUANAJUATO'), ('GUERRERO', 'GUERRERO'), ('HIDALGO', 'HIDALGO'), ('JALISCO', 'JALISCO'), ('MEXICO', 'MEXICO'), ('MICHOACAN', 'MICHOACAN'), ('MORELOS', 'MORELOS'), ('NAYARIT', 'NAYARIT'), ('NUEVO LEON', 'NUEVO LEON'), ('OAXACA', 'OAXACA'), ('PUEBLA', 'PUEBLA'), ('QUERETARO', 'QUERETARO'), ('QUINTANA ROO', 'QUINTANA ROO'), ('SAN LUIS POTOSI', 'SAN LUIS POTOSI'), ('SINALOA', 'SINALOA'), ('SONORA', 'SONORA'), ('TABASCO', 'TABASCO'), ('TAMAULIPAS', 'TAMAULIPAS'), ('TLAXCALA', 'TLAXCALA'), ('VERACRUZ', 'VERACRUZ'), ('YUCATAN', 'YUCATAN'), ('ZACATECAS', 'ZACATECAS')], max_length=64)),
                ('cologn', models.CharField(blank=True, max_length=100)),
                ('website', models.CharField(blank=True, max_length=100)),
                ('street', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': '_company',
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('url', models.URLField(help_text='File reference link (eg. http://localhost:8000/image.png)', max_length=1024)),
                ('size', models.IntegerField(blank=True, default=0, help_text='File size in bytes', null=True)),
                ('name', models.CharField(blank=True, default='', help_text='Common File Name (eg. Image.png)', max_length=1024, null=True)),
            ],
            options={
                'db_table': 'file',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('short_description', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='models.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='models.company')),
            ],
            options={
                'db_table': '_product',
            },
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('price', models.FloatField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('shipment', models.FloatField(default=0)),
                ('photos', models.ManyToManyField(related_name='variant_photoses', to='models.File')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='models.product')),
            ],
            options={
                'db_table': '_variant',
            },
        ),
        migrations.CreateModel(
            name='Variantoption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('value', models.CharField(blank=True, max_length=100)),
                ('variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variantoptions', to='models.variant')),
            ],
            options={
                'db_table': '_variantoption',
            },
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('info', models.TextField(blank=True)),
                ('folio', models.CharField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('status', models.CharField(choices=[('CREATED', 'CREATED'), ('SENT', 'SENT'), ('COMPLETED', 'COMPLETED')], max_length=64)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shippings', to='models.cart')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller_shippings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '_shipping',
            },
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('disscount', models.FloatField(default=0)),
                ('start_date', models.DateTimeField(default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(default=datetime.datetime.now)),
                ('banner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sale_banners', to='models.file')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='models.company')),
            ],
            options={
                'db_table': '_sale',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('amount', models.IntegerField(default=0)),
                ('product', models.JSONField(blank=True, default=dict)),
                ('sale', models.JSONField(blank=True, default=dict)),
                ('shipping', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='models.shipping')),
            ],
            options={
                'db_table': '_purchase',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='sale',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='models.sale'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('card_number', models.CharField(blank=True, max_length=100)),
                ('expire_date', models.CharField(blank=True, max_length=10)),
                ('type', models.CharField(choices=[('DEBIT', 'DEBIT'), ('CREDIT', 'CREDIT')], max_length=64)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('bank', models.CharField(blank=True, max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '_payment',
            },
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('title', models.CharField(blank=True, max_length=100)),
                ('description', models.TextField(blank=True)),
                ('rate', models.IntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='models.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '_opinion',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Indicates the date on which the model was created', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Indicates the date it was last updated', null=True)),
                ('hash', models.CharField(default='', editable=False, help_text='Unique identifier to identify the state of the model', max_length=32, null=True)),
                ('content', models.TextField(blank=True)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_messages', to=settings.AUTH_USER_MODEL)),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='target_messages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': '_message',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_photos', to='models.file'),
        ),
        migrations.AddField(
            model_name='cart',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to='models.payment'),
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='models.company'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_photos', to='models.file'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='user',
            name='wishlist',
            field=models.ManyToManyField(blank=True, db_table='_user__wishlist', related_name='wishlist_users', to='models.Product'),
        ),
    ]
