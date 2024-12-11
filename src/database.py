import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# link = create_engine('mysql+mysqldb://root:tupassword@localhost:3306/Diamond_Analyzer?unix_socket=/var/run/mysqld/mysqld.sock')
# Sesion = sessionmaker(link)
# sesion = Sesion()

sqlite_file_name = '../database.sqlite'
base_dir = os.path.dirname(os.path.realpath(__file__))

link = create_engine(f'sqlite:///{os.path.join(base_dir, sqlite_file_name)}')
Sesion = sessionmaker(link)
sesion = Sesion()