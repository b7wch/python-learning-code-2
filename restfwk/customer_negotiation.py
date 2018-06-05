#!/usr/bin/python
# -*- coding:utf-8 -*-
# 2018/5/3

from rest_framework.negotiation import DefaultContentNegotiation


class CustomNegotiation(DefaultContentNegotiation):
    def get_accept_list(self, request):
        header = request.META.get('HTTP_ACCEPT', '*/*')
        nsfocus_header = [item.strip() for item in header.split(";")]
        if nsfocus_header and nsfocus_header[0].lower() == "application/nsfocus.nti.spec+json":
            header = "*/*"
        return [token.strip() for token in header.split(',')]
