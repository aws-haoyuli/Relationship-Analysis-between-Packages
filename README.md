# Relationship-Analysis-between-Packages
Research on the relationship between packages in Python.


以下为统计、分析结果：

## Github仓库中packages使用情况统计
在通过爬虫获取的1000个仓库中，统计它们使用的packages，最常被使用的packages为：
<table>
    <thead> 
        <thead>
        <tr>
			<th>序号</th>
            <th>package名</th>
            <th>被使用次数</th>
        </tr>
    </thead>
<tbody>

<tr>
<td> 1 </td>
<td> os </td>
<td> 419 </td>
</tr>
<tr>
<td> 2 </td>
<td> sys </td>
<td> 366 </td>
</tr>
<tr>
<td> 3 </td>
<td> time </td>
<td> 183 </td>
</tr>
<tr>
<td> 4 </td>
<td> numpy </td>
<td> 180 </td>
</tr>
<tr>
<td> 5 </td>
<td> re </td>
<td> 136 </td>
</tr>
<tr>
<td> 6 </td>
<td> json </td>
<td> 118 </td>
</tr>
<tr>
<td> 7 </td>
<td> setuptools </td>
<td> 117 </td>
</tr>
<tr>
<td> 8 </td>
<td> datetime </td>
<td> 112 </td>
</tr>
<tr>
<td> 9 </td>
<td> django </td>
<td> 95 </td>
</tr>
<tr>
<td> 10 </td>
<td> random </td>
<td> 89 </td>
</tr>
<tr>
<td> 11 </td>
<td> logging </td>
<td> 89 </td>
</tr>
<tr>
<td> 12 </td>
<td> matplotlib </td>
<td> 83 </td>
</tr>
<tr>
<td> 13 </td>
<td> requests </td>
<td> 82 </td>
</tr>
<tr>
<td> 14 </td>
<td> argparse </td>
<td> 78 </td>
</tr>
<tr>
<td> 15 </td>
<td> __future__ </td>
<td> 76 </td>
</tr>
<tr>
<td> 16 </td>
<td> math </td>
<td> 69 </td>
</tr>
<tr>
<td> 17 </td>
<td> subprocess </td>
<td> 64 </td>
</tr>
<tr>
<td> 18 </td>
<td> pandas </td>
<td> 63 </td>
</tr>
<tr>
<td> 19 </td>
<td> unittest </td>
<td> 59 </td>
</tr>
<tr>
<td> 20 </td>
<td> urllib </td>
<td> 57 </td>
</tr>
<tr>
<td> 21 </td>
<td> collections </td>
<td> 53 </td>
</tr>
<tr>
<td> 22 </td>
<td> tensorflow </td>
<td> 48 </td>
</tr>
<tr>
<td> 23 </td>
<td> sklearn </td>
<td> 47 </td>
</tr>
<tr>
<td> 24 </td>
<td> flask </td>
<td> 44 </td>
</tr>
<tr>
<td> 25 </td>
<td> distutils </td>
<td> 41 </td>
</tr>
<tr>
<td> 26 </td>
<td> threading </td>
<td> 39 </td>
</tr>
<tr>
<td> 27 </td>
<td> scipy </td>
<td> 37 </td>
</tr>
<tr>
<td> 28 </td>
<td> shutil </td>
<td> 36 </td>
</tr>
<tr>
<td> 29 </td>
<td> csv </td>
<td> 35 </td>
</tr>
<tr>
<td> 30 </td>
<td> hashlib </td>
<td> 33 </td>
</tr>

</tbody>
</table>

## 同时出现在一个工程中的packages统计
在通过爬虫获取的1000个仓库中，统计它们使用的packages，最常被使用在同一个工程中的packages对为：

<table>
    <thead> 
        <thead>
        <tr>
			<th>序号</th>
            <th>package-1</th>
            <th>package-2</th>
            <th>同时出现次数</th>
        </tr>
    </thead>
<tbody>
<tr>
<td> 1 </td>
<td> os </td>
<td> sys </td>
<td> 283 </td>
</tr>
<tr>
<td> 2 </td>
<td> os </td>
<td> time </td>
<td> 118 </td>
</tr>
<tr>
<td> 3 </td>
<td> os </td>
<td> re </td>
<td> 101 </td>
</tr>
<tr>
<td> 4 </td>
<td> time </td>
<td> sys </td>
<td> 97 </td>
</tr>
<tr>
<td> 5 </td>
<td> os </td>
<td> django </td>
<td> 93 </td>
</tr>
<tr>
<td> 6 </td>
<td> django </td>
<td> sys </td>
<td> 91 </td>
</tr>
<tr>
<td> 7 </td>
<td> numpy </td>
<td> matplotlib </td>
<td> 86 </td>
</tr>
<tr>
<td> 8 </td>
<td> re </td>
<td> sys </td>
<td> 86 </td>
</tr>
<tr>
<td> 9 </td>
<td> os </td>
<td> numpy </td>
<td> 82 </td>
</tr>
<tr>
<td> 10 </td>
<td> logging </td>
<td> os </td>
<td> 73 </td>
</tr>
<tr>
<td> 11 </td>
<td> os </td>
<td> datetime </td>
<td> 70 </td>
</tr>
<tr>
<td> 12 </td>
<td> os </td>
<td> json </td>
<td> 70 </td>
</tr>
<tr>
<td> 13 </td>
<td> os </td>
<td> setuptools </td>
<td> 66 </td>
</tr>
<tr>
<td> 14 </td>
<td> numpy </td>
<td> sys </td>
<td> 66 </td>
</tr>
<tr>
<td> 15 </td>
<td> datetime </td>
<td> sys </td>
<td> 60 </td>
</tr>
<tr>
<td> 16 </td>
<td> os </td>
<td> argparse </td>
<td> 60 </td>
</tr>
<tr>
<td> 17 </td>
<td> json </td>
<td> sys </td>
<td> 57 </td>
</tr>
<tr>
<td> 18 </td>
<td> os </td>
<td> __future__ </td>
<td> 57 </td>
</tr>
<tr>
<td> 19 </td>
<td> time </td>
<td> re </td>
<td> 55 </td>
</tr>
<tr>
<td> 20 </td>
<td> os </td>
<td> subprocess </td>
<td> 54 </td>
</tr>
<tr>
<td> 21 </td>
<td> numpy </td>
<td> sklearn </td>
<td> 53 </td>
</tr>
<tr>
<td> 22 </td>
<td> time </td>
<td> datetime </td>
<td> 52 </td>
</tr>
<tr>
<td> 23 </td>
<td> time </td>
<td> json </td>
<td> 51 </td>
</tr>
<tr>
<td> 24 </td>
<td> pandas </td>
<td> numpy </td>
<td> 50 </td>
</tr>
<tr>
<td> 25 </td>
<td> logging </td>
<td> sys </td>
<td> 49 </td>
</tr>
<tr>
<td> 26 </td>
<td> os </td>
<td> random </td>
<td> 49 </td>
</tr>
<tr>
<td> 27 </td>
<td> sys </td>
<td> subprocess </td>
<td> 48 </td>
</tr>
<tr>
<td> 28 </td>
<td> argparse </td>
<td> sys </td>
<td> 48 </td>
</tr>
<tr>
<td> 29 </td>
<td> __future__ </td>
<td> sys </td>
<td> 48 </td>
</tr>
<tr>
<td> 30 </td>
<td> sys </td>
<td> __future__ </td>
<td> 48 </td>
</tr>
<tr>
<td> 31 </td>
<td> sklearn </td>
<td> matplotlib </td>
<td> 46 </td>
</tr>
<tr>
<td> 32 </td>
<td> os </td>
<td> requests </td>
<td> 45 </td>
</tr>
<tr>
<td> 33 </td>
<td> numpy </td>
<td> tensorflow </td>
<td> 45 </td>
</tr>
<tr>
<td> 34 </td>
<td> time </td>
<td> numpy </td>
<td> 44 </td>
</tr>
<tr>
<td> 35 </td>
<td> logging </td>
<td> time </td>
<td> 43 </td>
</tr>
<tr>
<td> 36 </td>
<td> os </td>
<td> matplotlib </td>
<td> 42 </td>
</tr>
<tr>
<td> 37 </td>
<td> math </td>
<td> sys </td>
<td> 40 </td>
</tr>
<tr>
<td> 38 </td>
<td> setuptools </td>
<td> sys </td>
<td> 39 </td>
</tr>
<tr>
<td> 39 </td>
<td> re </td>
<td> json </td>
<td> 39 </td>
</tr>
<tr>
<td> 40 </td>
<td> datetime </td>
<td> json </td>
<td> 38 </td>
</tr>
</tbody>
</table>

## GitHub上仓库使用的协议统计

在通过爬虫获取的16800个仓库中，使用协议的统计情况（协议项为None的在统计中会被忽略）：
<table>
    <thead> 
        <thead>
        <tr>
            <th>协议名</th>
            <th>仓库数</th>
            <th>百分比</th>
        </tr>
    </thead>
<tbody>
<tr>
<td> MIT License </td>
<td> 4736 </td>
<td> 38.90% </td>
</tr>
<tr>
<td> Apache License 2.0 </td>
<td> 1558 </td>
<td> 12.80% </td>
</tr>
<tr>
<td> Other </td>
<td> 1551 </td>
<td> 12.74% </td>
</tr>
<tr>
<td> BSD 3-clause "New" or "Revised" License </td>
<td> 1478 </td>
<td> 12.14% </td>
</tr>
<tr>
<td> GNU General Public License v3.0 </td>
<td> 1157 </td>
<td> 9.50% </td>
</tr>
<tr>
<td> GNU General Public License v2.0 </td>
<td> 532 </td>
<td> 4.37% </td>
</tr>
<tr>
<td> BSD 2-clause "Simplified" License </td>
<td> 433 </td>
<td> 3.56% </td>
</tr>
<tr>
<td> GNU Affero General Public License v3.0 </td>
<td> 191 </td>
<td> 1.57% </td>
</tr>
<tr>
<td> GNU Lesser General Public License v3.0 </td>
<td> 133 </td>
<td> 1.09% </td>
</tr>
<tr>
<td> The Unlicense </td>
<td> 96 </td>
<td> 0.79% </td>
</tr>
<tr>
<td> ISC License </td>
<td> 80 </td>
<td> 0.66% </td>
</tr>
<tr>
<td> GNU Lesser General Public License v2.1 </td>
<td> 67 </td>
<td> 0.55% </td>
</tr>
<tr>
<td> Do What The F*ck You Want To Public License </td>
<td> 48 </td>
<td> 0.39% </td>
</tr>
<tr>
<td> Creative Commons Zero v1.0 Universal </td>
<td> 40 </td>
<td> 0.33% </td>
</tr>
<tr>
<td> Mozilla Public License 2.0 </td>
<td> 37 </td>
<td> 0.30% </td>
</tr>
<tr>
<td> SIL Open Font License 1.1 </td>
<td> 12 </td>
<td> 0.10% </td>
</tr>
<tr>
<td> Eclipse Public License 1.0 </td>
<td> 6 </td>
<td> 0.05% </td>
</tr>
<tr>
<td> Creative Commons Attribution Share Alike 4.0 </td>
<td> 5 </td>
<td> 0.04% </td>
</tr>
<tr>
<td> zlib License </td>
<td> 4 </td>
<td> 0.03% </td>
</tr>
<tr>
<td> Creative Commons Attribution 4.0 </td>
<td> 3 </td>
<td> 0.02% </td>
</tr>
<tr>
<td> Artistic License 2.0 </td>
<td> 2 </td>
<td> 0.02% </td>
</tr>
<tr>
<td> BSD 3-clause Clear License </td>
<td> 2 </td>
<td> 0.02% </td>
</tr>
<tr>
<td> Open Software License 3.0 </td>
<td> 1 </td>
<td> 0.01% </td>
</tr>
<tr>
<td> European Union Public License 1.1 </td>
<td> 1 </td>
<td> 0.01% </td>
</tr>
<tr>
<td> PostgreSQL License </td>
<td> 1 </td>
<td> 0.01% </td>
</tr>
</tbody>
</table>