from flask import Flask, render_template, request, redirect # added request
app = Flask(__name__)   

@app.route('/')          
def submit_fourm():
    return render_template("index.html")

@app.route('/show', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name = request.form['name']
    location = request.form['location']
    fav_lang = request.form['fav']
    comment = request.form['comment']
    comm_length = len(comment)
    return render_template("show.html", name = name, location = location, fav_lang = fav_lang, comment = comment, length = comm_length )

if __name__=="__main__":   
    app.run(debug=True)