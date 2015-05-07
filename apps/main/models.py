from django.db import models

class Level(models.Model):
    number = models.IntegerField(default=1)
    exp = models.CharField(max_length=255, default='')
    def __unicode__(self):
        return str(self.number)

class Achievement(models.Model):
    uid = models.IntegerField(default=0)
    title = models.CharField(max_length=255,default='')
    def __unicode__(self):
        return self.title

class UserExt(models.Model):
    user = models.ForeignKey('auth.User', related_name='ue_u')
    current_level = models.IntegerField(default=1)
    current_exp = models.IntegerField(default=0)
    avatar = models.ImageField(upload_to='avatar', default='')
    achievement_list = models.ManyToManyField('main.Achievement', related_name='u_a')
    def __unicode__(self):
        return str(self.user.username)

class Category(models.Model):
    title = models.CharField(max_length=255, default='')
    def __unicode__(self):
        return self.title

class CategoryUserLevel(models.Model):
    user = models.ForeignKey('auth.User', related_name='cul_u')
    category = models.ForeignKey('main.Category', related_name='cul_c')
    current_level = models.IntegerField(default=1)
    current_exp = models.IntegerField(default=0)
    def __unicode__(self):
        return str(self.user.username)

class TaskType(models.Model):
    user = models.ForeignKey('auth.User', related_name='tt_u')
    category = models.ForeignKey('main.Category', related_name='tt_c')
    title = models.CharField(max_length=255, default='')
    cost = models.IntegerField(default=0)
    color = models.CharField(max_length=255, default='ff0000')
    def __unicode__(self):
        return str(self.user.username)

class Comment(models.Model):
    task = models.ForeignKey('main.Task', related_name='c_t')
    title = models.CharField(max_length=255, default='')
    content = models.TextField()
    image = models.ImageField(upload_to='comment', default='')
    def __unicode__(self):
        return self.title

class Progress(models.Model):
    task = models.ForeignKey('main.Task', related_name='p_t')
    percent = models.IntegerField(default=1)
    message = models.CharField(max_length=255, default='')
    def __unicode__(self):
        return str(self.task.title)+str(self.percent)

class ProgressImage(models.Model):
    progress = models.ForeignKey('main.Progress', related_name='pi_p')
    image = models.ImageField(upload_to='progress', default='')
    def __unicode__(self):
        return str(self.image.url)

class TaskImage(models.Model):
    task = models.ForeignKey('main.Task', related_name='ti_t')
    image = models.ImageField(upload_to='task', default='')
    def __unicode__(self):
        return str(self.task.title)

class Task(models.Model):
    MEMBER_CHOICES = (
        (1, u'Not more'),
        (2, u'Range'),
        (3, u'Unlimit'),
    )
    user_create = models.ForeignKey('auth.User', related_name='t_uc')
    task_type = models.ForeignKey('main.TaskType', related_name='t_tt')
    category = models.ForeignKey('main.Category', related_name='t_c')
    member_type = models.IntegerField(null=True, blank=True, choices=MEMBER_CHOICES)
    title = models.CharField(max_length=255, default='')
    text_content = models.TextField()
    video_link = models.CharField(max_length=255, default='')
    members_min = models.IntegerField(default=1)
    members_max = models.IntegerField(default=0)
    cost_need = models.IntegerField(default=0)
    cost_now = models.IntegerField(default=0)
    min_level = models.IntegerField(default=0)
    date_start = models.DateTimeField(auto_now_add=True)
    date_finish = models.DateTimeField(auto_now_add=True)
    date_add = models.DateTimeField(auto_now_add=True)
    geojson = models.TextField()
    def __unicode__(self):
        return self.title
