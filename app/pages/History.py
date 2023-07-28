import pandas as pd
import streamlit as st
from include.db import *


def history():
    df_hist = get_predictions(con=db_con())

    st.title("Last 25 Predictions")
    st.markdown(
        """
            [![LinkedIn](https://img.shields.io/badge/LinkedIn-igor--trevelin-blue)](https://www.linkedin.com/in/igor-trevelin/)
            [![GitHub](https://img.shields.io/badge/GitHub-IgorTrevelin-purple)](https://github.com/IgorTrevelin)
        """
    )
    st.table(data=df_hist)


if __name__ == "__main__":
    history()
