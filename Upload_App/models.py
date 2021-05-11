from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Uploader(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='post_author')
    upload_title=models.CharField(max_length=264,verbose_name='Put A Title')
    file_details = models.TextField(verbose_name="Put Your Files Detials?")
    thumbnail= models.FileField(upload_to='files_storage')
    uplaod_date=models.DateTimeField(auto_now_add= True)
    update_date=models.DateTimeField(auto_now= True)

    # class Meta:
    #     ordering = ['upload_date',]
    
    def __str__(self):
        return self.upload_title

    