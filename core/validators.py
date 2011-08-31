# -*- encoding: utf-8 -*-

from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError

def cpf_validator(value):
    is_valid = True

    def sum_of_digits(value, until=-2):
        sum_value = 0
        for i, v in enumerate(value[:until]):
            sum_value += (10 - i) * int(v)
        
        return sum_value
    
    def valid_digit(value, which_digit=-2):
        sum_value = sum_of_digits(value, which_digit)
        should_be = 0 if sum_value % 11 < 2 else 11 - sum_value % 11
        return str(should_be) == value[which_digit]


    if not value.isdigit():
        is_valid = False
        error_message = _(u'O CPF deve conter apenas números.')
    elif len(value) != 11:
        is_valid = False
        error_message = _(u'O CPF deve ter 11 dígitos.')
    elif len(set(value)) == 1:
        is_valid = False
        error_message = _(u'CPF inválido.')
    elif not valid_digit(value) and not valid_digit(value, -1):
        is_valid = False
        error_message = _(u'CPF inválido.')

    if not is_valid:
        raise ValidationError(error_message)
