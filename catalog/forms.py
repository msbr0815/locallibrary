from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

import datetime

class RenewBookForm(forms.Form):
    renewal_date = forms.DateField(help_text="Enter a date between now and in 4 weeks (default: 3).")

    def clean_renewal_date(self):
        # cleaned_data is an attribute of the generic forms.Form object
        data = self.cleaned_data['renewal_date']

        # Check if the date is in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal is set to a date in the past.'))

        # Check if a date is in the allowed range (max. 4 weeks in the future).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead.'))

        # Remember to always return the cleaned data.
        return data

# Alternative: Use ModelForm which contains the same fields as the original model
# Code is repeated, since one of these forms might be deleted or commented out in the future.
from django.forms import ModelForm

from catalog.models import BookInstance

class RenewBookModelForm(ModelForm):

    def clean_due_back(self):
        data = self.cleaned_data['due_back']

        # Check if the date is in the past
        if data < datetime.date.today():
            raise ValidationError(_('Invalid date - renewal is set to a date in the past.'))

        # Check if a date is in the allowed range (+4 weeks trom today).
        if data > datetime.date.today() + datetime.timedelta(weeks=4):
            raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead.'))

        # remember to always return cleaned data!
        return data

    class Meta:
        model = BookInstance
        fields = ['due_back']
        labels = {'due_back': _('New renewal date')}
        help_texts = {'due_back': _('Enter a date between now and 4 weeks (default: 3).')}
