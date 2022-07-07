import numpy as np
from flask import Flask
import pickle
from flask import Flask, request, render_template
model = pickle.load(open('model_heart.pkl', 'rb')) 
# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('index.html', 
                               result = 'Heart disease - Unlikely. No need to worry!')
    else:
        return render_template('index.html', 
                               result = 'Heart disease - Likely.Please go and see a doctor!')

if __name__ == '__main__':
#Run the application
    app.run()
