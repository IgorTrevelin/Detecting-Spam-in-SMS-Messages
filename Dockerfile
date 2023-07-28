FROM python:3.9.17

# set working directory
WORKDIR /app

# copying necessary resources
COPY /app .
COPY /sms.py .

# copy the serialized classifier
COPY /sms_spam_clf.pkl .

# # install dependencies with pip
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# expose flask default port
EXPOSE 8501

# run streamlit app
CMD [ "streamlit", "run", "Home.py" ]