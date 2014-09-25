# TestNetflix.py


from io       import StringIO
from unittest import main, TestCase

from Netflix import actual_rating, netflix_rmse, netflix_predict

# -----------
# TestNetflix
# -----------

class Testnettest (TestCase) :
    
    # ----
    # actual_rating
    # ----

    def test_actual_rating(self):
        c = actual_rating("1013875", "6287")
        self.assertEqual(c, 5)

    def test_actual_rating_2(self):
        c = actual_rating("2633447", "10906")
        self.assertEqual(c, 1)

    def test_actual_rating_3(self):
        c = actual_rating("347281", "4829")
        self.assertEqual(c,4)

    def test_actual_rating_4(self):
        c = actual_rating("733230", "2288")
        self.assertEqual(c, 3)

    # ----
    # predict
    # ----

    def test_netflix_predict(self):
        b = netflix_predict("3","3")
        self.assertEqual(b, 3.0)

    def test_netflix_predict_2(self):
        b = netflix_predict("2","4")
        self.assertEqual(b, 2.4)

    def test_netflix_predict_3(self):
        b = netflix_predict("1.5","4.5")
        self.assertEqual(b, 2.6)

    def test_netflix_predict_4(self):
        b = netflix_predict("1.8","3.8")
        self.assertEqual(b, 2.1)

    # ----
    # rmse
    # ----

    def test_netflix_rmse(self):
        v = netflix_rmse([2,2,2,2],[2,2,2,2])
        self.assertEqual(v, "0.00")

    def test_netflix_rmse_2(self):
        v = netflix_rmse([1,1,1,1],[3,3,3,3])
        self.assertEqual(v, "2.00")

    def test_netflix_rmse_3(self):
        v = netflix_rmse([1,1,1,1],[5,5,5,5])
        self.assertEqual(v, "4.00")

    def test_netflix_rmse_4(self):
        v = netflix_rmse([1,2,1,2],[2,1,2,1])
        self.assertEqual(v, "1.00")

# ----
# main
# ----

main()
