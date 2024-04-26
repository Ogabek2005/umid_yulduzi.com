from django.db import models
from django.core.validators import RegexValidator
phone_validator = RegexValidator(regex=r"^\+998\d{9}$", message='Telefon raqam xato kiritildi',
                                 code="invalid_phone")
card_validator = RegexValidator(regex=r'^\d+$', message="Faqat sonlardan tashkil topgan qiymat kiriting.")
passport_validator = RegexValidator(regex=r'^[A-Z]+$', message="Passport seriya xato kiritildi")

class BaseModel(models.Model):
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Claim(BaseModel):
    phone_number = models.CharField(max_length=13,
                                    validators =[phone_validator],
                                    verbose_name='Phone number'
                                    )
    first_name = models.CharField(max_length=250,
                                  verbose_name='First Name'
                                 )
    last_name = models.CharField(max_length=250,
                                 verbose_name='Last Name'
                                )
    description = models.TextField()
    card_number = models.CharField(max_length=16,
                                   validators = [card_validator],
                                   verbose_name='Card number')
    passport_series = models.CharField(max_length=2,
                                       validators = [passport_validator],
                                       verbose_name='Passport series'
                                       )
    passport_number = models.CharField(max_length=7,
                                      validators = [card_validator],
                                      verbose_name='Passport number'
                                      )
    location = models.CharField(max_length=255,
                                verbose_name='Location',
                                blank=True,
                                null=True
                                )
    media_file = models.FileField(upload_to='claim_media/')

    def __str__(self):
        return f"{self.id}-{self.first_name}-{self.last_name}"
    
class Confirmation(BaseModel):
    claim = models.ForeignKey(Claim,
                              related_name='confirmations',
                              verbose_name='Confirmation',
                              on_delete=models.PROTECT
                              )
    amount = models.DecimalField(max_digits=30,
                                 decimal_places=2,
                                 verbose_name='Amount'
                                 )
    dedlayn = models.DateTimeField(
                                   blank=True,
                                   null=True
                                   )
    
    def __str__(self):
        return f"{self.id}-{self.claim.first_name}-{self.claim.last_name}-{self.amount}"
    
class Sponsor(BaseModel):
    claim = models.ForeignKey(Claim,
                              related_name='sponsors',
                              verbose_name='Sponsor',
                              on_delete=models.PROTECT,
                            )
    sponsor_amount = models.DecimalField(max_digits=30,
                                         decimal_places=2,
                                         verbose_name='Sponsor amount',
                                         )
    sponsor_name = models.CharField(max_length=255,
                                    verbose_name='Sponsor name',
                                    blank=True,
                                    null = True,
                                    default = 'Anonim',
                                    )
    comment = models.TextField(
                               blank=True,
                               null=True,
                               verbose_name='Comment',
                               )
    payment_type = models.CharField(
                                    max_length=250,
                                    verbose_name='Payment type',
                                    )
    
    def __str__(self) -> str:
        return f"{self.id}-{self.sponsor_amount}-{self.sponsor_name}"
    
class Blog(BaseModel):
    title = models.CharField(
                             max_length=255,
                             verbose_name='Title',
                             )
    description = models.TextField()
    media_file = models.FileField(
                                  upload_to='blog_media/',
                                  verbose_name='Media file',
                                  )
    
    def __str__(self) -> str:
        return f"{self.id}-{self.title}-{self.description}"