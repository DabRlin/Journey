from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
#使用Flask-CORS库来解决跨域资源共享问题
CORS(app)