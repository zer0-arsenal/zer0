#!/bin/bash

#パッケージ管理ツールのインストール
apt-get install python-setuptools python-pip

#インストールできるかの確認(7.で使用するモジュールをインストール)
pip install github3.py

