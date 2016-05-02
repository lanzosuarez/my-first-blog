from django.db import models                         #if project is fresh. run migrate first. then create model. then run makemigration,migrate
from django.utils import timezone #for timezone      makemigrations, migrate

# Create your models hereself.

class Post(models.Model):                           #this line defines our model , Post is the name of our model. 
                                                    #models.Model means that the Post is a Django Model, 
                                                    #so Django knows that it should be saved in the database.

    author = models.ForeignKey('auth.User')         #this is a link to another model.   
    title = models.CharField(max_length=200)        #this is how you define text with a limited number of characters.
    text = models.TextField()                       #this is for long text without a limit.
    created_date = models.DateTimeField(            #this is a date and time.
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def trash(self):
        self.delete()

    def __str__(self):
        return self.title

    class Meta:
        db_table = "post_table"

