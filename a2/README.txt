############################################################
# PROPERTY OF B.J.S. INC.
############################################################
# CIT 470
# Spencer Klump
# Brian Solomon
# Johnny Rivera
############################################################
############################################################
# This README file Provides a list of files
# Describes the purpose of all files within the directory.
###########################################################
# FN = File Name
################
# FN: install-ldap-server
# This file initializes the Lightweight Directory Access Protocol (LDAP) server and sets
# the configurations that are needed to allow user authenication

# FN: install-nfs-server
# This file initializes the Network file system (NFS) server and sets
# the configurations to incorperate network security services (NSS)

# FN: client-ks.cfg
# This file is our client's kickstart that will be pushed onto the
# Apache server for download, the network configuration for these clients
# is set to run DHCP.

# FN: base.ldif
# This file is the basic base.ldif file that a LDAP server would need
# adding in the core minimum organizational units, these can be edited
# fit the clients need.

# FN:exports
# This file sets the standard read-write permissions for the client 
# IP subnet of 10.2.6.0/8.

# FN: migrate_common.ph
# This file is a copy of /usr/share/migrationtools/migrate_common.ph with our
# set configurations to match our domain name and LDAP server IP address.

# FN: olcDatabase={2}hdb.ldif
# This file is a copy of /etc/openldap/slapd.d/cn=config/olcDatabase={2}hdb.ldif
# in addition to our set configurations to match our domain name and LDAP server IP
# address.
