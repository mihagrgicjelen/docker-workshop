import multiprocessing

bind = "0.0.0.0:8000"
workers = 2  # multiprocessing.cpu_count() * 2 + 1
worker_tmp_dir = '/tmp_gunicorn'
