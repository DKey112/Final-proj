from django.contrib import admin

from gamenews.models import Game, Player, Team, Post, Comment
from django.utils.html import mark_safe


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name','create_date','team_img_preview',)
    list_filter = ('is_active',)

    @admin.display(description='team_logo')
    def team_img_preview(self, obj):
        return mark_safe(f'<img src = "{obj.team_logo.url}" width ="150px" height="200px"/>')

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('name','pub_date','img_preview','description',)
    list_filter=('name','description',)

    @admin.display(description='game_image')
    def img_preview(self, obj):
        return mark_safe(f'<img src = "{obj.game_image.url}" width ="150px" height="200px"/>')


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display=('nickname','team','rating','player_pic_preview',)
    list_filter=('rating',)

    @admin.display(description='player_pic')
    def player_pic_preview(self, obj):
        return mark_safe(f'<img src = "{obj.player_pic.url}" width ="150px" height="200px"/>')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','author','pub_date','author_id',)
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('id','author','author_id','date_added','text',)