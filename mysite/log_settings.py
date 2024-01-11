# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'standard': {
            'format': '[{levelname}] [{asctime}] [{module}] [{funcName}] [{message}]',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'info': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': BASE_DIR / 'logs/info.log',
        },
        'warning': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': BASE_DIR / 'logs/warning.log',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': BASE_DIR / 'logs/error.log',
        },
        'file_access_log': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/access.log',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'info', 'warning', 'error'],
            'level': 'INFO',
            'propagate': False,
        },
        '': {
            'handlers': ['file_access_log'],  # Assign the file_access_log handler to the root logger
            'level': 'INFO',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['info'],  # Assign the info handler to the django.server logger
            'level': 'INFO',
            'propagate': False,
        },
    },
}