# -*- encoding: utf-8 -*-
"""
Copyright (c) 2024 - XC/EVI
"""

from django.utils.deprecation import MiddlewareMixin
import logging

logger = logging.getLogger(__name__)

class LogRequestsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Get the client's IP address
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        # Log the request details
        logger.info(f"Request at {request.path} received from {ip} on {request.META.get('HTTP_USER_AGENT')}")

        # Continue processing the request
        return None
