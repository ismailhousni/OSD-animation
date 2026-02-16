from flask import Flask, render_template

# Step 1: create the app
app = Flask(__name__)

# Step 2: route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Step 3: run the app
if __name__ == "__main__":
    app.run(debug=True)
