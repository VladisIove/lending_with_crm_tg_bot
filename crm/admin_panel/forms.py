from django import forms 
from .models import ClothesView

class ClothesForm(forms.ModelForm):
    class Meta:
        model = ClothesView
        fields = ['name', 'description', 'type_clothes', 'enabled',
                    'old_price', 'price', 'count', 'img']

    class SIZE:
        XS = 1
        S = 2
        M = 3
        L = 4
        XL = 5
        XXL = 6

    MULTI_CHOICE_SIZE = (
        (SIZE.XS, "XS"),
        (SIZE.S, "S"),
        (SIZE.M, "M"),
        (SIZE.L, "L"),
        (SIZE.XL, "XL"),
        (SIZE.XXL, "XXL"),
        )
    
    class COLOR:
        RED = 1
        BLACK = 2
        WHITE = 3
        YELLOW = 4
        GREY = 5
    
    MULTI_CHOICE_COLOR = (
        (COLOR.RED, 'красный'),
        (COLOR.BLACK, 'чорный'),
        (COLOR.WHITE, 'белый'),
        (COLOR.YELLOW, 'жолтый'),
        (COLOR.GREY, 'серый'),
    )
    size = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=MULTI_CHOICE_SIZE, required=True)
    color = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=MULTI_CHOICE_COLOR, required=True)
    