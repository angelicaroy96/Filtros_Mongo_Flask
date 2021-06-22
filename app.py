#Importing required libraries
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
import flask

#declare an app variable
app=flask.Flask(__name__)
#declare tow variavle titles and headings
title="CRUD Example"
heading="with Flask and MongoDB"

#declare the connection string for MongoDB
#select the database
#after "2017/" write the name of your database
mongodb_client=PyMongo(app, uri="mongodb://localhost:27017/ejemplo")
db=mongodb_client.db
#select the collection name
#students=db.estudiantes

#students that their last name start with "s"
@app.route("/list_lastName")
def list_lns():
    estudiantes=db.estudiantes.find({
        "apellido":{
            "$regex":"^S"
        }
    })
    a1="activate"
    return render_template("lista_apellido.html",students=list(estudiantes),t=title,h=heading)

#students that their age is over  22 years old
@app.route("/list_overAge")
def list_age():
    estudiantes=db.estudiantes.find({   
        "edad":{"$gte":22}
    })
    a1="activate"
    return render_template("lista_edad.html",students=list(estudiantes),t=title,h=heading)

#data sort by last name
@app.route("/list_sortLast")
def list_lastname():
    estudian=db.estudiantes.aggregate(
        [   {
                "$project":{"_id":0,"nombre":1,"apellido":1,"edad":1}},
                {"$sort":{"apellido":1}
            }
        ]
    )
    a1="activate"
    return render_template("lista_orden_apellido.html",students=list(estudian),t=title,h=heading)
   

if __name__=="__main__":
    app.run()