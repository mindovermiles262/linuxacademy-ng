#!/usr/bin/env python3

import random
import requests
import string
import pdb

import login_params as lp


class LinuxAcademyLogin:
    def login(email, passwd):
        # Makes HTTP POST request to post_url with auth_params body
        post_url = 'https://login.linuxacademy.com/usernamepassword/login'
        params = lp.LoginParams.get()
        state = params['state']
        csrf = params['csrf']
        nonce = LinuxAcademyLogin.get_nonce(32)

        auth_params = {
            "client_id": "KaWxNn1C2Gc7n83W9OFeXltd8Utb5vvx",
            "redirect_uri": "https://linuxacademy.com/cp/ssologin",
            "tenant": "lacausers",
            "response_type": "token id_token",
            "connection": "Username-Password-Authentication",
            "username": email,
            "password": passwd,
            "nonce": nonce,
            "state": state,
            "sso": 'true',
            "_csrf": csrf,
            "audience": "https://linuxacademy.com",
            "auth0Client": "eyJuYW1lIjoiYXV0aDAuanMiLCJ2ZXJzaW9uIjoiOS40LjEifQ==",
            "scope": "openid email user_impersonation profile",
            "protocol": "oauth2",
            "sign_up": "false"
        }

        response = requests.post(post_url, json=auth_params)
        print(response)
        pdb.set_trace()

    def get_nonce(length):
        nonce = ""
        for n in range(length):
            rdm = random.choice(string.ascii_letters + string.digits)
            nonce += rdm
        return nonce


LinuxAcademyLogin.login('me@myself.com', 'password123')
