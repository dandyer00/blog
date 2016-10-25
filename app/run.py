from app import app
from flask import Flask

if __name__ == '__main__':
    print 'in main'
    app.run(debug=True,host='0.0.0.0')