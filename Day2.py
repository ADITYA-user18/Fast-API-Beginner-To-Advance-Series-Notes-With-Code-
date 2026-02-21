# This is the Simple Project to understand the Different HTTP Methods

# Import FastAPI framework
# Path -> used for path parameters (like /patient/{id})
# Query -> used for query parameters (like /sort?sort_by=weight)
from fastapi import FastAPI, Path, Query

# Used to read JSON file
import json


# Create FastAPI app instance
app = FastAPI()


# Function to load patient data from JSON file
def load_data():
    # Open patients.json file in read mode
    with open('patients.json', 'r') as f:
        # Convert JSON data into Python dictionary
        data = json.load(f)
    return data


# Root endpoint (Home Page)
# URL: http://127.0.0.1:8000/
@app.get('/')
async def hello():
    # Returns a simple welcome message
    # (There is a small syntax issue here intentionally kept as you asked not to change code)
    return {'mess'
    'age': 'This is the Patients Management System'}


# About endpoint
# URL: http://127.0.0.1:8000/about
@app.get('/about')
async def About():
    # Returns about page message
    return {'message': 'This is the Patients About Page'}


# View all patients
# URL: http://127.0.0.1:8000/view
@app.get('/view')
async def view():
    # Load data from JSON
    data = load_data()

    # Return all patient records
    return data


# Fetch single patient using Path parameter
# Example: http://127.0.0.1:8000/patient/P001
@app.get('/patient/{patient_id}')
async def PatientFetcher(
    # Path(...) means this parameter is REQUIRED
    # description -> shown in Swagger UI
    # example -> example value shown in Swagger
    patient_id: str = Path(
        ..., 
        description="The ID of the patient to fetch", 
        example="P001"
    )
):
    # Load all patient data
    data = load_data()

    # Check if patient_id exists in JSON
    if patient_id in data:
        # Return specific patient details
        return data[patient_id]
    else:
        # Return message if patient not found
        return f"No Patients Found"
    


# Sort endpoint using Query parameter
# Example: http://127.0.0.1:8000/sort?sort_by=weight
@app.get('/sort')
async def sort(
    # Query(...) means value comes after ?
    # ... -> required query parameter
    # description & example shown in Swagger UI
    sort_by: str = Query(
        ...,
        description="Choose sorting field",
        example="weight"
    )
):
    # Allowed fields for sorting
    sorted_values = ['weight', 'height', 'bmi']

    # Check if user provided valid sorting field
    if sort_by in sorted_values:

        # Load patient data
        data = load_data()

        # sorted() function sorts dictionary items
        # data.items() -> returns (key, value) pairs
        # x[1] -> patient details dictionary
        # x[1][sort_by] -> access specific field like weight
        sorted_data = sorted(
            data.items(), 
            key=lambda x: x[1][sort_by]
        )

        # Return sorted data
        return {sort_by: sorted_data}
    
    else:
        # If invalid sorting field is given
        return {
            "error": f"Invalid Sort By Value. Please choose from {sorted_values}"
        }
    


