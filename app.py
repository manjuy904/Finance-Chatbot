from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import os
from tradingbot.retrieval_generation import generation
from tradingbot.data_ingestion import ingestdata

# Initialize a new Flask web application
app = Flask(__name__)

# Loading Environment Variables
load_dotenv()

# Data Ingestion and Chain Generation
vstore=ingestdata("done") #Calls the ingestdata function with the argument "done". This likely sets up the vector store with preloaded data (since the status is not None)
chain=generation(vstore) #Calls the generation function with the vector store vstore as an argument. This likely sets up a chain of operations that can be used for generating responses.


# Route Definitions
 
# Home Route
# Defines a route for the home page ("/").
# When a user navigates to the home page, this function renders and returns the chat.html template
@app.route("/")
def index():
    return render_template('chat.html')

# Chat Route
# Defines a route for handling chat messages ("/get").
# Accepts both GET and POST requests.
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"] # Retrieves the message sent by the user from the data
    input = msg
    result = chain.invoke(input) #  Invokes the chain (set up earlier with the vector store) to process the input and generate a response
    print("Response : ", result)
    return str(result)


# Running the Application
if __name__=='__main__':
    app.run(debug=True) # Starts the Flask web server in debug mode, which provides more detailed error messages and automatically reloads the server when code changes
    