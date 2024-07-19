from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clothing')
def clothing():
    title = "Clothing"
    products = [
        {"name": "Product 1", "description": "Product 1 Description", "image_url": "https://via.placeholder.com/150"},
        {"name": "Product 2", "description": "Product 2 Description", "image_url": "https://via.placeholder.com/150"},
        {"name": "Product 3", "description": "Product 3 Description", "image_url": "https://via.placeholder.com/150"},
    ]
    return render_template('products.html', title=title, products=products)

@app.route('/jackets')
def jackets():
    title = "Jackets"
    products = [
        {"name": "Jacket 1", "description": "Jacket 1 Description", "image_url": "https://via.placeholder.com/150"},
        {"name": "Jacket 2", "description": "Jacket 2 Description", "image_url": "https://via.placeholder.com/150"},
        {"name": "Jacket 3", "description": "Jacket 3 Description", "image_url": "https://via.placeholder.com/150"},
    ]
    return render_template('products.html', title=title, products=products)

@app.route('/shoes')
def shoes():
    title = "Shoes"
    products = [
        {"name": "Shoe 1", "description": "Shoe 1 Description", "image_url": "https://via.placeholder.com/150"},
        {"name": "Shoe 2", "description": "Shoe 2 Description", "image_url": "https://via.placeholder.com/150"},
        {"name": "Shoe 3", "description": "Shoe 3 Description", "image_url": "https://via.placeholder.com/150"},
    ]
    return render_template('products.html', title=title, products=products)

if __name__ == '__main__':
    app.run(debug=True)
