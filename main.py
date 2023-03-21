from application import salary
from application.db import people
from datetime import datetime as date
from tqdm import tqdm

if __name__=="__main__":
    salary.calculate_salary()
    people.get_employees()

    print(date.today())

    for i in tqdm(range(1000000)):
        a = i^2


