from pydantic import BaseModel

class DataModel2(BaseModel):

    adult_mortality_e: float
    infant_deaths_e: float
    alcohol_e: float
    percentage_expenditure_e: float
    hepatitis_B_e: float
    measles_e: float
    bmi_e: float
    under_five_deaths_e: float
    polio_e: float
    total_expenditure_e: float
    diphtheria_e: float
    hiv_aids_e: float
    gdp_e: float
    population_e: float
    thinness_10_19_years_e: float
    thinness_5_9_years_e: float
    income_composition_of_resources_e: float
    schooling_e: float

    #Esta función retorna los nombres de las columnas correspondientes con el modelo esxportado en joblib.
    def columns(self):
        return ["Adult Mortality", "infant deaths", "Alcohol","percentage expenditure","Hepatitis B", "measles", "BMI",
                "under five deaths", "Polio", "Total expenditure", "Diphtheria", "hiv aids", "gdp", "population",
                "thinness 10-19 years", "thinness 5-9 years", "Income composition of resources", "Schooling"]
