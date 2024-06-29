
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as sl

try:
    df = pd.read_csv("weather analysis.csv")
    print(df)
    print(df.isna().sum())
    print(df.duplicated().sum())

    sl.sidebar.header('Main sidebar')
    sl.sidebar.write(df.columns)
    # num = sl.sidebar.selectbox("select average of weather", list(df.keys()))

    sl.title("Weather Analysis")
    sl.subheader('Original Dataset')
    sl.write(df.head())
    sl.write(df.shape)

    sl.subheader("Null values are:")
    sl.write(df.isna().sum())

    sl.subheader("Duplicated values are:")
    sl.write(df.duplicated().sum())

    num = sl.sidebar.selectbox("Choose one", df.columns, index=3)

    sl.write("Bar Chart")
    sl.bar_chart(df[num].head(30), color='#90EE90')

    sl.write("Line Chart")
    sl.line_chart(df[num].head(30))

    sl.write("Scatter Chart")
    sl.scatter_chart(df[num].head(30))

    sl.write("Pie Chart")
    plt.figure(figsize=[10, 10])
    plt.pie(df[num].head(30).value_counts().values, labels=df[num].head(30).value_counts().index, colors=['red', 'blue'], autopct='%1.2f%%')
    sl.pyplot(plt)

    sl.subheader("Bar Chart")
    plt.figure()
    plt.bar(df[num].head(30).value_counts().index, df[num].head(30).value_counts().values)
    sl.pyplot(plt)

except FileNotFoundError:
    sl.error("File not found. Please check the file path and name.")
except pd.errors.EmptyDataError:
    sl.error("The file is empty. Please check the file contents.")
except pd.errors.ParserError:
    sl.error("Error parsing the file. Please check the file format.")
except Exception as e:
    sl.error(f"An error occurred: {e}")



