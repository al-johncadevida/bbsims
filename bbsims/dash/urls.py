from django.urls import path
from .views import (
    RListView,
    RDetailView,
    RCreateView,
    RUpdateView,
    # addition
    bc_render_pdf_view,
    ci_render_pdf_view,
    cr_render_pdf_view,
    PeopleUpdateView,
    # blotter
    BPostListView,
    BPostDetailView,
    BPostCreateView,
    BPostUpdateView,
    BPostDeleteView,
    blotter_render_pdf_view,
    BlotterUpdateView,

    # barangay permit
    BPPostListView,
    BPPostDetailView,
    BPPostCreateView,
    BPPostUpdateView,
    BPermitUpdateView,
    BPPostDeleteView,
    bpermit_render_pdf_view,

    # bp transaction
    BPTListView,
    BPTDetailView,
    BPTCreateView,
    BPTUpdateView,
    BPTDeleteView,


    # newsfeed
    APostListView,
    APostDetailView,
    APostCreateView,
    APostUpdateView,
    APostDeleteView,
    news_feed,
    # Termofficial
    TOListView,
    TODetailView,
    TOCreateView,
    TOUpdateView,
    TODeleteView,
    # TermoNow
    TNListView,
    TNDetailView,
    TNUpdateView,
    # Vaccination
    VListView,
    VDetailView,
    VCreateView,
    VUpdateView,
    VDeleteView,
    # VaccinationSenior
    SVListView,
    SVDetailView,
    SVCreateView,
    SVUpdateView,
    SVDeleteView,
    # VaccinationPregnant
    PVListView,
    PVDetailView,
    PVCreateView,
    PVUpdateView,
    PVDeleteView,
    # household
    HouseholdCreateView,
    HhListView,
    HhDetailView,
    HhUpdateView,
    HhDeleteView,
    # resolution
    RSCreateView,
    RSListView,
    RSDetailView,
    RSUpdateView,
    RSDeleteView,
    # covidvac
    CVCreateView,
    CVListView,
    CVDetailView,
    CVUpdateView,
    CVDeleteView,
    # covidvac
    CCCreateView,
    CCListView,
    CCDetailView,
    CCUpdateView,
    CCDeleteView,
    # pregnant
    PCreateView,
    PListView,
    PDetailView,
    PUpdateView,
    PDeleteView,
)
from . import views



urlpatterns = [
    path('home2', RListView.as_view(), name='home2'),
    path('admins/<int:pk>/', RDetailView.as_view(), name='people-detail'),
    path('admins/new/', RCreateView.as_view(), name='people-create'),
    path('admins/<int:pk>/update/', PeopleUpdateView.as_view(), name='people-update'),
    path('dash-board/', views.dash_board, name='dash-board'),
    path('age-intervals/', views.intervals, name='age-intervals'),
    path('/Intervals/-1', views.zeroto11, name='zeroto11'),
    path('/Intervals/1-2', views.oneto2, name='oneto2'),
    path('/Intervals/3-4', views.threeto4, name='threeto4'),
    path('/Intervals/5-6', views.fiveto6, name='fiveto6'),
    path('/Intervals/7-8', views.sevento8, name='sevento8'),
    path('/Intervals/9-10', views.nineto10, name='nineto10'),
    path('/Intervals/11-12', views.elevento12, name='elevento12'),
    path('/Intervals/13-14', views.thirteento14, name='thirteento14'),
    path('/Intervals/15-17', views.fifteento17, name='fifteento17'),
    path('/Intervals/Male/18-59', views.adultmale, name='adultmale'),
    path('/Intervals/Female/18-59', views.adultfemale, name='adultfemale'),
    path('/65-&-above/', views.senior, name='senior'),
    path('/PWD/', views.pwd, name='pwd'),
    #addition
    path('pdf/bc/<int:pk>', bc_render_pdf_view, name='bc-view'),
    path('pdf/ci/<int:pk>', ci_render_pdf_view, name='ci-view'),
    path('pdf/cr/<int:pk>', cr_render_pdf_view, name='cr-view'),
    #     addition
    #     blotter
    path('blotter/home', BPostListView.as_view(), name='b-home'),
    path('blotter/<int:pk>/', BPostDetailView.as_view(), name='b-detail'),
    path('blotter/new/', BPostCreateView.as_view(), name='b-create'),
    path('blotter/<int:pk>/update/', BlotterUpdateView.as_view(), name='b-update'),
    path('blotter/<int:pk>/delete/', BPostDeleteView.as_view(), name='b-delete'),
    path('pdf/blotter/<int:pk>', blotter_render_pdf_view, name='blotter-view'),
    #     barangay permit
    path('Barangay-Permit/home', BPPostListView.as_view(), name='bp-home'),
    path('Barangay-Permit/<int:pk>/', BPPostDetailView.as_view(), name='bp-detail'),
    path('Barangay-Permit/new/', BPPostCreateView.as_view(), name='bp-create'),
    path('Barangay-Permit/<int:pk>/update/', BPermitUpdateView.as_view(), name='bp-update'),
    path('Barangay-Permit/<int:pk>/delete/', BPPostDeleteView.as_view(), name='bp-delete'),
    path('pdf/barangay-permit/<int:pk>', bpermit_render_pdf_view, name='bpermit-view'),
    #     newsfeed
    path('newsfeed', APostListView.as_view(), name='newsfeed'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('newsfeed/<int:pk>/', APostDetailView.as_view(), name='apost-detail'),
    path('newsfeed/new/', APostCreateView.as_view(), name='apost-create'),
    path('newsfeed/<int:pk>/update/', APostUpdateView.as_view(), name='apost-update'),
    path('newsfeed/<int:pk>/delete/', APostDeleteView.as_view(), name='apost-delete'),
    path('admin/newsfeed/', views.news_feed, name='news-feed'),
    path('admin/other-services/', views.other_services, name='other-services'),
    path('admin/health-services/', views.health_services, name='health-services'),
    path('admin/Transactions/', views.transactions, name='transactions'),
    #     termofficial
    path('official', TOListView.as_view(), name='o-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('official/<int:pk>/', TODetailView.as_view(), name='to-detail'),
    path('official/new/', TOCreateView.as_view(), name='to-create'),
    path('official/<int:pk>/update/', TOUpdateView.as_view(), name='to-update'),
    path('official/<int:pk>/delete/', TODeleteView.as_view(), name='to-delete'),

    #     organization
    path('Organizational-Chart/Home', TNListView.as_view(), name='org-home'),
    path('Organizational-Chart/<int:pk>/', TNDetailView.as_view(), name='tn-detail'),
    path('Organizational-Chart/<int:pk>/update/', TNUpdateView.as_view(), name='tn-update'),

    # vaccination
    path('vaccination', VListView.as_view(), name='v-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('vaccination/<int:pk>/', VDetailView.as_view(), name='v-detail'),
    path('vaccination/new/', VCreateView.as_view(), name='v-create'),
    path('vaccination/<int:pk>/update/', VUpdateView.as_view(), name='v-update'),
    path('vaccination/<int:pk>/delete/', VDeleteView.as_view(), name='v-delete'),
    # vaccinationsenior
    path('vaccination/senior', SVListView.as_view(), name='sv-home'),
    path('vaccination/senior/<int:pk>/', SVDetailView.as_view(), name='sv-detail'),
    path('vaccination/senior/new/', SVCreateView.as_view(), name='sv-create'),
    path('vaccination/senior/<int:pk>/update/', SVUpdateView.as_view(), name='sv-update'),
    path('vaccination/senior/<int:pk>/delete/', SVDeleteView.as_view(), name='sv-delete'),
    # vaccinationpregnant
    path('vaccination/pregnant', PVListView.as_view(), name='pv-home'),
    path('vaccination/pregnant/<int:pk>/', PVDetailView.as_view(), name='pv-detail'),
    path('vaccination/pregnant/new/', PVCreateView.as_view(), name='pv-create'),
    path('vaccination/pregnant/<int:pk>/update/', PVUpdateView.as_view(), name='pv-update'),
    path('vaccination/pregnant/<int:pk>/delete/', PVDeleteView.as_view(), name='pv-delete'),
    # household
    path('Household/new/', HouseholdCreateView.as_view(), name='hh-create'),
    path('Household', HhListView.as_view(), name='hh-home'),
    path('Household/<int:pk>/', HhDetailView.as_view(), name='hh-detail'),
    path('Household/<int:pk>/update/', HhUpdateView.as_view(), name='hh-update'),
    path('Household/<int:pk>/delete/', HhDeleteView.as_view(), name='hh-delete'),
    # bpertmit transaction
    path('Transaction/Business/new/', BPTCreateView.as_view(), name='bpt-create'),
    path('Transaction/Business', BPTListView.as_view(), name='bpt-home'),
    path('Transaction/Business/<int:pk>/', BPTDetailView.as_view(), name='bpt-detail'),
    path('Transaction/Business/<int:pk>/update/', BPTUpdateView.as_view(), name='bpt-update'),
    path('Transaction/Business/<int:pk>/delete/', BPTDeleteView.as_view(), name='bpt-delete'),
    # resolution
    path('Resolution/new/', RSCreateView.as_view(), name='rs-create'),
    path('Resolution/', RSListView.as_view(), name='rs-home'),
    path('Resolution/<int:pk>/', RSDetailView.as_view(), name='rs-detail'),
    path('Resolution/<int:pk>/update/', RSUpdateView.as_view(), name='rs-update'),
    path('Resolution/<int:pk>/delete/', RSDeleteView.as_view(), name='rs-delete'),
    # covidvac
    path('Covid-Vaccination/new/', CVCreateView.as_view(), name='cv-create'),
    path('Covid-Vaccination/', CVListView.as_view(), name='cv-home'),
    path('Covid-Vaccination/<int:pk>/', CVDetailView.as_view(), name='cv-detail'),
    path('Covid-Vaccination/<int:pk>/update/', CVUpdateView.as_view(), name='cv-update'),
    path('Covid-Vaccination/<int:pk>/delete/', CVDeleteView.as_view(), name='cv-delete'),
    # covidcase
    path('Covid-Case/new/', CCCreateView.as_view(), name='cc-create'),
    path('Covid-Case/', CCListView.as_view(), name='cc-home'),
    path('Covid-Case/<int:pk>/', CCDetailView.as_view(), name='cc-detail'),
    path('Covid-Case/<int:pk>/update/', CCUpdateView.as_view(), name='cc-update'),
    path('Covid-Case/<int:pk>/delete/', CCDeleteView.as_view(), name='cc-delete'),
    # pregnant
    path('Pregnant/new/', PCreateView.as_view(), name='p-create'),
    path('Pregnant/', PListView.as_view(), name='p-home'),
    path('Pregnant/<int:pk>/', PDetailView.as_view(), name='p-detail'),
    path('Pregnant/<int:pk>/update/', PUpdateView.as_view(), name='p-update'),
    path('Pregnant/<int:pk>/delete/', PDeleteView.as_view(), name='p-delete'),
]
