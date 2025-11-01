PY ?= python3

.PHONY: venv install jupyter clean
venv:
	$(PY) -m venv .venv
	. .venv/bin/activate; python -m pip install --upgrade pip

install: venv
	. .venv/bin/activate; pip install -r requirements.txt
	. .venv/bin/activate; python -m ipykernel install --user --name dlscratch --display-name "Python (dlscratch)"

jupyter:
	. .venv/bin/activate; jupyter notebook

clean:
	rm -rf .venv
