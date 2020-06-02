from django.contrib.sites.models import Site
from django.contrib.sites.shortcuts import get_current_site
from django.utils.deprecation import MiddlewareMixin

from tenant.models import Tenant
from tenant.utils import set_tenant


class TenantMiddleware(MiddlewareMixin):

    def process_request(self, request):
        site = get_current_site(request)
        print(site)
        if isinstance(site, Site):
            try:
                set_tenant(Tenant.objects.get(site=site))
            except Site.DoesNotExist:
                pass
