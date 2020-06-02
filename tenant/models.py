import uuid
from django.conf import settings
from django.contrib.sites.models import Site
from django.db import models
from django.utils.translation import gettext_lazy as _

from tenant.managers import TenantManager
from tenant.utils import get_tenant

class Tenant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.CharField(max_length=255)
    site = models.ForeignKey(Site, on_delete=models.PROTECT)

def assign_tenant(sender, instance, **kwargs):
    if not getattr(instance, settings.TENANT_FIELD):
        tenant = get_tenant()
        if tenant:
            setattr(instance, settings.TENANT_FIELD, tenant.id)

class TenantModel(models.Model):
    objects = TenantManager()
    tenant = models.ForeignKey(
        Tenant,
        null=True,
        on_delete=models.PROTECT,
        related_name='%(class)s_tenants',
        verbose_name=_('tenant')
    )

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        models.signals.pre_save.connect(assign_tenant, sender=cls)

    class Meta:
        abstract = True