import os
import pandas as pd

# web framework for build the api
from flask import Flask, request, abort, jsonify

# load custom transformer from include/sms.py
import joblib

import sqlite3

import warnings

import time

warnings.filterwarnings("ignore")

from sms import SMSSentenceTransformer

model = joblib.load("sms_spam_clf.pkl")

app = Flask(__name__)


def db_con():
    storage_dir = os.path.join(os.getcwd(), "storage")
    try:
        os.mkdir(storage_dir)
    except:
        pass

    return sqlite3.connect(os.path.join(storage_dir, "predictions.db"))


def init_sms_prediction_table(con):
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS sms_predictions (sms_text, spam_prob, non_spam_prob, pred_time)
        """
    )


def insert_sms_prediction(sms_text, spam_prob, non_spam_prob, con):
    cursor = con.cursor()

    sql = f"""
            INSERT INTO sms_predictions VALUES
                (?, ?, ?, ?)
        """

    cursor.execute(sql, (sms_text, spam_prob, non_spam_prob, time.time()))

    con.commit()


# api main route definition
@app.route("/sms/detect-spam", methods=["POST"])
def detect_spam():
    # if model not loaded, return status 500
    if not model:
        abort(500)

    # if sms parameter not sent, return status 400
    if not "sms" in request.json:
        abort(400)

    sms = request.json["sms"]

    # get spam probability from machine learning model
    pred = model.predict_proba(pd.DataFrame(data={"v2": [sms]}))

    p_spam = round(float(pred[0][1]), 3)
    p_not_spam = round(1.0 - p_spam, 3)

    insert_sms_prediction(sms, p_spam, p_not_spam, db_con())

    # return probabilities result in json format
    return jsonify({"p-spam": p_spam, "p-not-spam": p_not_spam})


@app.before_first_request
def init():
    init_sms_prediction_table(db_con())
