

import os
import urllib

import flask

import zoom
import zoom.request
import zoom.middleware


class CustomBlueprint(flask.Blueprint):

    zoom_params = {}

    def __init__(self):
        super().__init__('dynamic', __name__)


dynamic = CustomBlueprint()


def get_blueprint(username=None, instance=None):
    if username:
        dynamic.zoom_params['username'] = username
    if instance:
        dynamic.zoom_params['instance'] = instance
    return dynamic


def setup():

    params = dict(dynamic.zoom_params)

    specific_path = params.pop('instance')
    instance_path = specific_path or os.environ.get('ZOOM_INSTANCE_PATH', '.')

    url = flask.request.url
    parsed = urllib.parse.urlparse(url)

    data = {}
    for key in flask.request.values:
        value = flask.request.values.getlist(key)
        if len(value) == 1:
            data[key] = value[0]
        else:
            data[key] = value

    host = parsed.hostname + (
        (':' + str(parsed.port)) if str(parsed.port) != '80' else ''
    )

    request = zoom.request.Request(
        dict(
            REQUEST_METHOD=flask.request.method,
            SCRIPT_NAME='flask.wsgi',
            PATH_INFO=parsed.path,
            QUERY_STRING=parsed.query,
            SERVER_NAME=parsed.hostname,
            SERVER_PORT=parsed.port or 80,
            HTTP_HOST=host,
        ),
        instance_path,
        **params
    )
    request.cookies = flask.request.cookies
    if data:
        request.body_consumed = True
        request.data_values = data

    zoom.system.providers = []
    zoom.system.request = request
    return request


def get_response(value):
    response = value.as_wsgi()
    status, headers, body = response
    return flask.make_response(
        body, status, headers
    )


@dynamic.route('/')
@dynamic.route('/<path:path>', methods=['GET', 'POST'])
def dynamic_world(path=None):  # pylint: disable=unused-argument
    request = setup()
    return get_response(zoom.middleware.handle(request))
