#!/bin/sh

#Deploy site

# typical apache2 on debian (such as Ubuntu)
# Change dirs as needed.

# NOTE: Only run from this (scripts) directory
#       Copies ../*.* Not recursive

export APACHE_DOC_DIR=/var/www/votebugger.com/public_html/

echo ""
echo "---- Apache destination directory"
echo $APACHE_DOC_DIR

#Only run from this (scripts) directory
FILE=../scripts/linuxdeploy.sh
if [ ! -f "$FILE" ]; then
    echo "Error: only run: ./linuxdeploy.sh"
    exit 1
fi

echo ""
echo "---- Backing up"
OF="/tmp/var-www-votebugger.com-public_html_$(date +%s)_bkp.zip"
zip -rq $OF  $APACHE_DOC_DIR
ls -lth $OF

#ls -lth $APACHE_DOC_DIR/
#ls -lth ../*.*
echo ""
echo "---- Removing Apache files"

# Not recursive:
rm $APACHE_DOC_DIR/*.*

#ls -lth $APACHE_DOC_DIR/

#ls -lth ../*.* $APACHE_DOC_DIR
echo ""
echo "---- Copying site to Apache directory"
cp ../*.* $APACHE_DOC_DIR/

echo ""

tree $APACHE_DOC_DIR

sudo service apache2 restart





