import unittest
from AspiR import AspiR


class Test_Robot(unittest.TestCase):

    def test_Robot_can_move_Game_case_0(self):
        aspi_R = AspiR("0_Inputs/Case_Aspi_R_0.txt")
        r_b = aspi_R.get_robot("B")

        self.assertEqual("B", r_b.color)
        self.assertEqual(3, r_b.index)

        self.assertTrue(r_b.can_move(aspi_R, "N"))  # North
        self.assertTrue(r_b.can_move(aspi_R, "E"))  # East
        self.assertFalse(r_b.can_move(aspi_R, "S"))  # South
        self.assertFalse(r_b.can_move(aspi_R, "W"))  # West

        r_r = aspi_R.get_robot("R")
        self.assertEqual("R", r_r.color)
        self.assertEqual(6, r_r.index)

        self.assertFalse(r_r.can_move(aspi_R, "N"))  # North
        self.assertTrue(r_r.can_move(aspi_R, "E"))  # East
        self.assertTrue(r_r.can_move(aspi_R, "S"))  # South
        self.assertFalse(r_r.can_move(aspi_R, "W"))  # West

    def test_Robot_compute_move_Game_case_0(self):

        aspi_R = AspiR("0_Inputs/Case_Aspi_R_0.txt")
        r_b = aspi_R.get_robot("B")

        self.assertEqual("B", r_b.color)
        self.assertEqual(3, r_b.index)

        self.assertEqual(0, r_b.compute_move(aspi_R, "N"))  # North
        self.assertEqual(5, r_b.compute_move(aspi_R, "E"))  # East

        r_r = aspi_R.get_robot("R")
        self.assertEqual("R", r_r.color)
        self.assertEqual(6, r_r.index)

        self.assertEqual(8, r_r.compute_move(aspi_R, "E"))  # North
        self.assertEqual(9, r_r.compute_move(aspi_R, "S"))  # East


if __name__ == '__main__':
    unittest.main()
