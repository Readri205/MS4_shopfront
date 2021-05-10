from django import forms
from .models import Product, Type


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types = Type.objects.all()
        friendly_names = [(t.id, t.get_friendly_name()) for t in types]

        self.fields['type'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-burgundy rounded-0'
