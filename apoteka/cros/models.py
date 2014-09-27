from django.db import models

# Create your models here.

class Cros(models.Model):
    piktogram = models.CharField(
        max_length=255,
    )
    
    legenda = models.CharField(
        max_length=255,
    )
    
    sifra = models.CharField(
        max_length=255,

    )
    naziv_hemikalije = models.CharField(
        max_length=255,
    )
    
    oficinalno = models.CharField(
        max_length=255,
    )
    
    jedinica = models.CharField(
        max_length=255,
        
    )
    
    cena = models.CharField(
        max_length=255,
    )
   
        
    def __str__(self):

        return ' '.join([
            self.piktogram,
            self.legenda,
            self.sifra,
            self.naziv_hemikalije,
            self.oficinalno,
            self.jedinica,
            self.cena,
        ])