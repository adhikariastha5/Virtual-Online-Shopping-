
#import pygame
#import imutils
#import numpy as np 
from flask import Flask, redirect, render_template, url_for, request


app = Flask(__name__)

@app.route('/')
def index():
	'''main page'''
	return render_template('home.jinja2')


@app.route('/cam')
def get_image():
	'''get the image of the customer'''
	return render_template('home.jinja2')

@app.route('/dress')
def body_detect_and_dress():
	'''detects body and overlays the dress in the body'''
	return render_template('dress.jinja2')

@app.route('/dress1')
def body_detect_and_dress1():
	'''detects body and overlays the dress in the body'''
	return render_template('dress.jinja2')

@app.route('/dress2')
def body_detect_and_dress2():
	'''detects body and overlays the dress in the body'''
	return render_template('dress.jinja2')

@app.route('/dress3')
def body_detect_and_dress3():
	'''detects body and overlays the dress in the body'''
	return render_template('dress.jinja2')

@app.route('/dress4')
def body_detect_and_dress4():
	'''detects body and overlays the dress in the body'''
	return render_template('dress.jinja2')
if __name__ == "__main__":
	app.run(debug= True)