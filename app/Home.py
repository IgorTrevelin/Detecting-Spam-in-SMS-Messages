import os
import pandas as pd
import joblib
import sqlite3
import warnings
import streamlit as st
from sms import SMSSentenceTransformer
from include.db import *

warnings.filterwarnings("ignore")

model = joblib.load("sms_spam_clf.pkl")


def homepage():
    st.set_page_config(page_title="SMS Spam Detection - Igor Trevelin")
    st.title("SMS Spam Detection")
    st.markdown(
        """
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-igor--trevelin-blue)](https://www.linkedin.com/in/igor-trevelin/)
            [![GitHub](https://img.shields.io/badge/GitHub-IgorTrevelin-purple)](https://github.com/IgorTrevelin)
        """
    )
    st.markdown("This is a demo application of the SMS spam detection project.")
    st.markdown(
        "The project source codes are available on Github in the following [repository](https://github.com/IgorTrevelin/Detecting-Spam-in-SMS-Messages)."
    )
    st.markdown(
        "Insert a SMS message text in the text area below and click the submit button."
    )

    sms = st.text_area(label="SMS Message Text:", value="", height=200, max_chars=2000)

    submit_btn = st.button(label="Check Spam")

    if submit_btn and len(sms) == 0:
        st.error("Please enter a SMS message.")

    elif submit_btn:
        pred = model.predict_proba(pd.DataFrame(data={"v2": [sms]}))

        p_spam = round(float(pred[0][1]), 3)
        p_not_spam = round(1.0 - p_spam, 3)

        insert_sms_prediction(sms, p_spam, p_not_spam, db_con())

        if p_spam > p_not_spam:
            st.error(
                "Wow! This is a spam. The spam probability is {:.2f}%.".format(
                    p_spam * 100
                )
            )
        elif p_spam < p_not_spam:
            st.success(
                "Not a spam! The spam probability is {:.2f}%.".format(p_spam * 100)
            )


if __name__ == "__main__":
    init_sms_prediction_table(db_con())
    homepage()
