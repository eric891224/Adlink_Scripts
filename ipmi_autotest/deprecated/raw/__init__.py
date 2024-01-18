import os

files = os.listdir(os.path.dirname(__file__))

__all__ = [file[:-3] for file in files if file.endswith('.py') and file not in ['__template.py', '__init__.py']]