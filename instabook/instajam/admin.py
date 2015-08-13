from django.contrib import admin
from instajam.models import Profile, Post, Votes
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'age', 'slam_jams',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url_img', 'message', 'posted_by',
                    'posted_at', 'total_jams')


@admin.register(Votes)
class VotesAdmin(admin.ModelAdmin):
    list_display = ('up_jams', 'down_jams',)