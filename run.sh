. env/bin/activate
python interface.py
deactivate
. venv/bin/activate 
python tests/integration/test_end_to_end_election.py
deactivate 