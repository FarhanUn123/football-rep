from django.db import models

class Lat_news(models.Model):
    image1=models.URLField(max_length=1000)
    image2=models.URLField(max_length=1000)
    caption=models.CharField(max_length=100)
    text1=models.CharField(max_length=50)
    text2=models.CharField(max_length=50)
    link=models.URLField(max_length=200)

class Nex_match(models.Model):
    team1=models.CharField(max_length=50)
    team2=models.CharField(max_length=50)
    t1_img=models.URLField(max_length=1000)
    t2_img=models.URLField(max_length=1000)
    l_name=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    place=models.CharField(max_length=50)

class Ranking(models.Model):
    r=models.IntegerField()
    team=models.CharField(max_length=50)
    w=models.IntegerField()
    d=models.IntegerField()
    l=models.IntegerField()
    pts=models.IntegerField()

class Video(models.Model):
    image=models.URLField(max_length=1000)
    caption=models.CharField(max_length=100)
    link=models.URLField(max_length=200)

class Blog(models.Model):
    image=models.URLField(max_length=1000)
    date=models.DateField()
    caption=models.CharField(max_length=100)
    text=models.TextField()
    link=models.URLField(max_length=200)

class Score(models.Model):
    h_t=models.CharField(max_length=50)
    a_t=models.CharField(max_length=50)
    h_s=models.IntegerField()
    a_s=models.IntegerField()
    h_im=models.URLField(max_length=1000)
    a_im=models.URLField(max_length=1000)

class Event(models.Model):
    image=models.URLField(max_length=1000)
    head=models.CharField(max_length=50)
    text=models.TextField()
    count=models.DateField()

class Comment(models.Model):
    name=models.CharField(max_length=50)
    image=models.URLField(max_length=1000)
    time=models.CharField(max_length=50)
    message=models.TextField()

class Video2(models.Model):
    image=models.URLField(max_length=1000)
    name=models.CharField(max_length=100)
    num=models.IntegerField()
    pos=models.CharField(max_length=50)
    link=models.URLField(max_length=200)

class Comment2(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    subject=models.CharField(max_length=50)
    message=models.TextField()

class Blog2(models.Model):
    caption=models.CharField(max_length=100)
    image1=models.ImageField(upload_to='pics',)
    date=models.DateField()
    text=models.TextField()
    p1=models.TextField()
    image2=models.URLField(max_length=1000)
    p2=models.TextField()
    image3=models.URLField(max_length=1000)
    p3=models.TextField()
