from flask import Flask
import config

app = Flask(__name__, instance_relative_config=True)
app.secret_key = 'lab3'
app.config.from_object(config)
