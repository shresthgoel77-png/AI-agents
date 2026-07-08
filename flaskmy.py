from flask import Flask, request  # FIX 1: Imported request

app = Flask(__name__)

html_form = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>calculator</title>
</head>
<body>
    <!-- FIX 2: Added method and action to the form -->
    <form method="POST" action="/">
        <input type="number" name="num1">
        <select name="operation">
            <!-- FIX 3: Changed "Add" to lowercase "add" to match Python code -->
            <option value="add">+</option>
            <option value="sub"> - </option>
            <option value="mul"> * </option>
            <option value="div"> / </option>
        </select>
        <!-- FIX 4: Removed the accidental trailing space from "num2 " -->
        <input type="number" name="num2">
        <button type="submit">submit</button>
    </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculate():  # FIX 5: Removed 'num' parameter to clear the TypeError
    if request.method == "GET":
        return html_form
    elif request.method == "POST":
        n1 = float(request.form.get("num1"))
        n2 = float(request.form.get("num2"))
        op = request.form.get("operation")
        if op == "add":
            result = n1 + n2
            return f"<h3>Result: {n1} + {n2} = {result}</h3><br><a href='/'>Go Back</a>"
        
        elif op == "sub":
            result = n1 - n2
            return f"<h3>Result: {n1} - {n2} = {result}</h3><br><a href='/'>Go Back</a>"
            
        elif op == "mul":
            result = n1 * n2
            return f"<h3>Result: {n1} * {n2} = {result}</h3><br><a href='/'>Go Back</a>"
            
        elif op == "div":
            if n2 == 0:
                return "<h3>Error: Cannot divide by zero!</h3><br><a href='/'>Go Back</a>"
            result = n1 / n2
            return f"<h3>Result: {n1} / {n2} = {result}</h3><br><a href='/'>Go Back</a>"
        else:
            return "Invalid Operation"

if __name__ == "__main__":
    app.run(debug=True)
