import os
import pandas as pd
from sqlalchemy import create_engine

def get_engine():
    engine = create_engine("postgresql+psycopg2://postgres:Panamalara29x.@localhost/interestellardb")
    return engine

def load_data(engine):
    for index, file in enumerate(os.listdir(r"C:\Users\gcuci\Desktop\Interestellar Project\source\data")):
        df = pd.read_csv(r"C:\Users\gcuci\Desktop\Interestellar Project\source\data\\" + file)
        df.to_sql(file, con = engine)

def main():
    engine = get_engine()
    load_data(engine = engine)

if __name__ == "__main__":
    main()