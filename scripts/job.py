import sys

import flask.cli


def main() -> int:
    flask.cli.load_dotenv()
    from vault import app

    args = sys.argv
    job_name = args.pop(1)
    mod_name = 'vault.jobs.%s' % job_name
    mod = __import__(mod_name, fromlist=['*'])

    with app.app_context():
        mod.run(*sys.argv[1:])

    return 0


if __name__ == '__main__':
    sys.exit(main())
