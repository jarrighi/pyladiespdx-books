from django.db import models
from django.utils import timezone

class Book(models.Model):
  "Represents a book in the system"
  title = models.CharField(max_length=256)
  slug = models.SlugField(max_length=256, default=timezone.now)
  authors = models.CharField(max_length=256)
  isbn = models.CharField(max_length=256)

  # link to amazon, googlebooks, or publisher page
  url = models.CharField(max_length=256) 

  # Who purchased the book and eventually wants it back
  # Value should be PyladiesPDX for donated books
  owner = models.CharField(max_length=256)

  # Who current has the book and can hand it off 
  possessor = models.CharField(max_length=256)

  date_added = models.DateTimeField(default=timezone.now, editable=False)

  def __unicode__(self):
    return self.title

  def save(self, *args, **kwargs):
    if not self.pk:
        self.date_added = timezone.now()
    super(Book, self).save(*args, **kwargs)