import django_tables2 as tables

from .models import Presentation


class CheckBoxColumnWithName(tables.CheckBoxColumn):
    @property
    def header(self):
        return self.verbose_name


class PresentationTable(tables.Table):
    pagination_style = 'range'

    template = '<a href="/catalog/modify/{{record.presentation_id}}" class="btn btn-default">Modify</a>'
    modify = tables.TemplateColumn(template, orderable=False)

    class Meta:
        model = Presentation
