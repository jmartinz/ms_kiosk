from flask import Flask, render_template, request
import os
app = Flask(__name__)

# Load the main form template on webrequest for the root page
@app.route("/")
def main():

    # Create a template data dictionary to send any data to the template
    templateData = {
        'title' : 'index'
        }
    # Pass the template data into the template picam.html and return it to the user
    return render_template('index.html', **templateData)

# The function below is executed when someone requests a URL with a move direction
@app.route("/<direction>")
def move(direction):
    # Choose the direction of the request
    if direction == 'left':
	print 'left'
	bashCommand = "/home/pi/Quiosco/kiosk//scripts/play_nenes.sh"
	os.system(bashCommand)
	return 'left'
    elif direction == 'right':
	print 'right'
	return 'right'
    elif direction == 'up':
	bashCommand = "/home/jmartinpit/Desktop/rdeskCHERNO.sh &"
	os.system(bashCommand)
	return 'up'
    elif direction == 'down':
	for dirname, dirnames, filenames in os.walk('.'):
	    # print path to all subdirectories first.
	    for subdirname in dirnames:
		print(os.path.join(dirname, subdirname))

	    # print path to all filenames.
	    for filename in filenames:
		print(os.path.join(dirname, filename))
		return 'down'

# The function below is executed when someone requests a the pictures URL
@app.route("/pictures")
def pictures():
    files = "<html><body><table>"
    # for dirname, dirnames, filenames in os.walk('./static/Pictures'):
	#     # print path to all subdirectories first.
	#     #for subdirname in dirnames:
	# 	#print(os.path.join(dirname, subdirname))
    #
	#     # print path to all filenames.
	#     for filename in filenames:
	# 	print(os.path.join(dirname, filename))
	# 	item = os.path.join(dirname, filename) +"\n"
	# 	files += item

    for file in os.listdir("./static/Pictures"):
        if file.endswith(".png"):
            print(file)
            item = "<tr><td>"+file +"</td></tr>"
            files += item
    files += "</table></body></html>"
    return files

# Load the emplate on webrequest for the photos page
@app.route("/photos")
def photos():

    # Create a template data dictionary to send any data to the template
    templateData = {
        'title' : 'photos'
        }
    # Pass the template data into the template picam.html and return it to the user
    return render_template('photos.html', **templateData)    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5080, debug=True)
