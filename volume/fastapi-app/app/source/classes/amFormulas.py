import re;
import csv;
import json as JSON;
from classes.amTools import amTool;

class amFormulas:
 def __init__( self , cfg ):
  """Class for Parsing Formulas"""
  self.amTool = amTool();
  self.amTool.log( "Formulas Initiated" );
  self.cfg    = cfg;
  self.debug  = False;

 def getTranslation( self , source , target ):
     found = "";
     # print( "Translation for : " + str( source ) );
     for item in target : 
         if found != "" : 
             continue;

         # print( str( item[ 0 ] ) + " | " + str( source ) );
         if int( item[ 0 ] ) == int( source ): 
             found = str( item[ 1 ] );
     
     if source.isnumeric() and found == "" : 
         return source;
     else:
         return found;

 def getVocabularyFromFormulas( self , myInputsSchema , myFormulasList ):
     myVocabulary = [];

     for formula in myFormulasList : 
         # print( ">>>> Formula <<<<" );
         # print( formula );

         myNewFormula = formula.replace( "$" , "" ).replace( "INPUT!" , "" ).replace( "D" , "" ).replace( "E" , "" );
         # print( myNewFormula );

         myNumbers    = re.findall( r'\d+', myNewFormula );
         newNumbers   = [];
         for i in myNumbers: 
             myNormalizedNumber = str( i ) if ( int( i ) >= 10 ) else ( "0" + str( i ) );
             newNumbers.append( myNormalizedNumber );

         # print( ">>>> Split into Numbers " );
         # print( newNumbers );

         for num in newNumbers:
             # myNormalizedNumber = int( num ) if ( int( num ) >= 10 ) else ( "0" + str( num ) );
             for item in myInputsSchema[ "inputs" ][ "ContextEntity" ] : 
                 if item[ "posY" ] == num : 
                     myVocabulary.append( [ num , item[ "name" ] ] );
             for item in myInputsSchema[ "inputs" ][ "VolumeEntity" ] : 
                 if item[ "posY" ] == num : 
                     myVocabulary.append( [ num , item[ "name" ] ] );
             for item in myInputsSchema[ "inputs" ][ "TimeEntity" ] : 
                 if item[ "posY" ] == num : 
                     myVocabulary.append( [ num , item[ "name" ] ] );
             for item in myInputsSchema[ "inputs" ][ "PriceEntity" ] : 
                 if item[ "posY" ] == num : 
                     myVocabulary.append( [ num , item[ "name" ] ] );

         # print( ">>>> Derived Vocabulary  " );
         # print( myVocabulary );

     print( );
     print( ">>>> Vocabulary <<<<" );
     for vocItem in myVocabulary : 
         print( vocItem );
     print( );

     return myVocabulary;

 def getSplittedFormula( self , myList ):
     myFormulaSplit     = [];
     myChars            = "";
     myDigits           = "";

     # Split our Formula into an Array that differentiates the integer part of the formula from the rest
     for index , char in enumerate( myList ): 
         if char.isnumeric() == False : 
             if myDigits != "" : 
                 myFormulaSplit.append( myDigits );
                 myDigits = "";

             myChars += char;
         else:
             if myChars != "" : 
                 myFormulaSplit.append( myChars );
                 myChars = "";

             myDigits += char;
         
         if index == ( len( myList ) - 1 ) : 
              if myDigits != "" : 
                  myFormulaSplit.append( myDigits );
              else:
                  myFormulaSplit.append( myChars );

     return myFormulaSplit;

 def substitutePlaceholdersInFormula( self , myFormulaSplit , myVocabulary ):
     myTempRes = [];
     for index , char in enumerate( myFormulaSplit ): 
         if char.isnumeric() == False : 
             myTempRes.append( char );
         else:
             myTempRes.append( self.getTranslation( char , myVocabulary ) );

     myStringFormula = " ".join( myTempRes );
     return myStringFormula;



