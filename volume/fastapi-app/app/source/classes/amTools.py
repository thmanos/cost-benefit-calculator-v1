import os;
import datetime;
import sys;
import json as JSON;
import decimal;
import hashlib;
from random import random;
from time import time;
import csv;
from io import StringIO;

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[91m'
    FAIL = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class SafeJSONEncoder(JSON.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (decimal.Decimal)):
            return float(obj)
        return super().default(obj);

class amTool:
    def __init__( self ):
        """Class for Misc Tools"""
        self.log( "Tools Initiated" );
        self.cfg = self.load( "./cfg/" , "config" );

    def log( self , myString , debug = True  , frameinfo = None ):
        if debug == True : 
            if frameinfo is not None :
                myLine = "[ Line : " + str( frameinfo.lineno ) + " ] ";
            else :
                myLine = "";
            
            myCurrentTime = datetime.datetime.now();
            print( "[" + datetime.datetime.strftime( myCurrentTime , "%Y-%m-%d %H:%M:%S" ) + "] : " + myLine + " " + str( myString ) , flush=True);

    def load( self , filePath , fileName , type = "json" ):
        """
        Loads Configuration from Disk
        """
        myCFG = dict();
        try:
            fileName = filePath + fileName + "." + type;
            if( os.path.exists( fileName ) == False ):
                self.log("[ amModel Error ] : File [" + fileName + "] Not Found");
                return False;

            f = open( fileName, "r" );
            if f.mode == "r":
                myContents = f.read();
                try:
                    if( type == "json" ):
                        myCFG = dict( JSON.loads( myContents ) );
                        self.log( "File ["+fileName+"] loaded." );
                    else:
                        myCFG = myContents;
                except:
                    self.log( "File ["+fileName+"] could not be loaded. Reason : ["+ str(sys.exc_info()[1]) +"]" );
            f.close();
            return myCFG;
        except:
            self.log( "Unexpected error upon loading Storage ["+fileName+"]:" + str( sys.exc_info()[1] ) );
            return False;

    def logFile( self , myString ) : 
        myCurrentTime = datetime.datetime.now();
        myPrefix = "[" + datetime.datetime.strftime( myCurrentTime , "%Y-%m-%d %H:%M:%S" ) + "] : ";

        fd = open( os.path.abspath( self.cfg["logs"]["path"]+"log.log" ) , "a+");
        fd.write( myPrefix + str( myString ) + "\n");
        fd.close();

    def log_curl( self , method , postData , endpoint , file=False , auth=False ):
        myMethod      = "";
        myAuth        = "";
        myContentType = "Content-type: application/json";
        myEndpoint    = endpoint;

        if( method     == "post" ):   myMethod = "-XPOST";
        elif( method   == "get" ):    myMethod = "-XGET";
        elif( method   == "delete" ): myMethod = "-XDELETE";
        elif( method   == "put" ):    myMethod = "-XPUT";
        else: myMethod =  "XGET";

        if( auth is not False ): myAuth = auth;

        if( file == False ):
            myPostData  = JSON.dumps( postData ).replace( "'", "\\\"" ).replace( "\"", "\\\"" );
            myLogString = f"curl {myMethod} -u {myAuth} -H \"{myContentType}\" -d \"{myPostData}\" \"{myEndpoint}\" ";
        else:
            myFileName  = file["name"];
            myFilePath  = file["path"];
            myLogString = f"curl -u {myAuth} -F name=\"{myFileName}\" -F filedata=@{myFilePath}\" \"{myEndpoint}\" ";

        print();
        print( " [ CURL ] " )
        print( myLogString );
        print();
        return myLogString;

    def getUID( self ):
        randomHash      = random();
        currentDate     = datetime.datetime.now();
        currentTS       = round( currentDate.timestamp() );
        myStringHash    = str( currentTS ) + str( randomHash );
        return hashlib.sha256( myStringHash.encode() ).hexdigest();

    def isValidJSON( self , json ):
        try:
            myJSON = JSON.loads( json );
        except ValueError as error :
            return False;
        return True;

    def isInt( self , value ):
        try:
            isValueInt = int( value );
            return True;
        except( Exception ) as error:
            return False;

    def createFile( self , fileName , myString ) : 
        myCurrentTime = datetime.datetime.now();
        myPrefix = "[" + datetime.datetime.strftime( myCurrentTime , "%Y-%m-%d %H:%M:%S" ) + "] : ";

        fd = open( os.path.abspath( self.cfg["logs"]["path"] + datetime.datetime.strftime( myCurrentTime , "%Y_%m_%d_%H_%M_%S" ) + "_" + fileName + ".log" ) , "a+");
        fd.write( myPrefix + str( myString ) + "\n");
        fd.close();

    def parseCSV( self , filedata , toObject = False ):

        myFileData        = filedata.file.read();
        myDecodedFileData = myFileData.decode('cp1252');
        myCurrentTime     = datetime.datetime.now();
        
        filePath = self.cfg[ "uploads" ][ "tmp" ][ "path" ] + datetime.datetime.strftime( myCurrentTime , "%Y_%m_%d_%H_%M_%S" ) + "_log.log";
        fd       = open( os.path.abspath( filePath ) , "w");
        fd.write( myDecodedFileData );
        fd.close();

        myArrayResponse   = [];

        with open( os.path.abspath( filePath ) , newline='') as csvfile:
            myDecodedFileData = csv.reader(csvfile, delimiter=';', quotechar='|')
            for rowindex , row in enumerate( myDecodedFileData ) : 
                print( row );
                myArrayResponse.append( row );

        if toObject is True : 
            myObjectArray = [];

            for index , row in enumerate( myArrayResponse ):
                if index == 0 :
                    continue;

                myTempArray = {};
                for value_index , value in enumerate( row ) : 
                    myProperty = ( myArrayResponse[ 0 ][ value_index ].lower()
                                        .replace( "/" , "" )
                                        .replace( ")" , "" )
                                        .replace( "(" , "" )
                                        .replace( ":" , "" )
                                        .replace( "?" , "" )
                                        .replace( "%" , "" )
                                        .replace( "€" , "" )
                                        .replace( "." , "" )
                                        .strip()
                                        .replace( " " , "_" )
                                        .replace( "__" , "" )
                    );

                    if( myProperty == "id" ) : 
                        continue;

                    sanitizedValue = ( 
                    value
                        .replace( "," , "." ) 
                        .replace( "'" , "" ) 
                        .replace( "?" , "" ) 
                        .replace( "#" , "" ) 
                        .replace( "/" , "" ) 
                        .replace( "!" , "" ) 
                        .replace( "%" , "" ) 
                        .replace( "@" , "" ) 
                        .replace( "\r\n" , " " )
                        .replace( "\n" , " " )
                        .replace( "\r" , " " )
                    );

                    if sanitizedValue == "" : 
                        myTempArray[ myProperty ] = 0;
                    else:
                        myTempArray[ myProperty ] = sanitizedValue;

                myObjectArray.append( myTempArray );

            return myObjectArray;
        else:
            return myArrayResponse;

    def parseCSVFile( self , filePath , toObject = False ):
        myArrayResponse   = [];

        with open( os.path.abspath( filePath ) , newline='' , encoding='cp1252') as csvfile:
            myDecodedFileData = csv.reader(csvfile, delimiter=';', quotechar='|' );
            for rowindex , row in enumerate( myDecodedFileData ) : 
                print( str( rowindex ) + " : " + JSON.dumps( row ) );
                myArrayResponse.append( row );

        if toObject is True : 
            myObjectArray = [];

            for index , row in enumerate( myArrayResponse ):
                if index == 0 :
                    continue;

                myTempArray = {};
                for value_index , value in enumerate( row ) : 
                    myProperty = ( myArrayResponse[ 0 ][ value_index ].lower()
                                        .replace( "/" , "" )
                                        .replace( ")" , "" )
                                        .replace( "(" , "" )
                                        .replace( ":" , "" )
                                        .replace( "?" , "" )
                                        .replace( "%" , "" )
                                        .replace( "€" , "" )
                                        .replace( "." , "" )
                                        .strip()
                                        .replace( " " , "_" )
                                        .replace( "__" , "" )
                    );

                    if( myProperty == "id" ) : 
                        continue;

                    sanitizedValue = ( 
                    value
                        .replace( "#?????/0!" , "" ) 
                        .replace( "'" , "" ) 
                        .replace( "'X30'" , "" ) 
                        .replace( "," , "." ) 
                        .replace( "\r\n" , " " )
                        .replace( "\n" , " " )
                        .replace( "\r" , " " )
                        .replace( "%" , "" )
                        .replace( "!" , "" ) 
                    );

                    if sanitizedValue == "" : 
                        myTempArray[ myProperty ] = 0;
                    else:
                        myTempArray[ myProperty ] = sanitizedValue;

                print( myTempArray );
                myObjectArray.append( myTempArray );

            return myObjectArray;
        else:
            return myArrayResponse;

    def __parseCSV( self , filedata , toObject = False ):

     myFileData = filedata.file.read();
     myDecodedFileData = myFileData.decode('cp1252');
     myCurrentTime = datetime.datetime.now();
     
     filePath = self.cfg["uploads"]["tmp"]["path"] + datetime.datetime.strftime( myCurrentTime , "%Y_%m_%d_%H_%M_%S" ) + "_log.log";
     fd = open( os.path.abspath( filePath ) , "w");
     fd.write( myDecodedFileData );
     fd.close();

     with open( os.path.abspath( filePath ) , newline='') as csvfile:
         spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
         for row in spamreader:
             print( row )

     return;


     myFileData        = filedata.file.read();
     myDecodedFileData = myFileData.decode('cp1252').split( "\r\n" );
     myArrayResponse   = [];

     for rowindex , row in enumerate( myDecodedFileData ) : 
         if rowindex == 0 :
             mySanitizedHeaders = ( row.lower()
                                      .replace( " " , "_" )
                                      .replace( "/" , "" )
                                      .replace( ")" , "" )
                                      .replace( "(" , "" )
                                      .replace( ":" , "" )
                                      .replace( "?" , "" )
                                      .replace( "%" , "" )
                                      .replace( "€" , "" )
                                      .replace( "." , "" )
                                      .replace( "__" , "" )
                                      .replace( "_;" , ";" )
                                      .replace( "\r\n" , " " )
                                      .replace( "\n" , " " )
                                      .replace( "\r" , " " )
                                 );
             myArrayResponse.append( mySanitizedHeaders.split( ";" ) );
         else:
             myArrayResponse.append( row.split( ";" ) );

     if toObject is True : 
         myObjectArray = [];

         for index , row in enumerate( myArrayResponse ):
             if index == 0 :
                 continue;

             myTempArray = {};
             for value_index , value in enumerate( row ) : 
                 myProperty = myArrayResponse[ 0 ][ value_index ];

                 if( myProperty == "id" ) : 
                     continue;

                 sanitizedValue = ( 
                   value
                     .replace( "," , "." ) 
                     .replace( "'" , "" ) 
                     .replace( "?" , "" ) 
                     .replace( "#" , "" ) 
                     .replace( "/" , "" ) 
                     .replace( "!" , "" ) 
                     .replace( "%" , "" ) 
                     .replace( "@" , "" ) 
                     .replace( "\r\n" , " " )
                     .replace( "\n" , " " )
                     .replace( "\r" , " " )
                 );

                 if sanitizedValue == "" : 
                     myTempArray[ myProperty ] = 0;
                 else:
                     myTempArray[ myProperty ] = sanitizedValue;

             myObjectArray.append( myTempArray );

         return myObjectArray;
     else:
         return myArrayResponse;

    def json_dump( self , data ):
        print( JSON.dumps(data, indent=4, cls=SafeJSONEncoder) );