from pytest import approx
from math import sqrt
from shadow.polyedr import Polyedr

class TestPolyedr:

    def test_polyedr_1(self):
        assert Polyedr(f"data/test1.geom").part_area() == 0

    def test_polyedr_2(self):
        assert Polyedr(f"data/test2.geom").part_area() == 0

    def test_polyedr_3(self):
        assert Polyedr(f"data/test3.geom").part_area() == 0

    def test_polyedr_4(self):
        assert Polyedr(f"data/test4.geom").part_area() == 0

    def test_polyedr_5(self):
        assert Polyedr(f"data/test5.geom").part_area() == 0

    def test_polyedr_6(self):
        assert Polyedr(f"data/test6.geom").part_area() == 20000

    def test_polyedr_7(self):
        assert Polyedr(f"data/test7.geom").part_area() == 20000


    # python3 -B -m pytest -p no:cacheprovider tests/test_polyedr.py