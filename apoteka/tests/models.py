from django.db import models

# Create your models here.

class Test(models.Model):

    sifra = models.CharField(
        max_length=255,
    )
    naziv_medjuproizvoda = models.CharField(
        max_length=255,

    )
    oficinalno = models.CharField(
        max_length=255,
    )
    
    jedinica = models.CharField(
        max_length=255,
    )
    
    radna_tg = models.CharField(
        max_length=255,
    )
   
        
    def __str__(self):

        return ' '.join([
            self.sifra,
            self.naziv_medjuproizvoda,
            self.oficinalno,
            self.jedinica,
            self.radna_tg,
        ])