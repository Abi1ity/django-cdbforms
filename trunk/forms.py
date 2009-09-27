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
		self.base_fields[field.tag] = forms.CharField(label=field.title, required=field.required)
	    elif field.type in ["C", "M"]:
		choices = []
		for parameter in field.parameters():
		    if parameter.tag == "choice":
			choices.append((parameter.value, parameter.value))
                if field.type == "C":
                    self.base_fields[field.tag] = forms.ChoiceField(choices=choices, label=field.title, required=field.required)
                else:
                    self.base_fields[field.tag] = forms.MultipleChoiceField(choices=choices, label=field.title, required=field.required)
	    elif field.type == "E":
		self.base_fields[field.tag] = forms.EmailField(label=field.title, required=field.required)
	    elif field.type == "U":
		self.base_fields[field.tag] = forms.URLField(label=field.title, required=field.required)
	forms.Form.__init__(self, *args, **kwargs)

    def save(self, commit=True):
	data = self.cleaned_data
	if commit:
	    rec = Record(template=self.template, dt=datetime.now())
	    rec.save()
	    for k,v in data.iteritems():
		f = TemplateField.objects.get(template=self.template, tag=k)
		d = RecordData(record=rec, field=f, value=v)
		d.save()
	return data
