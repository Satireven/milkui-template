{{ cookiecutter.formal_name }}
{{ "=" * cookiecutter.formal_name|length }}

{{ cookiecutter.description }}

Usage
-----

* `milkui new` - Bootstrap a new project
* `milkui dev` - Run the app in developer mode, using the current virtual environment.
* `milkui create` - Use the platform template to generate the files needed to build a distributable artefact for the platform.
* `milkui update` - Update the source code of the application in the generated project.
* `milkui build` - Run whatever compilation process is necessary to produce an executable file for the platform.
* `milkui run` - Run the executable file for the platform.
* `milkui package` - Perform whatever post-processing is necessary to wrap the executable into a distributable artefact (e.g., an installer).
