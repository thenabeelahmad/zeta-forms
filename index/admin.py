from django.contrib import admin

# Register your models here.

from .models import Form
admin.site.register(Form)

from .models import Responses
admin.site.register(Responses)


from .models import User
admin.site.register(User)

