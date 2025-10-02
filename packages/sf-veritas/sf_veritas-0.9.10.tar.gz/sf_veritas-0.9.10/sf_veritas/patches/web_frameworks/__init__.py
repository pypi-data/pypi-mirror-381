from .aiohttp import patch_aiohttp
from .async_websocket_consumer import patch_async_consumer_call
from .blacksheep import patch_blacksheep
from .bottle import patch_bottle
from .cherrypy import patch_cherrypy
from .django import find_and_modify_output_wrapper, patch_django_middleware
from .eve import patch_eve
from .falcon import patch_falcon
from .fastapi import patch_fastapi
from .flask import patch_flask
from .klein import patch_klein
from .litestar import patch_litestar
from .pyramid import patch_pyramid
from .quart import patch_quart
from .robyn import patch_robyn
from .sanic import patch_sanic
from .starlette import patch_starlette
from .strawberry import patch_strawberry_schema
from .tornado import patch_tornado


def patch_web_frameworks():
    patch_strawberry_schema()
    patch_async_consumer_call()
    find_and_modify_output_wrapper()
    patch_django_middleware()
    patch_fastapi()
    patch_flask()
    patch_falcon()
    patch_bottle()
    patch_quart()
    patch_tornado()
    patch_aiohttp()
    patch_blacksheep()
    patch_cherrypy()
    patch_pyramid()
    patch_litestar()
    patch_klein()
    patch_eve()
    patch_sanic()
    patch_starlette()
    patch_robyn()


__all__ = ["patch_web_frameworks"]
