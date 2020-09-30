from django.forms import ModelForm
from enggapp.models import Register

class Usform(ModelForm):
	class Meta:
		model = Register
		fields = '__all__'