
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from django import forms

from .models import People, Blotter, BPermit, APost, TermOfficial, TermNow, Vaccination, Household, BPTransaction, \
    Resolution, CovidVac, CovidCase, SVaccination, PVaccination, Pregnant
from blog.models import Post

from django.views.generic import UpdateView
from .forms import BlotterUpdateForm, PeopleUpdateForm, APostUpdateForm, BPermitUpdateForm, TOUpdateForm, \
    TNUpdateForm, VUpdateForm, BPTUpdateForm, RSUpdateForm, CVUpdateForm, CCUpdateForm, SVUpdateForm, PVUpdateForm, PUpdateForm
from tempus_dominus.widgets import DatePicker
from .forms import PeopleAddForm, BlotterAddForm, HouseholdAddForm, BPTAddForm, RSAddForm, CVAddForm, CCAddForm, PAddForm

# updateviews new
@method_decorator(login_required, name='dispatch')
class BlotterUpdateView(UpdateView):
    model = Blotter
    form_class = BlotterUpdateForm
    template_name = 'dash/blotter_update_form.html'
@method_decorator(login_required, name='dispatch')
class PeopleUpdateView(UpdateView):
    model = People
    form_class = PeopleUpdateForm
    template_name = 'dash/people_update_form.html'
@method_decorator(login_required, name='dispatch')
class APostUpdateView(UpdateView):
    model = APost
    form_class = APostUpdateForm
    template_name = 'dash/apost_update_form.html'
@method_decorator(login_required, name='dispatch')
class BPermitUpdateView(UpdateView):
    model = BPermit
    form_class = BPermitUpdateForm
    template_name = 'dash/bpermit_update_form.html'
@method_decorator(login_required, name='dispatch')
class TOUpdateView(UpdateView):
    model = TermOfficial
    form_class = TOUpdateForm
    template_name = 'dash/to_update_form.html'
@method_decorator(login_required, name='dispatch')
class TNUpdateView(UpdateView):
    model = TermNow
    form_class = TNUpdateForm
    template_name = 'dash/tn_update_form.html'
@method_decorator(login_required, name='dispatch')
class VUpdateView(UpdateView):
    model = Vaccination
    form_class = VUpdateForm
    template_name = 'dash/v_update_form.html'
@method_decorator(login_required, name='dispatch')
class SVUpdateView(UpdateView):
    model = SVaccination
    form_class = SVUpdateForm
    template_name = 'dash/sv_update_form.html'
@method_decorator(login_required, name='dispatch')
class PVUpdateView(UpdateView):
    model = PVaccination
    form_class = PVUpdateForm
    template_name = 'dash/pv_update_form.html'
@method_decorator(login_required, name='dispatch')
class HhUpdateView(UpdateView):
    model = Household
    form_class = HouseholdAddForm
    template_name = 'dash/hh_update_form.html'
@method_decorator(login_required, name='dispatch')
class BPTUpdateView(UpdateView):
    model = BPTransaction
    form_class = BPTUpdateForm
    template_name = 'dash/bpt_update_form.html'
@method_decorator(login_required, name='dispatch')
class RSUpdateView(UpdateView):
    model = Resolution
    form_class = RSUpdateForm
    template_name = 'dash/rs_update_form.html'
@method_decorator(login_required, name='dispatch')
class CVUpdateView(UpdateView):
    model = CovidVac
    form_class = CVUpdateForm
    template_name = 'dash/cv_update_form.html'
@method_decorator(login_required, name='dispatch')
class CCUpdateView(UpdateView):
    model = CovidCase
    form_class = CCUpdateForm
    template_name = 'dash/cc_update_form.html'
@method_decorator(login_required, name='dispatch')
class PUpdateView(UpdateView):
    model = Pregnant
    form_class = PUpdateForm
    template_name = 'dash/p_update_form.html'



# div
@login_required
def home2(request):
    context = {
        'people': People.objects.all().order_by('last_name')
    }
    return render(request, 'dash/home2.html', context)

@method_decorator(login_required, name='dispatch')
class RListView(ListView):
    model = People
    template_name = 'dash/home2.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'people'
    ordering = ['last_name']
    # paginate_by = 5

@method_decorator(login_required, name='dispatch')
class RDetailView(DetailView):
    model = People

#addition
@login_required
def bc_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    people = get_object_or_404(People, pk=pk)

    template_path = 'dash/bc_pdf.html'
    context = {'people': people}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download run below
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display run below
    response['Content-Disposition'] = ' filename="Barangay-Clearance.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required
def ci_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    people = get_object_or_404(People, pk=pk)

    template_path = 'dash/ci_pdf.html'
    context = {'people': people}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download run below
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display run below
    response['Content-Disposition'] = ' filename="Certificate-of-Indigency.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
@login_required
def cr_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    people = get_object_or_404(People, pk=pk)

    template_path = 'dash/cr_pdf.html'
    context = {'people': people}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download run below
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display run below
    response['Content-Disposition'] = ' filename="Certificate-of-Residency.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

class DateInput(forms.DateInput):
    input_type = 'date'
@method_decorator(login_required, name='dispatch')
class RCreateView(CreateView):
    model = People
    form_class = PeopleAddForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)


# class RCreateView(LoginRequiredMixin, CreateView):
#     model = People
#     fields = ('last_name', 'first_name', 'middle_name', 'gender', 'age', 'birthday', 'birthplace',
#               'house_number', 'street', 'civil_status', 'religion', 'nationality', 'phone_number', 'image', 'status', 'year_of_residency')
#     widgets = {
#         'birthday': DatePicker(
#             options={
#                 'format': 'DD/MM/YYYY'
#             },
#             attrs={
#                 'prepend': 'fa fa-calendar',
#             },
#         )
#     }
#
#     # def form_valid(self, form):
#     #     form.instance.author = self.request.user
#     #     return super().form_valid(form)
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         post = form.save(commit=False)
#         post.save()
#         return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class RUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = People
    fields = ['last_name', 'middle_name', 'age', 'house_number', 'street', 'civil_status',
              'religion', 'phone_number', 'nationality', 'image', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        people = self.get_object()
        if self.request.user == people.author:
            return True
        return False

@login_required
def dash_board(request):
    rcount = People.objects.filter(status='Active').count()
    rmcount = People.objects.filter(status='Active',gender='Male').count()
    rfcount = People.objects.filter(status='Active',gender='Female').count()
    rpwdcount = People.objects.filter(status='Active',PWD='Yes').count()
    rb7count = People.objects.filter(status='Active',age__lte=65).count()
    ra65count = People.objects.filter(status='Active',age__gte=65).count()
    bpcount = BPermit.objects.count()
    bcount = Blotter.objects.count()
    hcount = Household.objects.count()
    btcount = BPTransaction.objects.filter(payment_status='Partial').count()
    arcount = Resolution.objects.filter(status='Active').count()
    cvccount = CovidVac.objects.filter(status='Complete').count()
    cvicount = CovidVac.objects.filter(status='Incomplete').count()
    cvi = CovidVac.objects.filter(status='Incomplete')
    ccacount = CovidCase.objects.filter(status='Active').count()
    covidcases = CovidCase.objects.all().order_by('name')
    residents = People.objects.all().order_by('last_name')
    pregnant = Pregnant.objects.filter(status='Active').count()
    return render(request, 'dash/dashboard.html', {'title': 'Dash-Board', 'rcount': rcount,'rmcount': rmcount, 'rfcount': rfcount,
                                                   'bcount': bcount, 'bpcount': bpcount, 'residents': residents, 'rpwdcount': rpwdcount,
                                                   'arcount': arcount, 'cvccount': cvccount, 'cvicount': cvicount,'hcount':hcount,
                                                   'btcount':btcount, 'covidcases':covidcases, 'cvi':cvi, 'ccacount':ccacount,
                                                   'rb7count':rb7count, 'ra65count':ra65count, 'pregnant':pregnant})
@login_required
def intervals(request):
    rcount = People.objects.filter(status='Active').count()
    rmcount = People.objects.filter(status='Active',gender='Male').count()
    rfcount = People.objects.filter(status='Active',gender='Female').count()
    rpwdcount = People.objects.filter(status='Active',PWD='Yes').count()
    ra65count = People.objects.filter(status='Active',age__gte=60).count()
    zeroto11 = People.objects.filter(status='Active',age__lt=1).count()
    oneto2 = People.objects.filter(status='Active',age__gte=1, age__lte=2).count()
    threeto4 = People.objects.filter(status='Active',age__gte=3, age__lte=4).count()
    fiveto6 = People.objects.filter(status='Active',age__gte=5, age__lte=6).count()
    sevento8 = People.objects.filter(status='Active',age__gte=7, age__lte=8).count()
    nineto10 = People.objects.filter(status='Active',age__gte=9, age__lte=10).count()
    elevento12 = People.objects.filter(status='Active',age__gte=11, age__lte=12).count()
    thirteento14 = People.objects.filter(status='Active',age__gte=13, age__lte=4).count()
    fifteento17 = People.objects.filter(status='Active',age__gte=15, age__lte=17).count()
    adultmale = People.objects.filter(status='Active',gender='Male',age__gte=18, age__lte=59).count()
    adultfemale = People.objects.filter(status='Active',gender='Female',age__gte=18, age__lte=59).count()
    return render(request, 'dash/intervals.html', {'title': 'Home-2', 'rcount': rcount,'rmcount': rmcount, 'rfcount': rfcount,
                                                   'ra65count':ra65count, 'zeroto11':zeroto11, 'rpwdcount':rpwdcount, 'oneto2':oneto2,
                                                   'threeto4':threeto4, 'fiveto6':fiveto6, 'sevento8':sevento8, 'nineto10':nineto10,
                                                   'elevento12':elevento12, 'thirteento14':thirteento14, 'fifteento17':fifteento17,
                                                   'adultmale':adultmale, 'adultfemale':adultfemale})

#intervals
@login_required
def zeroto11(request):
    zeroto11 = People.objects.filter(status='Active',age__lt=1).order_by('last_name')

    return render(request, 'dash/zeroto11.html', {'title': 'Intervals', 'zeroto11': zeroto11})
@login_required
def oneto2(request):
    oneto2 = People.objects.filter(status='Active',age__gte=1, age__lte=2).order_by('last_name')

    return render(request, 'dash/oneto2.html', {'title': 'Intervals', 'oneto2': oneto2})
@login_required
def threeto4(request):
    threeto4 = People.objects.filter(status='Active',age__gte=3, age__lte=4).order_by('last_name')

    return render(request, 'dash/threeto4.html', {'title': 'Intervals', 'threeto4': threeto4})
@login_required
def fiveto6(request):
    fiveto6 = People.objects.filter(status='Active',age__gte=5, age__lte=6).order_by('last_name')

    return render(request, 'dash/fiveto6.html', {'title': 'Intervals', 'fiveto6': fiveto6})
@login_required
def sevento8(request):
    sevento8 = People.objects.filter(status='Active',age__gte=7, age__lte=8).order_by('last_name')

    return render(request, 'dash/sevento8.html', {'title': 'Intervals', 'sevento8': sevento8})
@login_required
def nineto10(request):
    nineto10 = People.objects.filter(status='Active',age__gte=9, age__lte=10).order_by('last_name')

    return render(request, 'dash/nineto10.html', {'title': 'Intervals', 'nineto10': nineto10})
@login_required
def elevento12(request):
    elevento12 = People.objects.filter(status='Active',age__gte=11, age__lte=12).order_by('last_name')

    return render(request, 'dash/elevento12.html', {'title': 'Intervals', 'elevento12': elevento12})
@login_required
def thirteento14(request):
    thirteento14 = People.objects.filter(status='Active',age__gte=13, age__lte=4).order_by('last_name')

    return render(request, 'dash/thirteento14.html', {'title': 'Intervals', 'thirteento14': thirteento14})
@login_required
def fifteento17(request):
    fifteento17 = People.objects.filter(status='Active',age__gte=15, age__lte=17).order_by('last_name')

    return render(request, 'dash/fifteento17.html', {'title': 'Intervals', 'fifteento17': fifteento17})
@login_required
def adultmale(request):
    adultmale = People.objects.filter(status='Active',gender='Male',age__gte=18, age__lte=59).order_by('last_name')

    return render(request, 'dash/adultmale.html', {'title': 'Intervals', 'adultmale': adultmale})
@login_required
def adultfemale(request):
    adultfemale = People.objects.filter(status='Active',gender='Female',age__gte=18, age__lte=59).order_by('last_name')

    return render(request, 'dash/adultfemale.html', {'title': 'Intervals', 'adultfemale': adultfemale})
# 65above
@login_required
def senior(request):
    senior = People.objects.filter(status='Active',age__gte=60).order_by('last_name')

    return render(request, 'dash/senior.html', {'title': 'Dash-Board', 'senior': senior})
# pwd
@login_required
def pwd(request):
    pwd = People.objects.filter(status='Active',PWD='Yes').order_by('last_name')

    return render(request, 'dash/pwd.html', {'title': 'Dash-Board', 'pwd': pwd})

# blotter
@login_required
def Bhome(request):
    context = {
        'blotter': Blotter.objects.all().order_by('suspect_lastname')
    }
    return render(request, 'dash/bhome.html', context)

@method_decorator(login_required, name='dispatch')
class BPostListView(ListView):
    model = Blotter
    template_name = 'dash/bhome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'blotter'
    ordering = ['suspect_lastname']
    # paginate_by = 5

@method_decorator(login_required, name='dispatch')
class BPostDetailView(DetailView):
    model = Blotter


# class BPostCreateView(LoginRequiredMixin, CreateView):
#     model = Blotter
#     fields = ['victim_lastname', 'victim_firstname', 'victim_middlename', 'gender', 'age', 'birthday', 'birthplace',
#                'civil_status', 'religion', 'nationality', 'phone_number',
#               'suspect_lastname', 'suspect_firstname', 'suspect_middlename', 'status']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class BPostCreateView(CreateView):
    model = Blotter
    form_class = BlotterAddForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class BPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blotter
    fields = ['status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        blotter = self.get_object()
        if self.request.user == blotter.author:
            return True
        return False

@method_decorator(login_required, name='dispatch')
class BPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blotter
    success_url = reverse_lazy('b-home')

    def test_func(self):
        blotter = self.get_object()
        if self.request.user == blotter.author:
            return True
        return False
@login_required
def blotter_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    blotter = get_object_or_404(Blotter, pk=pk)

    template_path = 'dash/blotter_pdf.html'
    context = {'blotter': blotter}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download run below
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display run below
    response['Content-Disposition'] = ' filename="Barangay-Blotter.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


#barangay permit
@login_required
def BPhome(request):
    context = {
        'bpermit': BPermit.objects.all().order_by('business_name')
    }
    return render(request, 'dash/bphome.html', context)

@method_decorator(login_required, name='dispatch')
class BPPostListView(ListView):
    model = BPermit
    template_name = 'dash/bphome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'bpermit'
    ordering = ['business_name']
    # paginate_by = 5

@method_decorator(login_required, name='dispatch')
class BPPostDetailView(DetailView):
    model = BPermit

@method_decorator(login_required, name='dispatch')
class BPPostCreateView(LoginRequiredMixin, CreateView):
    model = BPermit
    fields = ['business_name', 'location', 'operator_lastname', 'operator_firstname', 'operator_middlename',
              'address', 'date_issued','closure_date', 'closure_reason', 'contact_person', 'contact_number',
              'classification','remarks', 'type_of_ownership', 'approved_by', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class BPPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = BPermit
    fields = ['business_name', 'location', 'address',
              'operator_lastname', 'operator_firstname', 'operator_middlename', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        bpermit = self.get_object()
        if self.request.user == bpermit.author:
            return True
        return False

@method_decorator(login_required, name='dispatch')
class BPPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BPermit
    success_url = reverse_lazy('bp-home')

    def test_func(self):
        bpermit = self.get_object()
        if self.request.user == bpermit.author:
            return True
        return False
@login_required
def bpermit_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    bpermit = get_object_or_404(BPermit, pk=pk)

    template_path = 'dash/bpermit_pdf.html'
    context = {'bpermit': bpermit}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download run below
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display run below
    response['Content-Disposition'] = ' filename="Barangay-Permit.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# newsfeed
def newsfeed(request):
    context = {
        'apost': APost.objects.all()
    }
    return render(request, 'dash/newsfeed2.html', context)

@method_decorator(login_required, name='dispatch')
class APostListView(ListView):
    model = APost
    template_name = 'dash/newsfeed2.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'apost'
    ordering = ['-date_posted']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class APostDetailView(DetailView):
    model = APost

@method_decorator(login_required, name='dispatch')
class APostCreateView(LoginRequiredMixin, CreateView):
    model = APost
    fields = [ 'content' ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# class APostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = APost
#     fields = ['content']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
#
#     def test_func(self):
#         apost = self.get_object()
#         if self.request.user == apost.author:
#             return True
#         return False

@method_decorator(login_required, name='dispatch')
class APostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = APost
    success_url = reverse_lazy('news-feed')

    def test_func(self):
        apost = self.get_object()
        if self.request.user == apost.author:
            return True
        return False
@login_required
def news_feed(request):
    announcements = APost.objects.all().order_by('-date_posted')
    resident_post = Post.objects.all().order_by('-date_posted')
    return render(request, 'dash/newsfeed.html', {'announcements': announcements, 'resident_post': resident_post})

# addition
@login_required
def tohome(request):
    context = {
        'tofficial': TermOfficial.objects.all()
    }
    return render(request, 'dash/tohome.html', context)

@method_decorator(login_required, name='dispatch')
class TOListView(ListView):
    model = TermOfficial
    template_name = 'dash/tohome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tofficial'
    ordering = ['-start_of_term']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class TODetailView(DetailView):
    model = TermOfficial

@method_decorator(login_required, name='dispatch')
class TOCreateView(LoginRequiredMixin, CreateView):
    model = TermOfficial
    fields = [ 'position', 'start_of_term', 'end_of_term', 'last_name', 'first_name', 'middle_name'
        , 'gender', 'age', 'address', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class TODeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TermOfficial
    success_url = reverse_lazy('o-home')

    def test_func(self):
        tofficial = self.get_object()
        if self.request.user == tofficial.author:
            return True
        return False


# organization
@login_required
def orghome(request):
    context = {
        'tnow': TermNow.objects.all()
    }
    return render(request, 'dash/orghome.html', context)
@method_decorator(login_required, name='dispatch')
class TNListView(ListView):
    model = TermNow
    template_name = 'dash/orghome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'tnow'
    ordering = ['-term_year']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class TNDetailView(DetailView):
    model = TermNow


# class TNCreateView(LoginRequiredMixin, CreateView):
#     model = TermOfficial
#     fields = [ 'position', 'start_of_term', 'end_of_term', 'last_name', 'first_name', 'middle_name'
#                , 'gender', 'age', 'address', 'image']
#
#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#
# class TNDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = TermNow
#     success_url = reverse_lazy('o-home')
#
#     def test_func(self):
#         tnow = self.get_object()
#         if self.request.user == tnow.author:
#             return True
#         return False

# other services
@login_required
def other_services(request):
    return render(request, 'dash/others.html', {'title': 'Other Services'})
# other services
@login_required
def health_services(request):
    return render(request, 'dash/health_services.html', {'title': 'Health Services'})


#  vaccination
@login_required
def vhome(request):
    context = {
        'vaccinations': Vaccination.objects.all()
    }
    return render(request, 'dash/vhome.html', context)

@method_decorator(login_required, name='dispatch')
class VListView(ListView):
    model = Vaccination
    template_name = 'dash/vhome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'vaccinations'
    ordering = ['-last_name']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class VDetailView(DetailView):
    model = Vaccination

@method_decorator(login_required, name='dispatch')
class VCreateView(LoginRequiredMixin, CreateView):
    model = Vaccination
    fields = ['last_name', 'first_name', 'middle_name'
        , 'gender', 'age', 'vaccine_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class VDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vaccination
    success_url = reverse_lazy('v-home')

    def test_func(self):
        vaccinations = self.get_object()
        if self.request.user == vaccinations.author:
            return True
        return False
@login_required
def hhhome(request):
    context = {
        'households': Household.objects.all()
    }
    return render(request, 'dash/hhhome.html', context)
@method_decorator(login_required, name='dispatch')
class HhListView(ListView):
    model = Household
    template_name = 'dash/hhhome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'households'
    ordering = ['-family_name']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class HouseholdCreateView(CreateView):
    model = Household
    form_class = HouseholdAddForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class HhDetailView(DetailView):
    model = Household

@method_decorator(login_required, name='dispatch')
class HhDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Household
    success_url = reverse_lazy('dash-board')

    def test_func(self):
        households = self.get_object()
        if self.request.user == households.author:
            return True
        return False

# transactions
@login_required
def transactions(request):
    return render(request, 'dash/transactions.html', {'title': 'Transactions'})
# bpermit transactions
@login_required
def bpthome(request):
    context = {
        'bptransaction': BPTransaction.objects.all()
    }
    return render(request, 'dash/bpthome.html', context)
@method_decorator(login_required, name='dispatch')
class BPTListView(ListView):
    model = BPTransaction
    template_name = 'dash/bpthome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'bptransaction'
    ordering = ['-date']
    # paginate_by = 5

@method_decorator(login_required, name='dispatch')
class BPTCreateView(CreateView):
    model = BPTransaction
    form_class = BPTAddForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class BPTDetailView(DetailView):
    model = BPTransaction

@method_decorator(login_required, name='dispatch')
class BPTDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = BPTransaction
    success_url = reverse_lazy('bpt-home')

    def test_func(self):
        bptransaction = self.get_object()
        if self.request.user == bptransaction.author:
            return True
        return False


# resolution
@login_required
def rshome(request):
    context = {
        'resolution': Resolution.objects.all()
    }
    return render(request, 'dash/rshome.html', context)
@method_decorator(login_required, name='dispatch')
class RSListView(ListView):
    model = Resolution
    template_name = 'dash/rshome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'resolution'
    ordering = ['-session_date']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class RSCreateView(CreateView):
    model = Resolution
    form_class = RSAddForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class RSDetailView(DetailView):
    model = Resolution

@method_decorator(login_required, name='dispatch')
class RSDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Resolution
    success_url = reverse_lazy('rs-home')

    def test_func(self):
        resolution = self.get_object()
        if self.request.user == resolution.author:
            return True
        return False

# covidvac
@login_required
def cvhome(request):
    context = {
        'covidvac': CovidVac.objects.all()
    }
    return render(request, 'dash/cvhome.html', context)
@method_decorator(login_required, name='dispatch')
class CVListView(ListView):
    model = CovidVac
    template_name = 'dash/cvhome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'covidvac'
    ordering = ['-name']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class CVCreateView(CreateView):
    model = CovidVac
    form_class = CVAddForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class CVDetailView(DetailView):
    model = CovidVac

@method_decorator(login_required, name='dispatch')
class CVDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CovidVac
    success_url = reverse_lazy('cv-home')

    def test_func(self):
        covidvac = self.get_object()
        if self.request.user == covidvac.author:
            return True
        return False

# covidcae
@login_required
def cchome(request):
    context = {
        'covidcase': CovidCase.objects.all()
    }
    return render(request, 'dash/cchome.html', context)
@method_decorator(login_required, name='dispatch')
class CCListView(ListView):
    model = CovidCase
    template_name = 'dash/cchome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'covidcase'
    ordering = ['-name']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class CCCreateView(CreateView):
    model = CovidCase
    form_class = CCAddForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class CCDetailView(DetailView):
    model = CovidCase

@method_decorator(login_required, name='dispatch')
class CCDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CovidCase
    success_url = reverse_lazy('cc-home')

    def test_func(self):
        covidcase = self.get_object()
        if self.request.user == covidcase.author:
            return True
        return False

# pregnant
@login_required
def phome(request):
    context = {
        'pregnant': Pregnant.objects.all()
    }
    return render(request, 'dash/phome.html', context)
@method_decorator(login_required, name='dispatch')
class PListView(ListView):
    model = Pregnant
    template_name = 'dash/phome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'pregnant'
    ordering = ['-last_name']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class PCreateView(CreateView):
    model = Pregnant
    form_class = PAddForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class PDetailView(DetailView):
    model = Pregnant

@method_decorator(login_required, name='dispatch')
class PDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Pregnant
    success_url = reverse_lazy('p-home')

    def test_func(self):
        pregnant = self.get_object()
        if self.request.user == pregnant.author:
            return True
        return False

#  vaccinationSenior
@login_required
def svhome(request):
    context = {
        'svaccinations': SVaccination.objects.all()
    }
    return render(request, 'dash/svhome.html', context)

@method_decorator(login_required, name='dispatch')
class SVListView(ListView):
    model = SVaccination
    template_name = 'dash/svhome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'svaccinations'
    ordering = ['-last_name']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class SVDetailView(DetailView):
    model = SVaccination

@method_decorator(login_required, name='dispatch')
class SVCreateView(LoginRequiredMixin, CreateView):
    model = SVaccination
    fields = ['last_name', 'first_name', 'middle_name'
        , 'gender', 'age', 'vaccine_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class SVDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = SVaccination
    success_url = reverse_lazy('sv-home')

    def test_func(self):
        svaccinations = self.get_object()
        if self.request.user == svaccinations.author:
            return True
        return False

#  vaccinationPregnant
@login_required
def pvhome(request):
    context = {
        'pvaccinations': PVaccination.objects.all()
    }
    return render(request, 'dash/pvhome.html', context)

@method_decorator(login_required, name='dispatch')
class PVListView(ListView):
    model = PVaccination
    template_name = 'dash/pvhome.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'pvaccinations'
    ordering = ['-last_name']
    # paginate_by = 5
@method_decorator(login_required, name='dispatch')
class PVDetailView(DetailView):
    model = PVaccination

@method_decorator(login_required, name='dispatch')
class PVCreateView(LoginRequiredMixin, CreateView):
    model = PVaccination
    fields = ['last_name', 'first_name', 'middle_name'
        , 'age', 'vaccine_type']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class PVDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PVaccination
    success_url = reverse_lazy('sv-home')

    def test_func(self):
        pvaccinations = self.get_object()
        if self.request.user == pvaccinations.author:
            return True
        return False
