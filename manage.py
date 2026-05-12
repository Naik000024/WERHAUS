#!/usr/bin/env python
import os
import sys
import subprocess

if __name__ == "__main__":
    os.chdir(os.path.join(os.path.dirname(__file__), "warehouse_config"))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "warehouse_config.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
