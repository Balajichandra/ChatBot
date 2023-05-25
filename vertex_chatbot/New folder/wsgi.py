from app import app as hello_app
from mail import app1 as bye_app
from werkzeug.wsgi import DispatcherMiddleware

application = DispatcherMiddleware(None, {
    '/hello': hello_app,
    '/bye': bye_app,
})