from flask import Flask, render_template,request,url_for
import joblib
model = joblib.load('bike_model.lb')
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')

# from sklearn.preprocessing import LabelEncoder
@app.route('/project', methods = ['POST','GET'])
def predict():
    if request.method == 'POST':   
        brand_name =request.form['brand_name']
        owner =request.form['owner']
        age =request.form['age']
        power =request.form['power']
        kms_driven =request.form['kms_driven']
        bike_number = {'TVS': 0,
                        'Royal Enfield': 1,
                        'Triumph': 2,
                        'Yamaha': 3,
                        'Honda': 4,
                        'Hero': 5,
                        'Bajaj': 6,
                        'Suzuki': 7,
                        'Benelli': 8,
                        'KTM': 9,
                        'Mahindra': 10,
                        'Kawasaki': 11,
                        'Ducati': 12,
                        'Hyosung': 13,
                        'Harley-Davidson': 14,
                        'Jawa': 15,
                        'BMW': 16,
                        'Indian': 17,
                        'Rajdoot': 18,
                        'LML': 19,
                        'Yezdi': 20,
                        'MV': 21,
                        'Ideal': 22}
        brand_name=bike_number[brand_name]

        print('output>>>>>>',brand_name,owner,age,power,kms_driven)
        lst = [[
            int(brand_name),
            int(owner),
            int(age),
            int(power),
            int(kms_driven)]]
        pred = model.predict(lst)[0]
        print('output from model',pred)
        pred= pred.item()
        pred= round(pred,2)
        print(pred)

        return render_template('project.html', prediction = str(pred))
    return render_template("project.html")


if __name__=='__main__':
    app.run(debug=True)