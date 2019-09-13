import subprocess

USER = 'whoami1000000'
REPOSITORY = 'echoservice'
TAG = '0.0.1'

IMAGE = f'{USER}/{REPOSITORY}:{TAG}'


def run_cmd(command: str):
    subprocess.run(command.split(' '))


def main():
    run_cmd(f'docker image rm {REPOSITORY}:{TAG} -f')
    run_cmd(f'docker build --tag={IMAGE} --file=docker/Dockerfile .')
    run_cmd('docker login')
    run_cmd(f'docker push {IMAGE}')


if __name__ == '__main__':
    main()
