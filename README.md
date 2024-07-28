# Interactly-task-Dhruvin
MongoDB Setup in Local in Windows
1. Install MongoDB Server, Shell and Compass
2. extract shell file into program files-mongodb
3. go to extracted file-bin and copy mongosh file (which is .exe file)
4. paste this file into the server-7.0-bin folder
5. copy the path "C:\...\MongoDB\Server\7.0\bin"
6. paste this path into system env variables-path-edit-new-paste_path
7. type mongosh in terminal and it should work

I first pre-processed the data:
1. saved into csv format
2. Experience column, I deleted the 'years' so the column can be decimal_128 instead of string

Then Data was inported then into mongodb collections

# How to Run:
## Flask App for Job Profile Matching

This is a Flask application that connects to a MongoDB database, retrieves candidate profiles, and matches them against a user-provided job description using TF-IDF and cosine similarity.

## Prerequisites

- Python 3.7 or later
- MongoDB server running locally or remotely

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/ddhruvin/Interactly-task-Dhruvin-.git
cd Interactly-task-Dhruvin-

## Create a Virtual Environment
It is recommended to use a virtual environment to manage dependencies:


python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. Install Dependencies
Install the required packages listed in requirements.txt:


pip install -r requirements.txt
4. Set Up MongoDB
Ensure you have a MongoDB server running and that the database and collection used in the app are properly set up. The app connects to the MongoDB instance using the default connection string:


client = MongoClient("mongodb://localhost:27017/")
Update the connection string in app.py if you are using a different MongoDB server.

## Update Database and Collection Names
Ensure the db and collection names in app.py match your MongoDB setup:


db = client["Indirectly_video"]
collection = db["Candidate_data"]
6. Run the Application
Start the Flask application:


python app.py
The app will be accessible at http://127.0.0.1:5000/.

## Usage
Open your web browser and navigate to http://127.0.0.1:5000/.
Enter a job description prompt in the text area and click "Generate Response".
The app will display the top 10 profiles from the database that match the provided job description.

## Troubleshooting
TemplateNotFound Error: Ensure that the index.html file is located in the templates directory.
Database Connection Issues: Verify that MongoDB is running and accessible at the specified connection string.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
Flask
pymongo
scikit-learn
MongoDB




