from django.db import models


# Create your models here.


class Automobilio_modelis(models.Model):
    # marke varchar not null
    # modelis varchar not null

    marke = models.CharField('Make', max_length=200, null=True)
    modelis = models.CharField('Model', max_length=200, null=True)

    def __str__(self):
        return self.modelis


class Uzsakymas(models.Model):
    # Data varchar not null
    # Automobilis_ID varchar not null (FK)

    data = models.CharField('Date', max_length=200)
    automobilis_ID = models.ForeignKey('Automobilis', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.data


class Automobilis(models.Model):
    # Valstybinis_NR varchar not null
    # Automobilio_modelis_ID varchar not null (FK)
    # VIN_kodas varchar not null
    # Klientas varchar not null

    Valstybinis_NR = models.CharField('Valstybinis_NR', max_length=200)
    Automobilio_modelis_ID = models.ForeignKey('Automobilio_modelis', on_delete=models.SET_NULL, null=True)
    VIN_kodas = models.CharField('VIN_kodas', max_length=200, null=True)
    Klientas = models.CharField('Klientas', max_length=200, null=True)

    def __str__(self):
        return self.Valstybinis_NR


class Uzsakymo_eilute(models.Model):
    # Paslauga_ID varchar not null (FK)
    # Uzsakymas_ID varchar not null (FK)
    # Kiekis varchar not null

    Paslauga_ID = models.ForeignKey('Paslauga', on_delete=models.SET_NULL, null=True)
    Uzsakymas_ID = models.ForeignKey('Uzsakymas', on_delete=models.SET_NULL, null=True)
    Kiekis = models.CharField('Kiekis', max_length=200, null=True)

    def __str__(self):
        return self.Kiekis


class Paslauga(models.Model):
    # Pavadinimas varchar not null
    # Kaina varchar not null

    Pavadinimas = models.CharField('Pavadinimas', max_length=200, null=True)
    Kaina = models.CharField('Kaina', max_length=200, null=True)

    def __str__(self):
        return self.Pavadinimas
