from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class NewsInfoMixin(models.Model):
    slug = models.SlugField(max_length=50, verbose_name='Short Name')
    is_active = models.BooleanField(default=True, verbose_name='Active?')

    class Meta:
        abstract = True

    
class Game(NewsInfoMixin):
    name = models.CharField(max_length=50, verbose_name='Game name')
    pub_date = models.DateField(auto_now_add=True, verbose_name='Publication date')
    release_date = models.DateField(auto_now_add=False, verbose_name='Release date')
    description = models.TextField(verbose_name='Game Description')
    game_image = models.ImageField(verbose_name='Game Image', upload_to='game_image', blank=True, null=True)
    post_amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name
        
class Team(NewsInfoMixin):
    team_name = models.CharField(max_length=50, verbose_name='Team name')
    description = models.TextField(verbose_name='Description Team')
    game = models.ForeignKey(Game, verbose_name='Discipline ', on_delete=models.SET_DEFAULT, default=None, null=True)
    create_date = models.DateField(auto_now_add=False, verbose_name='Create date')
    team_logo = models.ImageField(verbose_name='Team Logo', upload_to='team_logo', blank=True, null=True)
    

    @classmethod
    def default_team(cls):
        team, created = cls.objects.get_or_create(
            title='default',
            slug='default',
            description='default description',
            is_active=True
        )
        return team.pk

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'


    def __str__(self) -> str:
        return f"{self.team_name}"

class Player(NewsInfoMixin):
    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    nickname= models.CharField(max_length=50, verbose_name='Nickname')
    team = models.ForeignKey(Team, verbose_name='Team', on_delete=models.SET_DEFAULT, default=None ,null=True)
    player_pic = models.ImageField(verbose_name='Player pictures', upload_to='player_pic', blank=True, null=True)
    bio = models.TextField(null=True, blank=True, verbose_name='Bio')
    rating = models.IntegerField(verbose_name='Player rating', null=True)
    achievement = models.CharField(max_length=200,default=None, null=True, verbose_name='Achievement')
    game = models.ForeignKey(Game, verbose_name='Discipline ', on_delete=models.SET_DEFAULT, default=None, null=True)

    def __str__(self):
        return self.nickname

class Post(NewsInfoMixin):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    post_pic = models.ImageField(verbose_name='Post pictures', default='default_post_picture.png', upload_to='post_pic', blank=True, null=True)
    game = models.ForeignKey(Game, verbose_name='Discipline ', on_delete=models.SET_DEFAULT, default=None, null=True)
    likes = models.ManyToManyField(User, related_name="post_like", blank=True)

    def count_of_like(self):
        return self.likes.count()
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('gamenews:post_detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)

        img = Image.open(self.post_pic.path)
    
        if img.height > 600 or img.width > 500:
            output_size = (650, 500)
            img.thumbnail(output_size)
            img.save(self.post_pic.path)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="Post", related_name="comments")
    author = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="Author comments",related_name="comments_author")
    text = models.TextField(verbose_name="Text", max_length=280)
    date_added = models.DateTimeField(verbose_name="Pub date", auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.author} {self.post.title}"

    def get_absolute_url(self):
        return reverse("gamenews:post_detail", kwargs={"pk": self.post.pk})
        