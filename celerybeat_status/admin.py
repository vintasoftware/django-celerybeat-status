from django.contrib.admin.sites import AdminSite

AdminSite.index_template = "celerybeat_status/custom_admin/index.html"
