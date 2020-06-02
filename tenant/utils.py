from typing import Optional, Union

from django.conf import settings


tenant: Optional['tenant.models.Tenant'] = None

def get_tenant_filters():
    filters = {}

    tenant_id = get_tenant().id if get_tenant() else None

    if not tenant_id:
        return filters

    filters[settings.TENANT_FIELD] = tenant_id

    return filters

def set_tenant(current_tenant: Union[str, 'tenant.models.Tenant']):
    global tenant

    from tenant.models import Tenant

    tenant = current_tenant \
        if isinstance(current_tenant, Tenant) \
        else Tenant.objects.get(site__domain=current_tenant)


def get_tenant() -> Optional['tenant.models.Tenant']:
    return tenant
