from django.db import models

# Create your models here.

class Article(models.Model):

    sifra = models.CharField(
        max_length=255,
    )
    naziv = models.CharField(
        max_length=255,

    )
    cena = models.CharField(
        max_length=255,
    )
    
    
   
        
    def __str__(self):

        return ' '.join([
            self.sifra,
            self.naziv,
            self.cena,
          
        ])