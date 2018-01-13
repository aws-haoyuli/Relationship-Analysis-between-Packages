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


## Stackoverflow36k个问题中包出现情况
<table>
    <thead> 
        <thead>
        <tr>
            <th>序号</th>
            <th>包名</th>
            <th>出现次数</th>
        </tr>
    </thead>
<tbody>

<tr><td>0</td><td>numpy</td><td>2229</td></tr><tr><td>1</td><td>pandas</td><td>1902</td></tr><tr><td>2</td><td>matplotlib</td><td>1584</td></tr><tr><td>3</td><td>string</td><td>797</td></tr><tr><td>4</td><td>scipy</td><td>654</td></tr><tr><td>5</td><td>regex</td><td>527</td></tr><tr><td>6</td><td>tkinter</td><td>478</td></tr><tr><td>7</td><td>pip</td><td>474</td></tr><tr><td>8</td><td>json</td><td>401</td></tr><tr><td>9</td><td>opencv</td><td>396</td></tr><tr><td>10</td><td>csv</td><td>386</td></tr><tr><td>11</td><td>sqlalchemy</td><td>378</td></tr><tr><td>12</td><td>datetime</td><td>359</td></tr><tr><td>13</td><td>subprocess</td><td>348</td></tr><tr><td>14</td><td>multiprocessing</td><td>345</td></tr><tr><td>15</td><td>tensorflow</td><td>340</td></tr><tr><td>16</td><td>virtualenv</td><td>297</td></tr><tr><td>17</td><td>scikit-learn</td><td>289</td></tr><tr><td>18</td><td>pyqt</td><td>276</td></tr><tr><td>19</td><td>ipython</td><td>264</td></tr><tr><td>20</td><td>html</td><td>261</td></tr><tr><td>21</td><td>nltk</td><td>223</td></tr><tr><td>22</td><td>logging</td><td>202</td></tr><tr><td>23</td><td>lxml</td><td>174</td></tr><tr><td>24</td><td>math</td><td>170</td></tr><tr><td>25</td><td>pyqt4</td><td>167</td></tr><tr><td>26</td><td>cython</td><td>161</td></tr><tr><td>27</td><td>pickle</td><td>149</td></tr><tr><td>28</td><td>pygame</td><td>142</td></tr><tr><td>29</td><td>random</td><td>139</td></tr><tr><td>30</td><td>argparse</td><td>133</td></tr><tr><td>31</td><td>ctypes</td><td>132</td></tr><tr><td>32</td><td>setuptools</td><td>127</td></tr><tr><td>33</td><td>wxpython</td><td>124</td></tr><tr><td>34</td><td>jinja2</td><td>115</td></tr><tr><td>35</td><td>twisted</td><td>115</td></tr><tr><td>36</td><td>time</td><td>107</td></tr><tr><td>37</td><td>email</td><td>104</td></tr><tr><td>38</td><td>tornado</td><td>95</td></tr><tr><td>39</td><td>ssl</td><td>89</td></tr><tr><td>40</td><td>distutils</td><td>84</td></tr><tr><td>41</td><td>py2exe</td><td>82</td></tr><tr><td>42</td><td>mysql-python</td><td>81</td></tr><tr><td>43</td><td>sqlite3</td><td>80</td></tr><tr><td>44</td><td>networkx</td><td>73</td></tr><tr><td>45</td><td>io</td><td>72</td></tr><tr><td>46</td><td>pymongo</td><td>69</td></tr><tr><td>47</td><td>pywin32</td><td>63</td></tr><tr><td>48</td><td>types</td><td>62</td></tr><tr><td>49</td><td>pyside</td><td>62</td></tr><tr><td>50</td><td>pygtk</td><td>57</td></tr><tr><td>51</td><td>kivy</td><td>57</td></tr><tr><td>52</td><td>queue</td><td>54</td></tr><tr><td>53</td><td>pyodbc</td><td>51</td></tr><tr><td>54</td><td>jupyter</td><td>51</td></tr><tr><td>55</td><td>itertools</td><td>49</td></tr><tr><td>56</td><td>cgi</td><td>48</td></tr><tr><td>57</td><td>pytz</td><td>41</td></tr><tr><td>58</td><td>nose</td><td>41</td></tr><tr><td>59</td><td>gevent</td><td>41</td></tr><tr><td>60</td><td>sympy</td><td>40</td></tr><tr><td>61</td><td>pdb</td><td>39</td></tr><tr><td>62</td><td>console</td><td>38</td></tr><tr><td>63</td><td>pyserial</td><td>38</td></tr><tr><td>64</td><td>bokeh</td><td>38</td></tr><tr><td>65</td><td>statsmodels</td><td>37</td></tr><tr><td>66</td><td>pillow</td><td>35</td></tr><tr><td>67</td><td>decimal</td><td>34</td></tr><tr><td>68</td><td>theano</td><td>34</td></tr><tr><td>69</td><td>copy</td><td>32</td></tr><tr><td>70</td><td>spyder</td><td>31</td></tr><tr><td>71</td><td>pytables</td><td>30</td></tr><tr><td>72</td><td>reportlab</td><td>28</td></tr><tr><td>73</td><td>numbers</td><td>27</td></tr><tr><td>74</td><td>rpy2</td><td>27</td></tr><tr><td>75</td><td>zipfile</td><td>26</td></tr><tr><td>76</td><td>pyyaml</td><td>25</td></tr><tr><td>77</td><td>base64</td><td>24</td></tr><tr><td>78</td><td>warnings</td><td>24</td></tr><tr><td>79</td><td>h5py</td><td>24</td></tr><tr><td>80</td><td>heatmap</td><td>23</td></tr><tr><td>81</td><td>pycurl</td><td>23</td></tr><tr><td>82</td><td>collections</td><td>22</td></tr><tr><td>83</td><td>cmd</td><td>22</td></tr><tr><td>84</td><td>pyparsing</td><td>22</td></tr><tr><td>85</td><td>gzip</td><td>21</td></tr><tr><td>86</td><td>struct</td><td>21</td></tr><tr><td>87</td><td>smtplib</td><td>20</td></tr><tr><td>88</td><td>keyword</td><td>19</td></tr><tr><td>89</td><td>simplejson</td><td>19</td></tr><tr><td>90</td><td>ftplib</td><td>19</td></tr><tr><td>91</td><td>configparser</td><td>19</td></tr><tr><td>92</td><td>readline</td><td>19</td></tr><tr><td>93</td><td>scikit-image</td><td>18</td></tr><tr><td>94</td><td>pyaudio</td><td>18</td></tr><tr><td>95</td><td>python-dateutil</td><td>18</td></tr><tr><td>96</td><td>numba</td><td>18</td></tr><tr><td>97</td><td>sys</td><td>17</td></tr><tr><td>98</td><td>select</td><td>17</td></tr><tr><td>99</td><td>gensim</td><td>17</td></tr><tr><td>100</td><td>mercurial</td><td>17</td></tr>
</tbody>
</table>
## StackOverflow中同一问题下包出现情况：
<table>
    <thead> 
        <thead>
        <tr>
            <th>序号</th>
            <th>package1</th>
            <th>package2</th>
            <th>出现次数</th>
        </tr>
    </thead>
<tbody>

<tr><td>1</td><td>numpy</td><td>scipy</td><td>790</td></tr><tr><td>2</td><td>numpy</td><td>pandas</td><td>430</td></tr><tr><td>3</td><td>matplotlib</td><td>numpy</td><td>384</td></tr><tr><td>4</td><td>matplotlib</td><td>pandas</td><td>288</td></tr><tr><td>5</td><td>matplotlib</td><td>scipy</td><td>146</td></tr><tr><td>6</td><td>pyqt4</td><td>pyqt</td><td>146</td></tr><tr><td>7</td><td>pip</td><td>virtualenv</td><td>138</td></tr><tr><td>8</td><td>csv</td><td>pandas</td><td>126</td></tr><tr><td>9</td><td>datetime</td><td>pandas</td><td>104</td></tr><tr><td>10</td><td>regex</td><td>string</td><td>92</td></tr><tr><td>11</td><td>cython</td><td>numpy</td><td>92</td></tr><tr><td>12</td><td>scikit-learn</td><td>numpy</td><td>90</td></tr><tr><td>13</td><td>opencv</td><td>numpy</td><td>86</td></tr><tr><td>14</td><td>setuptools</td><td>pip</td><td>64</td></tr><tr><td>15</td><td>matplotlib</td><td>ipython</td><td>62</td></tr><tr><td>16</td><td>pyqt</td><td>pyside</td><td>62</td></tr><tr><td>17</td><td>setuptools</td><td>distutils</td><td>60</td></tr><tr><td>18</td><td>scikit-learn</td><td>pandas</td><td>60</td></tr><tr><td>19</td><td>numpy</td><td>math</td><td>60</td></tr><tr><td>20</td><td>pandas</td><td>ipython</td><td>56</td></tr><tr><td>21</td><td>jupyter</td><td>ipython</td><td>54</td></tr><tr><td>22</td><td>csv</td><td>numpy</td><td>54</td></tr><tr><td>23</td><td>datetime</td><td>time</td><td>50</td></tr><tr><td>24</td><td>pandas</td><td>scipy</td><td>50</td></tr><tr><td>25</td><td>tkinter</td><td>matplotlib</td><td>44</td></tr><tr><td>26</td><td>pip</td><td>numpy</td><td>44</td></tr><tr><td>27</td><td>random</td><td>numpy</td><td>44</td></tr><tr><td>28</td><td>multiprocessing</td><td>numpy</td><td>42</td></tr><tr><td>29</td><td>matplotlib</td><td>heatmap</td><td>38</td></tr><tr><td>30</td><td>datetime</td><td>pytz</td><td>36</td></tr><tr><td>31</td><td>numpy</td><td>tensorflow</td><td>36</td></tr><tr><td>32</td><td>json</td><td>pandas</td><td>34</td></tr><tr><td>33</td><td>queue</td><td>multiprocessing</td><td>34</td></tr><tr><td>34</td><td>scikit-learn</td><td>scipy</td><td>34</td></tr><tr><td>35</td><td>statsmodels</td><td>pandas</td><td>30</td></tr><tr><td>36</td><td>pytables</td><td>pandas</td><td>30</td></tr><tr><td>37</td><td>pandas</td><td>string</td><td>30</td></tr><tr><td>38</td><td>numba</td><td>numpy</td><td>30</td></tr><tr><td>39</td><td>multiprocessing</td><td>pickle</td><td>28</td></tr><tr><td>40</td><td>networkx</td><td>matplotlib</td><td>28</td></tr><tr><td>41</td><td>scipy</td><td>math</td><td>28</td></tr><tr><td>42</td><td>simplejson</td><td>json</td><td>26</td></tr><tr><td>43</td><td>h5py</td><td>numpy</td><td>24</td></tr><tr><td>44</td><td>pyqt</td><td>matplotlib</td><td>24</td></tr><tr><td>45</td><td>datetime</td><td>numpy</td><td>24</td></tr><tr><td>46</td><td>sympy</td><td>numpy</td><td>24</td></tr><tr><td>47</td><td>email</td><td>smtplib</td><td>22</td></tr><tr><td>48</td><td>statsmodels</td><td>numpy</td><td>20</td></tr><tr><td>49</td><td>pip</td><td>distutils</td><td>20</td></tr><tr><td>50</td><td>pytables</td><td>numpy</td><td>20</td></tr><tr><td>51</td><td>pickle</td><td>numpy</td><td>20</td></tr><tr><td>52</td><td>pandas</td><td>sqlalchemy</td><td>20</td></tr><tr><td>53</td><td>distutils</td><td>cython</td><td>20</td></tr><tr><td>54</td><td>datetime</td><td>matplotlib</td><td>20</td></tr><tr><td>55</td><td>html</td><td>regex</td><td>20</td></tr><tr><td>56</td><td>ctypes</td><td>numpy</td><td>18</td></tr><tr><td>57</td><td>pyqt4</td><td>pyside</td><td>18</td></tr><tr><td>58</td><td>csv</td><td>json</td><td>16</td></tr><tr><td>59</td><td>opencv</td><td>matplotlib</td><td>16</td></tr><tr><td>60</td><td>lxml</td><td>html</td><td>16</td></tr><tr><td>61</td><td>ode</td><td>scipy</td><td>16</td></tr><tr><td>62</td><td>sympy</td><td>scipy</td><td>16</td></tr><tr><td>63</td><td>matplotlib</td><td>wxpython</td><td>16</td></tr><tr><td>64</td><td>setuptools</td><td>virtualenv</td><td>14</td></tr><tr><td>65</td><td>pip</td><td>lxml</td><td>14</td></tr><tr><td>66</td><td>numpy</td><td>ipython</td><td>14</td></tr><tr><td>67</td><td>html</td><td>pandas</td><td>14</td></tr><tr><td>68</td><td>pip</td><td>matplotlib</td><td>14</td></tr><tr><td>69</td><td>json</td><td>pickle</td><td>14</td></tr><tr><td>70</td><td>json</td><td>string</td><td>14</td></tr><tr><td>71</td><td>virtualenv</td><td>matplotlib</td><td>14</td></tr><tr><td>72</td><td>pyqt4</td><td>matplotlib</td><td>14</td></tr><tr><td>73</td><td>datetime</td><td>string</td><td>14</td></tr><tr><td>74</td><td>pymongo</td><td>json</td><td>14</td></tr><tr><td>75</td><td>html</td><td>jinja2</td><td>14</td></tr><tr><td>76</td><td>statsmodels</td><td>scipy</td><td>14</td></tr><tr><td>77</td><td>pip</td><td>mysql-python</td><td>12</td></tr><tr><td>78</td><td>multiprocessing</td><td>subprocess</td><td>12</td></tr><tr><td>79</td><td>py2exe</td><td>pyqt</td><td>12</td></tr><tr><td>80</td><td>tkinter</td><td>wxpython</td><td>12</td></tr><tr><td>81</td><td>spyder</td><td>matplotlib</td><td>12</td></tr><tr><td>82</td><td>random</td><td>string</td><td>12</td></tr><tr><td>83</td><td>nltk</td><td>tokenize</td><td>12</td></tr><tr><td>84</td><td>json</td><td>html</td><td>12</td></tr><tr><td>85</td><td>pip</td><td>tensorflow</td><td>12</td></tr><tr><td>86</td><td>opencv</td><td>scikit-image</td><td>12</td></tr><tr><td>87</td><td>regex</td><td>pandas</td><td>10</td></tr><tr><td>88</td><td>csv</td><td>string</td><td>10</td></tr><tr><td>89</td><td>pip</td><td>pygame</td><td>10</td></tr><tr><td>90</td><td>nltk</td><td>regex</td><td>10</td></tr><tr><td>91</td><td>types</td><td>pandas</td><td>10</td></tr><tr><td>92</td><td>pandas</td><td>heatmap</td><td>10</td></tr><tr><td>93</td><td>numpy</td><td>string</td><td>10</td></tr><tr><td>94</td><td>py2exe</td><td>wxpython</td><td>10</td></tr><tr><td>95</td><td>ctypes</td><td>pywin32</td><td>10</td></tr><tr><td>96</td><td>tkinter</td><td>pygame</td><td>10</td></tr><tr><td>97</td><td>sympy</td><td>matplotlib</td><td>10</td></tr><tr><td>98</td><td>io</td><td>pandas</td><td>10</td></tr><tr><td>99</td><td>scikit-learn</td><td>multiprocessing</td><td>10</td></tr><tr><td>100</td><td>pip</td><td>ipython</td><td>10</td></tr>
</tbody>
</table>
