#! /usr/bin/python
# -*-coding:utf-8 -*-
# import unittest
# # from jieku_kuang.data.duqu import denglu
# # from jieku_kuang.config.login import deng
# # class qwe(unittest.TestCase):
# #     data=denglu().data()
# #     request=deng().get
# #     def test_1(self):
# #         aa=self.request(self.data[0][0],self.data[0][1])
# #         self.assertEqual(aa['code'],0)
# #     def test_2(self):
# #         for i in range(1,len(self.data)):
# #             bb = self.request(self.data[i][0],self.data[i][1])
# #             self.assertNotAlmostEqual(bb['code'],0)
# # if __name__=="__main__":
# #     unittest.main()
import unittest
from jieku_kuang.data.duqu import Shuju
from jieku_kuang.config.login import qingqiu
class qwe(unittest.TestCase):
    shuju=Shuju().shuju()
    denglu=qingqiu().denglu()
    def test_1(self):
        qq=self.denglu(int(self.shuju[0][0]),int(self.shuju[1][0]))
        self.assertEqual(qq['code'],'0')
        self.assertEqual(qq['msg'],'ok')
    def test_2(self):
        for i in range(1,len(self.shuju)):
            ww=self.denglu(int(self.shuju[i][0]),int(self.shuju[i][1]))
            self.assertNotAlmostEqual(ww['code'],'0')
            self.assertNotAlmostEqual(ww['msg'],'ok')
if __name__ == '__main__':
    unittest.main()