import multiprocessing

command = "/usr/local/bin/gunicorn"
pythonpath = "/var/www/our-school/backend"
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
