'''
  Jeswin Mathew
  CSE-4381-001
  Professor David Levine

Watermarking implementation:
Here is the app.py or the main python script needed to do the watermarking implementation

The link for the website is: http://jxm2012.pythonanywhere.com/

As mentioned in the previous email to Dr. Levine, for some reason the PythonAnywhere website is not properly displaying the final image after the watermaking process is done, but it works in my local machine or anywhere flask can be run.
The final output image is saved as "output.png" in the folder when it's run. Please read the README.txt file before running.

Resources used for this project:
https://pythonise.com/series/learning-flask/flask-uploading-files

https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/

'''

#libraries needed for image processing and Flask's methods
import os
from PIL import Image
from flask import Flask, request, render_template, send_file

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))


#function for watermarking, it takes in the original image
#with the image to be watermarked. 
def addWatermark(originalImg, watermarkImg, outputImg, position):
	orgImg = Image.open(originalImg).convert("RGBA")
	wmImg = Image.open(watermarkImg).convert("RGBA")
	orgImg.paste(wmImg, position, mask=wmImg)
	orgImg.save(outputImg)
	return orgImg;

#renders the index.html at the start of webpage
@app.route("/")
def index():
    return render_template("index.html")

#retrieves the uploaded images from user from POST method
@app.route("/upload", methods=["POST"])
def upload():
    origImg = request.files['originalImage']
    wmImg = request.files['watermark']
    #saves the output in a separate file
    outFileName = 'output.png'
    outputImg = addWatermark(origImg, wmImg, outFileName, position = (0,0))
    return send_file(outFileName, mimetype='image/png')

#run at 127.0.0.5000
if __name__ == "__main__":
    app.run(debug=True)

