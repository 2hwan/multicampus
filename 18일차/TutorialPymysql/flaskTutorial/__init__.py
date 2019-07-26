from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'abc1234qwer'

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)

    app.add_url_rule('/', endpoint='index')
    #app.add_url_rule('/', view_func=blog.index, methods=['GET'])

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app