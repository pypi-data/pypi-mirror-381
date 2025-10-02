from django.db import models
from django.utils.translation import gettext as _

from .library_parameter import LibraryParameter


__all__ = ['LibraryImportParameter']

from django.contrib.auth.models import User


class LibraryImportParameter(models.Model):
    library_import = models.ForeignKey(
        'libraries.LibraryImport',
        on_delete=models.CASCADE,
        related_name='kwargs'
    )
    library_parameter = models.ForeignKey(
        LibraryParameter,
        on_delete=models.CASCADE
    )
    value = models.CharField(max_length=255, verbose_name=_('Wert'))
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self.library_parameter.name

    class Meta:
        verbose_name = _('Parameter')
        verbose_name_plural = _('Parameters')
