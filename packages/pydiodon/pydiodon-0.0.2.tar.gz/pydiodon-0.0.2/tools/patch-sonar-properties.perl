#!/usr/bin/env perl -w

s{(?:^#\s*)?(sonar.links.homepage=).*}{$1$ENV{CI_PROJECT_URL}}g;
s{(?:^#\s*)?(sonar.links.scm=).*}{$1$ENV{CI_PROJECT_URL}.git}g;
s{(?:^#\s*)?(sonar.projectKey=).*}{$1pleiade:$Key}g;
s{(?:^#\s*)?(sonar.branch.name=).*}{$1$ENV{CI_COMMIT_REF_SLUG}}g;

BEGIN {
  # Project key is gitlab project path, plus commit ref slug
  ($Key = ($ENV{CI_PROJECT_PATH})) =~ s{/}{:}g;
}
