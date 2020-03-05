import unittest

from AspiR import AspiR


class Test_AspiR(unittest.TestCase):

    def test_Aspi_R_clean_Aspi_R_case_0(self):

        aspi_r = AspiR("0_Inputs/Case_Aspi_R_0.txt")
        path = aspi_r.clean()
        ref_path = 'BN BE BS RS BW BN'
        self.assertEqual(ref_path, path)
        self.assertEqual(6, len(path.split()))
        self.assertTrue(aspi_r.check_cleaning(path))
        self.assertFalse(aspi_r.check_cleaning('BN BE BS RS BW'))

    def test_Aspi_R_clean_Aspi_R_case_1(self):

        aspi_r = AspiR("0_Inputs/Case_Aspi_R_1.txt")
        path = aspi_r.clean()
        ref_path = "BE BN BW RE BS BE"
        self.assertEqual(6, len(path.split()))
        self.assertEqual(ref_path, path)
        self.assertTrue(aspi_r.check_cleaning(path))

    def test_Aspi_R_clean_Aspi_R_case_2(self):

        aspi_r = AspiR("0_Inputs/Case_Aspi_R_2.txt")
        path = aspi_r.clean()

        ref_path = 'BS BE BN BE BS RN RE RS BW BN'
        # ref_path = 'BE BS RN RE RS BW BN BW BS BE' # without pruning of branches
        self.assertEqual(10, len(path.split()))
        self.assertEqual(ref_path, path)
        self.assertTrue(aspi_r.check_cleaning(path))

    def test_Aspi_R_clean_Aspi_R_case_3(self):

        aspi_r = AspiR("0_Inputs/Case_Aspi_R_3.txt")
        path = aspi_r.clean()
        ref_path = 'BE BS YE YS BW RE RN RW RS RE YW YN YE YS YW BN'
        self.assertEqual(16, len(path.split()))
        # self.assertEqual(ref_path, path)
        self.assertTrue(aspi_r.check_cleaning(path))

    def test_Aspi_R_clean_Aspi_R_case_4(self):

        aspi_r = AspiR("0_Inputs/Case_Aspi_R_4.txt")
        aspi_r.write_svg("Case_Aspi_R_4.svg")
        path = aspi_r.clean()
        # print(path)
        aspi_r.write_svg("Case_Aspi_R_4_w_results.svg", path)
        self.assertEqual(13, len(path.split()))
        self.assertTrue(aspi_r.check_cleaning(path))

        ref_path = 'RE BS RN RE RS BE BN BE RE BS BW BN BW'
        self.assertEqual(ref_path, path)

    def test_Aspi_R_clean_Aspi_R_case_5(self):

        aspi_r = AspiR("0_Inputs/Case_Aspi_R_5.txt")
        aspi_r.write_svg("Case_Aspi_R_5.svg")
        path = aspi_r.clean()
        print(path)
        aspi_r.write_svg("Case_Aspi_R_5_w_results.svg", path)
        ref_path = 'RS BE BS BW BN BW RW BS BE BN BE BS'
        self.assertEqual(12, len(path.split()))
        self.assertEqual(ref_path, path)
        self.assertTrue(aspi_r.check_cleaning(path))

    def test_Aspi_R_clean_Aspi_R_case_6(self):

        aspi_r = AspiR("0_Inputs/Case_Aspi_R_6.txt")
        aspi_r.write_svg("Case_Aspi_R_6.svg")
        path = aspi_r.clean()
        print(path)
        aspi_r.write_svg("Case_Aspi_R_6_w_results.svg", path)
        ref_path = 'BW RS RW BS BE BN BE BS RE BE BN BW RN BE BS'
        self.assertEqual(15, len(path.split()))
        self.assertEqual(ref_path, path)
        self.assertTrue(aspi_r.check_cleaning(path))

    def test_Aspi_R_clean_Aspi_R_case_7(self):

        aspi_r = AspiR("0_Inputs/Case_Aspi_R_7.txt")
        aspi_r.write_svg("Case_Aspi_R_7.svg")
        path = aspi_r.clean()
        print(path)
        aspi_r.write_svg("Case_Aspi_R_7_w_results.svg", path)
        ref_path = 'BE RS RW BS RE RN RE RS BE BN BW BS BW BN'
        self.assertEqual(14, len(path.split()))
        self.assertEqual(ref_path, path)
        self.assertTrue(aspi_r.check_cleaning(path))

if __name__ == '__main__':
    unittest.main()
