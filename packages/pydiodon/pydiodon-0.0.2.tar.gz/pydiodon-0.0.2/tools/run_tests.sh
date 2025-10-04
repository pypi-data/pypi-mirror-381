#!/bin/sh

# static analysis using pylint
pylint pydiodon.py -r n --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint.txt

# unitary tests using pytest
python3-coverage run --source . -m pytest --junit-xml=test.xml

# show report for gitlab
python3-coverage report

# coverage report in xml for sonarqube
python3-coverage xml

# replace default properties of sonarqube config depending on the git branch
perl -pi tools/patch-sonar-properties.perl sonar-project.properties

# check sonarqube config
cat sonar-project.properties

# run sonarqube analysis and upload the reports on https://sonarqube.inria.fr/sonarqube
sonar-scanner -Dsonar.login=$SONARQUBE_LOGIN
