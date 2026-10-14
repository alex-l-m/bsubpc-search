export PYTHONPATH=../bsubpc-fundamentals/src:$PYTHONPATH
run_csd_python_api doi-list.py > dois.txt
rm -rf mol2
run_csd_python_api geom-mol2.py
