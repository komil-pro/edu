from flask import Flask

in_memory_datastore = {
   "COBOL" : {"name": "COBOL", "publication_year": 1960, "contribution": "record data"},
   "ALGOL" : {"name": "ALGOL", "publication_year": 1958, "contribution": "scoping and nested functions"},
   "APL" : {"name": "APL", "publication_year": 1962, "contribution": "array processing"},
}

app = Flask(__name__)

@app.get('/test')
def list_programming_languages():
   return {"programming_languages":list(in_memory_datastore.values())}