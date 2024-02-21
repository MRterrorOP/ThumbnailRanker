from flask import Flask, url_for, render_template, request, jsonify
from pytube import YouTube
app = Flask(__name__)
url = 'hello'
@app.route("/", methods=['GET', 'POST'])
def home(): 
    return render_template('index.html')
@app.route('/submit-form', methods=['POST'])
def submit_form():
    urlofimg = request.form['urlOFImg']
    title  = request.form['title']
    yt = YouTube(urlofimg)
    thumbnailUrl = yt.thumbnail_url
    # Process form data (e.g., save to database)
    
    # Return JSON response
    return jsonify({'url': thumbnailUrl,'title':title})


