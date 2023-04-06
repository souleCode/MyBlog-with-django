from django.contrib import admin
from .models import Post

from django.contrib.auth.models import Group
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    # fields=[
    #     'title',
    # ]
    # list_filter=['title']  #on utilise list_filter pour date de creation la c'est encore plus professionell

    # readonly_fields=['content']
    search_fields=['title','content']

#exclude permet de virer un champs.on ulise comme fields


admin.site.register(Post, PostAdmin)
admin.site.unregister(Group)

admin.site.site_header='MyBlog Administration'
admin.site.site_title='MyBlog'

