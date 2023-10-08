from flask import Flask , render_template , request
import pickle

app = Flask(__name__ )
#load the model 

model = pickle.load(open('saved_model.sav' , 'rb'))


@app.route('/')
def home():
    
  
    return render_template('Home.html', **locals())

@app.route('/Form.html')
def form():
    
    
    return render_template('Form.html')

@app.route('/portability' , methods = ['POST' , 'GET'])
def portability():
    
    ph = float(request.form['ph'])
    hardness = float(request.form['hardness'])
    solids = float(request.form['solids'])
    chloramines = float(request.form['chloramines'])
    sulfate = float(request.form['sulfate'])
    conductivity = float(request.form['conductivity'])
    organic_carbon = float(request.form['organic_carbon'])
    trihalomethanes = float(request.form['trihalomethanes'])
    turbidity = float(request.form['turbidity'])
    
    result = model.predict([[ph , hardness , solids , chloramines , sulfate , conductivity , organic_carbon , trihalomethanes , turbidity]])
    
    result_str = 'portable' if result == 1 else 'not portable'
    
    return render_template('portable.html' , result_str = result_str)

if __name__ == '__main__':
    
    app.run(debug=True)
    
    

