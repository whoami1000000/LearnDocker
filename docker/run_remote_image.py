import subprocess

USER = 'whoami1000000'
REPOSITORY = 'echoservice'
TAG = '0.0.1'

IMAGE = f'{USER}/{REPOSITORY}:{TAG}'

CONTAINER_NAME = REPOSITORY
PORT = '80:80'


def run_cmd(command: str):
    subprocess.run(command.split(' '))


def main():
    run_cmd('docker login')
    run_cmd(f'docker container stop {CONTAINER_NAME}')
    run_cmd(f'docker container rm {CONTAINER_NAME}')
    run_cmd(f'docker run --name {CONTAINER_NAME} -p {PORT} {IMAGE}')


if __name__ == '__main__':
    main()
