#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset

PGUSER="$POSTGRES_USER" psql --dbname="$POSTGRES_DB" <<-'EOSQL'
    CREATE DATABASE template_postgis;
    UPDATE pg_database SET datistemplate = TRUE WHERE datname = 'template_postgis';
EOSQL

for db in template_postgis "$POSTGRES_DB"; do
PGUSER="$POSTGRES_USER" psql --dbname="$db" <<-'EOSQL'
    CREATE EXTENSION IF NOT EXISTS postgis;
    CREATE EXTENSION IF NOT EXISTS hstore;
    CREATE EXTENSION IF NOT EXISTS unaccent;
    CREATE EXTENSION IF NOT EXISTS postgis_topology;
    CREATE EXTENSION IF NOT EXISTS fuzzystrmatch;
    CREATE EXTENSION IF NOT EXISTS postgis_tiger_geocoder
EOSQL
done

echo "Creating Database 'ws_cost_benefit_calculator'"
PGPASSWORD=mysecretpassword PGUSER=postgres psql --dbname=postgres <<-'EOSQL'
   CREATE SCHEMA ws_cost_benefit_calculator;
EOSQL