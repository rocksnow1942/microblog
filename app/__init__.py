from flask import Flask, request,current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel,lazy_gettext as _l


babel = Babel()
db = SQLAlchemy()
migrate=Migrate()
mail = Mail()
bootstrap = Bootstrap()
moment = Moment()
login = LoginManager()
login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    babel.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login.init_app(app)



    from app.errors import bp as errors_bp
    app.register_blueprint(errors_bp)

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp,url_prefix='/auth')

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    #setup log and mail log.
    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'],app.config['MAIL_PASSWORD'])
            secure=None
            if app.config['MAIL_USE_TLS']:
                secure = ()
            mail_handler = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'],app.config['MAIL_PORT']),
                fromaddr='no-reply@'+app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'],
                subject='FLASK TEST Microblog Failure',
                credentials=auth,secure=secure
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log',maxBytes=10240,backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
        ))
        file_handler.setLevel(logging.ERROR)
        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.ERROR)
        app.logger.info('Microblog startup')

    return app

@babel.localeselector
def get_locale():
    # return 'zh'
    return request.accept_languages.best_match(current_app.config['LANGUAGES'])

from app import models
