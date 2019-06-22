from django import forms
class contactform(forms.Form):
    name = forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Your Name',
                'class':'form-control'
            }
        )
    )
    loc = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Loc',
                'class': 'form-control'
            }
        )
    )
    sal = forms.IntegerField(
        label="Enter Your Salary",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your Sal',
                'class': 'form-control'
            }
        )
    )
    com = forms.CharField(
        label="Enter Your Company",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Your Comapany',
                'class': 'form-control'
            }
        )
    )