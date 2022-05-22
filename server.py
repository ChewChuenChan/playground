from flask import Flask, render_template

app = Flask(__name__)

# have the /play route render a template with 3 blue boxes
@app.route('/play')
def level_1():
    return render_template("index.html",times=3 ,colors="skyblue")

# have the /play/<x> route render a template with x number of blue boxes
@app.route('/play/<int:num>')
def level_2(num):
    return render_template("index.html",times=num, colors="skyblue")

# have the /play/<x>/<color> route render a template 
# with x number of boxes the color of the provided value
@app.route('/play/<int:num>/<string:boxcolor>')
def level_3(num, boxcolor):
    return render_template("index.html",times=num, colors=boxcolor)

if __name__=="__main__":
    app.run(debug=True)