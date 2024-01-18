# from dotenv import load_dotenv
# load_dotenv()


# import streamlit as st
# import os
# import sqlite3

# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# def get_gemini_response(question, prompt):
#     model = genai.GenerativeModel('gemini-pro')
#     response = model.generate_content([prompt,question])
#     return response.text

# def read_sql_query(sql, db):
#     conn = sqlite3.connect(db)
#     cur  = conn.cursor()
#     cur.execute(sql)
#     rows = cur.fetchall()
#     conn.commit()
#     conn.close()

#     for row in rows:
#         print(row)

#     return rows
# prompt=[
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     also the sql code should not have in beginning or end and sql word in output

#     """


# ]

# ## Streamlit App

# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("Gemini App To Retrieve SQL Data")

# question=st.text_input("Input: ",key="input")

# submit=st.button("Ask the question")

# # if submit is clicked
# if submit:
#     response=get_gemini_response(question,prompt)
#     print(response)
#     response=read_sql_query(response,"student.db")
#     st.subheader("The REsponse is")
#     for row in response:
#         print(row)
#         st.header(row)


from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt, question])
    return response.text

def execute_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# if submit is clicked
if submit:
    # Assuming prompt is a single string, not a list
    prompt = """
        You are an expert in converting English questions to SQL query!
        The SQL database has the name STUDENT and has the following columns - NAME, CLASS, SECTION 
        \n\nFor example,\nExample 1 - How many entries of records are present?, 
        the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
        \nExample 2 - Tell me all the students studying in Data Science class?, 
        the SQL command will be something like this SELECT * FROM STUDENT 
        where CLASS="Data Science"; 
        also the sql code should not have in beginning or end and sql word in output
    """

    response = get_gemini_response(question, prompt)
    st.write("Generated SQL Query:", response)

    try:
        result = execute_sql_query(response, "student.db")
        st.subheader("The Response is")
        for row in result:
            st.write(row)
    except Exception as e:
        st.error(f"Error executing SQL query: {str(e)}")
