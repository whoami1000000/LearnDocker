import json
import os
import socket

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    data = {
        'name': os.getenv('NAME', 'world'),
        'hostname': socket.gethostname()
    }

    return json.dumps(data, indent=4)


@app.route('/echo/<message>')
def echo(message):
    return json.dumps({'message': message}, indent=4)


def main():
    app.run(host='0.0.0.0', port=80)


if __name__ == '__main__':
    main()
