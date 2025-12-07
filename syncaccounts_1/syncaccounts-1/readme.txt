
SYNCACCOUNTS.PY VERSION 1

Overview:

This script will keep your Wolfpack accounts in sync with a backend account database
(From your website for instance). It uses a background worker thread to minimize the
impact on your normal server operation.

Requirements: 

- Wolfpack 12.9.9 

- MySQL-Python (1.0.0 recommended)
http://sourceforge.net/project/showfiles.php?group_id=22307&package_id=15775&release_id=243731

- MySQL Backend

Installation:

To install this script, add it to your scripts folder and add
<script>syncaccounts</script> to your scripts.xml

Please note that this script will not work out of the box since
it requires you to have a MySQL backend properly configured.

Configuration:

You need to change line 65 and below of the script to match your own database configuration.
