#!/usr/bin/env python
"""Root wrapper for Django management commands."""
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR / 'banking-system'

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'banking_system.settings')

try:
    from django.core.management import execute_from_command_line
except ImportError as exc:
    raise ImportError(
        "Couldn't import Django. Make sure dependencies are installed and "
        "that PYTHONPATH includes the project directory."
    ) from exc

if __name__ == '__main__':
    execute_from_command_line(sys.argv)
