from datetime import datetime
from django import forms
from django.utils.translation import ugettext

from models import *

class CDBForm(forms.Form):
    def __init__(self, template=None, tag=None, *args, **kwargs):
	if template:
	    self.template = template
	elif tag:
	    self.template = Template.objects.get(tag=tag)
	fields = self.template.fields()
	for field in fields:
	    if field.type == "B":
		self.base_fields[field.tag] = forms.BooleanField(label=field.title, required=field.required)
	    elif field.type == "T":
                self.base_fields[field.tag] = forms.CharField(label=field.title, required=field.required, widget=forms.TextInput(attrs={'style': 'width: 350px;'}))
	    elif field.type == "C":
		choices = [('', '-')]
		for parameter in field.parameters():
		    if parameter.tag == "choice":
			choices.append((parameter.value, parameter.value))
                self.base_fields[field.tag] = forms.ChoiceField(choices=choices, 
                                                                label=field.title, 
                                                                required=field.required)
            elif field.type == "M":
		choices = []
		for parameter in field.parameters():
		    if parameter.tag == "choice":
			choices.append((parameter.value, parameter.value))
                self.base_fields[field.tag] = forms.MultipleChoiceField(choices=choices, 
                                                                        label=field.title, 
                                                                        widget=forms.CheckboxSelectMultiple,
                                                                        required=field.required)
	    elif field.type == "E":
		self.base_fields[field.tag] = forms.EmailField(label=field.title, required=field.required)
	    elif field.type == "U":
		self.base_fields[field.tag] = forms.URLField(label=field.title, required=field.required)
	forms.Form.__init__(self, *args, **kwargs)

    def save(self, commit=True):
	data = self.cleaned_data
        rec = Record(template=self.template, dt=datetime.now())
	if commit:
	    rec.save()
	    for k,v in data.iteritems():
		f = TemplateField.objects.get(template=self.template, tag=k)
		d = RecordData(record=rec, field=f, value=('%s' % v))
		d.save()
	return rec
