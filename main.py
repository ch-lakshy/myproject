from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    # Get the uploaded file from the HTML form
    csv_file = request.files['csv_file']
    
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Convert the DataFrame into an HTML table
    table_html = df.to_html(index=False)
    
    # Pass the HTML table to the template
    return render_template('csvdisplay.html', table_html=table_html)


@app.route('/train_model')
def train_model():

if __name__ == '__main__':
    app.run(debug=True)