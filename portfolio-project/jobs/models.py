from django.db import models

# Create your models here.
class Job(models.Model):
    jobName = models.CharField(max_length = 200, default='Project Details')
    image = models.ImageField(upload_to = settings.MEDIA_ROOT)
    summary = models.CharField(max_length = 200, default='Summary is in GitHub ReadMe.')
    githubURL = models.CharField(max_length = 200, default='https://github.com/Deep9z')
    fullJobDetail = models.CharField(max_length = 2000, default='Summary is in GitHub ReadMe.')

    def __str__(self):
        return self.summary
