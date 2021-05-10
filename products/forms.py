from django import forms
from .models import (
    Product, Type, Variety, Appellation, Country)


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        types = Type.objects.all()
        varieties = Variety.objects.all()
        appellations = Appellation.objects.all()
        countries = Country.objects.all()
        friendly_names_type = [(t.id, t.get_friendly_name()) for t in types]
        friendly_names_variety = [(
            v.id, v.get_friendly_name()) for v in varieties]
        friendly_names_appellation = [(
            a.id, a.get_friendly_name()) for a in appellations]
        friendly_names_country = [(
            c.id, c.get_friendly_name()) for c in countries]

        self.fields['type'].choices = friendly_names_type
        for field_name, field in self.fields.items():
            field.widget.attrs[
                'class'] = 'border-burgundy rounded-0 text-capitalize'

        self.fields['variety'].choices = friendly_names_variety
        for field_name, field in self.fields.items():
            field.widget.attrs[
                'class'] = 'border-burgundy rounded-0 text-capitalize'

        self.fields['appellation'].choices = friendly_names_appellation
        for field_name, field in self.fields.items():
            field.widget.attrs[
                'class'] = 'border-burgundy rounded-0 text-capitalize'

        self.fields['country'].choices = friendly_names_country
        for field_name, field in self.fields.items():
            field.widget.attrs[
                'class'] = 'border-burgundy rounded-0 text-capitalize'

