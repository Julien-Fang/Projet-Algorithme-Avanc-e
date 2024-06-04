.PHONY: tests perf_shakespeare perf_filebino perf_tasmin perf_compar etudeexp clean

tests: tests.py
	python3 tests.py

perf_shakespeare: Shakespeare.py
	python3 Shakespeare.py

perf_filebino: testsPerf_FileBino.py
	python3 testsPerf_FileBino.py

perf_tasmin: testsPerf_TasMin.py
	python3 testsPerf_TasMin.py

perf_compar: perf_compar.py
	python3 perf_compar.py

etudeexp: etudeExp.py
	python3 etudeExp.py

clean:
	rm -rf __pycache__ *.pyc