from app import app

@app.route("/product/add")
def productAdd():
    return "Product add function"