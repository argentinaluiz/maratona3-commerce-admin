class AllowedHosts(object):
    __slots__ = ('defaults', 'sites', 'cache')

    def __init__(self, defaults=None, cache=True):
        self.defaults = defaults or ()
        self.sites = None
        self.cache = cache

    def get_sites(self):
        if self.cache is True and self.sites is not None:
            return self.sites + self.defaults

        from django.contrib.sites.models import Site, SITE_CACHE
        sites = Site.objects.all()
        self.sites = tuple(site.domain for site in sites)

        if self.cache is True:
            for site_to_cache in sites:
                if site_to_cache.pk not in SITE_CACHE:
                    SITE_CACHE[site_to_cache.pk] = site_to_cache

        return self.sites + self.defaults

    def __iter__(self):
        return iter(self.get_sites())

    def __str__(self):
        return ', '.join(self.get_sites())

    def __contains__(self, other):
        return other in self.get_sites()

    def __len__(self):
        return len(self.get_sites())

    def __add__(self, other):
        return self.__class__(defaults=self.defaults + other.defaults)
