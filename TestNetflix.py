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

from Netflix import netflix_predict, netflix_solve, netflix_rmse


# -----------
# Testnetflix
# -----------

class Testnetflix (TestCase) :

    # -------
    # predict
    # -------

    def test_predict_1 (self) :
      p = netflix_predict(2043, 1417435)
      assert 1 <= p <= 5

    def test_predict_2 (self) :
      p = netflix_predict(10851, 1417435)
      assert 1 <= p <= 5

    def test_predict_3 (self) :
      p = netflix_predict(2043, 462685)
      assert 1 <= p <= 5

    def test_predict_4 (self) :
      p = netflix_predict(10851, 462685)
      assert 1 <= p <= 5

    # ----
    # rmse
    # ----
    
    def test_rmse_1(self) :
      a = {0:0, 1:0, 2:0}
      p = {0:0, 1:0, 2:0}
      v = netflix_rmse(a,p)
      
      self.assertEqual(v, 0)
    
    def test_rmse_2(self):
      a = {0:0, 1:0, 2:0}
      p = {0:2, 1:2, 2:2}
      v = netflix_rmse(a,p)
      
      self.assertEqual(v, 2)
      
    def test_rmse_3(self):
      a = {0:0, 1:0, 2:0}
      p = {0:1, 1:2, 2:3}
      v = netflix_rmse(a,p)
     
      assert 2.1 < v < 2.2    

    # -----
    # solve
    # -----
    
    def test_solve_1 (self) :
      r = StringIO('10: \n 1952305 \n 1531863 \n')
      w = StringIO()
      netflix_solve(r, w)
      self.assertEqual(w.getvalue().count(':'), 2 )
    
    def test_solve_2(self) :
      r = StringIO('10006: \n 1093333 \n 1982605 \n 1534853 \n 1632583')
      w = StringIO()
      netflix_solve(r, w)
      self.assertEqual(w.getvalue().count(':'), 2 )
      
    def test_solve_3(self) : 
      r = StringIO('10007: \n 1204847 \n 10006: \n 1093333 \n 10: \n 1952305')
      w = StringIO()
      netflix_solve(r, w)
      self.assertEqual(w.getvalue().count(':'), 4 )     
  
# ----
# main
# ----

main()