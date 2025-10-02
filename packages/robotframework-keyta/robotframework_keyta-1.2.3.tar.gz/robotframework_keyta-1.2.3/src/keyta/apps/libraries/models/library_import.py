from typing import Optional
from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.translation import gettext as _

from apps.common.abc import AbstractBaseModel
from apps.rf_export.settings import RFLibraryImport

from .library import Library
from .library_import_parameter import LibraryImportParameter


__all__ = ['LibraryImport', 'LibraryImportType']


class LibraryImportType(models.TextChoices):
    FROM_EXECUTION = 'FROM_EXECUTION', _('Aus einer Ausführung')
    FROM_ACTION = 'FROM_ACTION', _('Aus einer Aktion')


class LibraryImport(AbstractBaseModel):
    execution = models.ForeignKey(
        'executions.Execution',
        on_delete=models.CASCADE,
        null=True,
        default=None,
        blank=True,
        related_name='library_imports'
    )
    keyword = models.ForeignKey(
        'keywords.Keyword',
        null=True,
        default=None,
        blank=True,
        on_delete=models.CASCADE,
        related_name='library_imports'
    )
    library = models.ForeignKey(
        Library,
        on_delete=models.CASCADE,
        verbose_name=_('Bibliothek')
    )
    type = models.CharField(max_length=255, choices=LibraryImportType.choices)

    def __str__(self):
        return f'{self.execution or self.keyword} -> {self.library}'

    def add_parameters(self, user: Optional[User]=None):
        for kwarg in self.library.kwargs.all():
            LibraryImportParameter.objects.get_or_create(
                library_import=self,
                user=user,
                library_parameter=kwarg,
                defaults={
                    'value': kwarg.default_value,
                }
            )

    def save(
        self, force_insert=False, force_update=False, using=None,
            update_fields=None
    ):
        if not self.pk:
            if self.keyword:
                self.type = LibraryImportType.FROM_ACTION
            if self.execution:
                self.type = LibraryImportType.FROM_EXECUTION

            super().save(force_insert, force_update, using, update_fields)

            if not self.execution:
                self.add_parameters()
        else:
            super().save(force_insert, force_update, using, update_fields)

    def to_robot(self, user: Optional[User]=None) -> RFLibraryImport:
        kwargs = self.kwargs.filter(user=user).all()

        return {
            'library': str(self.library),
            'kwargs': {kwarg.name: kwarg.value for kwarg in kwargs}
        }

    class QuerySet(models.QuerySet):
        def library_ids(self):
            return self.values_list('library', flat=True)

    objects = QuerySet.as_manager()

    class Meta:
        verbose_name = _('Bibliothek-Import')
        verbose_name_plural = _('Bibliothek-Imports')
        constraints = [
            models.CheckConstraint(
                name='library_import_sum_type',
                check=
                (Q(type=LibraryImportType.FROM_EXECUTION) &
                 Q(execution__isnull=False) &
                 Q(keyword__isnull=True))
                |
                (Q(type=LibraryImportType.FROM_ACTION) &
                 Q(execution__isnull=True) &
                 Q(keyword__isnull=False))
            ),
            models.UniqueConstraint(
                name='unique_execution_library_import',
                condition=Q(execution__isnull=False),
                fields=['execution', 'library'],
            ),
            models.UniqueConstraint(
                name='unique_keyword_library_import',
                condition=Q(keyword__isnull=False),
                fields=['keyword', 'library'],
            )
        ]
