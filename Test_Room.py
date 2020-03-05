import unittest
from Room import Room


class Test_Room(unittest.TestCase):

    def test_Room_Case_0(self):

        filename = "0_Inputs/Case_Aspi_R_0.txt"
        with open(filename, 'r') as file_in:

            first_line = file_in.readline()
            n_x, n_y, n_r = first_line.split()

            room = Room(int(n_x), int(n_y), file_in)
            self.assertEqual(12, room.size())
            self.assertEqual(4, room.n_x)
            self.assertEqual(3, room.n_y)

            self.assertTrue(room.has_wall(0, "N"))
            self.assertFalse(room.has_wall(0, "E"))
            self.assertFalse(room.has_wall(0, "S"))
            self.assertTrue(room.has_wall(0, "W"))

            self.assertTrue(room.has_wall(2, "N"))
            self.assertTrue(room.has_wall(2, "E"))
            self.assertFalse(room.has_wall(2, "S"))
            self.assertFalse(room.has_wall(2, "W"))

            self.assertFalse(room.has_wall(3, "N"))
            self.assertFalse(room.has_wall(3, "E"))
            self.assertFalse(room.has_wall(3, "S"))
            self.assertTrue(room.has_wall(3, "W"))

            self.assertFalse(room.has_wall(4, "N"))
            self.assertFalse(room.has_wall(4, "E"))
            self.assertFalse(room.has_wall(4, "S"))
            self.assertFalse(room.has_wall(4, "W"))

            self.assertFalse(room.has_wall(11, "N"))
            self.assertTrue(room.has_wall(11, "E"))
            self.assertTrue(room.has_wall(11, "S"))
            self.assertFalse(room.has_wall(11, "W"))


if __name__ == '__main__':
    unittest.main()
