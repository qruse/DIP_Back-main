#!/bin/bash
su post
psql -U postgres -d postgres -a -f /tmp/dbsql/dip_library.sql