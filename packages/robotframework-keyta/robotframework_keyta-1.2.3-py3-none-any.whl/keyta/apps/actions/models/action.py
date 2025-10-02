from django.db import models
from django.utils.translation import gettext as _

from apps.common.abc import AbstractBaseModel
from apps.keywords.models.keyword import KeywordType
from apps.windows.models import WindowKeyword


class Action(WindowKeyword):
    @property
    def library_ids(self) -> set[int]:
        return set(self.library_imports.values_list('library_id', flat=True))

    def save(
            self, force_insert=False, force_update=False,
            using=None, update_fields=None
    ):
        if not self.pk:
            self.type = KeywordType.ACTION

        super().save(force_insert, force_update, using, update_fields)

    class Manager(models.Manager):
        def get_queryset(self):
            return (
                super()
                .get_queryset()
                .filter(type=KeywordType.ACTION)
            )

    objects = Manager()

    class Meta:
        proxy = True
        verbose_name = _('Aktion')
        verbose_name_plural = _('Aktionen')


class ActionDocumentation(Action):
    class Meta:
        proxy = True
        verbose_name = _('Aktion Dokumentation')


class ActionWindow(AbstractBaseModel, Action.windows.through):
    def __str__(self):
        return str(self.window)

    class Meta:
        auto_created = True
        proxy = True
        verbose_name = _('Beziehung zu Maske')
        verbose_name_plural = _('Beziehungen zu Masken')


class WindowAction(Action):
    def __str__(self):
        return str(self.name)

    class Meta:
        proxy = True
        verbose_name = _('Aktion')
        verbose_name_plural = _('Aktionen')
