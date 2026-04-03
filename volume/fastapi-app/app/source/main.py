# uvicorn main:app --port 8686 --host 192.168.1.108 --reload --root-path /
from   inspect import currentframe, getframeinfo;
from   typing  import Optional , List;
from   fastapi import Depends;
from   fastapi import FastAPI;
from   fastapi import File;
from   fastapi import UploadFile;
from   fastapi import Form;
from   fastapi import Request;
from   fastapi import HTTPException;
from   fastapi import status;
from   fastapi import Query;
from   fastapi import Path;
from   fastapi.staticfiles   import StaticFiles;
from   fastapi.responses     import HTMLResponse, FileResponse;
from   fastapi.security      import HTTPBasic, HTTPBasicCredentials;
from   fastapi.openapi.utils import get_openapi;
from   enum     import Enum;
from   pydantic import BaseModel , Field , create_model;
import time;
import datetime;
from   datetime import timedelta;
import os;
import os.path;
import re;
import array;
from   os import path;
from decimal import *;
import aiohttp;
import aiofiles;
import asyncio;
import json as JSON;
import sys;
import random;
import hashlib;
import csv;
import psycopg2;
import models.inputs            as     Inputs;
from   cfg.tags                 import Tags;
from   classes.amModel          import amModel;
from   classes.amTools          import amTool;
from   classes.amFormulas       import amFormulas;

security         = HTTPBasic();
amTool           = amTool();
cfg              = amTool.load( "./cfg/" , "config" );
amTool.cfg       = cfg;
myModel          = amModel( cfg );
myFormulas       = amFormulas( cfg );
myTags           = Tags();

fromDate_default = datetime.date.today() - timedelta( days = 1);
toDate_default   = datetime.date.today();
endpoint_tags    = myTags.list;

DBsourceFileName = "schema";
debug            = True;
activateAddDataEndPoint = False;

app = FastAPI( 
              title        = cfg["service"]["title"],
              description  = cfg["service"]["description"],
              version      = cfg["service"]["version"],
              openapi_tags = endpoint_tags , 
              redoc_url    = None , 
              # openapi_url  = "/cfg/openapi.json" , 
              docs_url     = "/" + cfg["service"]["docs_url"]
      );

app.mount(
           "/"+cfg["uploads"]["images"]["service_name"] , 
           StaticFiles( directory = cfg["uploads"]["images"]["path"] ), 
           name=cfg["uploads"]["images"]["service_name"] 
         );

def getCredentials( credentials ):
    return { "username" : credentials.username, "password" : credentials.password }

def validateDate( date_string ):
    try:
        datetime.datetime.strptime( date_string , '%Y-%m-%d %H:%M:%S' );
        return True;
    except ValueError:
        return False;

def parseStringIntoArrayWithIntegers( string ):
   myListArrayResponse = list();
   print( string );
   if( string == "" or string is None ):
       return [];

   if( string is None ):
       return None;

   if( string.find(",") > 0 ):
       myList = string.split( "," );
       for item in myList : 
           if( amTool.isInt( item ) ):
               myListArrayResponse.append( item );
           else:
               print( "This is not a number" );
       return myListArrayResponse;
   else:
       if( amTool.isInt( string ) ):
           return [ string ];
       else:
           print( "This is not a number" );
           return myListArrayResponse;

def parseModelsStringIntoArray( models ):
   myListArrayResponse = list();

   if( models.find(",") > 0 ):
       myList = models.split( "," );
       for item in myList : 
           myListArrayResponse.append( item );

       return myListArrayResponse;
   else:
       return [ models ];

def logRequest( request ):
    amTool.log( request.url );

def printJSON( myJSON ):
    print( myJSON.schema_json( indent = 2 ) );

def turnIneligiblePropertiesIntoZero( dataset , filter ):
    groupName = False;
    for item in filter:
        if item[ "column" ] == "test_case_number" or item[ "column" ] == "cultivation_type" : 
            groupName = str( item[ "value" ] );

    if groupName is False : 
        return;
    
    print( str( groupName ) );

    ivaylo_mapping = amTool.load( "./cfg/" , "ivaylo_mapping" );
    specificGroup  = ivaylo_mapping[ "ineligible_groups" ][ str( groupName ) ];
    print( ">>>>>>>>>>>>>>>> GET FOR [ " + str( groupName ) + " ] <<<<<<<<<<<<<<<<<<<" );
    print( ">>>>>>>>>>>>>>>>>>>>> DATASET <<<<<<<<<<<<<<<<<<<<" );
    print( amTool.json_dump( dataset ) );
    print( "Ineligible Group" );
    print( amTool.json_dump( specificGroup ) );
    print( "Ineligible Properties" );
    if "error" not in dataset : 
        for group in specificGroup:
            specificProperties = ivaylo_mapping[ "form_fields" ][ group ];
            print( specificProperties );
            for property in specificProperties : 
                mySanitizedProperty = property.replace( "cropTC_" , "" );
                mySanitizedProperty = mySanitizedProperty.replace( "crop_" , "" );
                if mySanitizedProperty in dataset[ 0 ]:
                    print( " >>> " + str( mySanitizedProperty ) + " setting to 0" );
                    dataset[ 0 ][ mySanitizedProperty ] = 0;

# OTHER

async def validateRequest( request , typeOfValidation ):
    response = {
     "isvalid" : False , 
     "error"   : ""
    };

    myMainsearchCriteria = "";

    for type in typeOfValidation : 
        if( type == "coords" ) : 
            if ( "longitude" in request.query_params and "latitude" in request.query_params ):
                myMainsearchCriteria = "coords";
        if( type == "locationid" ) :
            if ( "locationid" in request.query_params ) : 
                myMainsearchCriteria = "locationid";
        if( type == "parcelid" ) :
            if ( "parcelid" in request.query_params ) : 
                myMainsearchCriteria = "parcelid";

    if( myMainsearchCriteria == "" ):
        raise HTTPException( status_code = 400, detail = "Missing query parameters. At least one entity of parameters from ( "+" , ".join( typeOfValidation )+" ) must be provided." );

async def isValidApp( request: Request , credentials  : HTTPBasicCredentials = Depends( security ) ):
    appCredentials  = getCredentials( credentials );
    myOptions       = dict();
    myOptions[ "un" ] = appCredentials[ "username" ];
    myOptions[ "pw" ] = appCredentials[ "password" ];

    hasAppAccess = await amAccess.getAppAccess( myOptions );

    if( hasAppAccess is False ):
        raise HTTPException( status_code = 401 );
    else:
        await amAccess.logSession( hasAppAccess[ 0 ][ "user_id" ] , request );
        return True;

@app.middleware("http")
async def add_process_time_header( request: Request, call_next ):
    startTime = time.time();
    response  = await call_next( request );
    endTime   = time.time();
    totalTime = endTime - startTime;
    response.headers[ "X-Process-Time" ] = str( totalTime );
    amTool.log( "\"" + str( request.method ) + "\"" + " " + str( request.url ) + " (Code:" + str( response.status_code ) + ")" + " [Duration : " + str( round( totalTime ,3 ) ) + "]" );
    return response;

# Administration EndPoints

@app.get( "/administration/create_db_tables", 
          tags         = [ "Administration" ] , 
          summary      = "Create basic Database Tables",
          description  = "Create the initial tables required for inserting user Data. This is an action that only needs to be performed once at the initial installation" 
        ) 
async def createDBTables():
    # Reads the SourceFile JSON and creates one Table for each entity defined in there.
    mySchema = amTool.cfg[ "database" ][ "schema" ];

    try:
        myInputsJSON = amTool.load( "" , DBsourceFileName , "json" );
        myWholeQuery = [];
        mySchema     = amTool.cfg[ "database" ][ "schema" ];

        for entity in myInputsJSON[ "inputs" ] :
            myQuery  = "DROP TABLE IF EXISTS " + str( mySchema ) + "." + str( entity ).lower() + ";";
            myQuery += "CREATE TABLE " + str( mySchema ) + "." + str( entity ).lower() + " ( ";
            myTempQuery = [];
            myTempQuery.append( "id serial NOT NULL" );
            for item in myInputsJSON[ "inputs" ][ entity ]:
                myFieldType = "varchar" if item[ "type" ] == "varchar" else "numeric";
                myTempQuery.append( str( item[ "name" ] ) + " " + str( myFieldType ) + " NULL" );
            myQuery += ",\r\n".join( myTempQuery );
            myQuery += ",PRIMARY KEY (id) ";
            myQuery += ");";
            myWholeQuery.append( myQuery );

        for aQuery in myWholeQuery:
            myModel.executeQuery( aQuery , None , "update" );

        # Populate with CSV Data
        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/dats_list.csv" , True );
        amTool.log( "--- Adding DATs to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="dat" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/live_stock_cattle_v2.csv" , True );
        amTool.log( "--- Adding DATs to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="cattle" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/live_stock_pigs_v2.csv" , True );
        amTool.log( "--- Adding DATs to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="pigs" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/live_stock_poultry_v2.csv" , True );
        amTool.log( "--- Adding DATs to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="poultry" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/live_stock_small_ruminants_v2.csv" , True );
        amTool.log( "--- Adding DATs to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="small_ruminants" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/arable_with_dats.csv" , True );
        amTool.log( "--- Adding Arable Table Data to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="arable" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/fruits_with_dats.csv" , True );
        amTool.log( "--- Adding Fruits Table Data to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="fruits" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/vineyards_with_dats.csv" , True );
        amTool.log( "--- Adding Vineyards Table Data to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="vineyards" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/vegetables_with_dats.csv" , True );
        amTool.log( "--- Adding Vegetables Table Data to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="vegetables" );

        myParsedCSV = amTool.parseCSVFile( "../resources/data/latest_update/orchards_with_dats.csv" , True );
        amTool.log( "--- Adding Orchards Table Data to Database ---" , cfg[ "settings" ][ "debug" ] );
        myResponse = [];
        myResponse = await myModel.addEntity( myParsedCSV , entity="orchards" );

    except( Exception ) as error :
        print( error );

@app.get( "/administration/create_input_models", 
          tags         = [ "Administration" ] , 
          summary      = "Create our Input BaseModels",
          description  = "Create our Input BaseModels" 
        ) 
async def createInputModels():
  # Loads the SourceFile JSON and creates our BaseModels that will populatee the Inputs for each EndPoint created
    targetFileName = "models/inputs.py";
    myFile         = [];

    try:
        myInputsJSON = amTool.load( "" , DBsourceFileName , "json" );
        amTool.log( "File has been opened" );
        amTool.log( myInputsJSON );

        f = open( targetFileName, "w" );
        f.write( "import time;\r\n" );
        f.write( "import datetime;\r\n" );
        f.write( "from datetime import timedelta;\r\n" );
        f.write( "from typing import Optional , List;\r\n" );
        f.write( "from enum import Enum;\r\n" );
        f.write( "from pydantic import BaseModel , Field , create_model;\r\n" );
        f.write( "\r\n" );

        myEntityClass    = [];
        for entity in myInputsJSON[ "inputs" ] :
            myEntityClassGet = [];
            myEntityClass.append( "class " + entity + "( BaseModel ):\r\n" );
            myEntityClassGet.append( "class get_" + entity + "( BaseModel ):\r\n" );
            myEntityClassGet.append( "\t\t\t\tid     : Optional[ str ] = Field( None , description = \"\" );\r\n" );
            myEntityClassGet.append( "\t\t\t\tlimit  : Optional[ int ] = Field( None , description = \"\" );\r\n" );
            myEntityClassGet.append( "\t\t\t\toffset : Optional[ int ] = Field( None , description = \"\" );\r\n" );

            for item in myInputsJSON[ "inputs" ][ entity ] :

                myType = "str";
                if str( item[ "type" ] ) == "numeric" : 
                    myType = "float";
                elif str( item[ "type" ] ) == "varchar" : 
                    myType = "str";
                elif str( item[ "type" ] ) == "float" : 
                    myType = "float";
                else:
                    myType = "int";

                myEntityClass.append( 
                   ( 
                     "\t\t\t\t" + 
                         str( item[ "name" ] ).lower() + " : " + 
                         "Optional[ " + str( myType ) + " ] " + 
                         "= " + 
                         "Field( None , description = \"" + str( item[ "desc" ] )  + "\" );\r\n" 
                   )
                );

                if item[ "filter" ] == "true" :
                    myEntityClassGet.append( 
                       ( 
                         "\t\t\t\t" + 
                             str( item[ "name" ] ).lower() + " : " + 
                             "Optional[ " + str( myType ) + " ] " + 
                             "= " + 
                             "Field( None , description = \"" + str( item[ "desc" ] )  + "\" );\r\n" 
                       )
                    );
            
            # print( entity + " | " + str( len( myEntityClassGet ) ) );

            myEntityClassGet.append( "\r\n\r\n" );
            myFile.append( "".join( myEntityClassGet ) );

            myEntityClass.append( "\r\n\r\n" );

        myFile.append( "".join( myEntityClass ) );
        # myFile.append( "".join( myEntityClassGet ) );
        print( myFile );

        for row in myFile : 
            f.writelines( row );

        f.close();

    except( Exception ) as error :
        print( error );

# Input Points 
myJSONSchema  = amTool.load( "" , DBsourceFileName , "json" );
myIterator    = iter( myJSONSchema[ "inputs" ] );
loopCompleted = False;
hasCSVImports = False;

# EndPoints for CRUD Operations. Only the ones int he following array will be created
# It will use the "schema.json" file in order to create the appropriate EndPoints
# visibleEndPoints = [ "dat" , "userdata_generic" , "userdata_generic_livestock" ];
visibleEndPoints = [ "dat" ];

while not loopCompleted : 
    try:
        item = next( myIterator );
        def preventLastBind( item = item ):
            if item in visibleEndPoints : 
                try:
                    eval( "Inputs." + item );
                    @app.put( "/" + item, 
                              tags           = [ item ] , 
                              summary        = "Add Item",
                              description    = "Add Item"
                            ) 
                    async def addContext( request : List[ eval( "Inputs." + item ) ] ):
                        myResponse = [];

                        if( cfg[ "settings" ][ "debug" ] is True ):
                            print( "" , flush=True );

                        amTool.log( "--- Adding Record to Database ---" , cfg[ "settings" ][ "debug" ] );
                        myResponse = await myModel.addEntity( request , entity=item.lower() );

                        return myResponse;

                    @app.get( "/" + item, 
                              tags           = [ item ] , 
                              response_model = List[ eval( "Inputs." + item ) ] ,
                              summary        = "Retrieve Item",
                              description    = "Retrieve Item"
                            ) 
                    async def getContext( params : eval( "Inputs.get_" + item ) = Depends() ):
                        myResponse = [];

                        if( cfg[ "settings" ][ "debug" ] is True ):
                            print( "" , flush=True );

                        amTool.log( "--- Getting Record from Database ---" , cfg[ "settings" ][ "debug" ] );
                        myResponse = await myModel.getEntityAllProperties( params , entity=item.lower() );

                        return myResponse;

                    @app.delete( "/" + item, 
                              tags         = [ item ] , 
                              summary      = "Delete Item",
                              description  = "Delete Item"
                            ) 
                    async def deleteContext( id : Optional[ str ] ):
                        myResponse = [];

                        if( cfg[ "settings" ][ "debug" ] is True ):
                            print( "" , flush=True );

                        amTool.log( "--- Deleting Record from Database ---" , cfg[ "settings" ][ "debug" ] );
                        myResponse = await myModel.deleteEntity( id=parseStringIntoArrayWithIntegers( id ) , entity=item.lower() );

                        return myResponse;

                    @app.post( "/" + item, 
                              tags         = [ item ] , 
                              summary      = "Update Item",
                              description  = "Update Item"
                            ) 
                    async def updateContext( id : str , request : eval( "Inputs." + item ) ):
                        myResponse = [];

                        if( cfg[ "settings" ][ "debug" ] is True ):
                            print( "" , flush=True );

                        amTool.log( "--- Updating Record in Database ---" , cfg[ "settings" ][ "debug" ] );
                        myResponse = await myModel.updateEntity( id=id , request=request , entity=item.lower() );

                        return myResponse;

                    if hasCSVImports == True : 

                        @app.post( "/csv/import/" + item, 
                                  tags         = [ item ] , 
                                  summary      = "Import " + str( item ),
                                  description  = "Import " + str( item )
                                ) 
                        async def uploadCSV( filedata : UploadFile = File(...) ):

                            myParsedCSV = amTool.parseCSV( filedata , True );
                            # print( myParsedCSV );

                            amTool.log( "--- Adding Record to Database ---" , cfg[ "settings" ][ "debug" ] );
                            myResponse = [];
                            myResponse = await myModel.addEntity( myParsedCSV , entity=item.lower() );

                            return myResponse;

                        @app.get( "/csv/export/" + item, 
                                  tags         = [ item ] , 
                                  summary      = "Export " + str( item ),
                                  description  = "Export " + str( item )
                                ) 
                        async def downloadCSV( params : eval( "Inputs.get_" + item ) = Depends() ):

                            exportsPath = cfg[ "exports" ][ "path" ];
                            dateString  = datetime.date.today().strftime('%a_%d_%b_%Y_%I_%M%p');
                            fileName    = amTool.cfg[ "service" ][ "title" ].replace( " " , "_" ).lower() + "_" + dateString + "_" + str( amTool.getUID() );
                            extension   = "csv";
                            filePath    = os.path.abspath( exportsPath + str( fileName ) + "." + str( extension ) );

                            amTool.log( "--- Getting Record from Database ---" , cfg[ "settings" ][ "debug" ] );
                            myResponse = await myModel.getEntityAllProperties( params , entity=item.lower() );

                            myHeaders = [];
                            myData    = [];
                            for index , row in enumerate( myResponse ) : 
                                myRowData = [];
                                for header in row :
                                    if( index == 0 ):
                                        myHeaders.append( header );

                                    myRowData.append( str( row[ header ] ) );

                                myData.append( myRowData );

                            myExportString = ";".join( myHeaders ) + "\r\n";
                            for row in myData:
                                myExportString += ";".join( row ) + "\r\n";

                            fd = open( filePath , "a+");
                            fd.write( myExportString );
                            fd.close();

                            return FileResponse(
                                filePath , 
                                media_type = 'application/octet-stream', 
                                filename   = ( fileName + "." + extension ) 
                            );

                        @app.get( "/csv/clear/" + item, 
                                  tags         = [ item ] , 
                                  summary      = "Clear Exports " + str( item ),
                                  description  = "Clear Exports " + str( item )
                                ) 
                        async def clearExports( ):

                            try:
                                threshold   = 50; # Seconds
                                exportsPath = cfg[ "exports" ][ "path" ];
                                currentTimestamp = round( time.time() );
                                for dir_item in os.listdir( exportsPath ):
                                    myFile = os.path.splitext( dir_item );
                                    if myFile[ 1 ] != ".csv" : 
                                        continue;
                                    else:
                                        itemTimeOfCreation = round( os.path.getmtime( exportsPath+"/"+dir_item ) );
                                        if currentTimestamp - itemTimeOfCreation > threshold : 
                                            os.remove( exportsPath+"/"+dir_item );
                                return [ "Succesfull clear of '" + item + "' exports greater than " + str( threshold ) + " seconds" ];
                            except( Exception ) as error:
                                return [ "fail" ];

                except( Exception ) as error :
                    print( "Nothing Found : " + str( item ) );

        preventLastBind();

    except StopIteration:
        loopCompleted = True;

# Create Input Forms
myObjects = {};

# Create the "Add Data" Object that will be later used to create the "Add Data" Endpoints
# Fields are found inside "userdata_generic" at "./schema.json".
# Not all Fields in a Table need to be populated by the user. Most are pre-populated with defaults values.
# This Object will have only the Fields that need User Data.
# Each EndPoint will get the "entity" from the JSON and the fields "name" will be added as the Post Paramters
for field in myJSONSchema[ "inputs" ][ "userdata_generic" ]:
    try:
        def preventLastBindInput( field = field ):
            try:
                if field[ "entity" ] not in myObjects and field[ "entity" ] != "" : 
                    myObjects[ field[ "entity" ] ] = { "user_id" : 0 };

                for property in field : 
                    fieldType = "varchar";
                    if( field[ "type" ] == "integer" ) :
                        myObjects[ field[ "entity" ] ][ field[ "name" ] ] = 0;
                    elif( field[ "type" ] == "float" ) :
                        myObjects[ field[ "entity" ] ][ field[ "name" ] ] = 0.0;

            except( Exception ) as error :
                print( error );

        preventLastBindInput();

    except StopIteration:
        loopInputCompleted = True;

# Create Endpoints for adding Data into the UserData Table
if activateAddDataEndPoint == True : 
    for myClassName in myObjects : 
        def PreventLastBindInput( myClassName = myClassName ):
            myInputClass = create_model( myClassName , **myObjects[ myClassName ] );
            @app.post( "/" + myClassName ,
                      tags         = [ "Add Data" ] , 
                      summary      = "Get Results",
                      description  = ( "" )
                    )
            async def getResults( 
                  request : List[ myInputClass ]
                ):

                myResponse = [];

                if( cfg[ "settings" ][ "debug" ] is True ):
                    print( "" , flush=True );
                    
                userID = str( dict( request[ 0 ] )[ "user_id" ] );

                # myResult = await myModel.getEntityByUserId( entity = "userdata_generic" , user_id = [ "1" ] );
                myResult = await myModel.getEntityByUserId( entity = "userdata_generic" , user_id = [ userID ] );
                if len( myResult ) <= 0 :
                    amTool.log( "--- Adding Record to userdata_generic ---" , cfg[ "settings" ][ "debug" ] );
                    myResponse = await myModel.addEntity( request , entity = "userdata_generic" );
                else:
                    amTool.log( "--- Updating Record to userdata_generic ---" , cfg[ "settings" ][ "debug" ] );
                    myResponse = await myModel.updateEntityByUserId( 
                        request = request[ 0 ] , 
                        user_id = userID , 
                        entity  = "userdata_generic" 
                    );

                return myResponse;

        PreventLastBindInput();

# Get User Data for Crops
@app.get( "/user_data/crop" ,
          tags         = [ "User Data Crops" ] , 
          summary        = "Retrieve Item",
          description    = "Retrieve Item"
        ) 
async def getUseDataCrops( user_id : str ):
    myResponse = {};

    if( cfg[ "settings" ][ "debug" ] is True ):
        print( "" , flush=True );

    amTool.log( "--- Getting Record from Database ---" , cfg[ "settings" ][ "debug" ] );
    myResult = await myModel.getEntityByUserId( entity = "userdata_generic" , user_id = [ str( user_id ) ] );
    if len( myResult ) <= 0 : 
        raise HTTPException( 
            status_code = 401, 
            detail      = "Resource not found. User ID has no records" 
        );

    myResponse[ "id" ] = myResult[ 0 ][ "id" ];

    for inputField in myJSONSchema[ "inputs" ][ "userdata_generic" ] : 
        print( "inputField : " + str( inputField ) );
        if inputField[ "entity" ] not in myResponse and inputField[ "entity" ] != "" : 
            myResponse[ inputField[ "entity" ] ] = {};

        if inputField[ "name" ] in myResult[ 0 ] : 
            print( inputField[ "name" ] + " Exists" );
            if inputField[ "name" ] != "user_id" and inputField[ "name" ] not in myResponse[ inputField[ "entity" ] ] : 
                myResponse[ inputField[ "entity" ] ][ inputField[ "name" ] ] = myResult[ 0 ][ inputField[ "name" ] ];

    return myResponse;

# This one either Adds or Updates Crop Data depending on State
@app.post( "/user_data/crop" ,
          tags         = [ "User Data Crops" ] , 
          summary        = "Add User Data",
          description    = ( 
          "<ul>" + 
            "<li>User has records <b>UPDATE</b> will be executed</li>" + 
            "<li>User has no records <b>INSERT</b> will be executed</li>" + 
          "</ul>"
          )
        ) 
async def addUserDataCrops( request : List[ Inputs.userdata_generic ] ):
    myResponse = {};

    if( cfg[ "settings" ][ "debug" ] is True ):
        print( "" , flush=True );

    amTool.log( "--- Getting Record from Database ---" , cfg[ "settings" ][ "debug" ] );
    userID = str( dict( request[ 0 ] )[ "user_id" ] );
    myResult = await myModel.getEntityByUserId( entity = "userdata_generic" , user_id = [ userID ] );

    if len( myResult ) <= 0 : 
        print( "No record exists : Adding" );
        myResponse = await myModel.addEntity( request , entity = "userdata_generic" );
    else:
        print( "Record exists : Updating" );
        myResponse = await myModel.updateEntity( id= str( myResult[ 0 ][ "id" ] ) , request=request[ 0 ] , entity = "userdata_generic" );

    return myResponse;

# Get User Data for Livestock
@app.get( "/user_data/livestock" ,
          tags         = [ "User Data Livestock" ] , 
          summary        = "Retrieve Item",
          description    = "Retrieve Item"
        ) 
async def getUseDataCrops( user_id : str ):
    myResponse = {};

    if( cfg[ "settings" ][ "debug" ] is True ):
        print( "" , flush=True );

    amTool.log( "--- Getting Record from Database ---" , cfg[ "settings" ][ "debug" ] );
    myResult = await myModel.getEntityByUserId( entity = "userdata_generic_livestock" , user_id = [ str( user_id ) ] );
    if len( myResult ) <= 0 : 
        raise HTTPException( 
            status_code = 401, 
            detail      = "Resource not found. User ID has no records" 
        );

    myResponse[ "id" ] = myResult[ 0 ][ "id" ];

    for inputField in myJSONSchema[ "inputs" ][ "userdata_generic_livestock" ] : 
        print( "inputField : " + str( inputField ) );
        if inputField[ "entity" ] not in myResponse and inputField[ "entity" ] != "" : 
            myResponse[ inputField[ "entity" ] ] = {};

        if inputField[ "name" ] in myResult[ 0 ] : 
            print( inputField[ "name" ] + " Exists" );
            if inputField[ "name" ] != "user_id" and inputField[ "name" ] not in myResponse[ inputField[ "entity" ] ] : 
                myResponse[ inputField[ "entity" ] ][ inputField[ "name" ] ] = myResult[ 0 ][ inputField[ "name" ] ];

    return myResponse;

# This one either Adds or Updates Livestock Data depending on State
@app.post( "/user_data/livestock" ,
          tags         = [ "User Data Livestock" ] , 
          summary        = "Add User Data",
          description    = ( 
          "<ul>" + 
            "<li>User has records <b>UPDATE</b> will be executed</li>" + 
            "<li>User has no records <b>INSERT</b> will be executed</li>" + 
          "</ul>"
          )
        ) 
async def addUserDataCrops( request : List[ Inputs.userdata_generic_livestock ] ):
    myResponse = {};

    if( cfg[ "settings" ][ "debug" ] is True ):
        print( "" , flush=True );

    amTool.log( "--- Getting Record from Database ---" , cfg[ "settings" ][ "debug" ] );
    userID = str( dict( request[ 0 ] )[ "user_id" ] );
    myResult = await myModel.getEntityByUserId( entity = "userdata_generic_livestock" , user_id = [ userID ] );

    if len( myResult ) <= 0 : 
        print( "No record exists : Adding" );
        myResponse = await myModel.addEntity( request , entity = "userdata_generic_livestock" );
    else:
        print( "Record exists : Updating" );
        myResponse = await myModel.updateEntity( id= str( myResult[ 0 ][ "id" ] ) , request=request[ 0 ] , entity = "userdata_generic_livestock" );

    return myResponse;


# Get Totals

class CultivationTypes( str , Enum ):
    arable          = "arable";
    fruits          = "fruits";
    vineyards       = "vineyards";
    vegetables      = "vegetables";
    orchards        = "orchards";
    cattle          = "cattle";
    pigs            = "pigs";
    poultry         = "poultry";
    small_ruminants = "small_ruminants";

class DATTypes( str , Enum ):
    crop      = "crop";
    livestock = "livestock";

async def getTotalsOptions( DATType , CultivationType , dat_name , user_id , userdata_entity , tableStartingIndex , tableStartingLetter ):
    myModels = [];

    if DATType == "livestock" : 
        myModels.append( "investment" );
        myModels.append( "milk_yield" );
        myModels.append( "labor_cost" );
        myModels.append( "energy_cost" );
        myModels.append( "water_usage" );
        myModels.append( "profit_per_animal" );
        myModels.append( "feed_cost" );
        myModels.append( "feed_waste" );
        myModels.append( "antibiotics_cost" );
        myModels.append( "mortality_cost" );
        myModels.append( "profitability_increase" );
        myModels.append( "totals" );
    else:
        myModels.append( "investment"  );
        myModels.append( "yield"  );
        myModels.append( "fertilizer_reduction"  );
        myModels.append( "water_reduction"  );
        myModels.append( "pesticide_reduction"  );
        myModels.append( "labor_reduction"  );
        myModels.append( "fuel_reduction"  );
        myModels.append( "totals"  );

    myObject = {
        "myModels" : myModels , 
        "dataSet"  : ""
    };

    dataSet = await myModel.getWholeDataset( 
      cultivationType = CultivationType , 
      dat_name        = dat_name , 
      user_id         = user_id , 
      userdata_entity = userdata_entity
    );

    # This Function directly changes the dataset. 
    # In the function i change the Objects properties which by default are passed by Reference in Python.
    # so changing them will result in changes in the underlying object.
    # That is the reason there is no return here.
    turnIneligiblePropertiesIntoZero(
        dataset = dataSet , 
        filter  = [ { "column" : "cultivation_type" , "value" : str( CultivationType.value ) } ]
    );

    print( "[ CREATION ] : Creating Memory Object from DataSet" );
    myResObject = createMemoryObject(
        dataSet , 
        tableStartingIndex  = tableStartingIndex, 
        tableStartingLetter = tableStartingLetter
    );

    if "error" in myResObject:
        return myResObject;
    else:
        return myObject;

@app.get( "/totals/" , 
          tags         = [ "totals" ] , 
          summary      = "Get Results",
          description  = ( "" )
        )
async def getResults( 
      user_id           : str , 
      dat_name          : str , 
      myCultivationType : CultivationTypes , 
      type              : DATTypes
    ):

    if type == "livestock" : 
        sourceFileName      = "calculator_schema_livestock_v2";
        userdata_entity     = "userdata_generic_livestock";
        tableStartingIndex  = 3;
        tableStartingLetter = "J";
    else:
        sourceFileName      = "calculator_schema_v2";
        userdata_entity     = "userdata_generic";
        tableStartingIndex  = 3;
        tableStartingLetter = "G";

    # CultivationType designates the name of the Table that holds the data
    myTotalOptions = await getTotalsOptions( 
        DATType             = type, 
        CultivationType     = myCultivationType, 
        dat_name            = dat_name, 
        user_id             = user_id, 
        userdata_entity     = userdata_entity,
        tableStartingIndex  = tableStartingIndex,
        tableStartingLetter = tableStartingLetter
    );
    
    # "dataset" property should be empty
    print( JSON.dumps( myTotalOptions , indent = 4 ) );

    if "error" in myTotalOptions : 
        raise HTTPException( 
            status_code = 401, 
            detail      = myTotalOptions[ "error" ]
        );

    # In the following file all the Excel functions are Defined
    myResponse     = {};

    # Now that we have all of our property:value pairs in memory we can proceed 
    # in executing all the Excel functions and print out the results
    try:
        myInputsJSON = amTool.load( "" , sourceFileName , "json" );
        myWholeQuery = [];

        print( "[ ENTITY ] " + str( myCultivationType ) );
        myResponse = { 
          "info" : { 
            "type_of_cultivation" : myCultivationType , 
            "totals"              : [ "annual_change_in_net_income" , "costs_saving" , "return_on_investment" , "net_benefit" ]
          } , 
          "result" : {} 
        };

        for myModelName in myTotalOptions[ "myModels" ]:
            print( myModelName );
            for item in myInputsJSON[ myModelName ]:
                print( "[ ITEM    ] : " + str( item[ "name" ] ) );

                if item[ "function" ] != "" : 
                    formula = str( item[ "function" ] );
                    printFormula( formula );
                    formRes = getResultFromFormula( formula );
                    print( "[ ADDITION ] : Adding ( " + str( formRes ) + " to " + str( item[ "column" ] ) + "3 )" );
                    globals()[ str( item[ "column" ] ) + str( "3" ) ] = formRes;
                    # myResponse[ "result" ][ str( item[ "name" ] ) ] = str( formRes );
                    if( myModelName not in myResponse[ "result" ] ):
                        myResponse[ "result" ][ myModelName ] = dict();

                    if( str( item[ "name" ] ) not in myResponse[ "result" ][ myModelName ] ):
                        myResponse[ "result" ][ myModelName ][ str( item[ "name" ] ) ] = str( formRes );

                    # myResponse[ "result" ][ str( item[ "name" ] ) ] = str( formRes );
                    print( "[ RESULT  ] : " + str( formRes ) );
                    print( "-----------------------------------------" );

    except( Exception ) as error :
        print( error );

    return myResponse;

@app.get( "/dat_tree" , 
          tags           = [ "dat_tree" ] , 
          summary        = "Retrieve DATs in a Tree like Object",
          description    = "Retrieve DATs in a Tree like Object"
        ) 
async def getContext(
      myDatType : DATTypes 
    ):

    if( myDatType == "crop" ):
        myResponse = {
            "arable"     : await myModel.getCultivationDATTree( "arable" ) ,
            "fruits"     : await myModel.getCultivationDATTree( "fruits" ),
            "vineyards"  : await myModel.getCultivationDATTree( "vineyards" ),
            "vegetables" : await myModel.getCultivationDATTree( "vegetables" ),
            "orchards"   : await myModel.getCultivationDATTree( "orchards" )
        };
    else:
        myResponse = {
            "cattle"          : await myModel.getCultivationDATTree( "cattle" ),
            "pigs"            : await myModel.getCultivationDATTree( "pigs" ),
            "poultry"         : await myModel.getCultivationDATTree( "poultry" ),
            "small_ruminants" : await myModel.getCultivationDATTree( "small_ruminants" )
        };

    return myResponse;

# Get Results

def getEntityResults( entityItem , parent ):
    myEntityResults = {
      "info"         : {},
      "calculations" : {},
      "total"        : 0
    }

    # Add info Properties in our Info Response 
    for entityProperty in entityItem:
        if entityProperty != "functions" and entityProperty != "aggregations" : 
            myEntityResults[ "info" ][ entityProperty ] = entityItem[ entityProperty ];

    print();
    print( ">>>>> [ Indicator ] : " + str( entityItem[ "indicator" ] ) );

    # Evaluate the Formulas and add them to our Response
    myFunctions = entityItem[ "functions" ];
    for nameOfFunction in myFunctions : 
        myFormula = myFunctions[ nameOfFunction ][ "formula" ];
        print( ">>>>> [ Formula ] : " + str( myFormula ) );
        try:
            myResult = eval( myFormula );
            myEntityResults[ "calculations" ][ nameOfFunction ] = round( myResult , 4 );
        except( Exception ) as error :
            myEntityResults[ "calculations" ][ nameOfFunction ] = 0;
        finally:
            globals()[ nameOfFunction ] = myEntityResults[ "calculations" ][ nameOfFunction ];
            globals()[ parent + "_" + entityItem[ "activity" ].replace( " " , "_" ) + "_" + entityItem[ "microactivity" ].replace( " " , "_" ) + "_" + entityItem[ "indicator" ].replace( " " , "_" ).replace( "(" , "" ).replace( ")" , "" ) + "_total" ] = myEntityResults[ "calculations" ][ nameOfFunction ];

    # Evaluate Aggregations (if any) and add them to the Result
    if "aggregations" in entityItem : 
        for nameOfAggregation in entityItem[ "aggregations" ] : 
            myFormula = entityItem[ "aggregations" ][ nameOfAggregation ];
            try:
                myResult = eval( myFormula );
                myEntityResults[ "total" ] = round( myResult , 4 );
                globals()[ parent + "_" + entityItem[ "activity" ].replace( " " , "_" ) + "_" + entityItem[ "microactivity" ].replace( " " , "_" ) + "_" + entityItem[ "indicator" ].replace( " " , "_" ).replace( "(" , "" ).replace( ")" , "" ) + "_total" ] = myEntityResults[ "total" ];
            except( Exception ) as error :
                myEntityResults[ "total" ] = 0;

    return myEntityResults;

def getRevenueResults( entityItem ):
    myEntityResults = {
      "info"         : {},
      "calculations" : {}
    }
    myFormulaResults = {};

    for entityProperty in entityItem:
        if entityProperty != "functions" and entityProperty != "aggregations" : 
            myEntityResults[ "info" ][ entityProperty ] = entityItem[ entityProperty ];

    myFunctions = entityItem[ "functions" ];
    for nameOfFunction in myFunctions : 
        myFormula = myFunctions[ nameOfFunction ][ "formula" ];
        try:
            myResult = eval( myFormula );
            myEntityResults[ "calculations" ][ nameOfFunction ] = myResult;
        except( Exception ) as error :
            print( error );
            myEntityResults[ "calculations" ][ nameOfFunction ] = 0;
        finally:
            globals()[ nameOfFunction ] = myEntityResults[ "calculations" ][ nameOfFunction ];

    return myEntityResults;

def printFormula( formula ):
    myFormula = ( formula.replace( "$" , "" )
                         .replace( "=" , "" )
                         .replace( "*" , "," )
                         .replace( "+" , "," )
                         .replace( "-" , "," )
                         .replace( "/" , "," ) 
                         .replace( ")" , "," ) 
                         .replace( "(" , "," ) 
                         .replace( "IF" , "," ) 
                         .replace( "if" , "," ) 
                         .replace( "OR" , "," ) 
                         .replace( "or" , "" ) 
                         .replace( "ELSE" , "," ) 
                         .replace( "else" , "," ) 
                         .replace( " " , "," )
                );

    print( "[ FORMULA ] : " + str( formula ) );
    myValues = [];
    for aField in myFormula.split( "," ):
        if aField.strip() != "" and aField.strip().isnumeric() is not True :
            myValue = round( eval( aField.strip() ) , 4 );
            myValues.append( str( myValue ) );

    print( "[ VALUES  ] : " + "|".join( myValues ) );

def __getResultFromFormula( formula ):
    myFormula = ( formula
                  .replace( "$" , "" )
                );

    if myFormula[0] == "=" : 
        myFormula = myFormula[1:];

    myResult = eval( myFormula );
    return myResult;

def getResultFromFormula( formula ):
    # Function to replace variable names with their actual values
    def replace_vars(expr):
        return re.sub(r'\b[A-Za-z_][A-Za-z0-9_]*\b',
                      lambda match: str(globals().get(match.group(), match.group())),
                      expr)

    myFormula = ( formula
                  .replace( "$" , "" )
                );

    if myFormula[ 0 ] == "=" : 
        myFormula = myFormula[ 1: ];

    # Replace variable names with values for display
    resolved_formula = replace_vars( formula );
    print( "[ RESOLVED ] : " +str( resolved_formula ) );
    
    try:
        myResult = eval( myFormula.replace( "="    , "=="  ) );
        return myResult;
    except( Exception ) as error :
        print( error );
        return [];

def createMemoryObject( dataSet , tableStartingIndex , tableStartingLetter ):
    # tableStartingLetter starts from 0 as the 1st Letter "A"
    # tableStartingIndex does not start from 0. The number set here is the exact row number the table starts.
    myLetters = [ 
                  "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
                  "AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ","AK","AL","AM","AN","AO","AP","AQ","AR","AS","AT","AU","AV","AW","AX","AY","AZ",
                  "BA","BB","BC","BD","BE","BF","BG","BH","BI","BJ","BK","BL","BM","BN","BO","BP","BQ","BR","BS","BT","BU","BV","BW","BX","BY","BZ"
                ];

    if "error" in dataSet : 
        return dataSet;

    for rindex , row in enumerate( dataSet ) : 
        myRowIndex = ( rindex + tableStartingIndex );
        for findex , field in enumerate( row ): 
            # All tables start with an ID column.
            # This column is not mapped on the Excel and is only for the DB auto increment
            # So i skip it and start assigning after the 0 index
            if findex > 0 : 
                myFieldIndex = ( ( findex - 1 ) + myLetters.index( tableStartingLetter ) );
                myFieldPos   = ( str( myLetters[ myFieldIndex ] ) + str( myRowIndex ) );
                print( 
                  "[ ADDITION ] : adding global : " + str( myFieldPos ) + 
                  " [ " + str( field ) + " ] : " + 
                  str( row[ field ] ) 
                );
                try :
                    if row[ field ].isnumeric() : 
                        globals()[ myFieldPos ] = float( row[ field ] );
                    else:
                        globals()[ myFieldPos ] = row[ field ];
                except( Exception ) as error :
                    if row[ field ] is not None:
                        globals()[ myFieldPos ] = float( row[ field ] );
    
    return { "res" : "success" };

def printGlobals():
    for variable in globals() : 
        print( str( variable ) + " : " + str( globals()[ variable ] ) );

def getObject( request , entity ):

    myInternalObject = eval( "TemplateInputs." + entity + "_put" );
    myResponse = dict();
    for item in myInternalObject.__fields__:
        myResponse[ item ] = eval( "request." + item );

    return myResponse;

myEndPoints = [
  "investment" , 
  "yield" , 
  "fertilizer_reduction" , 
  "water_reduction" , 
  "pesticide_reduction" , 
  "labor_reduction" , 
  "fuel_reduction"
];

# myEntities = [ "arable" , "fruits" , "vineyards" , "vegetables" , "orchards" ];
myEntities = [];

# Create EndPoints for Getting Calculated Results from each entity
for amModelName in myEntities: 
    for amResultName in myEndPoints : 
        def preventLastBind( amModelName = amModelName , amResultName = amResultName ):

            @app.post( "/results/" + amModelName + "/" + amResultName, 
                       tags         = [ amModelName + "_results" ] , 
                       summary      = "Get Results",
                       description  = ( "" )
                     )
            async def getResults(
                  dat_name : str,
                  user_id  : str
                ):

                # Retrieve the Record with all the Default Values from the Database based on the Dat Name
                dataSet = await myModel.getTableData( amModelName , { "column" : "dat_name" , "value" : dat_name } );
                if( len( dataSet ) <= 0 ) : 
                    raise HTTPException( 
                        status_code = 401, 
                        detail      = "Resource not found. Unknown DAT" 
                    );

                # Retrieve the User Data from the Database
                myUserDataObject = {};
                myUserData       = {};
                myResult = await myModel.getEntityByUserId( entity = "userdata_generic" , user_id = [ str( user_id ) ] );
                if len( myResult ) <= 0 : 
                    raise HTTPException( 
                        status_code = 401, 
                        detail      = "Resource not found. User ID has no records" 
                    );

                # for a in myResult[ 0 ] : 
                    # print( str( a ) + " : " + str( myResult[ 0 ][ a ] ) );

                # Create a Property = Value Object using the Results from the above Query
                # for inputField in myJSONSchema[ "inputs" ][ "userdata_generic" ] : 
                    # if inputField[ "entity" ] not in myUserDataObject and inputField[ "entity" ] != "" : 
                        # myUserDataObject[ inputField[ "entity" ] ] = {};

                    # if inputField[ "name" ] in myResult[ 0 ] : 
                        # if inputField[ "name" ] != "user_id" and inputField[ "name" ] not in myUserDataObject[ inputField[ "entity" ] ] : 
                            # myUserDataObject[ inputField[ "entity" ] ][ inputField[ "name" ] ] = myResult[ 0 ][ inputField[ "name" ] ];

                # for parentEntity in myUserDataObject : 
                    # for property in myUserDataObject[ parentEntity ] :
                        # myUserData[ property ] = myUserDataObject[ parentEntity ][ property ];

                # for b in myUserData : 
                    # print( str( b ) + " : " + str( myUserData[ b ] ) );

                # Update the database record of the "Default" values with the , "User Provided Values" , Database Record 
                print( "[ CREATION ] : Creating DataObject with Updated Values from the User Provided DataSet" );
                for item in dataSet[ 0 ]:
                    if item in myResult[ 0 ] : 
                        if myResult[ 0 ][ item ] is not None : 
                            print( str( item ) + " : " + str( myResult[ 0 ][ item ] ) );
                            dataSet[ 0 ][ item ] = myResult[ 0 ][ item ];

                for b in dataSet[ 0 ] : 
                    print( str( b ) + " : " + str( dataSet[ 0 ][ b ] ) );

                # Update the above database retrieved record with the values provided by the user in the Request
                # print( "[ CREATION ] : Creating DataObject with Updated Values from the User Provided DataSet" );
                # for item in dataSet[ 0 ]:
                    # if item in myUserData : 
                        # if myUserData[ item ] is not None : 
                            # print( str( item ) + " : " + str( myUserData[ item ] ) );
                            # dataSet[ 0 ][ item ] = myUserData[ item ];

                # I need to create an object in memory that will house all the values of the excel 
                # along with the corresponding letter. Something like:  { "A1" : 15 , "A2" : 16 , "BC34" : 123 }  , etc.
                # Every single property will be added to the "globals" namespace thus available everywhere in the code.
                # Then a simple eval over a string (function from excel) like "(A3+A4*AB45)" will bring results
                print( "[ CREATION ] : Creating Memory Object from DataSet" );
                createMemoryObject(
                    dataSet  , 
                    tableStartingIndex  = 3, 
                    tableStartingLetter = "I"
                );

                # In the following file all the Excel functions are Defined
                sourceFileName = "calculator_schema_v2";
                myResponse     = {};

                # Now that we have all of our property:value pairs in memory we can proceed 
                # in executing all the Excel functions and print out the results
                try:
                    myInputsJSON = amTool.load( "" , sourceFileName , "json" );
                    myWholeQuery = [];

                    print( "[ ENTITY ] " + str( amModelName ) );
                    myResponse[ amModelName ] = { "info" : {} , "result" : {} };

                    for item in myInputsJSON[ amResultName ]:
                        print( "[ ITEM    ] : " + str( item[ "name" ] ) );

                        if item[ "function" ] != "" : 
                            formula = str( item[ "function" ] );
                            printFormula( formula );
                            formRes = getResultFromFormula( formula );
                            globals()[ str( item[ "column" ] ) + str( "3" ) ] = formRes;
                            myResponse[ amModelName ][ "result" ][ str( item[ "name" ] ) ] = str( formRes );
                            print( "[ RESULT  ] : " + str( formRes ) );
                            print( "-----------------------------------------" );

                except( Exception ) as error :
                    print( error );

                return myResponse;

        preventLastBind();
