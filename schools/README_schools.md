# Chicago Data Portal Data
Each year, CPS schools release two files to Chicago Data Portal: a School Profile and a Progress Report. 

For good housekeeping, I am storing the endpoints in a json file within the schools folder.

## School Profile

## Prograess Report



# Using Postgresql
Install the current stable version of postgresql using brew install postgresql. This installed version @14 on my computer on 1/10/25.

1. Start postgresql in the background using   brew services start postgresql@14

## command line
connect to the db: psql chicago_schools
### DROP
DROP TABLE table_name;
^ Capital DROP TABLE required
^ semi colon required

### list tables
\dt

# Working instructions
The pr reports have dictionaries in the cps_school_profile and website fields.  This messes up sqlalchemy.
