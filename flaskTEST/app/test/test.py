from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app

from ..module import dbModule

test = Blueprint('test',__name__, url_prefix='/test')

@test.route('/',methods=['GET'])
def index():
    return render_template('/test/test.html',
                           result = None,
                           resultData = None,
                           resultUpdate = None)

@test.route('/insert',methods=['GET'])
def insert():
    db_class = dbModule.Database()
    sql = """INSERT INTO testDB.testTable(test) VALUES('%s')""" % ('testData')
    db_class.execute(sql)
    db_class.commit()

    return render_template('/test/test.html',
                           result='insert is done!',
                           resultData=None,
                           resultUpdate=None)
@test.route('/select',methods=['GET'])
def select():
    db_class = dbModule.Database()
    sql = """SELECT * FROM testDB.testTable"""
    row = db_class.executeAll(sql)
    print(row)
    return render_template('/test/test.html',
                           result=None,
                           resultData=row[0],
                           resultUpdate=None)

@test.route('/update',methods=['GET'])
def update():
    db_class = dbModule.Database()
    sql = """UPDATE testDB.testTable SET test='%s' WHERE test='testData'""" % ('Update_Data')
    db_class.execute(sql)
    db_class.commit()
    sql = """SELECT * FROM testDB.testTable"""
    row = db_class.executeAll(sql)
    return render_template('/test/test.html',
                           result=None,
                           resultData=None,
                           resultUpdate=row[0])
