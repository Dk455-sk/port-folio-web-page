from django.db import models

# Create your models here.
class About(models.Model):
    name=models.CharField(max_length=100)
    bio=models.TextField()
    profile_image=models.ImageField(upload_to='about/')

    def __str__(self):
        return self.name
    
class SkillCategory(models.Model):

    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Skill(models.Model):

    category = models.ForeignKey(
        SkillCategory,
        on_delete=models.CASCADE,
        related_name="skills"
    )

    name = models.CharField(max_length=100)

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    description = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name
    

class Project(models.Model):

    CATEGORY_CHOICES = (
        ('web', 'Web'),
        ('api', 'API'),
        ('fullstack', 'Full Stack'),
        ('ml', 'Machine Learning'),
        ('ai', 'AI'),
    )

    title = models.CharField(max_length=200)



    problem = models.TextField(
        blank=True,
        null=True
    )

    solution = models.TextField(
        blank=True,
        null=True
    )

    impact = models.TextField(
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='project_videos/',
        blank=True,
        null=True
    )

    # NEW FIELD → static video filename
    video_static = models.CharField(
        max_length=200,
        blank=True,
        null=True,
        help_text="Example: portfolio.mp4"
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES
    )

    tech_stack = models.CharField(max_length=300)

    github_link = models.URLField()

    live_link = models.URLField(
        blank=True,
        null=True
    )

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


class Hero(models.Model):

    availability = models.CharField(
        max_length=100
    )

    title = models.CharField(
        max_length=200
    )

    subtitle = models.TextField()

    profile_image = models.ImageField(
        upload_to='hero/'
    )

    def __str__(self):

        return self.title

class SocialLink(models.Model):

    PLATFORM_CHOICES = (

        ('github','GitHub'),
        ('linkedin','LinkedIn'),
        ('twitter','Twitter'),
        ('email','Email'),

    )

    platform = models.CharField(
        max_length=50,
        choices=PLATFORM_CHOICES
    )

    link = models.URLField()

    icon = models.CharField(
        max_length=50,
        help_text='Example: bi bi-github'
    )

    def __str__(self):

        return self.platform


class Counter(models.Model):

    number = models.CharField(
        max_length=20
    )

    title = models.CharField(
        max_length=100
    )

    def __str__(self):

        return self.title

class Timeline(models.Model):

    POSITION_CHOICES = (

        ('left','Left'),
        ('right','Right'),

    )

    year = models.CharField(
        max_length=20
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField()

    position = models.CharField(
        max_length=10,
        choices=POSITION_CHOICES,
        default='left'
    )

    def __str__(self):

        return self.title


class ContactInfo(models.Model):

    title = models.CharField(
        max_length=100
    )

    value = models.CharField(
        max_length=300
    )

    icon = models.CharField(
        max_length=50
    )

    def __str__(self):

        return self.title

class ContactMessage(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField()

    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.name

class Resume(models.Model):

    title = models.CharField(max_length=100)

    file = models.FileField(upload_to='resume/')

    def __str__(self):

        return self.title


class Education(models.Model):

    degree = models.CharField(max_length=200)

    institution = models.CharField(max_length=200)

    year = models.CharField(max_length=50)

    grade = models.CharField(max_length=50)

    description = models.TextField()

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):

        return self.degree

class Achievement(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/',blank=True,null=True)
    date = models.CharField(max_length=100)

    def __str__(self):
        return self.title