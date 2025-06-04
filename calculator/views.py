from django import forms
from django.shortcuts import render

CORTES_CHOICES = [
    ('vacío', 'Vacío'),
    ('costilla', 'Costilla'),
    ('pollo', 'Pollo'),
]

class AsadoForm(forms.Form):
    adults_full = forms.IntegerField(label='Adultos (comen mucho)', min_value=0)
    adults_light = forms.IntegerField(label='Adultos (comen poco)', min_value=0)
    kids = forms.IntegerField(label='Niños', min_value=0)
    vegetarian = forms.IntegerField(label='Vegetarianos', min_value=0)
    generous = forms.BooleanField(required=False, label='Porciones generosas')
    include_sides = forms.BooleanField(required=False, label='Incluir guarniciones')
    is_picada = forms.BooleanField(required=False, label='Es picada')
    cortes = forms.MultipleChoiceField(
        choices=CORTES_CHOICES, 
        widget=forms.CheckboxSelectMultiple, 
        required=False, 
        label="Cortes de carne"
    )
    opciones_vegetarianas = forms.BooleanField(required=False, label="¿Agregar opciones vegetarianas?")
    incluir_bebidas = forms.BooleanField(required=False, label="Incluir bebidas")

def index(request):
    result = None
    carne_por_tipo = {}
    bebidas = {}
    if request.method == 'POST':
        form = AsadoForm(request.POST)
        if form.is_valid():
            adults_full = form.cleaned_data['adults_full']
            adults_light = form.cleaned_data['adults_light']
            kids = form.cleaned_data['kids']
            vegetarian = form.cleaned_data['vegetarian']
            generous = form.cleaned_data['generous']
            include_sides = form.cleaned_data['include_sides']
            is_picada = form.cleaned_data['is_picada']
            cortes = form.cleaned_data.get('cortes', [])

            meat_kg = 0
            if 'vacío' in cortes:
                meat_kg += (adults_full * 0.3) + (adults_light * 0.2)
            if 'costilla' in cortes:
                meat_kg += (adults_full * 0.2) + (adults_light * 0.15)
            if 'pollo' in cortes:
                meat_kg += (adults_full * 0.1) + (adults_light * 0.1)

            chorizos = (adults_full * 1.5) + (adults_light * 1) + (kids * 0.5)

            if is_picada:
                meat_kg *= 0.5
                chorizos *= 1.2
            elif generous:
                meat_kg *= 1.2
                chorizos += (adults_full + adults_light) * 0.5

            mandioca_kg = ensalada_l = pan_units = 0
            if include_sides and not is_picada:
                mandioca_kg = (adults_full + adults_light) * 0.25 + kids * 0.15
                ensalada_l = (adults_full + adults_light) * 0.2
                pan_units = (adults_full + adults_light + kids) * 1

                if generous:
                    mandioca_kg *= 1.1
                    ensalada_l *= 1.1
                    pan_units *= 1.1

            if form.cleaned_data.get('opciones_vegetarianas', False):
                vegetarianas = vegetarian * 0.25  # 250g de opción vegetariana por persona
            else:
                vegetarianas = 0

            incluir_bebidas = form.cleaned_data.get('incluir_bebidas')
            if incluir_bebidas == 'True' or incluir_bebidas is True:
                bebidas['Agua'] = round((adults_full + adults_light + kids + vegetarian) * 0.5, 2)  # litros
                bebidas['Gaseosa'] = round((adults_full + adults_light + kids + vegetarian) * 0.5, 2)  # litros
                bebidas['Cerveza'] = round((adults_full + adults_light) * 1, 2)  # litros
                bebidas['Vino'] = round((adults_full + adults_light) * 0.5, 2)  # litros
            else:
                bebidas = {}

            total_people = adults_full + adults_light + kids + vegetarian

            result = {
                'total_people': total_people,
                'meat_kg': round(meat_kg, 2),
                'chorizo_units': round(chorizos, 1),
                'mandioca_kg': round(mandioca_kg, 2),
                'ensalada_liters': round(ensalada_l, 2),
                'pan_units': int(pan_units),
                'vegetarianos': vegetarian,
                'is_picada': is_picada,
                'vegetarianas_kg': round(vegetarianas, 2),
            }

            # Detalle de carne por tipo
            carne_por_tipo = {}
            if 'vacío' in cortes:
                carne_por_tipo['Vacío'] = round((adults_full * 0.3) + (adults_light * 0.2), 2)
            if 'costilla' in cortes:
                carne_por_tipo['Costilla'] = round((adults_full * 0.2) + (adults_light * 0.15), 2)
            if 'pollo' in cortes:
                carne_por_tipo['Pollo'] = round((adults_full * 0.1) + (adults_light * 0.1), 2)

    else:
        form = AsadoForm()

    return render(request, 'calculator/index.html', {
        'form': form,
        'result': result,
        'carne_por_tipo': carne_por_tipo,
        'bebidas': bebidas
    })