# Getting Started
Download or pull the files from the repository into the directory on the server in which you which to run the webapp. Install all necessary prerequisites below, navigate to the directory containing app.py, then run the following from the CLI.

 Ubuntu:

    export FLASK_APP=app && flask run 

From there the web application should be running at http://localhost:5000/

If you have a SQLite3 Database with your files, name it `students.db` and place it in the directory with app.py, otherwise, an empty database will be created for you. Click on a row to edit or delete that entry, click on the "New Student" button to add a new entry.



# API


## Get Commands

| URL | Parameters | Functionality |
|--|--| -- |
|/|  | Homepage, alias for /displayDB |
|/displayDB| | Shows the database in a web browser, click on a row to edit or delete that entry, click on the "New Student" button to add a new entry.|
|/edit|studentKey| Returns a form to edit the student with the internal key `studentKey` |
|/remove| | Returns an error page, do not use.|
|/getTable| | returns an HTML table for use in the home page, this function exists for updating the homepage regularly in the case of remote edits.|
|/addEntry| | Returns a form to generate a new student entry |
## Post Commands
| URL | Parameters | Functionality |
|--|--| -- |
|/edit|studentKey, name, sid, grade| Sets the values of the entry in the database with an internal key equal to `studentKey`, to those submitted in the request |
|/remove| studentKey| Deletes the entry with the internal id `studentKey`|
|/addEntry| name, sid, grade| Adds a new student with the given name, id, and grade |

# Known Dependencies
- python 3
- flask
- SQLite3

## Tested versions
|Software | Version|
|--|--|
|attrs | 19.3.0 |
|Automat | 0.8.0 |
|blinker | 1.4 |
|certifi | 2019.11.28 |
|chardet | 3.0.4 |
|click | 8.0.4 |
|cloud-init | 21.4 |
|colorama | 0.4.3 |
|command-not-found | 0.3 |
|configobj | 5.0.6 |
|constantly | 15.1.0 |
|cryptography | 2.8 |
|dbus-python | 1.2.16 |
|distlib | 0.3.4 |
|distro | 1.4.0 |
|distro-info | 0.23ubuntu1 |
|entrypoints | 0.3 |
|filelock | 3.6.0 |
|Flask | 2.0.3 |
|httplib2 | 0.14.0 |
|hyperlink | 19.0.0 |
|idna | 2.8 |
|importlib-metadata | 1.5.0 |
|incremental | 16.10.1 |
|itsdangerous | 2.1.0 |
|Jinja2 | 3.0.3 |
|jsonpatch | 1.22 |
|jsonpointer | 2.0 |
|jsonschema | 3.2.0 |
|keyring | 18.0.1 |
|language-selector | 0.1 |
|launchpadlib | 1.10.13 |
|lazr.restfulclient | 0.14.2 |
|lazr.uri | 1.0.3 |
|MarkupSafe | 2.1.0 |
|more-itertools | 4.2.0 |
|netifaces | 0.10.4 |
|oauthlib | 3.1.0 |
|pexpect | 4.6.0 |
|platformdirs | 2.5.1 |
|pyasn1 | 0.4.2 |
|pyasn1-modules | 0.2.1 |
|PyGObject | 3.36.0 |
|PyHamcrest | 1.9.0 |
|PyJWT | 1.7.1 |
|pymacaroons | 0.13.0 |
|PyNaCl | 1.3.0 |
|pyOpenSSL | 19.0.0 |
|pyrsistent | 0.15.5 |
|pyserial | 3.4 |
|python-apt | 2.0.0+ubuntu0.20.4.6 |
|python-debian | 0.1.36ubuntu1 |
|PyYAML | 5.3.1 |
|requests | 2.22.0 |
|requests-unixsocket | 0.2.0 |
|SecretStorage | 2.3.1 |
|service-identity | 18.1.0 |
|simplejson | 3.16.0 |
|six | 1.14.0 |
|sos | 4.1 |
|ssh-import-id | 5.10 |
|systemd-python | 234 |
|Twisted | 18.9.0 |
|ubuntu-advantage-tools | 27.5 |
|ufw | 0.36 |
|unattended-upgrades | 0.1 |
|urllib3 | 1.25.8 |
|virtualenv | 20.13.2 |
|wadllib | 1.3.3 |
|Werkzeug | 2.0.3 |
|zipp | 1.0.0 |
|zope.interface | 4.7.1 |


