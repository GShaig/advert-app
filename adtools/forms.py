from django import forms

from .models import Short, Dom

class DomainForm(forms.ModelForm):
    domain = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter Domain Name Here', 'class': 'shadow-lg textInput border-0 p-2'}))

    class Meta:
        model = Dom
        fields = ('domain',)

class IpForm(forms.Form):
    domain = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter IP Address Here', 'class': 'shadow-lg textInput border-0 p-2'}))

class ShortForm(forms.ModelForm):
    long_url = forms.URLField(widget=forms.URLInput(
        attrs={"placeholder": "Copy-Paste Long URL Here", "class": "shadow-lg textInput border-0 p-2"}))

    class Meta:
        model = Short
        fields = ('long_url',)

class HostingForm(forms.Form):
  site_choices = [
    (0, 'Blog'),
    (1, 'Portfolio'),
    (2, 'Company Website'),
    (3, 'eCommerce (Sell online)'),
    (0, 'Other')
  ]
  
  serv_choices = [
    ('min', 'Minimal'),
    ('wp', 'WordPress'),
    ('self', 'Self Managed'),
    ('dedicated', 'Dedicated Server'),
    ('unsure', 'Not sure')
  ]
  
  visitor_choices = [
    (0, 'Small Website (Up to 500 visitors)'),
    (1, 'Medium Website (500-3000 visitors)'),
    (2, 'Large Website (More than 5000 visitors)'),
    (0, 'Not sure')
  ]
  
  content_choices = [
    (0, 'Not Much (Up to 10 GB)'),
    (1, 'Some Content (10-50 GB)'),
    (2, 'Lots of Content (50-100 GB)'),
    (3, 'Full of Content (100 GB+)'),
    (0, 'Not sure')
  ]
  
  site = forms.CharField(widget=forms.RadioSelect(choices=site_choices, attrs={"class": "myRadio"}))
  serv = forms.CharField(widget=forms.RadioSelect(choices=serv_choices, attrs={"class": "myRadio"}))
  visitor = forms.CharField(widget=forms.RadioSelect(choices=visitor_choices, attrs={"class": "myRadio"}))
  content = forms.CharField(widget=forms.RadioSelect(choices=content_choices, attrs={"class": "myRadio"}))

class EmailForm(forms.Form):
  size_choices = [
    (5, '5GB Mailbox'),
    (30, '30GB Mailbox'),
    (75, '75GB Mailbox')
  ]
  
  size = forms.ChoiceField(widget=forms.RadioSelect, choices=size_choices)
  num = forms.IntegerField(min_value=1)

class SSLForm(forms.Form):
  num_choices = [
    (1, 'Single Domain'),
    (2, 'Multiple Domains')
  ]
  
  site_choices = [
    (1, 'Personal Website'),
    (2, 'Company Website'),
    (3, 'eCommerce Website (Sell online)')
  ]
  
  serv_choices = [
    (1, 'Yes'),
    (0, 'No')
  ]
  
  num = forms.ChoiceField(widget=forms.RadioSelect, choices=num_choices)
  site = forms.ChoiceField(widget=forms.RadioSelect, choices=site_choices)
  serv = forms.ChoiceField(widget=forms.RadioSelect, choices=serv_choices)