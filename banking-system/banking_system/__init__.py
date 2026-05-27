from __future__ import absolute_import, unicode_literals

# Import celery app if available. Make this tolerant so management
# commands (migrate, test, etc.) can run even if Celery/vine
# has compatibility issues with the current Python version.
try:
	from .celery import app as celery_app
except Exception:
	celery_app = None

__all__ = ('celery_app',)
