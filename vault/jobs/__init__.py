import click

from vault import app


@app.cli.command('job')
@click.argument('job_name')
def run_job(job_name: str):
    print(job_name)
