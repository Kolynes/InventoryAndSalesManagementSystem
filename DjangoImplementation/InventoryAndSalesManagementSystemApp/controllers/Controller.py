#!/usr/bin/python
#-*- coding: utf-8 -*-

from ..models import Action, Valuable, Transaction
from ...utils.decorators import ensure_superuser
from ...utils.shortcuts import json_response

class Controller:
    def __init__(self):
        pass

    @classmethod
    def index(cls, request):
        pass

    @ensure_superuser
    @classmethod
    def add_valuable(cls, request):
        """
        @post_param {string} name
        @post_param {float} price

        requires superuser
        """
        valuable = Valuable(
            name=request.POST["name"],
            price=request.POST["price"]
        )
        valuable.save()
        Action(
            type=Action.VALUABLE_CREATED,
            valuable=valuable,
            user=request.user
        ).save()
        return json_response(True)

    @ensure_superuser
    @classmethod
    def delete_valuable(cls, request):
        """
        @post_param {string} serial

        requires superuser
        """
        try:
            valuable = Valuable.objects.get(serial=request.POST["serial"])
            Action(
                type=Action.VALUABLE_DELETED,
                valuable=valuable,
                user=request.user
            ).save()
            valuable.delete()
            return json_response(True)
        except Valuable.DoesNotExist:
            return json_response(False, error={"serial": "Valuable with this serial number does not exist"})

    @ensure_superuser
    @classmethod
    def stock_valuable(cls, request):
        """
        @post_param {integer} stock
        @post_param {float} amount
        @post_param {string} serial

        requires superuser
        """
        try:
            valuable = Valuable.objects.get(serial=request.POST["serial"])
            valuable.stock += request.POST["stock"]
            valuable.save()
            Transaction(
                quantity=request.POST["stock"],
                amount=request.POST["amount"],
                type=Transaction.PURCHASE,
                valuable=valuable,
                user=request.user
            ).save()
            Action(
                type=Action.VALUABLE_STOCKED,
                valuable=valuable,
                user=request.user
            ).save()
            return json_response(True)
        except Valuable.DoesNotExist:
            return json_response(False, error={"serial": "Valuable with this serial number does not exist"})

    @classmethod
    def destock_valuable(cls, request):
        """
        @post_param {integer} stock
        @post_param {string} serial

        requires superuser
        """
        pass

    @classmethod
    def change_valuable_name(cls, request):
        """
        @post_param {string} name
        @post_param {string} serial

        requires superuser
        """
        pass

    @classmethod
    def change_valuable_price(cls, request):
        """
        @post_param {float} price
        @post_param {string} serial

        requires superuser
        """
        pass

    @classmethod
    def sell_valuable(cls, request):
        """
        @post_param {string} serial
        @post_param {string} quantity
        """
        pass

    @classmethod
    def load_valuables(cls, request):
        """
        @get_param {string} q
        @get_param {integer} p
        """
        pass

    @classmethod
    def load_actions(cls, request):
        """
        @get_param {timestamp} to
        @get_param {timestamp} from
        @get_param {integer} p

        requires superuser
        """
        pass

    @classmethod
    def load_demands(cls, request):
        """
        @get_param {timestamp} from
        @get_param {timestamp} to
        @get_param {integer} p

        requires superuser
        """
        pass

    @classmethod
    def load_supplies(cls, request):
        """
        @get_param {timestamp} from
        @get_param {timestamp} to
        @get_param {integer} p

        requires superuser
        """
        pass

