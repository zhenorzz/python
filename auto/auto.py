#!/usr/bin/python
from bs4 import BeautifulSoup
from src import test

try:
    auto = test.test()
    auto.read()
except Exception as e:
    print(e)
