from django.contrib import admin

from ads.models.ad import Ad
from ads.models.category import Category
from ads.models.location import Location
from ads.models.selection import Selection

admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Selection)

