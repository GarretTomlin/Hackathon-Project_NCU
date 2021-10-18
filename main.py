from WebApp import create_app
from flask import Flask, app, redirect, url_for, render_template, request, Blueprint




app = create_app()




if __name__ == "__main__":
    app.run(debug=True)