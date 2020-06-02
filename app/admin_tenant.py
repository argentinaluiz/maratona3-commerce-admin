from django.contrib.admin import ModelAdmin
from django.contrib import admin

from app.models import Category, Product
from tenant.admin_tenant import AdminTenantModelAdmin, admin_tenant_site


@admin.register(Category, site=admin_tenant_site)
class CategoryAdmin(ModelAdmin, AdminTenantModelAdmin):
    search_fields = ('name',)

@admin.register(Product, site=admin_tenant_site)
class ProductAdmin(ModelAdmin, AdminTenantModelAdmin):
    search_fields = ('name',)