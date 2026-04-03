import time;
import datetime;
from datetime import timedelta;
from typing import Optional , List;
from enum import Enum;
from pydantic import BaseModel , Field , create_model;

class investment_put( BaseModel ):
    dat_name                           : str               = Field( None , description = "DAT Name" );
    years_of_usage                     : float             = Field( None , description = "YEARS OF USAGE" );
    number_of_units_sensors_etc        : float             = Field( None , description = "Number of Units (sensors etc.)" );
    total_area_ha                      : float             = Field( None , description = "Total Area (ha)" );

class yield_put( BaseModel ):
    dat_name                           : str               = Field( None , description = "DAT Name" );
    current_yield_tonsha               : Optional[ float ] = Field( None , description = "Current Yield (tons/ha)" );
    market_price1ton                   : Optional[ float ] = Field( None , description = "Market Price (€/ 1ton)" );
    total_area_ha                      : float             = Field( None , description = "Total Area (ha)" );

class fertilizer_reduction_put( BaseModel ):
    dat_name                           : str               = Field( None , description = "DAT Name" );
    current_fertilizer_usage_kg_ha     : Optional[ float ] = Field( None , description = "Current fertilizer usage (Kg/ ha)" );
    current_fertilizer_cost1_kg        : Optional[ float ] = Field( None , description = "Current Fertilizer Cost (€/ 1 Kg)" );
    total_area_ha                      : float             = Field( None , description = "Total Area (ha)" );

class water_reduction_put( BaseModel ):
    dat_name                           : str               = Field( None , description = "DAT Name" );
    current_water_usage_m3ha           : Optional[ float ] = Field( None , description = "Current water usage (m3/ha)" );
    current_water_costm3               : Optional[ float ] = Field( None , description = "Current water cost (€/ m3)" );
    total_area_ha                      : float             = Field( None , description = "Total Area (ha)" );

class pesticide_reduction_put( BaseModel ):
    dat_name                           : str               = Field( None , description = "DAT Name" );
    current_pestcide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Current pestcide usage (kg or lt/ ha)" );
    current_pesticide_costkg_or_lt     : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ kg or lt)" );

class labor_reduction_put( BaseModel ):
    dat_name                           : str               = Field( None , description = "DAT Name" );
    current_labor_costin_1_year        : Optional[ float ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );

class fuel_reduction_put( BaseModel ):
    dat_name                           : str               = Field( None , description = "DAT Name" );
    current_fuel_costin_1_year         : Optional[ float ] = Field( None , description = "Current Fuel Cost (€ in 1 year)" );