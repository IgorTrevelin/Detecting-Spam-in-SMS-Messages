import os
import sqlite3
import datetime
import time
import pandas as pd


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


def get_predictions(con, per_page=25, page_num=1):
    cursor = con.cursor()

    sql = f"""
        SELECT * FROM sms_predictions
        ORDER BY pred_time DESC
        LIMIT ?
        OFFSET ?
    """

    cursor.execute(sql, (per_page, per_page * (page_num - 1)))

    df_preds = pd.DataFrame(
        data=cursor.fetchall(),
        columns=["SMS", "SPAM_PROB", "NOT_SPAM_PROB", "TIMESTAMP"],
    ).sort_values("TIMESTAMP", ascending=False).reset_index(drop=True)

    df_preds["TIMESTAMP"] = df_preds["TIMESTAMP"].apply(
        lambda x: datetime.datetime.fromtimestamp(x)
    )
    df_preds.rename(columns={"TIMESTAMP": "DATETIME"}, inplace=True)

    return df_preds
