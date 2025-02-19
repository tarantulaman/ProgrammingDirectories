from sqlalchemy import *
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
# We import this library to work with .json objects
import json

# We import the locations of the project configuration files
import config
data_json = config.DATA_JSON


# We open the .json file that will contain the object where the path to create the database is located
with open(data_json, 'r') as f:
    data = json.load(f)

# Dumps the json object into an element
json_str = json.dumps(data)
# Load the json to a string
resp = json.loads(json_str)
# Store the element to be extracted from the .json object in a variable
route_create_database = resp['route_create_database']




# We create the path where the database is going to be created, from here the other CRUD files will inherit 
# the path
#engine = create_engine('sqlite:///dictionary-english.db', echo=True)
engine = create_engine('sqlite:///{}'.format(route_create_database), echo=True)
Base = declarative_base()




'''
# We edit the .json file containing the object, where the path field where the database will be opened is found
with open('src/data.json', 'r+') as f:
    data = json.load(f)
    # Here we edit the value of the "route_open_database" field and replace it with "route_open_database"
    data["route_open_database"] = route_create_database
    # Should reset file position to the beginning
    f.seek(0)        
    json.dump(data, f, indent=4)
    # Remove remaining part
    f.truncate() 
'''





# We create the classes that will create the database with its tables tables

########################################################################
class ProgrammingLanguage(Base):
    """"""
    __tablename__ = "programming_language"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
   

    #----------------------------------------------------------------------
    def __init__(self, name):
        """"""
        self.name = name


########################################################################
class TypeCreation(Base):
    """"""
    __tablename__ = "type_creation"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    id_programming_language = Column(Integer, ForeignKey('programming_language.id'))

    #----------------------------------------------------------------------
    def __init__(self, name, id_programming_language):
        """"""
        self.name = name
        self.id_programming_language = id_programming_language


########################################################################
class TypeApplication(Base):
    """"""
    __tablename__ = "type_application"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    id_type_creation =  Column(Integer, ForeignKey('type_creation.id'))

    #----------------------------------------------------------------------
    def __init__(self, name, id_type_creation):
        """"""
        self.name = name
        self.id_type_creation = id_type_creation


########################################################################
class ProjectTutorial(Base):
    """"""
    __tablename__ = "project_tutorial"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    programming_language_version = Column(String)
    framework = Column(String)
    graphical_interface = Column(String)
    data_base = Column(String)
    data_base_version = Column(String)
    orm = Column(String)
    virtual_environment = Column(String)
    architecture = Column(String)
    cloud_server = Column(String)
    number_project_tutorial = Column(Integer)
    id_type_application =  Column(Integer, ForeignKey('type_application.id'))

    #----------------------------------------------------------------------
    def __init__(self, 
    name,
    programming_language_version, 
    framework, 
    graphical_interface, 
    data_base,
    data_base_version,
    orm, 
    virtual_environment,
    architecture,
    cloud_server,
    number_project_tutorial, 
    id_type_application):
        """"""
        self.name = name
        self.programming_language_version = programming_language_version
        self.framework = framework
        self.graphical_interface = graphical_interface
        self.data_base = data_base
        self.data_base_version = data_base_version
        self.orm = orm
        self.virtual_environment = virtual_environment
        self.architecture = architecture
        self.cloud_server = cloud_server
        self.number_project_tutorial = number_project_tutorial
        self.id_type_application = id_type_application
    

########################################################################
class Part(Base):
    """"""
    __tablename__ = "part"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    repository = Column(String)
    youtube_video = Column(String)
    number_part = Column(Integer)
    id_project_tutorial =  Column(Integer, ForeignKey('project_tutorial.id'))

    #----------------------------------------------------------------------
    def __init__(self, name, repository, youtube_video, number_part, id_project_tutorial):
        """"""
        self.name = name
        self.repository = repository
        self.youtube_video = youtube_video
        self.number_part = number_part
        self.id_project_tutorial = id_project_tutorial


# We create the tables
Base.metadata.create_all(engine)