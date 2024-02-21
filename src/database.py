from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

link = create_engine('mysql+mysqldb://root:tupassword@localhost:3306/Diamond_Analyzer?unix_socket=/var/run/mysqld/mysqld.sock')
Sesion = sessionmaker(link)
sesion = Sesion()


