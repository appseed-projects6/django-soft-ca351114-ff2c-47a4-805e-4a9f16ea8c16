# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Achat(models.Model):

    #__Achat_FIELDS__
    ref_his_achat = models.CharField(max_length=255, null=True, blank=True)
    ref_client = models.CharField(max_length=255, null=True, blank=True)
    ref_mar = models.CharField(max_length=255, null=True, blank=True)

    #__Achat_FIELDS__END

    class Meta:
        verbose_name        = _("Achat")
        verbose_name_plural = _("Achat")


class Client(models.Model):

    #__Client_FIELDS__
    ref_client = models.CharField(max_length=255, null=True, blank=True)
    nom_client = models.CharField(max_length=255, null=True, blank=True)
    adresse_client = models.CharField(max_length=255, null=True, blank=True)
    email_client = models.CharField(max_length=255, null=True, blank=True)

    #__Client_FIELDS__END

    class Meta:
        verbose_name        = _("Client")
        verbose_name_plural = _("Client")


class Approvi(models.Model):

    #__Approvi_FIELDS__
    ref_four = models.CharField(max_length=255, null=True, blank=True)
    ref_mar = models.CharField(max_length=255, null=True, blank=True)

    #__Approvi_FIELDS__END

    class Meta:
        verbose_name        = _("Approvi")
        verbose_name_plural = _("Approvi")


class Fournisseur(models.Model):

    #__Fournisseur_FIELDS__
    ref_four = models.CharField(max_length=255, null=True, blank=True)
    nom_four = models.CharField(max_length=255, null=True, blank=True)
    adress_four = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Fournisseur_FIELDS__END

    class Meta:
        verbose_name        = _("Fournisseur")
        verbose_name_plural = _("Fournisseur")



#__MODELS__END
