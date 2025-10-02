from django import forms
from django.utils.translation import gettext as _

from apps.common.widgets import ModelSelect2AdminWidget
from apps.keywords.admin.steps_inline import StepsForm
from apps.keywords.models import KeywordCall
from apps.sequences.models import Sequence
from apps.windows.models import Window


TestStepsForm = forms.modelform_factory(
    KeywordCall,
    StepsForm,
    [],
    widgets={
        'window': ModelSelect2AdminWidget(
            model=Window,
            search_fields=['name__icontains'],
            attrs={
                'data-placeholder': _('Maske auswählen'),
                'style': 'width: 95%'
            }
        ),
        'to_keyword': ModelSelect2AdminWidget(
            model=Sequence,
            search_fields=['name__icontains'],
            dependent_fields={'window': 'windows'},
            attrs={
                'data-placeholder': _('Sequenz auswählen'),
                'style': 'width: 95%',
            }
        )
    }
)

TestStepsForm.fields_can_view_related = ['window']
TestStepsForm.fields_can_change_related = ['to_keyword']
