from milkui.interface.process import Process
from .app import {{ cookiecutter.class_name }}
from .server import app

if __name__ == '__main__':
    Process(app={{ cookiecutter.class_name }}, server=app, api=None).run()