from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig

class TenantConfig(AdminConfig):
    name = 'tenant'
    default_site = 'tenant.admin_tenant.admin_tenant_site'


