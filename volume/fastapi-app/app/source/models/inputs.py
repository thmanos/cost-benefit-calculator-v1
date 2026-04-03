import time;
import datetime;
from datetime import timedelta;
from typing import Optional , List;
from enum import Enum;
from pydantic import BaseModel , Field , create_model;

class get_userdata_generic( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_userdata_generic_livestock( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_dat( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );
				type : Optional[ str ] = Field( None , description = "Type" );
				dat_category : Optional[ str ] = Field( None , description = "DAT category" );
				platform : Optional[ str ] = Field( None , description = "Platform " );
				purpose_for : Optional[ str ] = Field( None , description = "Purpose (For:)" );
				dat_name : Optional[ str ] = Field( None , description = "DAT name" );


class get_arable( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_fruits( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_vineyards( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_vegetables( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_orchards( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_cattle( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_pigs( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_poultry( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class get_small_ruminants( BaseModel ):
				id     : Optional[ str ] = Field( None , description = "" );
				limit  : Optional[ int ] = Field( None , description = "" );
				offset : Optional[ int ] = Field( None , description = "" );


class userdata_generic( BaseModel ):
				years_of_usage : Optional[ float ] = Field( None , description = "YEARS OF USAGE" );
				total_area_ha : Optional[ float ] = Field( None , description = "Total Area (ha)" );
				number_of_units_sensors_etc : Optional[ float ] = Field( None , description = "Number of Units (sensors etc.)" );
				current_yield_tonsha : Optional[ float ] = Field( None , description = "Current Yield (tons/ha)" );
				market_price1ton : Optional[ float ] = Field( None , description = "Market Price (€/ 1ton)" );
				current_fertilizer_usage_kg_ha : Optional[ float ] = Field( None , description = "Current fertilizer usage (Kg/ ha)" );
				current_fertilizer_cost1_kg : Optional[ float ] = Field( None , description = "Current Fertilizer Cost (€/ 1 Kg)" );
				current_water_usage_m3ha : Optional[ float ] = Field( None , description = "Current water usage (m3/ha)" );
				current_water_costm3 : Optional[ float ] = Field( None , description = "Current water cost (€/ m3)" );
				current_pestcide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Current pestcide usage (kg or lt/ ha)" );
				current_pesticide_costkg_or_lt : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ kg or lt)" );
				current_labor_costin_1_year : Optional[ float ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				current_fuel_costin_1_year : Optional[ float ] = Field( None , description = "Current Fuel Cost (€ in 1 year)" );
				user_id : Optional[ str ] = Field( None , description = "User ID" );


class userdata_generic_livestock( BaseModel ):
				number_of_animals : Optional[ float ] = Field( None , description = "Number of cows" );
				years_of_usage : Optional[ float ] = Field( None , description = "YEARS OF USAGE" );
				number_of_units_sensors_etc : Optional[ float ] = Field( None , description = "Number of Units (sensors etc.)" );
				average_milk_price_per_literliter : Optional[ float ] = Field( None , description = "Average milk price per liter (€/ liter)" );
				average_liters_of_milk_produced_per_cow_per_day_l : Optional[ float ] = Field( None , description = "Average liters of milk produced per cow per day (l)" );
				current_labor_costin_1_year : Optional[ float ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				current_energy_consumptionin_kwh : Optional[ float ] = Field( None , description = "Current Energy Consumption  (in kWh)" );
				cost_of_energy_per_kwh : Optional[ float ] = Field( None , description = "Cost of Energy per kWh (€)" );
				current_water_costin_1_year : Optional[ float ] = Field( None , description = "Current Water Cost (€ in 1 year)" );
				current_feed_costin_1_year : Optional[ float ] = Field( None , description = "Current Feed Cost (€ in 1 year)" );
				current_feed_waste_costin_1_year : Optional[ float ] = Field( None , description = "Current Feed Waste Cost (€ in 1 year)" );
				current_antibiotics_costin_1_year : Optional[ float ] = Field( None , description = "Current Antibiotics Cost (€ in 1 year)" );
				current_mortality_costin_1_year : Optional[ float ] = Field( None , description = "Current Mortality Cost (€ in 1 year)" );
				current_profitabilityin_1_year : Optional[ float ] = Field( None , description = "Current Profitability (€ in 1 year)" );
				user_id : Optional[ str ] = Field( None , description = "User ID" );


class dat( BaseModel ):
				type : Optional[ str ] = Field( None , description = "Type" );
				dat_category : Optional[ str ] = Field( None , description = "DAT category" );
				platform : Optional[ str ] = Field( None , description = "Platform " );
				purpose_for : Optional[ str ] = Field( None , description = "Purpose (For:)" );
				dat_name : Optional[ str ] = Field( None , description = "DAT name" );
				dat_provider_name : Optional[ str ] = Field( None , description = "DAT provider name" );
				dat_provider_website : Optional[ str ] = Field( None , description = "DAT provider website" );
				dat_short_description : Optional[ str ] = Field( None , description = "DAT short Description" );
				platform_link : Optional[ str ] = Field( None , description = "Link from Platform " );
				crop_type : Optional[ str ] = Field( None , description = "Crop type" );
				cost_info : Optional[ str ] = Field( None , description = "COST INFO" );


class arable( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT name" );
				years_of_usage : Optional[ float ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ float ] = Field( None , description = "Initial cost of Investment (€)" );
				subscription_cost_for_1ha : Optional[ float ] = Field( None , description = "Subscription Cost for 1ha (€)" );
				monthly_subscription_cost : Optional[ float ] = Field( None , description = "Monthly Subscription Cost (€)" );
				annual_subscription_cost : Optional[ float ] = Field( None , description = "Annual Subscription Cost (€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs_year : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ float ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ float ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				total_area_ha : Optional[ float ] = Field( None , description = "Total Area (ha)" );
				yield_increase : Optional[ float ] = Field( None , description = "Yield increase (%)" );
				current_yield_tonsha : Optional[ float ] = Field( None , description = "Current Yield (tons/ha)" );
				market_price1ton : Optional[ float ] = Field( None , description = "Market Price (€/ 1ton)" );
				current_revenuein_1_year : Optional[ float ] = Field( None , description = "Current Revenue (€ in 1 year)" );
				increased_yield_tonsha : Optional[ float ] = Field( None , description = "Increased Yield (tons/ha)" );
				price_of_increased_yieldha : Optional[ float ] = Field( None , description = "Price of Increased Yield (€/ ha)" );
				increased_revenuein_1_year : Optional[ float ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				fertilization_saving : Optional[ float ] = Field( None , description = "Fertilization saving (%)" );
				current_fertilizer_usage_kg_ha : Optional[ float ] = Field( None , description = "Current fertilizer usage (Kg/ ha)" );
				current_fertilizer_cost1_kg : Optional[ float ] = Field( None , description = "Current Fertilizer Cost (€/ 1 Kg)" );
				current_fertilization_costha : Optional[ float ] = Field( None , description = "Current Fertilization Cost (€/ ha)" );
				reduced_fertilizer_usage_kgha : Optional[ float ] = Field( None , description = "Reduced Fertilizer usage (kg/ha)" );
				fertilizer_cost_savingsha : Optional[ float ] = Field( None , description = "Fertilizer cost savings (€/ ha)" );
				fertilization_cost_savingin_1_year : Optional[ float ] = Field( None , description = "Fertilization cost saving (€ in 1 year)" );
				water_saving : Optional[ float ] = Field( None , description = "Water saving (%)" );
				current_water_usage_m3ha : Optional[ float ] = Field( None , description = "Current water usage (m3/ha)" );
				current_water_costm3 : Optional[ float ] = Field( None , description = "Current water cost (€/ m3)" );
				current_irrigation_costha : Optional[ float ] = Field( None , description = "Current Irrigation Cost (€/ ha)" );
				reduced_water_usage_m3ha : Optional[ float ] = Field( None , description = "Reduced water usage (m3/ha)" );
				water_cost_savings_ha : Optional[ float ] = Field( None , description = "Water cost savings  (€/ ha)" );
				water_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Water cost savings  (€ in 1 year)" );
				pesticide_saving : Optional[ float ] = Field( None , description = "Pesticide saving (%)" );
				current_pestcide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Current pestcide usage (kg or lt/ ha)" );
				current_pesticide_costkg_or_lt : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ kg or lt)" );
				current_pesticide_costha : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ ha)" );
				reduced_pesticide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Reduced pesticide usage (kg or lt /ha)" );
				pesticide_cost_savingha : Optional[ float ] = Field( None , description = "Pesticide cost saving (€/ ha)" );
				pesticide_cost_savingsin_1_year : Optional[ float ] = Field( None , description = "Pesticide cost savings (€ in 1 year)" );
				labor_saving : Optional[ float ] = Field( None , description = "Labor saving (%)" );
				current_labor_costin_1_year : Optional[ float ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				labor_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Labor cost savings  (€ in 1 year)" );
				fuel_saving : Optional[ float ] = Field( None , description = "Fuel Saving (%)" );
				current_fuel_costin_1_year : Optional[ float ] = Field( None , description = "Current Fuel Cost (€ in 1 year)" );
				fuel_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Fuel cost savings  (€ in 1 year)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


class fruits( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT name" );
				years_of_usage : Optional[ float ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ float ] = Field( None , description = "Initial cost of Investment (€)" );
				subscription_cost_for_1ha : Optional[ float ] = Field( None , description = "Subscription Cost for 1ha (€)" );
				monthly_subscription_cost : Optional[ float ] = Field( None , description = "Monthly Subscription Cost (€)" );
				annual_subscription_cost : Optional[ float ] = Field( None , description = "Annual Subscription Cost (€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs_year : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ float ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ float ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				total_area_ha : Optional[ float ] = Field( None , description = "Total Area (ha)" );
				yield_increase : Optional[ float ] = Field( None , description = "Yield increase (%)" );
				current_yield_tonsha : Optional[ float ] = Field( None , description = "Current Yield (tons/ha)" );
				market_price1ton : Optional[ float ] = Field( None , description = "Market Price (€/ 1ton)" );
				current_revenuein_1_year : Optional[ float ] = Field( None , description = "Current Revenue (€ in 1 year)" );
				increased_yield_tonsha : Optional[ float ] = Field( None , description = "Increased Yield (tons/ha)" );
				price_of_increased_yieldha : Optional[ float ] = Field( None , description = "Price of Increased Yield (€/ ha)" );
				increased_revenuein_1_year : Optional[ float ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				fertilization_saving : Optional[ float ] = Field( None , description = "Fertilization saving (%)" );
				current_fertilizer_usage_kg_ha : Optional[ float ] = Field( None , description = "Current fertilizer usage (Kg/ ha)" );
				current_fertilizer_cost1_kg : Optional[ float ] = Field( None , description = "Current Fertilizer Cost (€/ 1 Kg)" );
				current_fertilization_costha : Optional[ float ] = Field( None , description = "Current Fertilization Cost (€/ ha)" );
				reduced_fertilizer_usage_kgha : Optional[ float ] = Field( None , description = "Reduced Fertilizer usage (kg/ha)" );
				fertilizer_cost_savingsha : Optional[ float ] = Field( None , description = "Fertilizer cost savings (€/ ha)" );
				fertilization_cost_savingin_1_year : Optional[ float ] = Field( None , description = "Fertilization cost saving (€ in 1 year)" );
				water_saving : Optional[ float ] = Field( None , description = "Water saving (%)" );
				current_water_usage_m3ha : Optional[ float ] = Field( None , description = "Current water usage (m3/ha)" );
				current_water_costm3 : Optional[ float ] = Field( None , description = "Current water cost (€/ m3)" );
				current_irrigation_costha : Optional[ float ] = Field( None , description = "Current Irrigation Cost (€/ ha)" );
				reduced_water_usage_m3ha : Optional[ float ] = Field( None , description = "Reduced water usage (m3/ha)" );
				water_cost_savings_ha : Optional[ float ] = Field( None , description = "Water cost savings  (€/ ha)" );
				water_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Water cost savings  (€ in 1 year)" );
				pesticide_saving : Optional[ float ] = Field( None , description = "Pesticide saving (%)" );
				current_pesticide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Current pesticide usage (kg or lt/ ha)" );
				current_pesticide_costkg_or_lt : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ kg or lt)" );
				current_pesticide_costha : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ ha)" );
				reduced_pesticide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Reduced pesticide usage (kg or lt /ha)" );
				pesticide_cost_savingha : Optional[ float ] = Field( None , description = "Pesticide cost saving (€/ ha)" );
				pesticide_cost_savingsin_1_year : Optional[ float ] = Field( None , description = "Pesticide cost savings (€ in 1 year)" );
				labor_saving : Optional[ float ] = Field( None , description = "Labor saving (%)" );
				current_labor_costin_1_year : Optional[ float ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				labor_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Labor cost savings  (€ in 1 year)" );
				fuel_saving : Optional[ float ] = Field( None , description = "Fuel Saving (%)" );
				current_fuel_costin_1_year : Optional[ float ] = Field( None , description = "Current Fuel Cost (€ in 1 year)" );
				fuel_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Fuel cost savings  (€ in 1 year)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


class vineyards( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT name" );
				years_of_usage : Optional[ float ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ float ] = Field( None , description = "Initial cost of Investment (€)" );
				subscription_cost_for_1ha : Optional[ float ] = Field( None , description = "Subscription Cost for 1ha (€)" );
				monthly_subscription_cost : Optional[ float ] = Field( None , description = "Monthly Subscription Cost (€)" );
				annual_subscription_cost : Optional[ float ] = Field( None , description = "Annual Subscription Cost (€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs_year : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ float ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ float ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				total_area_ha : Optional[ float ] = Field( None , description = "Total Area (ha)" );
				yield_increase : Optional[ float ] = Field( None , description = "Yield increase (%)" );
				current_yield_tonsha : Optional[ float ] = Field( None , description = "Current Yield (tons/ha)" );
				market_price1ton : Optional[ float ] = Field( None , description = "Market Price (€/ 1ton)" );
				current_revenuein_1_year : Optional[ float ] = Field( None , description = "Current Revenue (€ in 1 year)" );
				increased_yield_tonsha : Optional[ float ] = Field( None , description = "Increased Yield (tons/ha)" );
				price_of_increased_yieldha : Optional[ float ] = Field( None , description = "Price of Increased Yield (€/ ha)" );
				increased_revenuein_1_year : Optional[ float ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				fertilization_saving : Optional[ float ] = Field( None , description = "Fertilization saving (%)" );
				current_fertilizer_usage_kg_ha : Optional[ float ] = Field( None , description = "Current fertilizer usage (Kg/ ha)" );
				current_fertilizer_cost1_kg : Optional[ float ] = Field( None , description = "Current Fertilizer Cost (€/ 1 Kg)" );
				current_fertilization_costha : Optional[ float ] = Field( None , description = "Current Fertilization Cost (€/ ha)" );
				reduced_fertilizer_usage_kgha : Optional[ float ] = Field( None , description = "Reduced Fertilizer usage (kg/ha)" );
				fertilizer_cost_savingsha : Optional[ float ] = Field( None , description = "Fertilizer cost savings (€/ ha)" );
				fertilization_cost_savingin_1_year : Optional[ float ] = Field( None , description = "Fertilization cost saving (€ in 1 year)" );
				water_saving : Optional[ float ] = Field( None , description = "Water saving (%)" );
				current_water_usage_m3ha : Optional[ float ] = Field( None , description = "Current water usage (m3/ha)" );
				current_water_costm3 : Optional[ float ] = Field( None , description = "Current water cost (€/ m3)" );
				current_irrigation_costha : Optional[ float ] = Field( None , description = "Current Irrigation Cost (€/ ha)" );
				reduced_water_usage_m3ha : Optional[ float ] = Field( None , description = "Reduced water usage (m3/ha)" );
				water_cost_savings_ha : Optional[ float ] = Field( None , description = "Water cost savings  (€/ ha)" );
				water_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Water cost savings  (€ in 1 year)" );
				pesticide_saving : Optional[ float ] = Field( None , description = "Pesticide saving (%)" );
				current_pestcide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Current pestcide usage (kg or lt/ ha)" );
				current_pesticide_costkg_or_lt : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ kg or lt)" );
				current_pesticide_costha : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ ha)" );
				reduced_pesticide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Reduced pesticide usage (kg or lt /ha)" );
				pesticide_cost_savingha : Optional[ float ] = Field( None , description = "Pesticide cost saving (€/ ha)" );
				pesticide_cost_savingsin_1_year : Optional[ float ] = Field( None , description = "Pesticide cost savings (€ in 1 year)" );
				labor_saving : Optional[ float ] = Field( None , description = "Labor saving (%)" );
				current_labor_costin_1_year : Optional[ float ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				labor_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Labor cost savings  (€ in 1 year)" );
				fuel_saving : Optional[ float ] = Field( None , description = "Fuel Saving (%)" );
				current_fuel_costin_1_year : Optional[ float ] = Field( None , description = "Current Fuel Cost (€ in 1 year)" );
				fuel_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Fuel cost savings  (€ in 1 year)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


class vegetables( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT name" );
				years_of_usage : Optional[ float ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ float ] = Field( None , description = "Initial cost of Investment (€)" );
				subscription_cost_for_1ha : Optional[ float ] = Field( None , description = "Subscription Cost for 1ha (€)" );
				monthly_subscription_cost : Optional[ float ] = Field( None , description = "Monthly Subscription Cost (€)" );
				annual_subscription_cost : Optional[ float ] = Field( None , description = "Annual Subscription Cost (€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs_year : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ float ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ float ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				total_area_ha : Optional[ float ] = Field( None , description = "Total Area (ha)" );
				yield_increase : Optional[ float ] = Field( None , description = "Yield increase (%)" );
				current_yield_tonsha : Optional[ float ] = Field( None , description = "Current Yield (tons/ha)" );
				market_price1ton : Optional[ float ] = Field( None , description = "Market Price (€/ 1ton)" );
				current_revenuein_1_year : Optional[ float ] = Field( None , description = "Current Revenue (€ in 1 year)" );
				increased_yield_tonsha : Optional[ float ] = Field( None , description = "Increased Yield (tons/ha)" );
				price_of_increased_yieldha : Optional[ float ] = Field( None , description = "Price of Increased Yield (€/ ha)" );
				increased_revenuein_1_year : Optional[ float ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				fertilization_saving : Optional[ float ] = Field( None , description = "Fertilization saving (%)" );
				current_fertilizer_usage_kg_ha : Optional[ float ] = Field( None , description = "Current fertilizer usage (Kg/ ha)" );
				current_fertilizer_cost1_kg : Optional[ float ] = Field( None , description = "Current Fertilizer Cost (€/ 1 Kg)" );
				current_fertilization_costha : Optional[ float ] = Field( None , description = "Current Fertilization Cost (€/ ha)" );
				reduced_fertilizer_usage_kgha : Optional[ float ] = Field( None , description = "Reduced Fertilizer usage (kg/ha)" );
				fertilizer_cost_savingsha : Optional[ float ] = Field( None , description = "Fertilizer cost savings (€/ ha)" );
				fertilization_cost_savingin_1_year : Optional[ float ] = Field( None , description = "Fertilization cost saving (€ in 1 year)" );
				water_saving : Optional[ float ] = Field( None , description = "Water saving (%)" );
				current_water_usage_m3ha : Optional[ float ] = Field( None , description = "Current water usage (m3/ha)" );
				current_water_costm3 : Optional[ float ] = Field( None , description = "Current water cost (€/ m3)" );
				current_irrigation_costha : Optional[ float ] = Field( None , description = "Current Irrigation Cost (€/ ha)" );
				reduced_water_usage_m3ha : Optional[ float ] = Field( None , description = "Reduced water usage (m3/ha)" );
				water_cost_savings_ha : Optional[ float ] = Field( None , description = "Water cost savings  (€/ ha)" );
				water_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Water cost savings  (€ in 1 year)" );
				pesticide_saving : Optional[ float ] = Field( None , description = "Pesticide saving (%)" );
				current_pestcide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Current pestcide usage (kg or lt/ ha)" );
				current_pesticide_costkg_or_lt : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ kg or lt)" );
				current_pesticide_costha : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ ha)" );
				reduced_pesticide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Reduced pesticide usage (kg or lt /ha)" );
				pesticide_cost_savingha : Optional[ float ] = Field( None , description = "Pesticide cost saving (€/ ha)" );
				pesticide_cost_savingsin_1_year : Optional[ float ] = Field( None , description = "Pesticide cost savings (€ in 1 year)" );
				labor_saving : Optional[ float ] = Field( None , description = "Labor saving (%)" );
				current_labor_costin_1_year : Optional[ float ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				labor_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Labor cost savings  (€ in 1 year)" );
				fuel_saving : Optional[ float ] = Field( None , description = "Fuel Saving (%)" );
				current_fuel_costin_1_year : Optional[ float ] = Field( None , description = "Current Fuel Cost (€ in 1 year)" );
				fuel_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Fuel cost savings  (€ in 1 year)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


class orchards( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT name" );
				years_of_usage : Optional[ float ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ float ] = Field( None , description = "Initial cost of Investment (€)" );
				subscription_cost_for_1ha : Optional[ float ] = Field( None , description = "Subscription Cost for 1ha (€)" );
				monthly_subscription_cost : Optional[ float ] = Field( None , description = "Monthly Subscription Cost (€)" );
				annual_subscription_cost : Optional[ float ] = Field( None , description = "Annual Subscription Cost (€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs_year : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ float ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ float ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				total_area_ha : Optional[ float ] = Field( None , description = "Total Area (ha)" );
				yield_increase : Optional[ float ] = Field( None , description = "Yield increase (%)" );
				current_yield_tonsha : Optional[ float ] = Field( None , description = "Current Yield (tons/ha)" );
				market_price1ton : Optional[ float ] = Field( None , description = "Market Price (€/ 1ton)" );
				current_revenuein_1_year : Optional[ float ] = Field( None , description = "Current Revenue (€ in 1 year)" );
				increased_yield_tonsha : Optional[ float ] = Field( None , description = "Increased Yield (tons/ha)" );
				price_of_increased_yieldha : Optional[ float ] = Field( None , description = "Price of Increased Yield (€/ ha)" );
				increased_revenuein_1_year : Optional[ float ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				fertilization_saving : Optional[ float ] = Field( None , description = "Fertilization saving (%)" );
				current_fertilizer_usage_kg_ha : Optional[ float ] = Field( None , description = "Current fertilizer usage (Kg/ ha)" );
				current_fertilizer_cost1_kg : Optional[ float ] = Field( None , description = "Current Fertilizer Cost (€/ 1 Kg)" );
				current_fertilization_costha : Optional[ float ] = Field( None , description = "Current Fertilization Cost (€/ ha)" );
				reduced_fertilizer_usage_kgha : Optional[ float ] = Field( None , description = "Reduced Fertilizer usage (kg/ha)" );
				fertilizer_cost_savingsha : Optional[ float ] = Field( None , description = "Fertilizer cost savings (€/ ha)" );
				fertilization_cost_savingin_1_year : Optional[ float ] = Field( None , description = "Fertilization cost saving (€ in 1 year)" );
				water_saving : Optional[ float ] = Field( None , description = "Water saving (%)" );
				current_water_usage_m3ha : Optional[ float ] = Field( None , description = "Current water usage (m3/ha)" );
				current_water_costm3 : Optional[ float ] = Field( None , description = "Current water cost (€/ m3)" );
				current_irrigation_costha : Optional[ float ] = Field( None , description = "Current Irrigation Cost (€/ ha)" );
				reduced_water_usage_m3ha : Optional[ float ] = Field( None , description = "Reduced water usage (m3/ha)" );
				water_cost_savings_ha : Optional[ float ] = Field( None , description = "Water cost savings  (€/ ha)" );
				water_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Water cost savings  (€ in 1 year)" );
				pesticide_saving : Optional[ float ] = Field( None , description = "Pesticide saving (%)" );
				current_pestcide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Current pestcide usage (kg or lt/ ha)" );
				current_pesticide_costkg_or_lt : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ kg or lt)" );
				current_pesticide_costha : Optional[ float ] = Field( None , description = "Current pesticide cost (€/ ha)" );
				reduced_pesticide_usage_kg_or_lt_ha : Optional[ float ] = Field( None , description = "Reduced pesticide usage (kg or lt /ha)" );
				pesticide_cost_savingha : Optional[ float ] = Field( None , description = "Pesticide cost saving (€/ ha)" );
				pesticide_cost_savingsin_1_year : Optional[ float ] = Field( None , description = "Pesticide cost savings (€ in 1 year)" );
				labor_saving : Optional[ float ] = Field( None , description = "Labor saving (%)" );
				current_labor_costin_1_year : Optional[ float ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				labor_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Labor cost savings  (€ in 1 year)" );
				fuel_saving : Optional[ float ] = Field( None , description = "Fuel Saving (%)" );
				current_fuel_costin_1_year : Optional[ float ] = Field( None , description = "Current Fuel Cost (€ in 1 year)" );
				fuel_cost_savings_in_1_year : Optional[ float ] = Field( None , description = "Fuel cost savings  (€ in 1 year)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


class cattle( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT Name" );
				number_of_animals : Optional[ int ] = Field( None , description = "Number of cows" );
				years_of_usage : Optional[ int ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ int ] = Field( None , description = "Initial cost of Investment (€)" );
				startup_fee_per_cow : Optional[ int ] = Field( None , description = "Startup Fee per Cow (€)" );
				monthly_cost_per_cow : Optional[ int ] = Field( None , description = "Monthly Cost per Cow (€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ int ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ int ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				milk_yield_increase : Optional[ int ] = Field( None , description = "Milk Yield Increase (%)" );
				average_milk_price_per_literliter : Optional[ int ] = Field( None , description = "Average milk price per liter (€/ liter)" );
				average_liters_of_milk_produced_per_cow_per_day_l : Optional[ int ] = Field( None , description = "Average liters of milk produced per cow per day (l)" );
				price_of_milk_yield_in_one_year : Optional[ int ] = Field( None , description = "Price of Milk Yield in one year (€)" );
				price_of_increased_milk_yield_in_one_year : Optional[ int ] = Field( None , description = "Price of Increased Milk Yield in one year (€)" );
				increased_revenuein_1_year : Optional[ int ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				labor_saving : Optional[ int ] = Field( None , description = "Labor saving (%)" );
				current_labor_costin_1_year : Optional[ int ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				labor_cost_savings_in_1_year : Optional[ int ] = Field( None , description = "Labor cost savings  (€ in 1 year)" );
				energy_saving : Optional[ int ] = Field( None , description = "Energy Saving(%)" );
				current_energy_consumptionin_kwh : Optional[ int ] = Field( None , description = "Current Energy Consumption  (in kWh)" );
				cost_of_energy_per_kwh : Optional[ int ] = Field( None , description = "Cost of Energy per kWh (€)" );
				currentcost_of_energyin_1_year : Optional[ int ] = Field( None , description = "Current  Cost of Energy (€ in 1 year)" );
				energy_cost_savingsin_1_year : Optional[ int ] = Field( None , description = "Energy Cost Savings (€ in 1 year)" );
				water_saving : Optional[ int ] = Field( None , description = "Water Saving (%)" );
				current_water_costin_1_year : Optional[ int ] = Field( None , description = "Current Water Cost (€ in 1 year)" );
				water_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Water Cost Saving (€ in 1 year)" );
				increase_profit_per_cow_per_year : Optional[ int ] = Field( None , description = "Increase Profit per Cow per Year (€)" );
				profit_per_cow_increase_in_1_year : Optional[ int ] = Field( None , description = "Profit per Cow Increase in 1 year (€)" );
				feed_saving : Optional[ int ] = Field( None , description = "Feed Saving (%)" );
				current_feed_costin_1_year : Optional[ int ] = Field( None , description = "Current Feed Cost (€ in 1 year)" );
				feed_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Feed Cost Saving (€ in 1 year)" );
				feed_waste_saving : Optional[ int ] = Field( None , description = "Feed Waste Saving (%)" );
				current_feed_waste_costin_1_year : Optional[ int ] = Field( None , description = "Current Feed Waste Cost (€ in 1 year)" );
				feed_waste_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Feed Waste Cost Saving (€ in 1 year)" );
				antibiotics_saving : Optional[ int ] = Field( None , description = "Antibiotics Saving (%)" );
				current_antibiotics_costin_1_year : Optional[ int ] = Field( None , description = "Current Antibiotics Cost (€ in 1 year)" );
				antibiotics_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Antibiotics Cost Saving (€ in 1 year)" );
				mortality_rate_decrease : Optional[ int ] = Field( None , description = "Mortality Rate Decrease (%)" );
				current_mortality_costin_1_year : Optional[ int ] = Field( None , description = "Current Mortality Cost (€ in 1 year)" );
				mortality_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Mortality Cost Saving (€ in 1 year)" );
				profitability_increase : Optional[ int ] = Field( None , description = "Profitability Increase (%)" );
				current_profitabilityin_1_year : Optional[ int ] = Field( None , description = "Current Profitability (€ in 1 year)" );
				profit_increase_in_1_year : Optional[ int ] = Field( None , description = "Profit Increase in 1 year (€)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


class pigs( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT Name" );
				number_of_animals : Optional[ int ] = Field( None , description = "Number of pigs" );
				years_of_usage : Optional[ int ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ int ] = Field( None , description = "Initial cost of Investment (€)" );
				startup_fee_per_pig : Optional[ int ] = Field( None , description = "Startup Fee per Pig(€)" );
				monthly_cost_per_pig : Optional[ int ] = Field( None , description = "Monthly Cost per Pig(€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ int ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ int ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				milk_yield_increase : Optional[ int ] = Field( None , description = "Milk Yield Increase (%)" );
				average_milk_price_per_literliter : Optional[ int ] = Field( None , description = "Average milk price per liter (€/ liter)" );
				average_liters_of_milk_produced_per_animal_per_day_l : Optional[ int ] = Field( None , description = "Average liters of milk produced per animal per day (l)" );
				price_of_milk_yield_in_one_year : Optional[ int ] = Field( None , description = "Price of Milk Yield in one year (€)" );
				price_of_increased_milk_yield_in_one_year : Optional[ int ] = Field( None , description = "Price of Increased Milk Yield in one year (€)" );
				increased_revenuein_1_year : Optional[ int ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				labor_saving : Optional[ int ] = Field( None , description = "Labor saving (%)" );
				current_labor_costin_1_year : Optional[ int ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				labor_cost_savings_in_1_year : Optional[ int ] = Field( None , description = "Labor cost savings  (€ in 1 year)" );
				energy_saving_in_lighting_systems : Optional[ int ] = Field( None , description = "Energy Saving in Lighting Systems (%)" );
				current_energy_cosumption_for_lighting_systems_in_kwh : Optional[ int ] = Field( None , description = "Current Energy Cosumption for Lighting Systems (in kWh)" );
				cost_of_energy_per_kwh : Optional[ int ] = Field( None , description = "Cost of energy per kWh (€)" );
				currentcost_of_energy_for_lighting_systemsin_1_year : Optional[ int ] = Field( None , description = "Current  Cost of Energy for Lighting Systems (€ in 1 year)" );
				energy_cost_savingsin_1_year : Optional[ int ] = Field( None , description = "Energy Cost Savings (€ in 1 year)" );
				water_saving : Optional[ int ] = Field( None , description = "Water Saving (%)" );
				current_water_costin_1_year : Optional[ int ] = Field( None , description = "Current Water Cost (€ in 1 year)" );
				water_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Water Cost Saving (€ in 1 year)" );
				icrease_profit_per_cow_per_year : Optional[ int ] = Field( None , description = "Icrease Profit per Cow per Year (€)" );
				profit_per_cow_increase_in_1_year : Optional[ int ] = Field( None , description = "Profit per Cow Increase in 1 year (€)" );
				feed_saving : Optional[ int ] = Field( None , description = "Feed Saving (%)" );
				current_feed_costin_1_year : Optional[ int ] = Field( None , description = "Current Feed Cost (€ in 1 year)" );
				feed_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Feed Cost Saving (€ in 1 year)" );
				feed_waste_saving : Optional[ int ] = Field( None , description = "Feed Waste Saving (%)" );
				current_feed_waste_costin_1_year : Optional[ int ] = Field( None , description = "Current Feed Waste Cost (€ in 1 year)" );
				feed_waste_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Feed Waste Cost Saving (€ in 1 year)" );
				antibiotics_saving : Optional[ int ] = Field( None , description = "Antibiotics Saving (%)" );
				current_antibiotics_costin_1_year : Optional[ int ] = Field( None , description = "Current Antibiotics Cost (€ in 1 year)" );
				antibiotics_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Antibiotics Cost Saving (€ in 1 year)" );
				mortality_rate_decrease : Optional[ int ] = Field( None , description = "Mortality Rate Decrease (%)" );
				current_mortality_costin_1_year : Optional[ int ] = Field( None , description = "Current Mortality Cost (€ in 1 year)" );
				mortality_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Mortality Cost Saving (€ in 1 year)" );
				profitability_increase : Optional[ int ] = Field( None , description = "Profitability Increase (%)" );
				current_profitabilityin_1_year : Optional[ int ] = Field( None , description = "Current Profitability (€ in 1 year)" );
				profit_increase_in_1_year : Optional[ int ] = Field( None , description = "Profit Increase in 1 year (€)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


class poultry( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT Name" );
				number_of_animals : Optional[ int ] = Field( None , description = "Number of birds" );
				years_of_usage : Optional[ int ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ int ] = Field( None , description = "Initial cost of Investment (€)" );
				startup_fee_per_bird : Optional[ int ] = Field( None , description = "Startup Fee per Bird (€)" );
				monthly_cost_per_bird : Optional[ int ] = Field( None , description = "Monthly Cost per Bird (€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ int ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ int ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				milk_yield_increase : Optional[ int ] = Field( None , description = "Milk Yield Increase (%)" );
				average_milk_price_per_literliter : Optional[ int ] = Field( None , description = "Average milk price per liter (€/ liter)" );
				average_liters_of_milk_produced_per_cow_per_day_l : Optional[ int ] = Field( None , description = "Average liters of milk produced per cow per day (l)" );
				price_of_milk_yield_in_one_year : Optional[ int ] = Field( None , description = "Price of Milk Yield in one year (€)" );
				price_of_increased_milk_yield_in_one_year : Optional[ int ] = Field( None , description = "Price of Increased Milk Yield in one year (€)" );
				increased_revenuein_1_year : Optional[ int ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				labor_saving : Optional[ int ] = Field( None , description = "Labor saving (%)" );
				current_labor_costin_1_year : Optional[ int ] = Field( None , description = "Current Labor Cost (€ in 1 year)" );
				labor_cost_savings_in_1_year : Optional[ int ] = Field( None , description = "Labor cost savings  (€ in 1 year)" );
				energy_saving_in_lighting_systems : Optional[ int ] = Field( None , description = "Energy Saving in Lighting Systems (%)" );
				current_energy_cosumption_for_lighting_systems_in_kwh : Optional[ int ] = Field( None , description = "Current Energy Cosumption for Lighting Systems (in kWh)" );
				cost_of_energy_per_kwh : Optional[ int ] = Field( None , description = "Cost of energy per kWh (€)" );
				currentcost_of_energy_for_lighting_systemsin_1_year : Optional[ int ] = Field( None , description = "Current  Cost of Energy for Lighting Systems (€ in 1 year)" );
				energy_cost_savingsin_1_year : Optional[ int ] = Field( None , description = "Energy Cost Savings (€ in 1 year)" );
				water_saving : Optional[ int ] = Field( None , description = "Water Saving (%)" );
				current_water_costin_1_year : Optional[ int ] = Field( None , description = "Current Water Cost (€ in 1 year)" );
				water_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Water Cost Saving (€ in 1 year)" );
				increase_profit_per_bird_per_year : Optional[ int ] = Field( None , description = "Increase Profit per Bird per Year (€)" );
				profit_per_bird_increase_in_1_year : Optional[ int ] = Field( None , description = "Profit per Bird Increase in 1 year (€)" );
				feed_saving : Optional[ int ] = Field( None , description = "Feed Saving (%)" );
				current_feed_costin_1_year : Optional[ int ] = Field( None , description = "Current Feed Cost (€ in 1 year)" );
				feed_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Feed Cost Saving (€ in 1 year)" );
				feed_waste_saving : Optional[ int ] = Field( None , description = "Feed Waste Saving (%)" );
				current_feed_waste_costin_1_year : Optional[ int ] = Field( None , description = "Current Feed Waste Cost (€ in 1 year)" );
				feed_waste_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Feed Waste Cost Saving (€ in 1 year)" );
				antibiotics_saving : Optional[ int ] = Field( None , description = "Antibiotics Saving (%)" );
				current_antibiotics_costin_1_year : Optional[ int ] = Field( None , description = "Current Antibiotics Cost (€ in 1 year)" );
				antibiotics_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Antibiotics Cost Saving (€ in 1 year)" );
				mortality_rate_decrease : Optional[ int ] = Field( None , description = "Mortality Rate Decrease (%)" );
				current_mortality_costin_1_year : Optional[ int ] = Field( None , description = "Current Mortality Cost (€ in 1 year)" );
				mortality_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Mortality Cost Saving (€ in 1 year)" );
				profitability_increase : Optional[ int ] = Field( None , description = "Profitability Increase (%)" );
				current_profitabilityin_1_year : Optional[ int ] = Field( None , description = "Current Profitability (€ in 1 year)" );
				profit_increase_in_1_year : Optional[ int ] = Field( None , description = "Profit Increase in 1 year (€)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


class small_ruminants( BaseModel ):
				dat_name : Optional[ str ] = Field( None , description = "DAT Name" );
				number_of_animals : Optional[ int ] = Field( None , description = "Number of animals" );
				years_of_usage : Optional[ int ] = Field( None , description = "YEARS OF USAGE" );
				initial_cost_of_investment : Optional[ int ] = Field( None , description = "Initial cost of Investment (€)" );
				startup_fee_per_animal : Optional[ int ] = Field( None , description = "Startup Fee per Animal(€)" );
				monthly_cost_per_animal : Optional[ int ] = Field( None , description = "Monthly Cost per Animal(€)" );
				depreciation : Optional[ float ] = Field( None , description = "Depreciation" );
				maintenance_costs : Optional[ float ] = Field( None , description = "Maintainance Costs (€)/year" );
				number_of_units_sensors_etc : Optional[ int ] = Field( None , description = "Number of Units (sensors etc.)" );
				total_cost_of_dat_purchase : Optional[ int ] = Field( None , description = "Total cost of DAT Purchase (€)" );
				milk_yield_increase : Optional[ int ] = Field( None , description = "Milk Yield Increase (%)" );
				average_milk_price_per_literliter : Optional[ int ] = Field( None , description = "Average milk price per liter (€/ liter)" );
				average_liters_of_milk_produced_per_animal_per_day_l : Optional[ int ] = Field( None , description = "Average liters of milk produced per animal per day (l)" );
				price_of_milk_yield_in_one_year : Optional[ int ] = Field( None , description = "Price of Milk Yield in one year (€)" );
				price_of_increased_milk_yield_in_one_year : Optional[ int ] = Field( None , description = "Price of Increased Milk Yield in one year (€)" );
				increased_revenuein_1_year : Optional[ int ] = Field( None , description = "Increased Revenue (€ in 1 year)" );
				labour_saving : Optional[ int ] = Field( None , description = "Labour saving (%)" );
				current_labour_costin_1_year : Optional[ int ] = Field( None , description = "Current Labour Cost (€ in 1 year)" );
				labour_cost_savings_in_1_year : Optional[ int ] = Field( None , description = "Labour cost savings  (€ in 1 year)" );
				energy_saving_in_lighting_systems : Optional[ int ] = Field( None , description = "Energy Saving in Lighting Systems (%)" );
				current_energy_consumption_for_lighting_systems_in_kwh : Optional[ int ] = Field( None , description = "Current Energy Consumption for Lighting Systems (in kWh)" );
				cost_of_energy_per_kwh : Optional[ int ] = Field( None , description = "Cost of energy per kWh (€)" );
				currentcost_of_energy_for_lighting_systemsin_1_year : Optional[ int ] = Field( None , description = "Current  Cost of Energy for Lighting Systems (€ in 1 year)" );
				energy_cost_savingsin_1_year : Optional[ int ] = Field( None , description = "Energy Cost Savings (€ in 1 year)" );
				water_saving : Optional[ int ] = Field( None , description = "Water Saving (%)" );
				current_water_costin_1_year : Optional[ int ] = Field( None , description = "Current Water Cost (€ in 1 year)" );
				water_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Water Cost Saving (€ in 1 year)" );
				increase_profit_per_animal_per_year : Optional[ int ] = Field( None , description = "Increase Profit per Animal per Year (€)" );
				profit_per_animal_increase_in_1_year : Optional[ int ] = Field( None , description = "Profit per Animal Increase in 1 year (€)" );
				feed_saving : Optional[ int ] = Field( None , description = "Feed Saving (%)" );
				current_feed_costin_1_year : Optional[ int ] = Field( None , description = "Current Feed Cost (€ in 1 year)" );
				feed_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Feed Cost Saving (€ in 1 year)" );
				feed_waste_saving : Optional[ int ] = Field( None , description = "Feed Waste Saving (%)" );
				current_feed_waste_costin_1_year : Optional[ int ] = Field( None , description = "Current Feed Waste Cost (€ in 1 year)" );
				feed_waste_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Feed Waste Cost Saving (€ in 1 year)" );
				antibiotics_saving : Optional[ int ] = Field( None , description = "Antibiotics Saving (%)" );
				current_antibiotics_costin_1_year : Optional[ int ] = Field( None , description = "Current Antibiotics Cost (€ in 1 year)" );
				antibiotics_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Antibiotics Cost Saving (€ in 1 year)" );
				mortality_rate_decrease : Optional[ int ] = Field( None , description = "Mortality Rate Decrease (%)" );
				current_mortality_costin_1_year : Optional[ int ] = Field( None , description = "Current Mortality Cost (€ in 1 year)" );
				mortality_cost_savingin_1_year : Optional[ int ] = Field( None , description = "Mortality Cost Saving (€ in 1 year)" );
				profitability_increase : Optional[ int ] = Field( None , description = "Profitability Increase (%)" );
				current_profitabilityin_1_year : Optional[ int ] = Field( None , description = "Current Profitability (€ in 1 year)" );
				profit_increase_in_1_year : Optional[ int ] = Field( None , description = "Profit Increase in 1 year (€)" );
				annual_change_in_net_income : Optional[ float ] = Field( None , description = "Annual change in Net Income  (€)" );
				return_on_investment_roi : Optional[ float ] = Field( None , description = "Return on Investment (ROI %)" );
				payback_period : Optional[ float ] = Field( None , description = "Payback Period (years)" );
				is_the_dat_beneficial : Optional[ float ] = Field( None , description = "Is the DAT Beneficial?" );


