from django.contrib import admin
from .models import Company, HomePage, Slider, Message, AboutPage,Report
from django import forms
from django.contrib.auth.models import User


class CompanyAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        """
        Make the 'subs' field read-only for regular users when editing an existing object.
        """
        readonly_fields = super().get_readonly_fields(request, obj)
        if obj and not request.user.is_superuser:
            # If editing an existing object and not a superuser
            readonly_fields = list(readonly_fields)  # Convert to list to modify
            readonly_fields.append('subs')
        return readonly_fields

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        
        user_companies = qs.filter(user=request.user)
        return user_companies

    def get_subdivision_ids(self, company):
        """Recursively get all subdivisions for a given company."""
        subdivision_ids = set(company.subs.values_list('id', flat=True))
        for sub_company in company.subs.all():
            subdivision_ids.update(self.get_subdivision_ids(sub_company))
        return subdivision_ids

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If the object is being created
            obj.user = request.user
        super().save_model(request, obj, form, change)
        
    def formfield_for_dbfield(self, db_field, request, **kwargs):
        """
        Conditionally exclude the 'user' field for regular users when editing an existing object.
        """
        # Check if the field is 'user' and the user is not a superuser
        if db_field.name == 'user' and not request.user.is_superuser:
            # Remove the 'user' field from the form if not a superuser
            return None
        
        # Call the parent method for other fields
        return super().formfield_for_dbfield(db_field, request, **kwargs)


    list_display = ('name', 'description')  # Fields to display in the list view
    search_fields = ['name']
    filter_horizontal = ('subs',)  # For ManyToManyFields
    

admin.site.register(Company, CompanyAdmin)


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'address', 'email')
    actions = None  # Disables actions like delete

    def has_add_permission(self, request):
        # Allow adding only if no instance exists
        return not HomePage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the singleton instance
        return False

admin.site.register(HomePage, HomePageAdmin)

class AboutPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date')
    actions = None  # Disables actions like delete

    def has_add_permission(self, request):
        # Allow adding only if no instance exists
        return not AboutPage.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Prevent deletion of the singleton instance
        return False

admin.site.register(AboutPage, AboutPageAdmin)


class SliderAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')  # Fields to display in the list view

admin.site.register(Slider, SliderAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject')  # Fields to display in the list view

admin.site.register(Message, MessageAdmin)

    
class ReportFormAdd(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        user = self.user
        super().__init__(*args, **kwargs)
        if user:
            self.fields['company'].queryset = Company.objects.filter(user=user) 


class ReportFormEdit(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'

class ReportAdmin(admin.ModelAdmin):
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs
        
        user_reports = qs.filter(company__user=request.user)
        companies_list = []
        for company in request.user.companies.all():
            companies_list += company.subs.all().values_list('id', flat=True)
        companies_list = set(companies_list)
        subs_reports = qs.filter(company__in=companies_list)
        return user_reports|subs_reports
    
    def get_form(self, request, obj=None, **kwargs):
        if not 'change' in request.path:
            self.form = ReportFormAdd
        else:
             self.form = ReportFormEdit
        form = super().get_form(request, obj, **kwargs)
        form.user = request.user
        return form

    list_display = ['company','annual_profit','budget','expected_budget','staff_number','current_expense','year_analysis']
    
            
    
admin.site.register(Report,ReportAdmin)


   