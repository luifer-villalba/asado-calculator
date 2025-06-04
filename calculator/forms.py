from django import forms

class AsadoForm(forms.Form):
    adults_full = forms.IntegerField(min_value=0, label="Adultos (porción completa)")
    adults_light = forms.IntegerField(min_value=0, label="Adultos (porción moderada)")
    kids = forms.IntegerField(min_value=0, label="Niños")
    vegetarian = forms.IntegerField(min_value=0, label="Personas vegetarianas")
    generous = forms.BooleanField(required=False, label="¿Modo generoso?")
    include_sides = forms.BooleanField(required=False, label="¿Incluir acompañamientos?")
    is_picada = forms.BooleanField(required=False, label="¿Solo picada (sin plato principal)?")
