from django.contrib import admin
from  .models import *
# Register your models here.

# admin.site.register(Book)

#定制admin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publish_date')
    search_fields = ('title',)
    list_filter = ('publish_date',)
    date_hierarchy = 'publish_date'
    ordering = ('-publish_date',)


    # fields = ('title','author','publishers','publish_date')
    # exclude = ('title',)
    # filter_horizontal = ('publishers',)
    # filter_vertical = ('publishers',)
    raw_id_fields = ('publishers',)
    fieldsets = (
        ('作者',{'fields':('author',)}),
        ('出版社', {'fields': ('publishers',)}),
    )

admin.site.register(Book,BookAdmin)