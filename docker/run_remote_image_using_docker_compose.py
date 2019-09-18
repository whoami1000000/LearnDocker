import subprocess

COMPOSE_FILE = 'docker/docker-compose.yml'

APP_NAME = 'echoservice'


def run_cmd(command: str):
    subprocess.run(command.split(' '))


def main():
    run_cmd('docker swarm init --force-new-cluster')
    run_cmd(f'docker stack deploy -c {COMPOSE_FILE} {APP_NAME}')


if __name__ == '__main__':
    main()
