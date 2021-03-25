from flask import Flask
import datetime


app=Flask(__name__, templates_folder='.')

@app.route('/')
def index():
    bday=datetime.datetime.now()
    
    return render_template('index.html', dt=bday)


if __name__ =='__main__':
    app.run()
    
