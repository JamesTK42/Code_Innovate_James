from distutils import ccompiler


countries = {
    "UK": {
        "Country": "United Kingdom",
        "Capital": "London"},
    "FR": {
        "Country": "France",
        "Capital": "Paris"},
    "ES": {
        "Country": "Spain",
        "Capital": "Madrid"},
    "IT": {
        "Country": "Italy",
        "Capital": "Rome"},
}


countries.setdefault("AU", {"Country": "Australia", "Capital": "Canberra"})

countries.setdefault(
    "USA", {"Country": "United States of America", "Capital": "Wasington DC"})

# countries.pop("Capital")

del countries["Capital"]


for x in countries.items():
    print(x)
