from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': ' [{levelname}] [{asctime}] [{module}] [{funcName}] [{message}]',
            'style': '{',
        },
    },
    'handlers': {
        # Send all messages to console
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        # Send info messages to syslog
        'info':{
            'level':'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/info.log',
        },
        # Warning messages are sent to admin emails
        'warning': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/warnning.log',
        },
        # critical errors are logged to sentry
        'error': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs/error.log',
        },
    },
    'loggers': {
        'error_logger': {
            'handlers': ['console', 'info', 'warning', 'error'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # This is the "catch all" logger
        '': {
            'handlers': ['console', 'info', 'warning', 'error'],
            'level': 'DEBUG',
            'propagate': False,
        },
    }
}