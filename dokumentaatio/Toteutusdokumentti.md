Viikko2:
ChatGPT:n avulla tutustuin poetry juttuihin. Elikkä poetry testaus asioiden alustamisessa oli itsellä muistissa vähän mustia aukkoja, tällaiset yksityiskohdat tarkistin ChatGPT:llä:

[tool.pytest.ini_options]
addopts = "--cov=src --cov-report=term-missing"
testpaths = ["tests"]