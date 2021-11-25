from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Blotter, People, BPermit, APost, TermOfficial, TermNow, Vaccination, Household, BPTransaction, \
    Resolution, CovidVac, CovidCase, SVaccination, PVaccination, Pregnant

from django.forms import ModelForm

class BlotterUpdateForm(forms.ModelForm):
    class Meta:
        model = Blotter
        fields = ('victim_lastname', 'victim_firstname', 'victim_middle_name', 'gender', 'age', 'birthday', 'birthplace',
                  'civil_status', 'religion', 'nationality', 'phone_number', 'address', 'suspect_lastname', 'suspect_firstname',
                  'suspect_middle_name', 'suspect_gender', 'suspect_age', 'suspect_birthday', 'suspect_birthplace',
                  'suspect_civil_status', 'suspect_religion', 'suspect_nationality', 'suspect_phone_number', 'suspect_address',
                  'suspect_height', 'suspect_weight', 'suspect_description', 'narrative_report', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Blotter'))

class DateInput(forms.DateInput):
    input_type = 'date'

class PeopleUpdateForm(forms.ModelForm):
    class Meta:
        model = People
        fields = ('last_name', 'first_name', 'middle_name', 'gender', 'age', 'birthday', 'birthplace',
                  'house_number', 'street', 'civil_status', 'religion', 'nationality', 'phone_number', 'PWD', 'image', 'status', 'year_of_residency')
        widgets = {
            'birthday': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Resident'))

class BPermitUpdateForm(forms.ModelForm):
    class Meta:
        model = BPermit
        fields = ('business_name', 'location', 'operator_lastname', 'operator_firstname', 'operator_middlename', 'address', 'status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Permit'))

# bpermit transaction
class BPTUpdateForm(forms.ModelForm):
    class Meta:
        model = BPTransaction
        fields = ('business_name', 'transaction_title', 'contact_person', 'contact_number', 'mode_of_payment', 'transfer_of'
                  , 'transaction_amount', 'actual_amount', 'approved_by', 'remarks', 'payment_status')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Transaction'))

class BPTAddForm(ModelForm):
    business_name = forms.ModelChoiceField(queryset=BPermit.objects.all())
    class Meta:
        model = BPTransaction

        fields = ('date', 'business_name', 'transaction_title', 'contact_person', 'contact_number', 'mode_of_payment', 'transfer_of'
                  , 'transaction_amount', 'actual_amount', 'approved_by', 'remarks', 'payment_status')
        widgets = {
            'date': DateInput(),
        }





class APostUpdateForm(forms.ModelForm):
    class Meta:
        model = APost
        fields = ('content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Post'))


class TOUpdateForm(forms.ModelForm):
    class Meta:
        model = TermOfficial
        fields = ('start_of_term', 'end_of_term', 'last_name', 'first_name', 'middle_name', 'gender', 'age', 'address', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Official'))

class TNUpdateForm(forms.ModelForm):
    class Meta:
        model = TermNow
        fields = ('Barangay_chairman', 'peace_and_order', 'environmental_protection_and_safety', 'health_and_sanitation', 'public_works_and_infrastructure', 'law_ordinances_education_and_family', 'transportation_and_communication', 'budget_and_appropriation', 'sk_chairman', 'sk_councilor1'
                  , 'sk_councilor2', 'sk_councilor3', 'sk_councilor4', 'barangay_secretary', 'barangay_treasurer', 'barangay_accounting_clerk', 'barangay_clerk', 'assistant_clerk', 'barangay_day_care_worker', 'barangay_agrarian'
                  , 'barangay_health_worker1', 'barangay_health_worker2', 'barangay_health_worker3', 'barangay_health_worker4', 'barangay_health_worker5', 'barangay_health_worker6', 'barangay_health_worker7', 'barangay_health_worker8', 'barangay_health_worker9', 'barangay_health_worker10'
                  , 'barangay_health_worker11', 'barangay_health_worker12', 'barangay_tanod1', 'barangay_tanod2', 'barangay_tanod3', 'barangay_tanod4', 'barangay_tanod5', 'barangay_tanod6', 'barangay_tanod7', 'barangay_tanod8'
                  , 'barangay_tanod9', 'barangay_tanod10', 'barangay_justice1', 'barangay_justice2', 'barangay_justice3', 'barangay_justice4', 'barangay_justice5', 'barangay_justice6', 'barangay_justice7', 'barangay_justice8'
                  , 'barangay_justice9', 'barangay_justice10', 'barangay_helper_and_driver1', 'barangay_helper_and_driver2', 'barangay_helper_and_driver3', 'barangay_helper_and_driver4', 'barangay_helper_and_driver5', 'barangay_helper_and_driver6', 'barangay_helper_and_driver7', 'term_year')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Term'))

        # vaccination

class VUpdateForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = ('last_name', 'first_name', 'middle_name', 'gender', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Vaccination'))

class SVUpdateForm(forms.ModelForm):
    class Meta:
        model = SVaccination
        fields = ('last_name', 'first_name', 'middle_name', 'gender', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Vaccination'))

class PVUpdateForm(forms.ModelForm):
    class Meta:
        model = PVaccination
        fields = ('last_name', 'first_name', 'middle_name', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Vaccination'))




class PeopleAddForm(ModelForm):

    class Meta:
        model = People
        fields = ('last_name', 'first_name', 'middle_name', 'gender', 'age', 'birthday', 'birthplace',
                  'house_number', 'street', 'civil_status', 'religion', 'nationality', 'phone_number', 'PWD', 'image',
                  'status', 'year_of_residency')
        widgets = {
            'birthday': DateInput(),
        }


class BlotterAddForm(ModelForm):

    class Meta:
        model = Blotter
        fields = ('victim_lastname', 'victim_firstname', 'victim_middle_name', 'gender', 'age', 'birthday', 'birthplace',
                  'civil_status', 'religion', 'nationality', 'phone_number', 'address', 'suspect_lastname', 'suspect_firstname',
                  'suspect_middle_name', 'suspect_gender', 'suspect_age', 'suspect_birthday', 'suspect_birthplace',
                  'suspect_civil_status', 'suspect_religion', 'suspect_nationality', 'suspect_phone_number', 'suspect_address',
                  'suspect_height', 'suspect_weight', 'suspect_description', 'narrative_report', 'status')
        widgets = {
            'birthday': DateInput(),
            'suspect_birthday': DateInput(),
        }

class HouseholdAddForm(forms.ModelForm):

    class Meta:
        model = Household
        fields = ('family_name', 'number_of_member', 'members')

class HhUpdateForm(forms.ModelForm):
    class Meta:
        model = Household
        fields = ('family_name', 'number_of_member', 'members')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Household'))


#resolution
class RSAddForm(ModelForm):
    class Meta:
        model = Resolution

        fields = ('resolution_number', 'session_date', 'resolution_author', 'resolution_co_author', 'forwarded_to', 'status'
                  , 'resolution_details_summary', 'notes')
        widgets = {
            'session_date': DateInput(),
        }

class RSUpdateForm(forms.ModelForm):
    class Meta:
        model = Resolution
        fields = ( 'resolution_number', 'session_date', 'resolution_author', 'resolution_co_author', 'forwarded_to', 'status'
                   , 'resolution_details_summary', 'notes')
        widgets = {
            'session_date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Resolution'))


#covidvac
class CVAddForm(ModelForm):
    class Meta:
        model = CovidVac

        fields = ('name', 'gender', 'age', 'birthday', 'vaccine_type', 'status'
                  , 'with_covid19_history')
        widgets = {
            'birthday': DateInput(),
        }

class CVUpdateForm(forms.ModelForm):
    class Meta:
        model = CovidVac
        fields = ( 'name', 'gender', 'age', 'birthday', 'vaccine_type', 'status'
                   , 'with_covid19_history')
        widgets = {
            'birthday': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Vaccination'))

#covidcase
class CCAddForm(ModelForm):
    class Meta:
        model = CovidCase

        fields = ('name', 'gender', 'age', 'birthday', 'status'
                  , 'recent_contacts')
        widgets = {
            'birthday': DateInput(),
        }

class CCUpdateForm(forms.ModelForm):
    class Meta:
        model = CovidCase
        fields = ( 'name', 'gender', 'age', 'birthday', 'status'
                   , 'recent_contacts')
        widgets = {
            'birthday': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save Case'))

#pregnant
class PAddForm(ModelForm):
    class Meta:
        model = Pregnant

        fields = ('last_name', 'first_name', 'middle_name', 'age', 'expected_labor', 'status')
        widgets = {
            'expected_labor': DateInput(),
        }

class PUpdateForm(forms.ModelForm):
    class Meta:
        model = Pregnant
        fields = ( 'last_name', 'first_name', 'middle_name', 'age', 'expected_labor', 'status')
        widgets = {
            'expected_labor': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Save'))

