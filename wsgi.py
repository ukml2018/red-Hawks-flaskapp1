from flask import Flask,render_template, request, jsonify, redirect, flash, url_for
import speech_recognition as sr
from flask_mysqldb import MySQL
import pymysql
import os
import yaml
from werkzeug.utils import secure_filename
import json
from watson_developer_cloud import VisualRecognitionV3
UPLOAD_FOLDER = '/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

#app = Flask(__name__)
application = Flask(__name__)
GOOGLE_SPEECH_API_KEY = None
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#config Db
#db =yaml.load(open('db.yaml'))
#app.config["MYSQL_HOST"] =db['mysql_host']
#app.config["MYSQL_USER"] =db['mysq_user']
#app.config["MYSQL_PASSWORD"] =db['mysql_password']
#app.config["MYSQL_DB"] =db['mysql_db']
#mysql=MySQL(app)
#dbServerName = "129.146.85.135"
dbServerName = "172.30.132.124"
dbUser = "xxuser"
dbPassword = "welcome1"
dbName = "sampledb"
charSet = "utf8mb4"
cusrorType = pymysql.cursors.DictCursor
connectionObject = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword,
                                   db=dbName, charset=charSet, cursorclass=cusrorType)


#@app.route('/', methods=['GET', 'POST'])
@application.route('/', methods=['GET', 'POST'])
def find():
    #print(os.path)
    if request.method == 'POST':
        #userDetails = request.form
        #input = userDetails["name"]
        input = request.form["name"]
        #print(request.files)
        file = request.files['file']
        #print(type(file))
        if file.filename != '':
            filename = secure_filename(file.filename)
            #print(filename)
            SRCDIR = os.path.dirname(os.path.abspath(__file__))
            #print(SRCDIR)
            DATADIR = os.path.join(SRCDIR, 'images')
            #print(DATADIR)
            file.save(os.path.join(DATADIR, filename))
            #print('uploaded')
            apiKey = "vtrNuNjYNOQ82JmjBi7X0vmpsQT9jc5z7Nu9P6rWJv3h"
            version = "2020-01-16"
            visual_recognition = VisualRecognitionV3(version=version, iam_apikey=apiKey)
            with open(os.path.join(DATADIR, filename), 'rb') as images_file:
                classes = visual_recognition.classify(
                    images_file,
                    threshold='0.6',
                    classifier_ids='DefaultCustomModel_1149885701').get_result()
            data = (json.dumps(classes, indent=2))
            data = (data[data.index('"class": "') + 10:data.index(''"score"'') - 2]).rstrip()
            data = data[0:data.index('"')]
            if data !='':
                if data== 'tshirt':
                    input ='shirt'
                else:
                    input =data
        input = '%'+input +'%'
        #print(input)
            #email = userDetails["email"]
        #cur = mysql.connection.cursor()
        cur = connectionObject.cursor()
        query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
        resultValue = cur.execute(query_string,(input,))
        if resultValue > 0:
            #print('1')
            userDetails = cur.fetchall()
            #print('2')
            return render_template('users.html', userDetails=userDetails)
        #mysql.connection.commit()
        cur.close()
        #return 'Success'
    return render_template('index1.html')
#@app.route('/contact', )
@application.route('/contact', )
def contact():
    return render_template('contact.html')

#@app.route('/about', )
@application.route('/about', )
def about():
    return render_template('about.html')

#@app.route('/login', )
@application.route('/login', )
def login():
    return render_template('login.html')

#@app.route('/Technolgy', )
@application.route('/Technolgy', )
def Technolgy():
    return render_template('Technolgy.html')

#@app.route('/Project', )
@application.route('/Project', )
def Project():
    return render_template('project.html')

#@app.route('/all')
@application.route('/all')
def all():
    #cur = mysql.connection.cursor()
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number ";
    resultValue=cur.execute(query_string )
    if resultValue>0:
        userDetails =cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
#@app.route('/Search')
#def users():
#    cur = mysql.connection.cursor()
#    resultValue=cur.execute("Select * from  users")
#    if resultValue>0:
#        userDetails =cur.fetchall()
#        return render_template('users.html',userDetails=userDetails)
#@app.route('/Reflex Women')
@application.route('/Reflex Women')
def Reflex_Women():
    #cur = mysql.connection.cursor()
    input = '%'+'Reflex Women'+ '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue=cur.execute(query_string ,(input,))
    if resultValue>0:
        userDetails =cur.fetchall()
        return render_template('users.html',userDetails=userDetails)

#@app.route('/Reflex Men')
@application.route('/Reflex Men')
def Reflex_Men():
    #cur = mysql.connection.cursor()
    input = '%'+'Reflex Men'+ '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue=cur.execute(query_string ,(input,))
    if resultValue>0:
        userDetails =cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
#@app.route('/MLANM Mens')
@application.route('/MLANM Mens')
def MLANM_Mens():
    #cur = mysql.connection.cursor()
    input = '%'+'MLANM Mens'+ '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue=cur.execute(query_string ,(input,))
    if resultValue>0:
        userDetails =cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
#@app.route('/Gildan Men')
@application.route('/Gildan Men')
def Gildan_Men():
    #cur = mysql.connection.cursor()
    input = '%'+'Gildan Men'+ '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue=cur.execute(query_string ,(input,))
    if resultValue>0:
        userDetails =cur.fetchall()
        return render_template('users.html',userDetails=userDetails)
#@app.route('/IWOLLENCE Womens')
@application.route('/IWOLLENCE Womens')
def IWOLLENCE_Womens():
    #cur = mysql.connection.cursor()
    input = '%'+'IWOLLENCE Womens'+ '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue=cur.execute(query_string ,(input,))
    if resultValue>0:
        userDetails =cur.fetchall()
        return render_template('users.html',userDetails=userDetails)


#@app.route('/Disposable')
@application.route('/Disposable')
def Disposable():
    # cur = mysql.connection.cursor()
    input = '%' + 'Disposable' + '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue = cur.execute(query_string, (input,))
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)

#@app.route('/PAUL JONES Men')
@application.route('/PAUL JONES Men')
def PAUL_JONES_Men():
    # cur = mysql.connection.cursor()
    input = '%' + 'PAUL JONES Men' + '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue = cur.execute(query_string, (input,))
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)

#@app.route('/MUSHARE Women')
@application.route('/MUSHARE Women')
def MUSHARE_Women():
    # cur = mysql.connection.cursor()
    input = '%' + 'MUSHARE Women' + '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue = cur.execute(query_string, (input,))
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)
#@app.route('/Kenneth Cole')
@application.route('/Kenneth Cole')
def Kenneth_Cole():
    # cur = mysql.connection.cursor()
    input = '%' + 'Kenneth Cole' + '%'
    print(input)
    cur = connectionObject.cursor()
    query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(sku.description) like  lower(%s)";
    resultValue = cur.execute(query_string, (input,))
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)



#@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
@application.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    print(product_id)
    if request.method == 'GET':

        input = product_id

            #email = userDetails["email"]
        #cur = mysql.connection.cursor()
        cur = connectionObject.cursor()
        query_string = "select pr.item_number itemid, sku.description descp, pr.list_price rprice, pr.price_effective_date edate, (pr.list_price -  IFNULL(pr.discount,0)) dis, sku.SKU_ATTRIBUTE_VALUE1 size, sku.SKU_ATTRIBUTE_VALUE2 color, concat('http://getproductimage-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/get-image-for-item-id/',pr.item_number)  image from XXIBM_PRODUCT_PRICING pr, XXIBM_PRODUCT_SKU sku where pr.item_number = sku.item_number and lower(pr.item_number)  = (%s)";
        print(query_string)
        resultValue = cur.execute(query_string,(input,))
        if resultValue > 0:
            #print('1')
            userDetails = cur.fetchall()
            #print('2')
            return render_template('product.html', userDetails=userDetails)
        #mysql.connection.commit()
        cur.close()
        #return 'Success'
    return render_template('index1.html')

#@app.route('/product/checkout',  methods=['GET', 'POST'])
@application.route('/product/checkout',  methods=['GET', 'POST'])
def Checkout():
    if request.method == 'GET':
        return render_template('Checkout.html')
#@app.route('/mic', methods=["GET", "POST"] )
@application.route('/mic', methods=["GET", "POST"] )
def mic():
    extra_line = ''

    if request.method == "POST":
       # Speech Recognition stuff.
       r = sr.Recognizer()
       m = sr.Microphone()
       #with m as source: r.adjust_for_ambient_noise(source)
       print('test1')
       #while True:
       with m as source:audio = r.listen(source)
       print('test 1.5')
       try:
           print('test2')
           text = r.recognize_google(audio)
           extra_line = f'"{text}"'
           print(extra_line)
       except:
            print('test3')
            text ="Sorry Could not recognize your voice"
            extra_line = f'"{text}"'
            print(extra_line)
               # we need some special handling here to correctly print unicode characters to standard output

            #except KeyboardInterrupt:
            #pass
         #   audio_data = recognizer.listen(source)
         #   try:
         #       text = recognizer.recognize_google(audio_data)
         #       extra_line = f'"{text}"'
         #   except:
         #       text ="Sorry Could not reconize your voice"
         #       extra_line = f'"{text}"'

        #text = recognizer.recognize_google(
         #       audio_data, key=GOOGLE_SPEECH_API_KEY, language="ru-RU"
        #    )
    return f"""
    <!doctype html>
    <title>Microphone</title>
    <h1>Microphone</h1>
    <form method=post enctype=multipart/form-data name='myForm'>
      <input type=text name=name value= " ">
      <p/>
      <input type=submit value=record>
     <input type=button  onclick="newfind(extra_line)" value=search>
    </form>
    <script type="text/javascript"> 
    document.forms['myForm']['name'].value = {extra_line};
</script>
    """


if __name__ =='__main__':
    application.run(debug = True)