{% set app_class_name = cookiecutter.formal_name.title().replace(' ','').replace('-','').replace('!','').replace('.','').replace(',','') -%}
from milkui.interface.process import Process
from .app import {{ app_class_name }}
from .server import app

if __name__ == '__main__':
    Process(app={{ app_class_name }}, server=app, api=None).run()
