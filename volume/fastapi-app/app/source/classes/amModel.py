import os;
import datetime;
import time;
import sys;
import aiohttp;
import asyncio;
import psycopg2;
import base64;
import hashlib;
from psycopg2 import sql;
from psycopg2.extras import RealDictCursor;
import csv;
import json as JSON;
from classes.amTools import amTool;

class amModel:
 def __init__( self , cfg ):
  """Class for Queryinjg Database"""
  self.amTool = amTool();
  self.amTool.log( "Model Initiated" );
  self.cfg    = cfg;
  self.debug  = False;

 def executeQuery( self , query , customConnectionString = None , type="select"):
    connection = False;
    cursor     = False;
    try: 
    
       if( customConnectionString is not None ):
           connection = psycopg2.connect( user     = customConnectionString["user"],
                                          password = customConnectionString["password"],
                                          host     = customConnectionString["host"],
                                          port     = customConnectionString["port"],
                                          database = customConnectionString["database"] );
       else:
           connection = psycopg2.connect( user     = self.cfg["database"]["connection"]["user"],
                                          password = self.cfg["database"]["connection"]["password"],
                                          host     = self.cfg["database"]["connection"]["host"],
                                          port     = self.cfg["database"]["connection"]["port"],
                                          database = self.cfg["database"]["connection"]["database"] );

       cursor = connection.cursor( cursor_factory = RealDictCursor );

       cursor.execute( query );

       if( type == "select" ):
           my_query_response = cursor.fetchall();
       elif( type == "insert" ):
           my_query_response = cursor.fetchone();
       else:
           my_query_response = { "success" : "ok"  };

       if( self.debug is True ) :
           print( cursor.query );

       cursor.close();
       connection.commit();

       return my_query_response;

    except( Exception, psycopg2.Error ) as error :
        self.amTool.logFile( error );
        if( self.debug is True ) :
            print( error );

        if( error.pgcode == "23505" ):
            return { "error" : "duplicate" };
        else:
            return [];

    finally:
        if( connection ):
            connection.close();
            if( self.debug is True ) :
                print( "["+__name__+"] : DB Connection Closed" );

 def parseStringIntoArrayWithIntegers( self , string ):
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

 async def getEntityByDatName( self , dat_name ):
 
    mySchema = self.cfg["database"]["schema"];
    myQuery  = ( "select " + 
                 " * " + 
                 "from {mySchema_param}.dat " + 
                 "where dat_name = {myDatNameParam} " + 
                 "order by id DESC "
    );

    qData    = sql.SQL( myQuery ).format( 
                   mySchema_param = sql.Identifier( mySchema ),
                   myDatNameParam = sql.Literal( dat_name )
               );

    myResponse = self.executeQuery( qData , None , "select" );

    return myResponse;

 async def getEntity( self , entity , id=[] , limit=None , offset=None ):
 
    mySchema = self.cfg["database"]["schema"];
    myLimit   = "" if ( limit is None )  else ( "limit " + str( limit ) );
    myOffset  = "" if ( offset is None ) else ( "offset " + str( offset ) );

    myWhereClause = "";
    if( len( id ) > 0 ):
        id            = "','".join( id );
        myWhereClause = "where id in ('" + id + "') ";

    myQuery  = ( "select " + 
                 " * " + 
                 "from {mySchema_param}.{myEntityParam} " + 
                 myWhereClause + 
                 "order by id DESC " + 
                 str( myLimit ) + " " + str( myOffset )
    );

    qData    = sql.SQL( myQuery ).format( 
                   mySchema_param = sql.Identifier( mySchema ),
                   myEntityParam  = sql.Identifier( entity )
               );

    myResponse = self.executeQuery( qData , None , "select" );

    return myResponse;

 async def getEntityByUserId( self , entity , user_id=[] , limit=None , offset=None ):
 
    mySchema = self.cfg["database"]["schema"];
    myLimit   = "" if ( limit is None )  else ( "limit " + str( limit ) );
    myOffset  = "" if ( offset is None ) else ( "offset " + str( offset ) );

    myWhereClause = "";
    if( len( user_id ) > 0 ):
        user_id            = "','".join( user_id );
        myWhereClause = "where user_id in ('" + user_id + "') ";

    myQuery  = ( "select " + 
                 " * " + 
                 "from {mySchema_param}.{myEntityParam} " + 
                 myWhereClause + 
                 "order by user_id DESC " + 
                 str( myLimit ) + " " + str( myOffset )
    );

    qData    = sql.SQL( myQuery ).format( 
                   mySchema_param = sql.Identifier( mySchema ),
                   myEntityParam  = sql.Identifier( entity )
               );

    myResponse = self.executeQuery( qData , None , "select" );

    return myResponse;

 async def getEntityAllProperties( self , params , entity ):
    mySchema = self.cfg["database"]["schema"];
    myLimit   = "" if ( params.limit is None )  else ( "limit " + str( params.limit ) );
    myOffset  = "" if ( params.offset is None ) else ( "offset " + str( params.offset ) );

    myWhereClauseArray  = [];
    myWhereClauseString = "";
    for item in params : 
        if item[ 1 ] is not None:
            if item[ 1 ].isnumeric() is True :
                myWhereClauseArray.append( str( item[ 0 ] ) + " = " + str( item[ 1 ] ) + "" );
            else:
                myWhereClauseArray.append( str( item[ 0 ] ) + " = '" + str( item[ 1 ] ) + "'" );

    if( len( myWhereClauseArray ) > 0 ):
        myWhereClauseString = "where " + " and ".join( myWhereClauseArray ) + " " ;

    myQuery  = ( "select " + 
                 " * " + 
                 "from {mySchema_param}.{myEntityParam} " + 
                 myWhereClauseString + 
                 "order by id DESC " + 
                 str( myLimit ) + " " + str( myOffset )
    );

    qData    = sql.SQL( myQuery ).format( 
                   mySchema_param = sql.Identifier( mySchema ),
                   myEntityParam  = sql.Identifier( entity )
               );

    myResponse = self.executeQuery( qData , None , "select" );

    return myResponse;

 async def addEntity( self , request , entity ):
    mySchema = self.cfg[ "database" ][ "schema" ];

    for record in request:
        myQueryObject = {};
        myColumns = [];
        myValues  = [];
        if isinstance( record , dict ) is True :
            for property in record:
                myString = [];
                myQueryObject[ property ] = str( record[ property ] );
        else:
            for item in record:
                myString = [];
                print( item );
                for value in item:
                    myString.append( str( value ) );
                myQueryObject[ myString[ 0 ] ] = myString[ 1 ];

        for prop in myQueryObject :
            myColumns.append( "\"" + prop.lower() + "\"" );
            myValues.append( myQueryObject[ prop ] );

        myQuery = "INSERT INTO {mySchema_param}.\"" + entity + "\" ";
        myQuery += "(" + " , ".join( myColumns ) + ")";
        myQuery += " VALUES ";
        myQuery += "('" + "' , '".join( myValues ) + "') RETURNING ID;";

        qData    = sql.SQL( myQuery ).format( 
                       mySchema_param = sql.Identifier( mySchema )
                   );

        result = self.executeQuery( qData , None , "insert" );
        if( "error" in result ):
            return { "error" : result[ "error" ] };

    return [];

 async def updateEntity( self , id , request , entity ):
    mySchema = self.cfg[ "database" ][ "schema" ];

    myResponse = {};
    myEntityData = await self.getEntity( id=[id] , entity=entity , limit=1 , offset=0 );

    if( len( myEntityData ) <= 0 ):
        return { "error" : "Nothing to update" };

    myValues = [];
    myFields = [];

    for item in request:
        print( item );
        myProperty = item[ 0 ];
        myValue    = item[ 1 ];

        if myProperty in myEntityData[ 0 ] : 
            myFields.append( myProperty );
            myValues.append( myValue );

    myUpdates = [];
    for index, field in enumerate( myFields ) : 
       if( myValues[ index ] is not None ) :
           myUpdates.append( str( field ) + " = '" + str( myValues[ index ] ) + "'" );

    myQuery = ( "update {mySchema_param}.{myEntity_param} " + 
                "set " + 
                " , ".join( myUpdates ) + 
                "where id = {myId_param};"
    );

    qData   = sql.SQL( myQuery ).format( 
                  mySchema_param  = sql.Identifier( mySchema ),
                  myEntity_param  = sql.Identifier( entity ),
                  myId_param      = sql.Literal( id[ 0 ] )
            );

    myResponse = self.executeQuery( qData , None , "update" );

    return myResponse;

 async def updateEntityByUserId( self , request , user_id , entity ):
    mySchema = self.cfg[ "database" ][ "schema" ];

    myResponse = {};
    myEntityData = await self.getEntityByUserId( user_id=[user_id] , entity=entity , limit=1 , offset=0 );

    if( len( myEntityData ) <= 0 ):
        return { "error" : "Nothing to update" };

    myValues = [];
    myFields = [];

    for item in request:
        myProperty = item[ 0 ];
        myValue    = item[ 1 ];

        if myProperty in myEntityData[ 0 ] : 
            myFields.append( myProperty );
            myValues.append( myValue );

    myUpdates = [];
    for index, field in enumerate( myFields ) : 
       if( myValues[ index ] is not None ) :
           myUpdates.append( str( field ) + " = '" + str( myValues[ index ] ) + "'" );

    myQuery = ( "update {mySchema_param}.{myEntity_param} " + 
                "set " + 
                " , ".join( myUpdates ) + 
                "where user_id = {myId_param};"
    );

    qData   = sql.SQL( myQuery ).format( 
                  mySchema_param  = sql.Identifier( mySchema ),
                  myEntity_param  = sql.Identifier( entity ),
                  myId_param      = sql.Literal( user_id[ 0 ] )
            );

    myResponse = self.executeQuery( qData , None , "update" );

    return myResponse;

 async def deleteEntity( self , entity , id=[] ):

    mySchema      = self.cfg["database"]["schema"];
    myWhereClause = "";
    if( len( id ) > 0 ):
        id            = "','".join( id );
        myWhereClause = "where id in ('" + id + "') ";

    myQuery  = ( "delete  " + 
                 "from {mySchema_param}.{myEntityParam} " + 
                 myWhereClause 
    );

    qData    = sql.SQL( myQuery ).format( 
                   mySchema_param = sql.Identifier( mySchema ),
                   myEntityParam  = sql.Identifier( entity )
               );

    myResponse = self.executeQuery( qData , None , "delete" );

    return myResponse;

 async def createInMemoryObject( self ):
    mySchema = self.cfg[ "database" ][ "schema" ];

    myResults = {};
    for entity in [ "contextentity" , "priceentity" , "volumeentity" , "timeentity" , "n2o_emissions_direct" , "n2o_emissions_indirect" , "co2_emissions_fuel" ]:
        myQuery = "select * from {mySchema_param}.{myEntityParam};";
        qData   = sql.SQL( myQuery ).format( 
                      mySchema_param = sql.Identifier( mySchema ),
                      myEntityParam  = sql.Identifier( entity )
                  );
        result = self.executeQuery( qData , None , "select" );
        myResults[ entity ] = result;

        if( "error" in result ):
            myResults.append( { "error" : result[ "error" ] } );

    myMemoryObject = {};
    for entity in myResults: 
        for row in myResults[ entity ] : 
            type = row[ "type" ] + "_" if ( row[ "type" ] != "default" and row[ "type" ] != "" ) else "";
            for property in row:
                if property == "id" : 
                    continue;
                myMemoryObject[ type + property ] = row[ property ];

    

    return myMemoryObject;

 async def getValues( self , arrayOfProperties ):
    mySchema = self.cfg[ "database" ][ "schema" ];

    myObject = {};
    for item in request:
        myString = [];
        for value in item:
            myString.append( str( value ) );
        myObject[ myString[ 0 ] ] = myString[ 1 ];

    myColumns = [];
    myValues  = [];
    for prop in myObject :
        myColumns.append( "\"" + prop + "\"" );
        myValues.append( myObject[ prop ] );

    myQuery = "INSERT INTO {mySchema_param}.\"" + entity + "\" ";
    myQuery += "(" + " , ".join( myColumns ) + ")";
    myQuery += " VALUES ";
    myQuery += "(" + " , ".join( myValues ) + ") RETURNING ID;";

    qData    = sql.SQL( myQuery ).format( 
                   mySchema_param = sql.Identifier( mySchema )
               );

    result = self.executeQuery( qData , None , "insert" );
    if( "error" in result ):
        return { "error" : result[ "error" ] };

    return result;

 async def getTableData( self , tableName , SearchFilter = None , operator = None ):
    mySchema = self.cfg[ "database" ][ "schema" ];
    
    # print( "--------------------------------------------------" );
    # print( tableName );
    
    if SearchFilter is not None : 
        myQuery  = ( 
                    "select * from {mySchema_param}.{myTableName_param} " + 
                    "where " + str( SearchFilter[ "column" ] ) + " = '" + str( SearchFilter[ "value" ] ) + "' " + 
                    "order by id asc;"
                   );

        if operator is not None : 
            if operator == "in" : 
                myQuery  = ( 
                            "select * from {mySchema_param}.{myTableName_param} " + 
                            "where " + str( SearchFilter[ "column" ] ) + " in ( " + str( SearchFilter[ "value" ] ) + " ) " + 
                            "order by id asc;"
                           );
    else:
        myQuery  = "select * from {mySchema_param}.{myTableName_param} order by id asc;";

    qData    = sql.SQL( myQuery ).format( 
                   mySchema_param    = sql.Identifier( mySchema ),
                   myTableName_param = sql.Identifier( tableName )
               );

    result = self.executeQuery( qData , None , "select" );
    if( "error" in result ):
        return { "error" : result[ "error" ] };

    return result;
 
 async def getWholeDataset( self , cultivationType , dat_name , user_id , userdata_entity ):
    dataSet = await self.getTableData( cultivationType , { "column" : "dat_name" , "value" : dat_name } );
    if( len( dataSet ) <= 0 ) : 
        return { "error" : "Resource not found. Unknown DAT" , "status_code" : 401 };

    # Retrieve the User Data from the Database
    myUserDataObject = {};
    myUserData       = {};
    myResult = await self.getEntityByUserId( entity = userdata_entity , user_id = [ str( user_id ) ] );
    if len( myResult ) <= 0 : 
        return { "error" : "Resource not found. User ID has no records" , "status_code" : 401 };

    # Update the database record of the "Default" values with the , "User Provided Values" , Database Record 
    print( "[ CREATION ] : Creating DataObject with Updated Values from the User Provided DataSet" );
    for item in dataSet[ 0 ]:
        if item in myResult[ 0 ] : 
            if myResult[ 0 ][ item ] is not None : 
                print( str( item ) + " : " + str( myResult[ 0 ][ item ] ) );
                dataSet[ 0 ][ item ] = myResult[ 0 ][ item ];

    for b in dataSet[ 0 ] : 
        print( str( b ) + " : " + str( dataSet[ 0 ][ b ] ) );

    return dataSet;

 def get_tree_from_object(self, data, keys):
     result = {}

     for item in data:
         current = result
         for i, key in enumerate(keys):
             key_val = item.get(key);
             # print( " >>>>>>>>>>> " + str( key_val ) );
             if key_val is None:
                 break

             # Create nested dict or final list
             if i == len( keys ) - 1:
                 current.setdefault(key_val, []).append(item["dat_name"])
             else:
                 current = current.setdefault(key_val, {})

     return result

 async def getCultivationDATTree( self , cultivation_type ):
     cultivationDataset = await self.getTableData( cultivation_type );
     myDATs  = [];
     for row in cultivationDataset : 
         myDATs.append( row[ "dat_name" ] );
     
     # print( JSON.dumps( myDATs , indent = 4 ) );

     cultivationDataset = await self.getTableData( "dat" , { "column" : "dat_name" , "value" : "'" + "','".join( myDATs ) + "'" } , operator = "in" );
     
     # for item in cultivationDataset:
         # if item[ "dat_category" ] == "Farm Management Information Systems (FMIS) and applications (inc. Decision Support Systems (DSS). Quality Management Systems (QMS))" :
             # print( JSON.dumps( {
                 # "dat_category" : item[ "dat_category" ] , 
                 # "purpose_for"  : item[ "purpose_for" ] , 
                 # "dat_name"     : item[ "dat_name" ] 
             # } ) );
     
     myDATTree     = self.get_tree_from_object( cultivationDataset, [ "dat_category", "purpose_for" ] );

     return myDATTree;