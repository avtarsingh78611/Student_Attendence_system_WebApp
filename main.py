from flask import Flask, render_template, request, redirect
import os
import face_rec
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = "/Users/avtar/PycharmProjects/flaskProject/static/images"

from werkzeug.utils import secure_filename
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='face'
mysql=MySQL(app)
# fname = ("Rosss", 37, 12345, 'av@gmail.com')
#         cur = mysql.connection.cursor()
#         cur.execute("",fname)
#         mysql.connection.commit()
#         cur.close()

headings = ("Students Present")

@app.route('/Home', methods=["POST", "GET"])
def upload_image():  # put application's code here
    if request.method == "POST":
        image = request.files.get('file', '')
        image_name = image.filename
        print(image.filename)
        new_image = face_rec.classify_face(image_name)
        data = tuple(face_rec.face_names)
        print(data)
        dy = list(map(int, data))
        lst = []
        for i in range(len(data)):
            lst.append(int(data[i]))
        print(lst)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        for i in range(len(dy)):
            cursor.execute("select * from st_details ")
                            #where rollno = ?", dy[i])
            dt = cursor.fetchall()
            print(dt)

        if image.filename == '':
            print("File name is invalid")
            return redirect(request.url)

        #filename = secure_filename(new_image.filename)
        basedir = os.path.abspath(os.path.dirname(__file__))
        #image.save(os.path.join(basedir, app.config["IMAGE_UPLOADS"], filename))
        return render_template("index.html", filename='one.png',headings=headings, data=data, dt=dt)
    return render_template('index.html')

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename="/images"+'one.png'), code=301)


if __name__ == '__main__':
    app.run(port=5000, debug=True)  #to run the application