twaddress - 台灣地址中翻英
--------------------------

把中文地址翻譯成英文。使用最大正向匹配。

Usage
-----

```python
>>> import twaddress
>>> twaddress.get('高雄市前鎮區成功二路25號5樓之1')
'5F-1, No. 25, Chenggong 2nd Rd., Qianzhen Dist., Kaohsiung City 806, Taiwan (R.O.C.)'
```

Notes
-----
為了方便使用,地址中不會有傳統文字'臺',請先自行轉換。

This project is forked from mlouielu/twaddress.
I only added a helper function and a couple of tests.
Also packaged so this can be installed using pip.
