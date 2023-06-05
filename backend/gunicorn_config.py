import multiprocessing

command = '/usr/local/bin/gunicorn'
pythonpath = '/var/www/our-school/backend'
bind = 'unix:/run/our-school.sock'
workers = multiprocessing.cpu_count() * 2 + 1
