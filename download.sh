export PYTHONPATH=../bsubpc-fundamentals/src:$PYTHONPATH
run_csd_python_api doi-list.py > dois.txt
run_csd_python_api geom-mol2.py
