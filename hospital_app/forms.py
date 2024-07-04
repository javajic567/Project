from django import forms
class Patient_form(forms.Form):
    time=(
        ('10am','10am'),
        ('11am','11am'),
        ('3pm','3pm'),
        ('4pm','4pm')
    )
    patient_name=forms.CharField(max_length=80,visible=False)
    patient_age=forms.CharField(max_length=80)
    patient_email=forms.EmailField(help_text='@ is mandatary')
    appointment_cause=forms.CharField(max_length=50)
    appointment_date=forms.CharField(max_length=1000,widget=forms.RadioSelect(choices=time))
