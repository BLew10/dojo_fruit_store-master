from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    cart = request.form
    strawberries = int(request.form['strawberry'])
    apples = int(request.form['apple'])
    raspberries = int(request.form['raspberry'])
    cart_num = int(request.form['strawberry']) + int(request.form['apple']) + int(request.form['raspberry']) 
    return render_template("checkout.html", cart = cart, cart_num = cart_num )

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    
