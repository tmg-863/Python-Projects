# -*- coding:utf-8 -*-
#This script uses several operations to wrangle, enrich, and export population data

import arcpy
from arcpy import env

env.overwriteOutput = 1 
arcpy.env.workspace= "D:/pythongis.gdb"

# Local variables:
project_counties= "D:/pythongis.gdb/project_counties"
RB17 = "D:/pythongis.gdb/RB17"
RB00 = "D:/pythongis.gdb/RB00"
RB70 = "D:/pythongis.gdb/RB70"

# Set the local parameters
inFeatures = "project_counties"
joinField = "NAME2"
joinTable = "RB70"
fieldList = ["F70_1", "F70_2", "F70_3", "F70_4","F70_5","F70_6"]

#Join the tabular 1970 demographic county data to counties boundary feature class

arcpy.JoinField_management ("project_counties", "NAME2", "RB70", "County2",["F70_1", "F70_2", "F70_3", "F70_4","F70_5","F70_6"])

#Join the tabular 2000 demographic county data to counties boundary feature class
# Set the local parameters
inFeatures = "project_counties"
joinField = "NAME2"
joinTable = "RB00"
fieldList = ["F00_1", "F00_2", "F00_3", "F00_4","F00_5","F00_6"]

arcpy.JoinField_management ("project_counties", "NAME2", "RB00", "County2",["F00_1", "F00_2", "F00_3", "F00_4","F00_5","F00_6"])

#Join the tabular 2017 demographic county data to counties boundary feature class
# Set the local parameters
inFeatures = "project_counties"
joinField = "NAME2"
joinTable = "RB17"
fieldList = ["F17_1", "F17_2", "F17_3", "F17_4","F17_5","F17_6"]

arcpy.JoinField_management ("project_counties", "NAME2", "RB17", "County2",["F17_1", "F17_2", "F17_3", "F17_4","F17_5","F17_6"])

#export the newly joined project_counties FEATURE CLASS to "lock-in" these values
#export to feature class
arcpy.FeatureClassToFeatureClass_conversion("project_counties", "D:/pythongis.gdb", "counties_final")

#adding 3 fields to calculate percent change over the years

#new field 1 is going to be the year 2000 minus the year 1970, labeled as "PC1" and "P" for population change
#new field 2 is going to be the year 2017 minus the year 2000, labeled as "PC2"
#new field 3 is going to be the year 2017 minus the year 1970, labeled as "PC3"

#also going to add 3 fields for unemployment change: "UC1...2...3...etc"

counties_final= "D:/pythongis.gdb/counties_final" #defining the feature class to which I intend to add new fields

#this defines all the field parameters needed to add each field
fields = [
    ("PC1", "DOUBLE","5","4","","","NULLABLE","NON_REQUIRED",""),
      ("PC2","DOUBLE","5","4","","","NULLABLE","NON_REQUIRED",""),
      	   ("PC3","DOUBLE","5","4","","","NULLABLE","NON_REQUIRED",""),
      	   		("UC1", "DOUBLE","5","4","","","NULLABLE","NON_REQUIRED",""),
      				("UC2","DOUBLE","5","4","","","NULLABLE","NON_REQUIRED",""),
      	   				("UC3","DOUBLE","5","4","","","NULLABLE","NON_REQUIRED",""),
    ]
for field in fields:
	arcpy.AddField_management(*(counties_final,)+field)

mapdoc= arcpy.mapping.MapDocument("CURRENT")
title

