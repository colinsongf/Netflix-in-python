# TestNetflix.py


from io       import StringIO
from unittest import main, TestCase

from Netflix import actual_rating, rmse, predict

class Testnettest (TestCase) :
    # ----
    # read
    # ----

    #def test_netflix_solve(self):

    def test_actual_rating(self):
        c = actual_rating("6287","1013875")
        self.assertEqual(c, "5")

    def test_actual_rating_2(self):
        c = actual_rating("10906","2633447")
        self.assertEqual(c, "1")

    def test_actual_rating_3(self):
        c = actual_rating("4829","347281")
        self.assertEqual(c,"4")

    def test_actual_rating_4(self):
        c = actual_rating("2288","733230")
        self.assertEqual(c, "3")


    def test_predict(self):
        b = predict("","")
        self.assertEqual(b,"")

    def test_predict_2(self):
        b = predict("","")
        self.assertEqual(b,"")

    def test_predict_3(self):
        b = predict("","")
        self.assertEqual(b,"")

    def test_predict_4(self):
        b = predict("","")
        self.assertEqual(b,"")



    def test_rmse(self):
        v = rmse([2,2,2,2],[2,2,2,2])
        self.assertEqual(v, 0)

    def test_rmse_2(self):
        v = rmse([1,1,1,1],[3,3,3,3])
        self.assertEqual(v, 2)

    def test_rmse_3(self):
        v = rmse([1,1,1,1],[5,5,5,5])
        self.assertEqual(v, 4)

    def test_rmse_4(self):
        v = rmse([1,2,1,2],[2,1,2,1])
        self.assertEqual(v, 1)

