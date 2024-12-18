from django.db import models

# Create your models here.
class Pokemon(models.Model):

      pass
      name=models.CharField(max_length=30, null=False) #Para vachar 
      type=models.CharField(max_length=30, null=False)
      weight=models.CharField(max_length=6 ,decimal_places=4)
      weight=models.CharField(max_length=6 ,decimal_places=4)
      
      def __str__(self):
            return self.name
        
