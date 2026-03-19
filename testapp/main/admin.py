from django.contrib import admin
from . import models
from django.contrib.auth.models import User, Group

admin.site.register([
    models.Type,
    models.Category,
    models.Subcategory,
    models.Status,
    models.Record,
])
admin.site.unregister([
    Group, User
])
