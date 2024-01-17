 
# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask app
app = Flask(__name__)

# Define the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_app', methods=['GET', 'POST'])
def create_app():
    if request.method == 'POST':
        # Get the form data
        app_name = request.form['app_name']
        app_description = request.form['app_description']

        # Create a new web application
        new_app = App(app_name, app_description)
        db.session.add(new_app)
        db.session.commit()

        # Redirect to the view apps page
        return redirect(url_for('view_apps'))
    else:
        return render_template('create_app.html')

@app.route('/view_apps')
def view_apps():
    # Get all the web applications from the database
    apps = App.query.all()

    # Render the view apps page
    return render_template('view_apps.html', apps=apps)

@app.route('/delete_app/<int:app_id>')
def delete_app(app_id):
    # Get the app by id
    app = App.query.get_or_404(app_id)

    # Delete the app from the database
    db.session.delete(app)
    db.session.commit()

    # Redirect to the view apps page
    return redirect(url_for('view_apps'))

@app.route('/edit_app/<int:app_id>', methods=['GET', 'POST'])
def edit_app(app_id):
    # Get the app by id
    app = App.query.get_or_404(app_id)

    if request.method == 'POST':
        # Get the form data
        app_name = request.form['app_name']
        app_description = request.form['app_description']

        # Update the app
        app.app_name = app_name
        app.app_description = app_description
        db.session.commit()

        # Redirect to the view apps page
        return redirect(url_for('view_apps'))
    else:
        # Render the edit app page
        return render_template('edit_app.html', app=app)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
