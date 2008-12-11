from django.db import models

class Template(models.Model):
    tag = models.SlugField(max_length=16, unique=True)
    title = models.CharField(max_length=50)
    
    def fields(self):
	return TemplateField.objects.filter(template=self).order_by('tab')

    def __unicode__(self):
	return self.title

class TemplateField(models.Model):
    FieldTypes = (('T', 'Text'), ('B', 'Bool'), ('E', 'E-mail'), ('U', 'URL'), ('C', 'Choices'),)
    template = models.ForeignKey(Template)
    tag = models.SlugField(max_length=32)
    title = models.CharField(max_length=50)
    type = models.CharField(max_length=1, choices=FieldTypes)
    tab = models.IntegerField(default=0)
    required = models.BooleanField(default=True)

    def __unicode__(self):
        return u'%s: %s' % (self.template, self.tag)

    def parameters(self):
	return FieldParameter.objects.filter(field=self).order_by('tab')
	
    class Meta:
	unique_together = ("template", "tag")
	
class FieldParameter(models.Model):
    field = models.ForeignKey(TemplateField)
    tag = models.SlugField(max_length=32)
    value = models.CharField(max_length=255)
    tab = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s: %s = %s' % (self.field, self.tag, self.value)
	
    class Meta:
	unique_together = ("field", "tag", "value")

class Record(models.Model):
    template = models.ForeignKey(Template)
    dt = models.DateTimeField()
    
    def __unicode__(self):
	return u'%s @ %s' % (self.template, self.dt)

class RecordData(models.Model):
    record = models.ForeignKey(Record)
    field = models.ForeignKey(TemplateField)
    value = models.CharField(max_length=255)
    
    def __unicode__(self):
	return u'%s %s' % (self.record, self.field)
	
    class Meta:
	unique_together = ("record", "field")
