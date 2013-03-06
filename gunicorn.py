import os

# Bind to PORT if defined, otherwise default to 5000.
port = int(os.environ.get('PORT', 5000))

bind = '0.0.0.0:' + str(port)
workers = 3
