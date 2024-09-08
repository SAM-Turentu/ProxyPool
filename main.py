# -*- coding: utf-8 -*-
# Author: SAM
# Email: SAM-Turentu@outlook.com
# Name: ProxyPool
# Filename: main
# CreateTime: 2024/9/8 23:08
# Summary: ''
import json

import requests


def get_ip():
    url = ''
    data = {}
    cookies = {}
    headers = {}
    response = requests.get(url, headers=headers, cookies=cookies, timeout=5)
    # for i in json.loads(response.text)["data"]:
    #     ip = {
    #         "http": f'{i["ip"]}: {i["port"]}',
    #         "https": f'{i["ip"]}: {i["port"]}',
    #     }
    return response.text


def save_ip(ip, port):
    ...


def check_ip():
    ...


def main():
    ip, port = get_ip()
    save_ip(ip, port)


if __name__ == '__main__':
    main()
