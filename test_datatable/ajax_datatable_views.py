from ajax_datatable.views import AjaxDatatableView
from .models import *


class StudiesAjaxDatatableView(AjaxDatatableView):

    model = Studies
    title = 'Studies'
    initial_order = [ ]
    length_menu = [[10, 20, 50, 100, -1], [10, 20, 50, 100, 'all']]
    search_values_separator = '+'

    column_defs = [
        AjaxDatatableView.render_row_tools_column_def(),
        {'name': 'id', 'visible': True, },
        {'name': 'patient_fio', 'visible': True, },
        {'name': 'patient_birthdate', 'visible': True, },
        {'name': 'study_uid', 'visible': True, },
        {'name': 'study_date', 'visible': True, },
        {'name': 'study_modality', 'foreign_field': 'study_modality__name', 'visible': True, },
    ]

