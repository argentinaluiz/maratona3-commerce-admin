from django.contrib.auth.models import UserManager
from django.db import models
from tenant.utils import get_tenant, get_tenant_filters


class TenantManager(models.Manager):
    def get_queryset(self):
        queryset = self._queryset_class(self.model)
        current_tenant = get_tenant()
        if current_tenant:
            kwargs = get_tenant_filters()
            return queryset.filter(**kwargs)
        return queryset


class UserTenantManager(UserManager):
    def get_queryset(self):
        current_tenant = get_tenant()
        return super().get_queryset().filter(user_member__tenant=current_tenant)