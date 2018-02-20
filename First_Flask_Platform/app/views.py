from flask import render_template
from app import app
import SystemInfo.main

@app.route('/')
def index():
    sysInfo = SystemInfo.main.main()
    returnDict = {}
    returnDict['title'] = 'Assignment 2: Flask & Systeminfo'
    returnDict['heading'] = 'COMP30670'
    returnDict['subHeading'] = 'Assignment 2: Flask & Systeminfo'
    returnDict['body'] = sysInfo
    return render_template("/index.html", **returnDict)