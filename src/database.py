from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

link = create_engine('mysql+mysqldb://root:tupassword@localhost:3306/Diamond_Analyzer')
Sesion = sessionmaker(link)
sesion = Sesion()
