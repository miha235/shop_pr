from django import forms
from .models import Product
from .models import Version

# Список запрещенных слов
FORBIDDEN_WORDS = ["казино","криптовалюта","крипта","биржа","дешево","бесплатно","обман","полиция",
                   "радар"]


class ProductForm (forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','image','price','category']

    def clean_name(self):
        name = self.cleaned_data.get('name','').lower()
        for word in FORBIDDEN_WORDS:
            if word in name:
                raise forms.ValidationError ( f"Название продукта содержит запрещенное слово: {word}" )
        return name

    def clean_description(self):
        description = self.cleaned_data.get ('description','').lower()
        for word in FORBIDDEN_WORDS:
            if word in description:
                raise forms.ValidationError ( f"Описание продукта содержит запрещенное слово: {word}" )
        return description


class StyledFormMixin:
    def __init__(self,*args,**kwargs):
        super ().__init__ ( *args,**kwargs )
        # Добавляем общий стиль к каждому полю
        for field_name,field in self.fields.items ():
            if isinstance ( field.widget,forms.CheckboxInput ):
                field.widget.attrs.update ( {'class': 'form-check-input'} )
            else:
                field.widget.attrs.update ( {'class': 'form-control'} )

class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = ['version_name', 'version_number', 'is_current']



