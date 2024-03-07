from flask import Flask,  render_template, request, jsonify, session
from init_db import getImagesFromDatabase, handleImageVote, insertToDatabase, Get_comapre_images
import time
import random
from pytube import YouTube
app = Flask(__name__)


@app.route('/get-images', methods=['GET'])
def get_images():
    images = getImagesFromDatabase()
    return jsonify(images)


@app.route("/", methods=['GET', 'POST'])
def home(): 
    if request.method == 'POST':
        urlofimg = request.form['urlOFImg']
        title  = request.form['title']
        yt = YouTube(urlofimg)
        thumbnailUrl = yt.thumbnail_url
        try:
            insertToDatabase(title,thumbnailUrl)
            return render_template('index.html')
        except:
            return print('try to insert but fail')
    return render_template('index.html')


@app.route("/get-compare-images")
def getCompaireImages():
    image = Get_comapre_images()
    newArray = image["topFive"] + image["medium"]
    random.shuffle(newArray)
    img1 = random.choice(newArray)
    img2 = random.choice(newArray)
    
    while img1 == img2:
        img2 = random.choice(newArray)

    return jsonify([img1, img2])


@app.route("/post-image-vote", methods=["POST","GET"])
def postImageVotes(): 
    if request.method == 'POST':
        selectedId = request.form['selectedID'] 
        remainingId = request.form['remainingID']
        
        try:
           handleImageVote(selectedId, remainingId)
           return jsonify({"status": True})
        except:
            print('try to insert but fail')
            return jsonify({"status": False})
        
    return jsonify({"status": True})