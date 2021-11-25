from django.db import models
from django.contrib.auth.models import AbstractUser, User
from PIL import Image


class User(AbstractUser):
    is_resident = models.BooleanField(default=False)
    is_official = models.BooleanField(default=False)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    last_name = models.CharField(max_length=150, default='None')
    first_name = models.CharField(max_length=150, default='None')
    middle_name = models.CharField(max_length=150, default='None', null=True, blank=True)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='None')
    age = models.IntegerField(default='00')
    birthday = models.DateField( default='1111-11-11', null=True, blank=True)
    house_number = models.IntegerField(default='00', null=True, blank=True)
    street = models.CharField(max_length=150, default='None', null=True, blank=True)
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'
    CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    civil_status = models.CharField(max_length=8, choices=CIVIL_STATUS, default='None', null=True, blank=True)
    religion = models.CharField(max_length=150, default='None', null=True, blank=True)
    nationality = models.CharField(max_length=150, default='None', null=True, blank=True)
    phone_number = models.IntegerField(default='0000000000', null=True, blank=True)
    #
    # def __str__(self):
    #     return {self.user.username}

    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)
        img = Image.open(self.image.path)

        # When image height is greater than its width
        if img.height > img.width:
            # make square by cutting off equal amounts top and bottom
            left = 0
            right = img.width
            top = (img.height - img.width) / 2
            bottom = (img.height + img.width) / 2
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

        # When image width is greater than its height
        elif img.width > img.height:
            # make square by cutting off equal amounts left and right
            left = (img.width - img.height) / 2
            right = (img.width + img.height) / 2
            top = 0
            bottom = img.height
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            img.save(self.image.path)

class Resident(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    last_name = models.CharField(max_length=150, default='None')
    first_name = models.CharField(max_length=150, default='None')
    middle_name = models.CharField(max_length=150, default='None', null=True, blank=True)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='None')
    age = models.IntegerField(default='00')
    birthday = models.DateField(default='1111-11-11', null=True, blank=True)
    house_number = models.IntegerField(default='00', null=True, blank=True)
    street = models.CharField(max_length=150, default='None', null=True, blank=True)
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'
    CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    civil_status = models.CharField(max_length=8, choices=CIVIL_STATUS, default='None', null=True, blank=True)
    religion = models.CharField(max_length=150, default='None', null=True, blank=True)
    nationality = models.CharField(max_length=150, default='None', null=True, blank=True)
    phone_number = models.IntegerField(default='0000000000', null=True, blank=True)

    def __str__(self):
        if self is not None:
            return self.user.username

    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)
        img = Image.open(self.image.path)

        # When image height is greater than its width
        if img.height > img.width:
            # make square by cutting off equal amounts top and bottom
            left = 0
            right = img.width
            top = (img.height - img.width) / 2
            bottom = (img.height + img.width) / 2
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

        # When image width is greater than its height
        elif img.width > img.height:
            # make square by cutting off equal amounts left and right
            left = (img.width - img.height) / 2
            right = (img.width + img.height) / 2
            top = 0
            bottom = img.height
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            img.save(self.image.path)

class Official(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    last_name = models.CharField(max_length=150, default='None')
    first_name = models.CharField(max_length=150, default='None')
    middle_name = models.CharField(max_length=150, default='None')
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='None')
    age = models.IntegerField(default='00')
    birthday = models.DateField(default='1111-11-11')
    house_number = models.IntegerField(default='00')
    street = models.CharField(max_length=150, default='None')
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'
    CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    civil_status = models.CharField(max_length=8, choices=CIVIL_STATUS, default='None')
    religion = models.CharField(max_length=150, default='None')
    nationality = models.CharField(max_length=150, default='None')
    phone_number = models.IntegerField(default='0000000000', null=True, blank=True)

    def __str__(self):
        if self is not None:
            return self.user.username

    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)
        img = Image.open(self.image.path)

        # When image height is greater than its width
        if img.height > img.width:
            # make square by cutting off equal amounts top and bottom
            left = 0
            right = img.width
            top = (img.height - img.width) / 2
            bottom = (img.height + img.width) / 2
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

        # When image width is greater than its height
        elif img.width > img.height:
            # make square by cutting off equal amounts left and right
            left = (img.width - img.height) / 2
            right = (img.width + img.height) / 2
            top = 0
            bottom = img.height
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            img.save(self.image.path)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    last_name = models.CharField(max_length=150, default='None')
    first_name = models.CharField(max_length=150, default='None')
    middle_name = models.CharField(max_length=150, default='None', null=True, blank=True)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='None')
    age = models.IntegerField(default='00')
    birthday = models.DateField(default='1111-11-11', null=True, blank=True)
    house_number = models.IntegerField(default='00', null=True, blank=True)
    street = models.CharField(max_length=150, default='None', null=True, blank=True)
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'
    CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    civil_status = models.CharField(max_length=8, choices=CIVIL_STATUS, default='None', null=True, blank=True)
    religion = models.CharField(max_length=150, default='None', null=True, blank=True)
    nationality = models.CharField(max_length=150, default='None', null=True, blank=True)
    phone_number = models.IntegerField(blank=True, null=True)
    bio = models.TextField(max_length=300, default='None', null=True, blank=True)
    # def __str__(self):
    #     return f'{self.user.username} Profile'
    #
    # def save(self):
    #     super().save()
    #
    #     img = Image.open(self.image.path)
    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

    def __str__(self):
        if self is not None:
            return self.user.username

    def save(self, *args, **kwargs):
        super().save( *args, **kwargs)
        img = Image.open(self.image.path)

        # When image height is greater than its width
        if img.height > img.width:
            # make square by cutting off equal amounts top and bottom
            left = 0
            right = img.width
            top = (img.height - img.width) / 2
            bottom = (img.height + img.width) / 2
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)

        # When image width is greater than its height
        elif img.width > img.height:
            # make square by cutting off equal amounts left and right
            left = (img.width - img.height) / 2
            right = (img.width + img.height) / 2
            top = 0
            bottom = img.height
            img = img.crop((left, top, right, bottom))
            # Resize the image to 300x300 resolution
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
            img.save(self.image.path)