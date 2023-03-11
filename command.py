from doit.tools import LongRunning
def task_runworker():
    """
    run Worker
    """
    command = "celery -A main worker -l INFO -n puller@worker"

    yield {
        'actions': [LongRunning(command)],
        'watch': ['.'],
        'basename': 'runworker'
    }
