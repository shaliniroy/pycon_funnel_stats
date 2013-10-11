import flask
import subprocess
import time          #You don't need this. Just included it so you can see the output stream.
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

app = flask.Flask(__name__)

@app.route('/')
def index():
    def inner():
        proc = subprocess.Popen(
            ['python project1.py'],             #call something with a lot of output so we can see it
            shell=True,
            stdout=subprocess.PIPE
        )

        for line in iter(proc.stdout.readline,''):
            time.sleep(1)                           # Don't need this just shows the text streaming
            yield line.rstrip() + '<br/>\n'

    env = Environment(loader=FileSystemLoader('templates'))
    tmpl = env.get_template('project.html')
    return flask.Response(tmpl.generate(project=inner()))

app.run(debug=True, port=5000, host='0.0.0.0')
