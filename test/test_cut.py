# -*- coding: utf-8 -*-

import unittest
import twaddress


@unittest.skip('Just skip...')
class CutTest(unittest.TestCase):
    def test_short_address(self):
        expect = ['高雄市', '三民區', '建工路', '415號']
        self.assertEqual(twaddress.cut('高雄市三民區建工路415號'), expect)

    def test_normal_address(self):
        expect = ['高雄市', '前鎮區', '成功二路', '25號', '5樓之1']
        self.assertEqual(twaddress.cut('高雄市前鎮區成功二路25號5樓之1'), expect)

    def test_hard_address(self):
        expect = []
        self.assertEqual(twaddress.cut('嘉義市溪興街153巷12弄25號5樓3室'), expect)

    def test_sections_numbers(self):
        expect = ('114', 'Neihu Dist., Taipei City', 'Sec. 1, Neihu Rd.', '', {'巷': '', '弄': '', '號': '306', '樓': '', '室': ''})
        cut_result = twaddress.cut('台北市內湖區內湖路1段306號')
        print(cut_result)
        self.assertEqual(cut_result, expect)


class GetTest(unittest.TestCase):
    def test_hard_address(self):
        expect = ('50F-60, No.30, Aly. 20, Ln. 10, Qixian 1st Rd., '
                  'Xinxing Dist., Kaohsiung City 800, Taiwan (R.O.C.)')
        self.assertEqual(twaddress.get('高雄市新興區七賢一路10巷20弄30號50樓之60'), expect)

    def test_sections_numbers(self):
        expect = "No.306, Sec. 1, Neihu Rd., Neihu Dist., Taipei City 114, Taiwan (R.O.C.)"
        get_result_1 = twaddress.get("台北市內湖區內湖路1段306號")
        get_result_2 = twaddress.get("台北市內湖區內湖路一段306號")
        self.assertEqual(get_result_1, expect)
        self.assertEqual(get_result_2, expect)
