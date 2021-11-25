from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User
from django.urls import reverse
from PIL import Image

class People(models.Model):
    image = models.ImageField(default='default.png', upload_to='R_profile_pics')
    logo1 = models.ImageField(default='logo1.png')
    logo2 = models.ImageField(default='logo2.png')
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    birthday = models.DateField(default='00/00/0000', blank=True)

    birthplace = models.CharField(max_length=150, default='Bauan, Batangas')
    year_of_residency = models.IntegerField(default='0000')
    house_number = models.IntegerField()
    street = models.CharField(max_length=150)
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'
    CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    civil_status = models.CharField(max_length=8, choices=CIVIL_STATUS)
    religion = models.CharField(max_length=150)
    nationality = models.CharField(max_length=150, default='Filipino')
    phone_number = models.IntegerField(default=None, blank=True, null=True)
    Yes = 'Yes'
    No = 'No'
    CHOICES = [(Yes, 'Yes'), (No, 'No')]
    PWD = models.CharField(max_length=3, choices=CHOICES, blank=True, null=True)
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'
    STATUS_CHOICES = [(STATUS_ACTIVE, 'Active'), (STATUS_INACTIVE, 'Inactive')]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        super().save()
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


    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('people-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.last_name = self.last_name.capitalize()
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.street = self.street.capitalize()
        self.religion = self.religion.capitalize()
        self.nationality = self.nationality.capitalize()

#         addition
# blotter
class Blotter(models.Model):
    logo1 = models.ImageField(default='logo1.png')
    victim_lastname = models.CharField(max_length=150)
    victim_firstname = models.CharField(max_length=150)
    victim_middle_name = models.CharField(max_length=150, null=True, blank=True)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    birthday = models.DateField( blank=True, null=True)
    birthplace = models.CharField(max_length=150, default='Bauan, Batangas')
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'
    CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    civil_status = models.CharField(max_length=8, choices=CIVIL_STATUS, null=True, blank=True)
    religion = models.CharField(max_length=150, null=True, blank=True)
    nationality = models.CharField(max_length=150, default='Filipino', null=True, blank=True)
    phone_number = models.IntegerField( blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    suspect_lastname = models.CharField(max_length=150)
    suspect_firstname = models.CharField(max_length=150)
    suspect_middle_name = models.CharField(max_length=150, null=True, blank=True)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    suspect_gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    suspect_age = models.IntegerField( blank=True, null=True)
    suspect_birthday = models.DateField( blank=True, null=True)
    suspect_birthplace = models.CharField(max_length=150, default='Bauan, Batangas', null=True, blank=True)
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'
    CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    suspect_civil_status = models.CharField(max_length=8, choices=CIVIL_STATUS, default='None', null=True, blank=True)
    suspect_religion = models.CharField(max_length=150, null=True, blank=True)
    suspect_nationality = models.CharField(max_length=150, default='Filipino', null=True, blank=True)
    suspect_phone_number = models.IntegerField( blank=True, null=True)
    suspect_address = models.CharField(max_length=150, blank=True, null=True)
    suspect_height = models.IntegerField( blank=True, null=True)
    suspect_weight = models.IntegerField( blank=True, null=True)
    suspect_description = models.TextField( blank=True, null=True)
    narrative_report = models.TextField()
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'
    STATUS_CHOICES = [(STATUS_ACTIVE, 'Active'), (STATUS_INACTIVE, 'Inactive')]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.suspect_lastname

    def get_absolute_url(self):
        return reverse('b-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.victim_lastname = self.victim_lastname.capitalize()
        self.victim_firstname = self.victim_firstname.capitalize()

        self.suspect_lastname = self.suspect_lastname.capitalize()
        self.suspect_firstname = self.suspect_firstname.capitalize()


# barangay permit
class BPermit(models.Model):
    logo1 = models.ImageField(default='logo1.png')
    business_name = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    operator_lastname = models.CharField(max_length=150)
    operator_firstname = models.CharField(max_length=150)
    operator_middlename = models.CharField(max_length=150, null=True, blank=True)
    address = models.CharField(max_length=150)
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'
    STATUS_CHOICES = [(STATUS_ACTIVE, 'Active'), (STATUS_INACTIVE, 'Inactive')]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    date_issued = models.DateField(default=timezone.now)
    closure_date = models.DateField(default=timezone.now, blank=True, null=True)
    closure_reason = models.TextField( blank=True, null=True)
    contact_person = models.CharField(max_length=150, null=True, blank=True)
    contact_number = models.IntegerField( blank=True, null=True)
    classification = models.CharField(max_length=150, null=True, blank=True)
    remarks = models.TextField( blank=True, null=True)
    type_of_ownership = models.CharField(max_length=150, null=True, blank=True)
    approved_by = models.CharField(max_length=150, null=True, blank=True)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.business_name

    def get_absolute_url(self):
        return reverse('bp-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.business_name = self.business_name
        self.location = self.location.upper()
        self.operator_lastname = self.operator_lastname.upper()
        self.operator_firstname = self.operator_firstname.upper()
        # self.operator_middlename = self.operator_middlename.upper()
        self.address = self.address.upper()

# bpermit - transactions
class BPTransaction(models.Model):
    date = models.DateField(default=timezone.now)
    business_name = models.CharField(max_length=150, blank=True, null=True)
    transaction_title = models.CharField(max_length=150)
    contact_person = models.CharField(max_length=150)
    contact_number = models.IntegerField()
    mode_of_payment = models.CharField(max_length=150)
    transfer_of = models.CharField(max_length=150)
    transaction_amount = models.IntegerField()
    actual_amount = models.IntegerField()
    approved_by = models.CharField(max_length=150)
    remarks = models.TextField( blank=True, null=True)
    Full = 'Full'
    Partial = 'Partial'
    STATUS_CHOICES = [(Full, 'Full'), (Partial, 'Partial')]
    payment_status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.transaction_title

    def get_absolute_url(self):
        return reverse('bpt-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.contact_person = self.contact_person.upper()
        self.approved_by = self.approved_by.upper()



class APost(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('apost-detail', kwargs={'pk': self.pk})

class TermOfficial(models.Model):
    image = models.ImageField(default='default.png', upload_to='O_profile_pics')
    One = 'Barangay Chairman'
    Two = 'Peace and Order'
    Three = 'Environmental Protection and Safety'
    Four = 'Health and Sanitation'
    Five = 'Public Works and Infrastructure'
    Six = 'Law Ordinances, Education and Family'
    Seven = 'Transportation and Communication'
    Eight = 'Budget and Appropriation'
    Nine = 'SK Chairman'
    Ten = 'SK Councilor'
    Eleven = 'Barangay Secretary'
    Twelve = 'Barangay Treasurer'
    Thirteen = 'Barangay Accounting Clerk'
    Fourteen = 'Barangay Clerk'
    Fifteen = 'Assistant Clerk'
    Sixteen = 'Barangay Day Care Worker'
    Seventeen = 'Barangay Agrarian'
    Eighteen = 'Barangay Health Worker'
    Nineteen = 'Barangay Tanod'
    Twenty = 'Barangay Justice'
    Twenty1 = 'Barangay Helper and Driver'
    POSITION_CHOICES = [(One, 'Barangay Captain'), (Two, 'Peace and Order'), (Three, 'Environmental Protection and Safety'), (Four, 'Health and Sanitation')
        , (Five, 'Public Works and Infrastructure'), (Six, 'Law Ordinances, Education and Family'), (Seven, 'Transportation and Communication'), (Eight, 'Budget and Appropriation')
        , (Nine, 'SK Chairman'), (Ten, 'SK Councilor'), (Eleven, 'Barangay Secretary'), (Twelve, 'Baranfay Treasurer')
        , (Thirteen, 'Barangay Accounting Clerk'), (Fourteen, 'Barangay Clerk'), (Fifteen, 'Assistant Clerk'), (Sixteen, 'Barangay Day Care Worker')
        , (Seventeen, 'Barangay Agrarian'), (Eighteen, 'Barangay Health Worker'), (Nineteen, 'Barangay Tanod'),
                        (Twenty, 'Barangay Justice'), (Twenty1, 'Barangay Helper and Driver')]
    position = models.CharField(max_length=150, choices=POSITION_CHOICES)
    First = '2018'
    Second = '2022'
    TERM_CHOICES = [(First, '2018'), (Second, '2022')]
    start_of_term = models.CharField(max_length=8, choices=TERM_CHOICES)
    First = '2022'
    Second = '2026'
    TERM_CHOICES = [(First, '2022'), (Second, '2026')]
    end_of_term = models.CharField(max_length=8, choices=TERM_CHOICES)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    address = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super().save()
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

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('to-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.last_name = self.last_name.capitalize()
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.gender = self.gender.capitalize()
        self.address = self.address.capitalize()
        self.position = self.position.capitalize()

class TermNow(models.Model):
    Barangay_chairman = models.CharField(default='None', max_length=150)
    peace_and_order = models.CharField(default='None',max_length=150)
    environmental_protection_and_safety = models.CharField(default='None',max_length=150)
    health_and_sanitation = models.CharField(default='None',max_length=150)
    public_works_and_infrastructure = models.CharField(default='None',max_length=150)
    law_ordinances_education_and_family = models.CharField(default='None',max_length=150)
    transportation_and_communication = models.CharField(default='None',max_length=150)
    budget_and_appropriation = models.CharField(default='None',max_length=150)
    sk_chairman = models.CharField(default='None',max_length=150)
    sk_councilor1 = models.CharField(default='None',max_length=150)
    sk_councilor2 = models.CharField(default='None',max_length=150)
    sk_councilor3 = models.CharField(default='None',max_length=150)
    sk_councilor4 = models.CharField(default='None',max_length=150)
    barangay_secretary = models.CharField(default='None',max_length=150)
    barangay_treasurer = models.CharField(default='None',max_length=150)
    barangay_accounting_clerk = models.CharField(default='None',max_length=150)
    barangay_clerk = models.CharField(default='None',max_length=150)
    assistant_clerk = models.CharField(default='None',max_length=150)
    barangay_day_care_worker = models.CharField(default='None',max_length=150)
    barangay_agrarian = models.CharField(default='None',max_length=150)
    barangay_health_worker1 = models.CharField(default='None',max_length=150)
    barangay_health_worker2 = models.CharField(default='None',max_length=150)
    barangay_health_worker3 = models.CharField(default='None',max_length=150)
    barangay_health_worker4 = models.CharField(default='None',max_length=150)
    barangay_health_worker5 = models.CharField(default='None',max_length=150)
    barangay_health_worker6 = models.CharField(default='None',max_length=150)
    barangay_health_worker7 = models.CharField(default='None',max_length=150)
    barangay_health_worker8 = models.CharField(default='None',max_length=150)
    barangay_health_worker9 = models.CharField(default='None',max_length=150)
    barangay_health_worker10 = models.CharField(default='None',max_length=150)
    barangay_health_worker11 = models.CharField(default='None',max_length=150)
    barangay_health_worker12 = models.CharField(default='None',max_length=150)
    barangay_tanod1 = models.CharField(default='None',max_length=150)
    barangay_tanod2 = models.CharField(default='None',max_length=150)
    barangay_tanod3 = models.CharField(default='None',max_length=150)
    barangay_tanod4 = models.CharField(default='None',max_length=150)
    barangay_tanod5 = models.CharField(default='None',max_length=150)
    barangay_tanod6 = models.CharField(default='None',max_length=150)
    barangay_tanod7 = models.CharField(default='None',max_length=150)
    barangay_tanod8 = models.CharField(default='None',max_length=150)
    barangay_tanod9 = models.CharField(default='None',max_length=150)
    barangay_tanod10 = models.CharField(default='None',max_length=150)
    barangay_justice1 = models.CharField(default='None',max_length=150)
    barangay_justice2 = models.CharField(default='None',max_length=150)
    barangay_justice3 = models.CharField(default='None',max_length=150)
    barangay_justice4 = models.CharField(default='None',max_length=150)
    barangay_justice5 = models.CharField(default='None',max_length=150)
    barangay_justice6 = models.CharField(default='None',max_length=150)
    barangay_justice7 = models.CharField(default='None',max_length=150)
    barangay_justice8 = models.CharField(default='None',max_length=150)
    barangay_justice9 = models.CharField(default='None',max_length=150)
    barangay_justice10 = models.CharField(default='None',max_length=150)
    barangay_helper_and_driver1 = models.CharField(default='None',max_length=150)
    barangay_helper_and_driver2 = models.CharField(default='None',max_length=150)
    barangay_helper_and_driver3 = models.CharField(default='None',max_length=150)
    barangay_helper_and_driver4 = models.CharField(default='None',max_length=150)
    barangay_helper_and_driver5 = models.CharField(default='None',max_length=150)
    barangay_helper_and_driver6 = models.CharField(default='None',max_length=150)
    barangay_helper_and_driver7 = models.CharField(default='None',max_length=150)
    c1 = '2018 - 2022'
    c2 = '2022 - 2026'
    CHOICES = [(c1, '2018 - 2022'), (c2, '2022 - 2026')]
    term_year = models.CharField(max_length=12, choices=CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.term_year

    def get_absolute_url(self):
        return reverse('tn-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.Barangay_chairman = self.Barangay_chairman.upper()
        self.peace_and_order = self.peace_and_order.upper()
        self.environmental_protection_and_safety = self.environmental_protection_and_safety.upper()
        self.health_and_sanitation = self.health_and_sanitation.upper()
        self.public_works_and_infrastructure = self.public_works_and_infrastructure.upper()
        self.law_ordinances_education_and_family = self.law_ordinances_education_and_family.upper()
        self.transportation_and_communication = self.transportation_and_communication.upper()
        self.budget_and_appropriation = self.budget_and_appropriation.upper()
        self.sk_chairman = self.sk_chairman.upper()
        self.sk_councilor1 = self.sk_councilor1.upper()
        self.sk_councilor2 = self.sk_councilor2.upper()
        self.sk_councilor3 = self.sk_councilor3.upper()
        self.sk_councilor4 = self.sk_councilor4.upper()
        self.barangay_secretary = self.barangay_secretary.upper()
        self.barangay_treasurer = self.barangay_treasurer.upper()
        self.barangay_accounting_clerk = self.barangay_accounting_clerk.upper()
        self.barangay_clerk = self.barangay_clerk.upper()
        self.assistant_clerk = self.assistant_clerk.upper()
        self.barangay_day_care_worker = self.barangay_day_care_worker.upper()
        self.barangay_agrarian = self.barangay_agrarian.upper()
        self.barangay_health_worker1 = self.barangay_health_worker1.upper()
        self.barangay_health_worker2 = self.barangay_health_worker2.upper()
        self.barangay_health_worker3 = self.barangay_health_worker3.upper()
        self.barangay_health_worker4 = self.barangay_health_worker4.upper()
        self.barangay_health_worker5 = self.barangay_health_worker5.upper()
        self.barangay_health_worker6 = self.barangay_health_worker6.upper()
        self.barangay_health_worker7 = self.barangay_health_worker7.upper()
        self.barangay_health_worker8 = self.barangay_health_worker8.upper()
        self.barangay_health_worker9 = self.barangay_health_worker9.upper()
        self.barangay_health_worker10 = self.barangay_health_worker10.upper()
        self.barangay_health_worker11 = self.barangay_health_worker11.upper()
        self.barangay_health_worker12 = self.barangay_health_worker12.upper()
        self.barangay_tanod1 = self.barangay_tanod1.upper()
        self.barangay_tanod2 = self.barangay_tanod2.upper()
        self.barangay_tanod3= self.barangay_tanod3.upper()
        self.barangay_tanod4 = self.barangay_tanod4.upper()
        self.barangay_tanod5 = self.barangay_tanod5.upper()
        self.barangay_tanod6 = self.barangay_tanod6.upper()
        self.barangay_tanod7 = self.barangay_tanod7.upper()
        self.barangay_tanod8 = self.barangay_tanod8.upper()
        self.barangay_tanod9 = self.barangay_tanod9.upper()
        self.barangay_tanod10 = self.barangay_tanod10.upper()
        self.barangay_justice1 = self.barangay_justice1.upper()
        self.barangay_justice2= self.barangay_justice2.upper()
        self.barangay_justice3 = self.barangay_justice3.upper()
        self.barangay_justice4 = self.barangay_justice4.upper()
        self.barangay_justice5 = self.barangay_justice5.upper()
        self.barangay_justice6 = self.barangay_justice6.upper()
        self.barangay_justice7 = self.barangay_justice7.upper()
        self.barangay_justice8 = self.barangay_justice8.upper()
        self.barangay_justice9 = self.barangay_justice9.upper()
        self.barangay_justice10 = self.barangay_justice10.upper()
        self.barangay_helper_and_driver1 = self.barangay_helper_and_driver1.upper()
        self.barangay_helper_and_driver2 = self.barangay_helper_and_driver2.upper()
        self.barangay_helper_and_driver3 = self.barangay_helper_and_driver3.upper()
        self.barangay_helper_and_driver4 = self.barangay_helper_and_driver4.upper()
        self.barangay_helper_and_driver5 = self.barangay_helper_and_driver5.upper()
        self.barangay_helper_and_driver6 = self.barangay_helper_and_driver6.upper()
        self.barangay_helper_and_driver7 = self.barangay_helper_and_driver7.upper()

# vaccination

class Vaccination(models.Model):
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    TYPE1 = 'Bacille-Calmette-Guerin'
    TYPE2 = 'Hepatitis B'
    TYPE3 = 'Pentavalent vaccine'
    TYPE4 = 'Oral Polio Vaccine o OPV'
    TYPE5 = 'Inactivated polio vaccine'
    TYPE6 = 'Pneumococcal conjugate vaccine o PCV'
    TYPE7 = 'Measles, Mumps, Rubella o MMR vaccine'
    TYPE8 = 'Rubella vaccine'
    TYPE_CHOICES = [(TYPE1, 'Bacille-Calmette-Guerin'), (TYPE2, 'Hepatitis B'), (TYPE3, 'Pentavalent vaccine'),
                    (TYPE4, 'Oral Polio Vaccine o OPV'), (TYPE5, 'Inactivated polio vaccine'), (TYPE6, 'Pneumococcal conjugate vaccine o PCV'),
                    (TYPE7, 'Measles, Mumps, Rubella o MMR vaccine'),(TYPE4, 'Rubella vaccine')]
    vaccine_type = models.CharField(max_length=80, choices=TYPE_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('v-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.last_name = self.last_name.capitalize()
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.gender = self.gender.capitalize()
        self.vaccine_type = self.vaccine_type.capitalize()

class Household(models.Model):
    family_name = models.CharField(max_length=150)
    number_of_member = models.IntegerField()
    members = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.family_name

    def get_absolute_url(self):
        return reverse('hh-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.family_name = self.family_name.upper()
        self.members = self.members.upper()


# resolution
class Resolution(models.Model):
    resolution_number = models.IntegerField()
    session_date = models.DateTimeField(default=timezone.now)
    resolution_author = models.CharField(max_length=150)
    resolution_co_author = models.CharField(max_length=150)
    forwarded_to = models.CharField(max_length=150)
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'
    STATUS_CHOICES = [(STATUS_ACTIVE, 'Active'), (STATUS_INACTIVE, 'Inactive')]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    resolution_details_summary = models.CharField(max_length=150, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.resolution_number

    def get_absolute_url(self):
        return reverse('rs-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.resolution_author = self.resolution_author.upper()
        self.resolution_co_author = self.resolution_co_author.upper()
        self.forwarded_to = self.forwarded_to.upper()

# covidvac
class CovidVac(models.Model):
    name = models.CharField(max_length=150)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    birthday = models.DateField( blank=True, null=True)
    TYPE1 = 'Sinovac'
    TYPE2 = 'Moderna'
    TYPE3 = 'Gamaleya(Sputnik Light)'
    TYPE4 = 'Gamaleya(Sputnik V)'
    TYPE5 = 'Janssen(Johnson & Johnson)'
    TYPE6 = 'Oxford/AstraZeneca'
    TYPE7 = 'Bharat Biotech'
    TYPE8 = 'Sinopharm(Beijing)'
    TYPE9 = 'Sinopharm(Wuhan)'
    TYPE10 = 'Pfizer/BioNTech'
    TYPE_CHOICES = [(TYPE1, 'Sinovac'), (TYPE2, 'Moderna'), (TYPE3, 'Gamaleya(Sputnik Light)'),
                    (TYPE4, 'Gamaleya(Sputnik V)'), (TYPE5, 'Janssen(Johnson & Johnson)'), (TYPE6, 'Oxford/AstraZeneca'),
                    (TYPE7, 'Bharat Biotech'), (TYPE8, 'Sinopharm(Beijing)'), (TYPE9, 'Sinopharm(Wuhan)'), (TYPE10, 'Pfizer/BioNTech')]
    vaccine_type = models.CharField(max_length=80, choices=TYPE_CHOICES)
    STATUS_ACTIVE = 'Complete'
    STATUS_INACTIVE = 'Incomplete'
    STATUS_CHOICES = [(STATUS_ACTIVE, 'Complete'), (STATUS_INACTIVE, 'Incomplete')]
    status = models.CharField(max_length=12, choices=STATUS_CHOICES)
    STATUS_YES = 'Yes'
    STATUS_NO = 'No'
    STATUS_CHOICE = [(STATUS_YES, 'Yes'), (STATUS_NO, 'No')]
    with_covid19_history = models.CharField(max_length=12, choices=STATUS_CHOICE, default="No", blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cv-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.name = self.name.upper()


# covicase
class CovidCase(models.Model):
    name = models.CharField(max_length=150)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    birthday = models.DateField( blank=True, null=True)
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'
    STATUS_CHOICES = [(STATUS_ACTIVE, 'Active'), (STATUS_INACTIVE, 'Inactive')]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    recent_contacts = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cc-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.name = self.name.upper()
        self.recent_contacts = self.recent_contacts.upper()

# vaccinationSenior

class SVaccination(models.Model):
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    age = models.IntegerField()
    TYPE1 = 'PCV13'
    TYPE2 = 'Pfizer(Anti Pneumonia)'
    TYPE3 = 'Prevnar 13'
    TYPE4 = 'Fluarix Tetra'
    TYPE5 = 'Influvac'
    TYPE6 = 'Vaxigrip'
    TYPE7 = 'Vaxigrip Tetra'
    TYPE8 = 'Other(Anti Pneumonia)'
    TYPE9 = 'Other(Anti Flu)'
    TYPE_CHOICES = [(TYPE1, 'PCV13'), (TYPE2, 'Pfizer(Anti Pneumonia)'), (TYPE3, 'Prevnar 13'),
                    (TYPE4, 'Fluarix Tetra'), (TYPE5, 'Influvac'), (TYPE6, 'Vaxigrip'),
                    (TYPE7, 'Vaxigrip Tetra'),(TYPE8, 'Other(Anti Pneumonia)'),(TYPE9, 'Other(Anti Flu)')]
    vaccine_type = models.CharField(max_length=80, choices=TYPE_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('sv-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.last_name = self.last_name.capitalize()
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.gender = self.gender.capitalize()
        self.vaccine_type = self.vaccine_type.capitalize()

# vaccinationPregnant

class PVaccination(models.Model):
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    age = models.IntegerField()
    TYPE1 = 'Tetanus Toxoid'
    TYPE2 = 'TT1 Vaccine'
    TYPE3 = 'Other'
    TYPE_CHOICES = [(TYPE1, 'Tetanus Toxoid'), (TYPE2, 'TT1 Vaccine'), (TYPE3, 'Other'),]
    vaccine_type = models.CharField(max_length=80, choices=TYPE_CHOICES)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('pv-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.last_name = self.last_name.capitalize()
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()
        self.vaccine_type = self.vaccine_type.capitalize()

# Pregnant

class Pregnant(models.Model):
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    age = models.IntegerField()
    expected_labor = models.DateField( blank=True, null=True)
    STATUS_ACTIVE = 'Active'
    STATUS_INACTIVE = 'Inactive'
    STATUS_CHOICES = [(STATUS_ACTIVE, 'Active'), (STATUS_INACTIVE, 'Inactive')]
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('accounts.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name

    def get_absolute_url(self):
        return reverse('p-detail', kwargs={'pk': self.pk})

    def clean(self):
        self.last_name = self.last_name.capitalize()
        self.first_name = self.first_name.capitalize()
        self.middle_name = self.middle_name.capitalize()