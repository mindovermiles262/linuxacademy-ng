#!/usr/bin/env python3

import requests


class LoginParams:
    def get():
        # Returns dict of URL Parameters including 'state', 'client',
        # 'protocol', and 'response_type'

        params = (
            ('client_id', 'KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx'),
            ('response_type', 'token')
        )

        response = requests.get(
            'https://login.linuxacademy.com/authorize',
            params=params
        )
        params_dict = LoginParams.split_url(response.url)
        params_dict['csrf'] = response.cookies.get_dict()['_csrf']
        params_dict['referer'] = response.url
        return params_dict

    def split_url(url):
        # Parses passed URL for query strings
        url_parameters = url.split('?')[1].split('&')
        return_dict = {}
        for param in url_parameters:
            kv = param.split('=')
            key = kv[0]
            value = kv[1]
            return_dict[key] = value
        return return_dict
