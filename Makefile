# Makefile for sales.

# Configuration.
SHELL = /bin/bash
ROOT_DIR = $(shell pwd)
BIN_DIR = $(ROOT_DIR)/bin
DATA_DIR = $(ROOT_DIR)/var
SCRIPT_DIR = $(ROOT_DIR)/script

WGET = wget

# Bin scripts
ANSIBLE_PROVISION = $(shell) $(SCRIPT_DIR)/provision.sh
ANSIBLE_DEPLOY = $(shell) $(SCRIPT_DIR)/deploy.sh
CLEAN = $(shell) $(SCRIPT_DIR)/clean.sh
CLEAN_MIGRATIONS = $(shell) $(SCRIPT_DIR)/clean_migrations.sh
GRIP = $(shell) $(SCRIPT_DIR)/grip.sh
PYENV = $(shell) $(SCRIPT_DIR)/pyenv.sh
SETUP = $(shell) $(SCRIPT_DIR)/setup.sh
INSTALL = $(shell) $(SCRIPT_DIR)/install.sh
LINTCODE = $(shell) $(SCRIPT_DIR)/lintcode.sh
TEST = $(shell) $(SCRIPT_DIR)/test.sh
RUNSERVER = $(shell) $(SCRIPT_DIR)/runserver.sh
SYNC = $(shell) $(SCRIPT_DIR)/sync.sh
WATCH = $(shell) $(SCRIPT_DIR)/watch.sh
PM = $(shell) $(SCRIPT_DIR)/pm.sh

ansible_provision:
	$(ANSIBLE_PROVISION)


ansible_deploy:
	$(ANSIBLE_DEPLOY)


clean:
	$(CLEAN)


clean_migrations: clean
	$(CLEAN_MIGRATIONS)


deploy:
	$(ANSIBLE_PROVISION)
	$(ANSIBLE_DEPLOY)


distclean: clean
	rm -rf $(ROOT_DIR)/lib
	rm -rf $(ROOT_DIR)/*.egg-info
	rm -rf $(ROOT_DIR)/demo/*.egg-info


environment:
	$(PYENV)


grip:
	$(GRIP)


install:
	$(INSTALL)


roles:
	$(ROLES_ANSIBLE)


maintainer-clean: distclean
	rm -rf $(BIN_DIR)
	rm -rf $(ROOT_DIR)/lib/


lintcode:
	$(LINTCODE)


sync:
	$(SYNC)


watch:
	$(WATCH)


test:
	$(TEST)

pm:
	echo "${action}"
	@if [ "${action}" == '' ]; then \
		echo "Error: Variables not set correctly"; exit 2; \
	fi
	$(PM) "${action}"


runserver:
	$(RUNSERVER)