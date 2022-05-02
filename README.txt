Para la instalación de este API es necesario que se cuente con un entorno que tenga previamente
instalado Python 3. Además de lo anterior es imprescindible que se cuente con el framework FastAPI
que se descarga de la siguiente manera desde la terminal:

pip install fastapi
pip install "uvicorn[standard]"

Además de lo anterior, se deberá de ejecutar desde la terminal el comando:
pip install -r requirements.txt


Una vez instalados los requerimientos, solo hace falta correr el API a través del comando:
uvicorn main:app --reload

Por último para darle uso, únicamente hace falta enviar las solicitudes correspondientes a las
siguientes URL's con sus determinados formatos:

http://127.0.0.1:8000/predict

curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "adult_mortality": 40,
  "infant_deaths": 40,
  "alcohol": 40,
  "percentage_expenditure": 0,
  "hepatitis_B": 40,
  "measles": 40,
  "bmi": 40,
  "under_five_deaths": 40,
  "polio": 40,
  "total_expenditure": 40,
  "diphtheria": 40,
  "hiv_aids": 40,
  "gdp": 40,
  "population": 40,
  "thinness_10_19_years": 40,
  "thinness_5_9_years": 40,
  "income_composition_of_resources": 40,
  "schooling": 40
}'




http://127.0.0.1:8000/r2

curl -X 'POST' \
  'http://127.0.0.1:8000/r2' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "dataModel": {
    "adult_mortality": 0,
    "infant_deaths": 0,
    "alcohol": 0,
    "percentage_expenditure": 0,
    "hepatitis_B": 0,
    "measles": 0,
    "bmi": 0,
    "under_five_deaths": 0,
    "polio": 0,
    "total_expenditure": 0,
    "diphtheria": 0,
    "hiv_aids": 0,
    "gdp": 0,
    "population": 0,
    "thinness_10_19_years": 0,
    "thinness_5_9_years": 0,
    "income_composition_of_resources": 0,
    "schooling": 0
  },
  "dataModel2": {
    "adult_mortality_e": 1,
    "infant_deaths_e": 1,
    "alcohol_e": 1,
    "percentage_expenditure_e": 1,
    "hepatitis_B_e": 1,
    "measles_e": 1,
    "bmi_e": 1,
    "under_five_deaths_e": 1,
    "polio_e": 1,
    "total_expenditure_e": 1,
    "diphtheria_e": 1,
    "hiv_aids_e": 1,
    "gdp_e": 1,
    "population_e": 1,
    "thinness_10_19_years_e": 1,
    "thinness_5_9_years_e": 1,
    "income_composition_of_resources_e": 1,
    "schooling_e": 1
  }
}'

