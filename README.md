# Cut Order Plan Optimization in Apparel Industry

Cut order planning (COP) plays an important role in managing fabric costs and setting up for starting a new section in the manufacturing process. An efficient COP solution can significantly reduce the total manufacturing cost in the apparel industry. In most countries, the cut order plan had been done by the traditional approach. The main purpose of this project was to find the optimal Cut Order Plan ( or Marker Plan) for a specific order quantity. In this project, I have followed the "[Hybrid heuristics for the cut ordering planning problem in the apparel industry](https://www.sciencedirect.com/science/article/abs/pii/S0360835220302126)" research paper. The codes were written in Python.

## The Input of this Code:

| Size | Demand | Lenght Consumition (Yard) |
| :---: | :---: | :---: |
| XS   | 1686 | 1.01 |
| S   | 4310 | 1.08 |
| M   | 4228 | 1.15 |
| L   | 2924 | 1.21 |
| XL   | 1946 | 1.42 |

Cutter Max Height = 200 (yrd), Cutter Min Height = 10 (yrd) and Lay Lenght = 22 (yrd)

## The Output of this Code (The Cut Order Plan):

| Marker<br>Plan No.| XS | S | M | L | XL | Plies | Yards | Inchs | Total Fabric<br>Used |
|:-:|:-:|:-:|:-:|:-:|:---:|:-----:|:-----:|:-----:|:-----------------:| 
| 1 | 2 | 18 | 0 | 0 | 0 | 23 | 21 | 17 | 494 |
| 2	|2 | 7 | 6 | 4 | 0 | 193 | 21 | 12 | 4115 |
| 3	|18 | 3 | 0 | 0 | 0 | 67 | 21 | 15 | 1436 |
| 4	|0	|10|	9	|0	|0	|195	|21	|5	|4125 |
| 5	|0	|0	|9	|2	|6	|138	|21	|10	|2939 |
| 6	|0	|3	|0	|15	|0	|91	|21	|14|	1947 |
| 7	|0	|1	|0	|4	|9	|116	|18	|25	|2170 |
| 8	|0	|0	|1|	0|	0|	54	|1|	5	|63 |
| 9	|4	|1	|1|	4	|7	|10	|21	|2	|211 |
| **Total**| **1688** | **4315**	| **4229**	| **2927**	| **1952**	| 897	| 170	| 133 | **17548**|

