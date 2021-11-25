from builtins import super

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User, Resident, Official, Profile

class DateInput(forms.DateInput):
    input_type = 'date'

class ResidentSignUpForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(max_length=150, required=False)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    age = forms.IntegerField()
    birthday = forms.DateField(required=False, widget=DateInput)
    # house_number = forms.IntegerField(required=False)
    # street = forms.CharField(max_length=150,required=False)
    # SINGLE = 'Single'
    # MARRIED = 'Married'
    # DIVORCED = 'Divorced'
    # WIDOWED = 'Widowed'
    # CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    # civil_status = forms.ChoiceField(choices=CIVIL_STATUS, required=False)
    # religion = forms.CharField(max_length=150, required=False)
    # nationality = forms.CharField(max_length=150, required=False)
    # phone_number = forms.IntegerField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'last_name', 'first_name', 'middle_name', 'gender', 'age', 'birthday')

    def __init__(self, *args, **kwargs):
        super(ResidentSignUpForm, self).__init__(*args, **kwargs)
        # self.fields['phone_number'].required = False
        # self.fields['house_number'].required = False
        # self.fields['street'].required = False
        self.fields['middle_name'].required = False
        self.fields['birthday'].required = False

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_resident = True
        user.email = self.cleaned_data.get('email')
        user.last_name = self.cleaned_data.get('last_name').capitalize()
        user.first_name = self.cleaned_data.get('first_name').capitalize()
        user.middle_name = self.cleaned_data.get('middle_name').capitalize()
        user.gender = self.cleaned_data.get('gender')
        user.age = self.cleaned_data.get('age')
        user.birthday = self.cleaned_data.get('birthday')
        # user.house_number = self.cleaned_data.get('house_number')
        # user.street = self.cleaned_data.get('street').capitalize()
        # user.civil_status = self.cleaned_data.get('civil_status')
        # user.religion = self.cleaned_data.get('religion').capitalize()
        # user.nationality = self.cleaned_data.get('nationality').capitalize()
        # user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        resident = Resident.objects.create(user=user)
        user.email = self.cleaned_data.get('email')
        resident.last_name = self.cleaned_data.get('last_name').capitalize()
        resident.first_name = self.cleaned_data.get('first_name').capitalize()
        resident.middle_name = self.cleaned_data.get('middle_name').capitalize()
        resident.gender = self.cleaned_data.get('gender')
        resident.age = self.cleaned_data.get('age')
        resident.birthday = self.cleaned_data.get('birthday')
        # resident.house_number = self.cleaned_data.get('house_number')
        # resident.street = self.cleaned_data.get('street').capitalize()
        # resident.civil_status = self.cleaned_data.get('civil_status')
        # resident.religion = self.cleaned_data.get('religion').capitalize()
        # resident.nationality = self.cleaned_data.get('nationality').capitalize()
        # resident.phone_number = self.cleaned_data.get('phone_number')
        resident.save()
        profile = Profile.objects.create(user=user)
        user.email = self.cleaned_data.get('email')
        profile.last_name = self.cleaned_data.get('last_name').capitalize()
        profile.first_name = self.cleaned_data.get('first_name').capitalize()
        profile.middle_name = self.cleaned_data.get('middle_name').capitalize()
        profile.gender = self.cleaned_data.get('gender')
        profile.age = self.cleaned_data.get('age')
        profile.birthday = self.cleaned_data.get('birthday')
        # profile.house_number = self.cleaned_data.get('house_number')
        # profile.street = self.cleaned_data.get('street').capitalize()
        # profile.civil_status = self.cleaned_data.get('civil_status')
        # profile.religion = self.cleaned_data.get('religion').capitalize()
        # profile.nationality = self.cleaned_data.get('nationality').capitalize()
        # profile.phone_number = self.cleaned_data.get('phone_number')
        profile.save()
        return user


class OfficialSignUpForm(UserCreationForm):
    email = forms.EmailField()
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    middle_name = forms.CharField(max_length=150)
    GENDER_MALE = 'Male'
    GENDER_FEMALE = 'Female'
    GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    age = forms.IntegerField()
    birthday = forms.DateField( widget=DateInput)
    house_number = forms.IntegerField()
    street = forms.CharField(max_length=150)
    SINGLE = 'Single'
    MARRIED = 'Married'
    DIVORCED = 'Divorced'
    WIDOWED = 'Widowed'
    CIVIL_STATUS = [(SINGLE, 'Single'), (MARRIED, 'Married'), (DIVORCED, 'Divorced'), (WIDOWED, 'Widowed')]
    civil_status = forms.ChoiceField(choices=CIVIL_STATUS)
    religion = forms.CharField(max_length=150)
    nationality = forms.CharField(max_length=150)
    phone_number = forms.IntegerField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','email', 'last_name', 'first_name', 'middle_name', 'gender', 'age', 'birthday',
                  'house_number', 'street', 'civil_status', 'religion', 'nationality', 'phone_number')

    def __init__(self, *args, **kwargs):
        super(OfficialSignUpForm, self).__init__(*args, **kwargs)
        self.fields['phone_number'].required = False

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_official = True
        user.is_staff = True
        user.email = self.cleaned_data.get('email')
        user.last_name = self.cleaned_data.get('last_name').capitalize()
        user.first_name = self.cleaned_data.get('first_name').capitalize()
        user.middle_name = self.cleaned_data.get('middle_name').capitalize()
        user.gender = self.cleaned_data.get('gender')
        user.age = self.cleaned_data.get('age')
        user.birthday = self.cleaned_data.get('birthday')
        user.house_number = self.cleaned_data.get('house_number')
        user.street = self.cleaned_data.get('street').capitalize()
        user.civil_status = self.cleaned_data.get('civil_status')
        user.religion = self.cleaned_data.get('religion').capitalize()
        user.nationality = self.cleaned_data.get('nationality').capitalize()
        user.phone_number = self.cleaned_data.get('phone_number')
        user.save()
        official = Official.objects.create(user=user)
        user.email = self.cleaned_data.get('email')
        official.last_name = self.cleaned_data.get('last_name').capitalize()
        official.first_name = self.cleaned_data.get('first_name').capitalize()
        official.middle_name = self.cleaned_data.get('middle_name').capitalize()
        official.gender = self.cleaned_data.get('gender')
        official.age = self.cleaned_data.get('age')
        official.birthday = self.cleaned_data.get('birthday')
        official.house_number = self.cleaned_data.get('house_number')
        official.street = self.cleaned_data.get('street').capitalize()
        official.civil_status = self.cleaned_data.get('civil_status')
        official.religion = self.cleaned_data.get('religion').capitalize()
        official.nationality = self.cleaned_data.get('nationality').capitalize()
        official.phone_number = self.cleaned_data.get('phone_number')
        official.save()
        profile = Profile.objects.create(user=user)
        user.email = self.cleaned_data.get('email')
        profile.last_name = self.cleaned_data.get('last_name').capitalize()
        profile.first_name = self.cleaned_data.get('first_name').capitalize()
        profile.middle_name = self.cleaned_data.get('middle_name').capitalize()
        profile.gender = self.cleaned_data.get('gender')
        profile.age = self.cleaned_data.get('age')
        profile.birthday = self.cleaned_data.get('birthday')
        profile.house_number = self.cleaned_data.get('house_number')
        profile.street = self.cleaned_data.get('street').capitalize()
        profile.civil_status = self.cleaned_data.get('civil_status')
        profile.religion = self.cleaned_data.get('religion').capitalize()
        profile.nationality = self.cleaned_data.get('nationality').capitalize()
        profile.phone_number = self.cleaned_data.get('phone_number')
        profile.save()
        return user



class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email','last_name', 'first_name', 'middle_name', 'gender', 'age', 'birthday',
               'civil_status', 'religion', 'nationality', 'phone_number']
        widgets = {
            'birthday': DateInput(),
        }

        def __init__(self, *args, **kwargs):
            super(UserUpdateForm, self).__init__(*args, **kwargs)
            # self.fields['phone_number'].required = False
            # self.fields['house_number'].required = False
            # self.fields['street'].required = False
            self.fields['middle_name'].required = False
            self.fields['civil_status'].required = False


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio']

