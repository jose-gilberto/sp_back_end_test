from flask import Blueprint
from flask import current_app
from flask import request
from flask import json

from urllib.parse import urlparse, parse_qs
import requests

bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    current_app.logger.debug("site Index called")
    return 'index route'


@bp.route("/api/users/")
def github_users_list():
    """List all the github users in this page"""
    since = request.args.get('since')

    req = requests.get(
        'https://api.github.com/users?since={}'.format(
            0 if since is None else since
        ))

    next_page_url = req.headers['link']. \
        split(',')[0].split(';')[0].replace("<", "").replace(">", "")
    next_page_url = urlparse(next_page_url)
    
    query_params = parse_qs(next_page_url.query)
    url = next_page_url._replace(query=None).geturl()

    res = {
        'status': 200,
        'message': 'Users listed with success',
        'data': req.json(),
        'next_page': '{}?since={}'.format(request.base_url, query_params['since'][0])
    }

    return res

@bp.route("/api/users/<username>/details/")
def github_user_details(username: str):
    """Get the user details"""

    req = requests.get(
        'https://api.github.com/users/{}'.format(username))
    
    res = {
        'status': 200,
        'message': 'List user details with success',
        'data': req.json()
    }

    return res


@bp.route("/api/users/<username>/repos/")
def github_user_repo_list(username: str):
    """List all the user repositories"""

    req = requests.get(
        'https://api.github.com/users/{}/repos'.format(username))
    
    res = {
        'status': 200,
        'message': 'Repository list returned with success',
        'data': req.json()
    }

    return res
