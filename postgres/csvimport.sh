#!/bin/bash
su - postgres
psql -U postgres -d postgres -a -f /tmp/dbsql/dip_library.sql

