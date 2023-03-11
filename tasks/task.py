from main import app

@app.task(name='puller-beam')
def some_work():
    print('Doing some work')
