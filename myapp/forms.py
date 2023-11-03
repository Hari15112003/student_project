# # form.py
# from django import forms
# from django.forms import formset_factory

# class ReportForm(forms.Form):
#     title = forms.CharField(label='Title', initial='Default Title')
#     candidate_name = forms.CharField(label='Candidate Name', initial='Default Candidate Name')
#     award_degree = forms.CharField(label='Award Degree', initial='Default Award Degree')
#     branch_study = forms.CharField(label='Branch of Study', initial='Default Branch of Study')
#     college_name = forms.CharField(label='College Name', initial='Default College Name')
#     university = forms.CharField(label='University', initial='Default University')
#     month_year = forms.CharField(label='Month & Year', initial='Default')
#     problem_statement = forms.CharField(label='Problem Statement', widget=forms.Textarea, initial='Default')
#     origin_of_problem = forms.CharField(label='Origin of the Problem', widget=forms.Textarea, initial='Default')
#     motivation = forms.CharField(label='Motivation to do this project', widget=forms.Textarea, initial='Default')
#     beneficiary = forms.CharField(label='Beneficiary of the final product', widget=forms.Textarea, initial='Default')
#     case_studies = forms.CharField(label='Case Studies', widget=forms.Textarea, initial='Default')
#     literature_survey = forms.CharField(label='Literature Survey', widget=forms.Textarea, initial='Default')
#     project_image = forms.ImageField(label='Project Image',required=False)
#     subject_Code = forms.CharField(label='Subject Code', initial='Default')
#     labname = forms.CharField(label='Lab Name', initial='Default')
#     labhelddate = forms.CharField(label='Lab Held Date', initial='Default')
    
# class CandidateForm(forms.Form):
#     candidate_name = forms.CharField(label='Candidate Name', initial='Default Candidate Name')