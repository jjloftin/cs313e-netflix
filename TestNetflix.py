#!/usr/bin/env python3

# -------------------------------
# projects/netflix/Testnetflix.py
# Copyright (C) 2014
# Glenn P. Downing
# -------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_predict, netflix_print, netflix_solve, netflix_RMSE


# -----------
# Testnetflix
# -----------

class Testnetflix (TestCase) :

    # ----
    # predict
    # ----

    def test_predict_1 (self) :
        v = netflix_predict(2043, 1417435)
        self.assertEqual(v, 3)

    def test_predict_2 (self) :
        v = netflix_predict(10851, 1417435)
        self.assertEqual(, 125)

    def test_predict_3 (self) :
        v = netflix_predict(2043, 462685)
        self.assertEqual(v, 89)

    def test_predict_4 (self) :
        v = netflix_predict(10851, 462685)
        self.assertEqual(v, 174)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print(w, 1, 10, netflix_predict(1, 10))
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
       w = StringIO()
       netflix_print(w, 100, 200, netflix_predict(100, 200))
       self.assertEqual(w.getvalue(), "100 200 125\n")
       
    def test_print_3 (self) :
       w = StringIO()
       netflix_print(w, 201, 210, netflix_predict(201, 210))
       self.assertEqual(w.getvalue(), "201 210 89\n")
       
    def test_print_4 (self) :
      w = StringIO()
      netflix_print(w, 900, 1000, netflix_predict(900, 1000))
      self.assertEqual(w.getvalue(), "900 1000 174\n")
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("2048: \n 1417435 \n 2312054 \n 462685")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "2048: \n 3 3 3")
    
    def test_solve_2 (self) :
       r = StringIO("")
       w = StringIO()
       netflix_solve(r, w)
       self.assertEqual(w.getvalue(), '')
       
     def test_solve_3 (self) :
        r = StringIO("2048: \n 1417435 \n 2312054 \n 462685 \n 10851: \n 1417435")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "2048: \n 3 \n 3 \n 3 \n 1045: \n 3 \n")
    
    def test_solve_4 (self) :
       r = StringIO("2048: \n ")
       w = StringIO()
       netflix_solve(r, w)
       self.assertEqual(w.getvalue(), '')
       
# ----
# main
# ----

main()