# 💬 Detecting Spam in SMS Messages 💬

[![LinkedIn](https://img.shields.io/badge/LinkedIn-igor--trevelin-blue)](https://www.linkedin.com/in/igor-trevelin/)
[![GitHub](https://img.shields.io/badge/GitHub-IgorTrevelin-purple)](https://github.com/IgorTrevelin)

![image](https://storage.googleapis.com/kaggle-datasets-images/483/982/15b24a8964e8d4afadff79a1a5543450/dataset-cover.jpg)

SMS spam detection is a crucial and evolving field aimed at identifying and mitigating the influx of unsolicited and fraudulent text messages sent to mobile users. By employing sophisticated algorithms and machine learning techniques, SMS spam detection systems analyze the content and metadata of incoming messages to distinguish between legitimate and spam messages. These systems can recognize patterns, keywords, and sender behavior indicative of spam, enabling mobile service providers and users to filter out unwanted messages effectively. As SMS spam tactics become more sophisticated, continuous research and development in this area remain essential to staying one step ahead of spammers and ensuring a seamless and secure mobile messaging experience for users worldwide.

The goal of this project is to build a spam detection solution for SMS messages texts using machine learning techniques. Also, a demo application code is included.

### **Project Results and Resources**

[Data Analysis and Modeling](https://github.com/IgorTrevelin/Detecting-Spam-in-SMS-Messages/blob/main/Detecting_Spam_in_SMS_Messages.ipynb)
[Demo App](https://github.com/IgorTrevelin/Detecting-Spam-in-SMS-Messages/tree/main/app)

## Running the Demo App
  
The demo app was build with the app framework [Streamlit](https://streamlit.io/). To run it locally, first execute all the cells from the [Notebook](https://github.com/IgorTrevelin/Detecting-Spam-in-SMS-Messages/blob/main/Detecting_Spam_in_SMS_Messages.ipynb). A machine learning exported model file called sms_spam_clf.pkl will be created in the project root directory. After doing this, run the following commands in your terminal.

**With Docker:**
```
  docker compose up -d
```

**Without Docker:**
```
  cd app/
  pip install -r requirements.txt
  streamlit run Home.py
```

Them access `http://127.0.0.1:8501` in your browser. The app looks like this:

  
![Demo App Print](/demo-app.jpg)

Feel free to give your feedback and to contact me. Connect with me in my networks:

[![LinkedIn](https://img.shields.io/badge/LinkedIn-igor--trevelin-blue)](https://www.linkedin.com/in/igor-trevelin/)
[![GitHub](https://img.shields.io/badge/GitHub-IgorTrevelin-purple)](https://github.com/IgorTrevelin)
