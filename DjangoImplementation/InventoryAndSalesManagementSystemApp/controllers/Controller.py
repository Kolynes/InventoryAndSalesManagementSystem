#!/usr/bin/python
#-*- coding: utf-8 -*-

class Controller:
    def __init__(self):
        pass

    @classmethod
    def add_valuable(cls, request):
        """
        @post_param {string} name
        @post_param {float} price
        @post_param {integer} stock

        requires superuser
        """
        pass

    @classmethod
    def delete_valuable(cls, request):
        """
        @post_param {string} serial

        requires superuser
        """
        pass

    @classmethod
    def update_valuable(cls, request):
        """
        @post_param {string} name
        @post_param {float} price
        @post_param {integer} stock
        @post_param {string} serial

        requires superuser
        """
        pass

    @classmethod
    def sell_valuable(cls, request):
        """
        @post_param {string} valuable_serial
        @post_param {string} quantity
        @post_param {integer}  user_id
        """
        pass

