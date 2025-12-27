from flask import Flask
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

#Calling API KEY cREATING eNV
load_dotenv()

#Config Gemini

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")

#reading Data pandas to read csv or DataFRamework
df=pd.read_csv("qa_data (1).csv")

#Convert Csv into Text content
context_text = "" 
for _, row in df.iterrows():
    context_text +=f"Q: {row['question']}\nA: {row['answer']}\n\n"

def ask_gemini(query):
    prompt =f"""
You are a Q&A assistant.property

Answer ONLY using the content below.
If the answer is not present,say:No relevant Q&A found.

Context:
{context_text}

Question: {query}
"""
    response=model.generate_content(prompt)
    return response.text.strip()
print("Chat Bot running")
print("ENTER EXIT TO TERMINATE")

while True:
    user_input=input("You: ")
    if user_input.lower() =="exit":
        print("Goodbye")
        break
    answer=ask_gemini(user_input)
    print(f"Bot: {answer}\n")

    from flask import Flask,render_template,request
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv
import os

#Calling API KEy Creating Env
load_dotenv()

app=Flask(__name__)

#Cofigure Gemini #env creat Model version
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-2.5-flash")

#reading Data pandas to read csv or DataFramework
df=pd.read_csv("qa_data (1).csv")

#convert Csv info into Text Content
context_text= ""
for _, row in df.iterrows():
    context_text +=f"Q: {row['question']}\nA: {row['answer']}\n\n"

def ask_gemini(query):
    prompt = f"""
You are a Q&A assistant.

Answer ONLY using the context below.
If the answer is not present, say: No relevant Q&A found.

Context:
{context_text}

Question: {query}
"""
    response=model.generate_content(prompt)
    return response.text.strip()

##Route Function
@app.route("/",methods=["GET","POST"])
def home():
    answer = ""
    if request.method=="POST":
        query=request.form["query"]
        answer=ask_gemini(query)
    return render_template("index.html",answer=answer)
#run Flask App
if __name__=="__main__":
    app.run()
