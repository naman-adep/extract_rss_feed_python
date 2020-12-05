#Import the modules
import streamlit as st
import pandas as pd 
import feedparser

#Accepting the text input through Web GUI
st.title("Extract RSS Feed")
rss_url = st.text_input("Enter URL Here")

#Parse the feed using feedparser and display it
if st.button("Pull RSS Feed"):

	feed = feedparser.parse(rss_url)

	news = [newsitem['title'] for newsitem in feed['items']]

	news_df = pd.DataFrame(zip(news),columns=['News'])
	st.dataframe(news_df)



