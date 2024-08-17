from django.urls import path
from .views import *

urlpatterns = [
    

    # Customer URLs
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    # Company URLs
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='company-detail'),

    #customer sign up
    path('signup/', CustomerRegisterView.as_view(), name='signup'),
    
    #company sign up
    path('register/', CompanyRegisterView.as_view(), name='register'),

    #login of company and  customer 
    path('login/', LoginView.as_view(), name='login'),

    #logout
    path('logout/',LogoutView.as_view(),name='logout'),

    
    
    # Nominee URLs


    #for list of nominess of a customer who logged in
    path('list/',NomineesListView.as_view(),name='listofnominees'),
    
    # to add nominee
    path('nominees/', NomineeCreateView.as_view(), name='nomineeCreate'),
    
    # for Update, delete , details of nominees
    path('nominees/<int:pk>/', NomineeDetailView.as_view(), name='nominee-detail'),
    
    

    # InsurancePolicy URLs
    path('policies_list/', InsurancePolicyListView.as_view(), name='policy-list'),
    path('policies_create/', InsurancePolicyCreateView.as_view(), name='policy-create'),
    path('policies/<int:pk>/', InsurancePolicyDetailView.as_view(), name='policy-detail'),

    # PolicyPurchase URLs
    path('purchases_list/', PolicyPurchaseListView.as_view(), name='purchase-list'),
    path('purchases_create/', PolicyPurchaseCreateView.as_view(), name='purchase-create'),
    path('purchases/<int:pk>/', PolicyPurchaseDetailView.as_view(), name='purchase-detail'),

    # Claim URLs
    path('claims_list/', ClaimListView.as_view(), name='claim-list'),
    path('claims_create/', ClaimCreateView.as_view(), name='claim-create'),
    path('claims/<int:pk>/', ClaimDetailView.as_view(), name='claim-detail'),

    # Payment URLs
    path('payments_list/', PaymentListView.as_view(), name='payment-list'),
    path('payments_create/', PaymentCreateView.as_view(), name='payment-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
]
