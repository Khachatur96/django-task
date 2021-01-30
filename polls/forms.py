from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import University
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UnivercityForm(ModelForm):
	class Meta:
		model = University
		fields = "__all__"

	def clean(self,*args,**kwargs):
		a = len(self.cleaned_data.get('subjects'))
		if a<2:
			raise ValidationError("At least 2 Subjects should be selected")
		
		return self.cleaned_data

