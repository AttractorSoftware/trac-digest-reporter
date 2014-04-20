Trac Digest Reporter
====================

## Problem

When I follow a project in trac, I get tonns of email. Single email for every comment, for every ticket created, for each changeset , etc.
When I follow few porject, it becomes a nightmare. Sometimes I get hundreds of email daily.
Moreover, there two much routine information, which does not contain any value, but still draws my precious attention.

## Solution

Create a pluggin the would

1. summarize changes to the project (tickets, changesets) made in particular period (since last notification);
2. present the information in a more readable form, compared to what trac does now.

## Developer Start Guide

1. Clone the repo
1. install virtualenv
1. create test trac environment,
1. run `python setup.py develop -mxd /path/to/trac-env/plugins`

