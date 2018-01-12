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

<tr><td>0</td><td>numpy</td><td>2229</td></tr><tr><td>1</td><td>pandas</td><td>1902</td></tr><tr><td>2</td><td>matplotlib</td><td>1584</td></tr><tr><td>3</td><td>string</td><td>797</td></tr><tr><td>4</td><td>scipy</td><td>654</td></tr><tr><td>5</td><td>regex</td><td>527</td></tr><tr><td>6</td><td>tkinter</td><td>478</td></tr><tr><td>7</td><td>pip</td><td>474</td></tr><tr><td>8</td><td>json</td><td>401</td></tr><tr><td>9</td><td>opencv</td><td>396</td></tr><tr><td>10</td><td>csv</td><td>386</td></tr><tr><td>11</td><td>sqlalchemy</td><td>378</td></tr><tr><td>12</td><td>datetime</td><td>359</td></tr><tr><td>13</td><td>subprocess</td><td>348</td></tr><tr><td>14</td><td>multiprocessing</td><td>345</td></tr><tr><td>15</td><td>tensorflow</td><td>340</td></tr><tr><td>16</td><td>virtualenv</td><td>297</td></tr><tr><td>17</td><td>scikit-learn</td><td>289</td></tr><tr><td>18</td><td>pyqt</td><td>276</td></tr><tr><td>19</td><td>ipython</td><td>264</td></tr><tr><td>20</td><td>html</td><td>261</td></tr><tr><td>21</td><td>nltk</td><td>223</td></tr><tr><td>22</td><td>logging</td><td>202</td></tr><tr><td>23</td><td>lxml</td><td>174</td></tr><tr><td>24</td><td>math</td><td>170</td></tr><tr><td>25</td><td>pyqt4</td><td>167</td></tr><tr><td>26</td><td>cython</td><td>161</td></tr><tr><td>27</td><td>pickle</td><td>149</td></tr><tr><td>28</td><td>pygame</td><td>142</td></tr><tr><td>29</td><td>random</td><td>139</td></tr><tr><td>30</td><td>argparse</td><td>133</td></tr><tr><td>31</td><td>ctypes</td><td>132</td></tr><tr><td>32</td><td>setuptools</td><td>127</td></tr><tr><td>33</td><td>wxpython</td><td>124</td></tr><tr><td>34</td><td>jinja2</td><td>115</td></tr><tr><td>35</td><td>twisted</td><td>115</td></tr><tr><td>36</td><td>time</td><td>107</td></tr><tr><td>37</td><td>email</td><td>104</td></tr><tr><td>38</td><td>tornado</td><td>95</td></tr><tr><td>39</td><td>ssl</td><td>89</td></tr><tr><td>40</td><td>distutils</td><td>84</td></tr><tr><td>41</td><td>py2exe</td><td>82</td></tr><tr><td>42</td><td>mysql-python</td><td>81</td></tr><tr><td>43</td><td>sqlite3</td><td>80</td></tr><tr><td>44</td><td>networkx</td><td>73</td></tr><tr><td>45</td><td>io</td><td>72</td></tr><tr><td>46</td><td>pymongo</td><td>69</td></tr><tr><td>47</td><td>pywin32</td><td>63</td></tr><tr><td>48</td><td>types</td><td>62</td></tr><tr><td>49</td><td>pyside</td><td>62</td></tr><tr><td>50</td><td>pygtk</td><td>57</td></tr><tr><td>51</td><td>kivy</td><td>57</td></tr><tr><td>52</td><td>queue</td><td>54</td></tr><tr><td>53</td><td>pyodbc</td><td>51</td></tr><tr><td>54</td><td>jupyter</td><td>51</td></tr><tr><td>55</td><td>itertools</td><td>49</td></tr><tr><td>56</td><td>cgi</td><td>48</td></tr><tr><td>57</td><td>pytz</td><td>41</td></tr><tr><td>58</td><td>nose</td><td>41</td></tr><tr><td>59</td><td>gevent</td><td>41</td></tr><tr><td>60</td><td>sympy</td><td>40</td></tr><tr><td>61</td><td>pdb</td><td>39</td></tr><tr><td>62</td><td>console</td><td>38</td></tr><tr><td>63</td><td>pyserial</td><td>38</td></tr><tr><td>64</td><td>bokeh</td><td>38</td></tr><tr><td>65</td><td>statsmodels</td><td>37</td></tr><tr><td>66</td><td>pillow</td><td>35</td></tr><tr><td>67</td><td>decimal</td><td>34</td></tr><tr><td>68</td><td>theano</td><td>34</td></tr><tr><td>69</td><td>copy</td><td>32</td></tr><tr><td>70</td><td>spyder</td><td>31</td></tr><tr><td>71</td><td>pytables</td><td>30</td></tr><tr><td>72</td><td>reportlab</td><td>28</td></tr><tr><td>73</td><td>numbers</td><td>27</td></tr><tr><td>74</td><td>rpy2</td><td>27</td></tr><tr><td>75</td><td>zipfile</td><td>26</td></tr><tr><td>76</td><td>pyyaml</td><td>25</td></tr><tr><td>77</td><td>base64</td><td>24</td></tr><tr><td>78</td><td>warnings</td><td>24</td></tr><tr><td>79</td><td>h5py</td><td>24</td></tr><tr><td>80</td><td>heatmap</td><td>23</td></tr><tr><td>81</td><td>pycurl</td><td>23</td></tr><tr><td>82</td><td>collections</td><td>22</td></tr><tr><td>83</td><td>cmd</td><td>22</td></tr><tr><td>84</td><td>pyparsing</td><td>22</td></tr><tr><td>85</td><td>gzip</td><td>21</td></tr><tr><td>86</td><td>struct</td><td>21</td></tr><tr><td>87</td><td>smtplib</td><td>20</td></tr><tr><td>88</td><td>keyword</td><td>19</td></tr><tr><td>89</td><td>simplejson</td><td>19</td></tr><tr><td>90</td><td>ftplib</td><td>19</td></tr><tr><td>91</td><td>configparser</td><td>19</td></tr><tr><td>92</td><td>readline</td><td>19</td></tr><tr><td>93</td><td>scikit-image</td><td>18</td></tr><tr><td>94</td><td>pyaudio</td><td>18</td></tr><tr><td>95</td><td>python-dateutil</td><td>18</td></tr><tr><td>96</td><td>numba</td><td>18</td></tr><tr><td>97</td><td>sys</td><td>17</td></tr><tr><td>98</td><td>select</td><td>17</td></tr><tr><td>99</td><td>gensim</td><td>17</td></tr><tr><td>100</td><td>mercurial</td><td>17</td></tr><tr><td>101</td><td>timeit</td><td>16</td></tr><tr><td>102</td><td>traceback</td><td>16</td></tr><tr><td>103</td><td>locale</td><td>16</td></tr><tr><td>104</td><td>imaplib</td><td>16</td></tr><tr><td>105</td><td>inspect</td><td>15</td></tr><tr><td>106</td><td>mayavi</td><td>14</td></tr><tr><td>107</td><td>biopython</td><td>14</td></tr><tr><td>108</td><td>glob</td><td>13</td></tr><tr><td>109</td><td>xgboost</td><td>13</td></tr><tr><td>110</td><td>doctest</td><td>13</td></tr><tr><td>111</td><td>gettext</td><td>13</td></tr><tr><td>112</td><td>pyglet</td><td>13</td></tr><tr><td>113</td><td>calendar</td><td>13</td></tr><tr><td>114</td><td>hashlib</td><td>12</td></tr><tr><td>115</td><td>uuid</td><td>12</td></tr><tr><td>116</td><td>shapely</td><td>12</td></tr><tr><td>117</td><td>gdal</td><td>11</td></tr><tr><td>118</td><td>zlib</td><td>11</td></tr><tr><td>119</td><td>ode</td><td>11</td></tr><tr><td>120</td><td>tokenize</td><td>11</td></tr><tr><td>121</td><td>optparse</td><td>10</td></tr><tr><td>122</td><td>concurrent.futures</td><td>10</td></tr><tr><td>123</td><td>pygraphviz</td><td>10</td></tr><tr><td>124</td><td>libsvm</td><td>9</td></tr><tr><td>125</td><td>pymc</td><td>9</td></tr><tr><td>126</td><td>functools</td><td>8</td></tr><tr><td>127</td><td>socketserver</td><td>8</td></tr><tr><td>128</td><td>curses</td><td>8</td></tr><tr><td>129</td><td>mako</td><td>8</td></tr><tr><td>130</td><td>shelve</td><td>8</td></tr><tr><td>131</td><td>multiprocess</td><td>8</td></tr><tr><td>132</td><td>pyopengl</td><td>8</td></tr><tr><td>133</td><td>pymssql</td><td>8</td></tr><tr><td>134</td><td>wave</td><td>8</td></tr><tr><td>135</td><td>shutil</td><td>8</td></tr><tr><td>136</td><td>pty</td><td>7</td></tr><tr><td>137</td><td>mmap</td><td>7</td></tr><tr><td>138</td><td>vtk</td><td>7</td></tr><tr><td>139</td><td>polygon</td><td>7</td></tr><tr><td>140</td><td>difflib</td><td>7</td></tr><tr><td>141</td><td>hmac</td><td>7</td></tr><tr><td>142</td><td>posix</td><td>7</td></tr><tr><td>143</td><td>pyhook</td><td>6</td></tr><tr><td>144</td><td>numeric</td><td>6</td></tr><tr><td>145</td><td>abc</td><td>6</td></tr><tr><td>146</td><td>asyncore</td><td>6</td></tr><tr><td>147</td><td>pysqlite</td><td>6</td></tr><tr><td>148</td><td>aiohttp</td><td>6</td></tr><tr><td>149</td><td>psycopg</td><td>6</td></tr><tr><td>150</td><td>tty</td><td>5</td></tr><tr><td>151</td><td>pprint</td><td>5</td></tr><tr><td>152</td><td>fractions</td><td>5</td></tr><tr><td>153</td><td>errno</td><td>5</td></tr><tr><td>154</td><td>winreg</td><td>5</td></tr><tr><td>155</td><td>pycairo</td><td>5</td></tr><tr><td>156</td><td>persistent</td><td>5</td></tr><tr><td>157</td><td>spacy</td><td>5</td></tr><tr><td>158</td><td>trace</td><td>5</td></tr><tr><td>159</td><td>scons</td><td>5</td></tr><tr><td>160</td><td>python-ldap</td><td>5</td></tr><tr><td>161</td><td>sendkeys</td><td>5</td></tr><tr><td>162</td><td>fcntl</td><td>4</td></tr><tr><td>163</td><td>six</td><td>4</td></tr><tr><td>164</td><td>pydoc</td><td>4</td></tr><tr><td>165</td><td>orange</td><td>4</td></tr><tr><td>166</td><td>pycuda</td><td>4</td></tr><tr><td>167</td><td>shlex</td><td>4</td></tr><tr><td>168</td><td>noise</td><td>4</td></tr><tr><td>169</td><td>os.path</td><td>4</td></tr><tr><td>170</td><td>cartopy</td><td>4</td></tr>
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

<tr><td>1</td><td>numpy</td><td>scipy</td><td>790</td></tr><tr><td>2</td><td>numpy</td><td>pandas</td><td>430</td></tr><tr><td>3</td><td>matplotlib</td><td>numpy</td><td>384</td></tr><tr><td>4</td><td>matplotlib</td><td>pandas</td><td>288</td></tr><tr><td>5</td><td>matplotlib</td><td>scipy</td><td>146</td></tr><tr><td>6</td><td>pyqt4</td><td>pyqt</td><td>146</td></tr><tr><td>7</td><td>pip</td><td>virtualenv</td><td>138</td></tr><tr><td>8</td><td>csv</td><td>pandas</td><td>126</td></tr><tr><td>9</td><td>datetime</td><td>pandas</td><td>104</td></tr><tr><td>10</td><td>regex</td><td>string</td><td>92</td></tr><tr><td>11</td><td>cython</td><td>numpy</td><td>92</td></tr><tr><td>12</td><td>scikit-learn</td><td>numpy</td><td>90</td></tr><tr><td>13</td><td>opencv</td><td>numpy</td><td>86</td></tr><tr><td>14</td><td>setuptools</td><td>pip</td><td>64</td></tr><tr><td>15</td><td>matplotlib</td><td>ipython</td><td>62</td></tr><tr><td>16</td><td>pyqt</td><td>pyside</td><td>62</td></tr><tr><td>17</td><td>setuptools</td><td>distutils</td><td>60</td></tr><tr><td>18</td><td>scikit-learn</td><td>pandas</td><td>60</td></tr><tr><td>19</td><td>numpy</td><td>math</td><td>60</td></tr><tr><td>20</td><td>pandas</td><td>ipython</td><td>56</td></tr><tr><td>21</td><td>jupyter</td><td>ipython</td><td>54</td></tr><tr><td>22</td><td>csv</td><td>numpy</td><td>54</td></tr><tr><td>23</td><td>datetime</td><td>time</td><td>50</td></tr><tr><td>24</td><td>pandas</td><td>scipy</td><td>50</td></tr><tr><td>25</td><td>tkinter</td><td>matplotlib</td><td>44</td></tr><tr><td>26</td><td>pip</td><td>numpy</td><td>44</td></tr><tr><td>27</td><td>random</td><td>numpy</td><td>44</td></tr><tr><td>28</td><td>multiprocessing</td><td>numpy</td><td>42</td></tr><tr><td>29</td><td>matplotlib</td><td>heatmap</td><td>38</td></tr><tr><td>30</td><td>datetime</td><td>pytz</td><td>36</td></tr><tr><td>31</td><td>numpy</td><td>tensorflow</td><td>36</td></tr><tr><td>32</td><td>json</td><td>pandas</td><td>34</td></tr><tr><td>33</td><td>queue</td><td>multiprocessing</td><td>34</td></tr><tr><td>34</td><td>scikit-learn</td><td>scipy</td><td>34</td></tr><tr><td>35</td><td>statsmodels</td><td>pandas</td><td>30</td></tr><tr><td>36</td><td>pytables</td><td>pandas</td><td>30</td></tr><tr><td>37</td><td>pandas</td><td>string</td><td>30</td></tr><tr><td>38</td><td>numba</td><td>numpy</td><td>30</td></tr><tr><td>39</td><td>multiprocessing</td><td>pickle</td><td>28</td></tr><tr><td>40</td><td>networkx</td><td>matplotlib</td><td>28</td></tr><tr><td>41</td><td>scipy</td><td>math</td><td>28</td></tr><tr><td>42</td><td>simplejson</td><td>json</td><td>26</td></tr><tr><td>43</td><td>h5py</td><td>numpy</td><td>24</td></tr><tr><td>44</td><td>pyqt</td><td>matplotlib</td><td>24</td></tr><tr><td>45</td><td>datetime</td><td>numpy</td><td>24</td></tr><tr><td>46</td><td>sympy</td><td>numpy</td><td>24</td></tr><tr><td>47</td><td>email</td><td>smtplib</td><td>22</td></tr><tr><td>48</td><td>statsmodels</td><td>numpy</td><td>20</td></tr><tr><td>49</td><td>pip</td><td>distutils</td><td>20</td></tr><tr><td>50</td><td>pytables</td><td>numpy</td><td>20</td></tr><tr><td>51</td><td>pickle</td><td>numpy</td><td>20</td></tr><tr><td>52</td><td>pandas</td><td>sqlalchemy</td><td>20</td></tr><tr><td>53</td><td>distutils</td><td>cython</td><td>20</td></tr><tr><td>54</td><td>datetime</td><td>matplotlib</td><td>20</td></tr><tr><td>55</td><td>html</td><td>regex</td><td>20</td></tr><tr><td>56</td><td>ctypes</td><td>numpy</td><td>18</td></tr><tr><td>57</td><td>pyqt4</td><td>pyside</td><td>18</td></tr><tr><td>58</td><td>csv</td><td>json</td><td>16</td></tr><tr><td>59</td><td>opencv</td><td>matplotlib</td><td>16</td></tr><tr><td>60</td><td>lxml</td><td>html</td><td>16</td></tr><tr><td>61</td><td>ode</td><td>scipy</td><td>16</td></tr><tr><td>62</td><td>sympy</td><td>scipy</td><td>16</td></tr><tr><td>63</td><td>matplotlib</td><td>wxpython</td><td>16</td></tr><tr><td>64</td><td>setuptools</td><td>virtualenv</td><td>14</td></tr><tr><td>65</td><td>pip</td><td>lxml</td><td>14</td></tr><tr><td>66</td><td>numpy</td><td>ipython</td><td>14</td></tr><tr><td>67</td><td>html</td><td>pandas</td><td>14</td></tr><tr><td>68</td><td>pip</td><td>matplotlib</td><td>14</td></tr><tr><td>69</td><td>json</td><td>pickle</td><td>14</td></tr><tr><td>70</td><td>json</td><td>string</td><td>14</td></tr><tr><td>71</td><td>virtualenv</td><td>matplotlib</td><td>14</td></tr><tr><td>72</td><td>pyqt4</td><td>matplotlib</td><td>14</td></tr><tr><td>73</td><td>datetime</td><td>string</td><td>14</td></tr><tr><td>74</td><td>pymongo</td><td>json</td><td>14</td></tr><tr><td>75</td><td>html</td><td>jinja2</td><td>14</td></tr><tr><td>76</td><td>statsmodels</td><td>scipy</td><td>14</td></tr><tr><td>77</td><td>pip</td><td>mysql-python</td><td>12</td></tr><tr><td>78</td><td>multiprocessing</td><td>subprocess</td><td>12</td></tr><tr><td>79</td><td>py2exe</td><td>pyqt</td><td>12</td></tr><tr><td>80</td><td>tkinter</td><td>wxpython</td><td>12</td></tr><tr><td>81</td><td>spyder</td><td>matplotlib</td><td>12</td></tr><tr><td>82</td><td>random</td><td>string</td><td>12</td></tr><tr><td>83</td><td>nltk</td><td>tokenize</td><td>12</td></tr><tr><td>84</td><td>json</td><td>html</td><td>12</td></tr><tr><td>85</td><td>pip</td><td>tensorflow</td><td>12</td></tr><tr><td>86</td><td>opencv</td><td>scikit-image</td><td>12</td></tr><tr><td>87</td><td>regex</td><td>pandas</td><td>10</td></tr><tr><td>88</td><td>csv</td><td>string</td><td>10</td></tr><tr><td>89</td><td>pip</td><td>pygame</td><td>10</td></tr><tr><td>90</td><td>nltk</td><td>regex</td><td>10</td></tr><tr><td>91</td><td>types</td><td>pandas</td><td>10</td></tr><tr><td>92</td><td>pandas</td><td>heatmap</td><td>10</td></tr><tr><td>93</td><td>numpy</td><td>string</td><td>10</td></tr><tr><td>94</td><td>py2exe</td><td>wxpython</td><td>10</td></tr><tr><td>95</td><td>ctypes</td><td>pywin32</td><td>10</td></tr><tr><td>96</td><td>tkinter</td><td>pygame</td><td>10</td></tr><tr><td>97</td><td>sympy</td><td>matplotlib</td><td>10</td></tr><tr><td>98</td><td>io</td><td>pandas</td><td>10</td></tr><tr><td>99</td><td>scikit-learn</td><td>multiprocessing</td><td>10</td></tr><tr><td>100</td><td>pip</td><td>ipython</td><td>10</td></tr><tr><td>101</td><td>types</td><td>numpy</td><td>10</td></tr><tr><td>102</td><td>html</td><td>cgi</td><td>10</td></tr><tr><td>103</td><td>multiprocessing</td><td>pandas</td><td>10</td></tr><tr><td>104</td><td>numbers</td><td>string</td><td>10</td></tr><tr><td>105</td><td>pip</td><td>scipy</td><td>8</td></tr><tr><td>106</td><td>multiprocessing</td><td>logging</td><td>8</td></tr><tr><td>107</td><td>warnings</td><td>numpy</td><td>8</td></tr><tr><td>108</td><td>cython</td><td>scipy</td><td>8</td></tr><tr><td>109</td><td>random</td><td>scipy</td><td>8</td></tr><tr><td>110</td><td>pip</td><td>ssl</td><td>8</td></tr><tr><td>111</td><td>csv</td><td>tensorflow</td><td>8</td></tr><tr><td>112</td><td>html</td><td>string</td><td>8</td></tr><tr><td>113</td><td>virtualenv</td><td>opencv</td><td>8</td></tr><tr><td>114</td><td>decimal</td><td>string</td><td>8</td></tr><tr><td>115</td><td>logging</td><td>subprocess</td><td>8</td></tr><tr><td>116</td><td>tkinter</td><td>opencv</td><td>8</td></tr><tr><td>117</td><td>time</td><td>tkinter</td><td>8</td></tr><tr><td>118</td><td>statsmodels</td><td>matplotlib</td><td>8</td></tr><tr><td>119</td><td>pdb</td><td>ipython</td><td>8</td></tr><tr><td>120</td><td>spyder</td><td>ipython</td><td>8</td></tr><tr><td>121</td><td>nltk</td><td>scikit-learn</td><td>8</td></tr><tr><td>122</td><td>numba</td><td>pandas</td><td>8</td></tr><tr><td>123</td><td>numpy</td><td>scikit-image</td><td>8</td></tr><tr><td>124</td><td>zlib</td><td>gzip</td><td>8</td></tr><tr><td>125</td><td>bokeh</td><td>matplotlib</td><td>8</td></tr><tr><td>126</td><td>pip</td><td>pandas</td><td>8</td></tr><tr><td>127</td><td>multiprocessing</td><td>concurrent.futures</td><td>8</td></tr><tr><td>128</td><td>numpy</td><td>io</td><td>8</td></tr><tr><td>129</td><td>ctypes</td><td>cython</td><td>8</td></tr><tr><td>130</td><td>jupyter</td><td>pandas</td><td>8</td></tr><tr><td>131</td><td>virtualenv</td><td>mysql-python</td><td>8</td></tr><tr><td>132</td><td>networkx</td><td>pygraphviz</td><td>8</td></tr><tr><td>133</td><td>numpy</td><td>pillow</td><td>8</td></tr><tr><td>134</td><td>datetime</td><td>sqlalchemy</td><td>8</td></tr><tr><td>135</td><td>networkx</td><td>numpy</td><td>8</td></tr><tr><td>136</td><td>theano</td><td>numpy</td><td>8</td></tr><tr><td>137</td><td>datetime</td><td>sqlite3</td><td>8</td></tr><tr><td>138</td><td>mysql-python</td><td>numpy</td><td>8</td></tr><tr><td>139</td><td>virtualenv</td><td>distutils</td><td>8</td></tr><tr><td>140</td><td>itertools</td><td>numpy</td><td>8</td></tr><tr><td>141</td><td>tkinter</td><td>multiprocessing</td><td>8</td></tr><tr><td>142</td><td>jupyter</td><td>matplotlib</td><td>8</td></tr><tr><td>143</td><td>time</td><td>timeit</td><td>6</td></tr><tr><td>144</td><td>argparse</td><td>optparse</td><td>6</td></tr><tr><td>145</td><td>tkinter</td><td>subprocess</td><td>6</td></tr><tr><td>146</td><td>csv</td><td>io</td><td>6</td></tr><tr><td>147</td><td>ctypes</td><td>struct</td><td>6</td></tr><tr><td>148</td><td>time</td><td>pytz</td><td>6</td></tr><tr><td>149</td><td>json</td><td>numpy</td><td>6</td></tr><tr><td>150</td><td>pyqt</td><td>numpy</td><td>6</td></tr><tr><td>151</td><td>mayavi</td><td>vtk</td><td>6</td></tr><tr><td>152</td><td>jinja2</td><td>mako</td><td>6</td></tr><tr><td>153</td><td>virtualenv</td><td>scipy</td><td>6</td></tr><tr><td>154</td><td>rpy2</td><td>matplotlib</td><td>6</td></tr><tr><td>155</td><td>scikit-learn</td><td>tensorflow</td><td>6</td></tr><tr><td>156</td><td>datetime</td><td>json</td><td>6</td></tr><tr><td>157</td><td>html</td><td>matplotlib</td><td>6</td></tr><tr><td>158</td><td>html</td><td>email</td><td>6</td></tr><tr><td>159</td><td>tornado</td><td>twisted</td><td>6</td></tr><tr><td>160</td><td>sqlite3</td><td>sqlalchemy</td><td>6</td></tr><tr><td>161</td><td>pyglet</td><td>pygame</td><td>6</td></tr><tr><td>162</td><td>opencv</td><td>scipy</td><td>6</td></tr><tr><td>163</td><td>warnings</td><td>logging</td><td>6</td></tr><tr><td>164</td><td>pygtk</td><td>virtualenv</td><td>6</td></tr><tr><td>165</td><td>pyqt</td><td>wxpython</td><td>6</td></tr><tr><td>166</td><td>cython</td><td>pickle</td><td>6</td></tr><tr><td>167</td><td>pyodbc</td><td>pip</td><td>6</td></tr><tr><td>168</td><td>datetime</td><td>calendar</td><td>6</td></tr><tr><td>169</td><td>pymongo</td><td>pandas</td><td>6</td></tr><tr><td>170</td><td>csv</td><td>matplotlib</td><td>6</td></tr><tr><td>171</td><td>virtualenv</td><td>tensorflow</td><td>6</td></tr><tr><td>172</td><td>scikit-learn</td><td>matplotlib</td><td>6</td></tr><tr><td>173</td><td>py2exe</td><td>pywin32</td><td>6</td></tr><tr><td>174</td><td>mayavi</td><td>scipy</td><td>6</td></tr><tr><td>175</td><td>csv</td><td>scipy</td><td>6</td></tr><tr><td>176</td><td>multiprocessing</td><td>pyqt</td><td>6</td></tr><tr><td>177</td><td>multiprocessing</td><td>opencv</td><td>6</td></tr><tr><td>178</td><td>logging</td><td>console</td><td>6</td></tr><tr><td>179</td><td>sympy</td><td>math</td><td>6</td></tr><tr><td>180</td><td>setuptools</td><td>numpy</td><td>6</td></tr><tr><td>181</td><td>mayavi</td><td>matplotlib</td><td>6</td></tr><tr><td>182</td><td>pyqt</td><td>ipython</td><td>6</td></tr><tr><td>183</td><td>cartopy</td><td>matplotlib</td><td>6</td></tr><tr><td>184</td><td>multiprocessing</td><td>py2exe</td><td>6</td></tr><tr><td>185</td><td>multiprocessing</td><td>wxpython</td><td>6</td></tr><tr><td>186</td><td>datetime</td><td>python-dateutil</td><td>6</td></tr><tr><td>187</td><td>bokeh</td><td>pandas</td><td>6</td></tr><tr><td>188</td><td>multiprocessing</td><td>twisted</td><td>6</td></tr><tr><td>189</td><td>pyqt4</td><td>py2exe</td><td>6</td></tr><tr><td>190</td><td>logging</td><td>wxpython</td><td>6</td></tr><tr><td>191</td><td>readline</td><td>ipython</td><td>6</td></tr><tr><td>192</td><td>json</td><td>sqlalchemy</td><td>6</td></tr><tr><td>193</td><td>numeric</td><td>scipy</td><td>6</td></tr><tr><td>194</td><td>python-dateutil</td><td>matplotlib</td><td>6</td></tr><tr><td>195</td><td>random</td><td>pandas</td><td>6</td></tr><tr><td>196</td><td>html</td><td>ipython</td><td>6</td></tr><tr><td>197</td><td>pickle</td><td>pandas</td><td>6</td></tr><tr><td>198</td><td>datetime</td><td>math</td><td>4</td></tr><tr><td>199</td><td>matplotlib</td><td>scikit-image</td><td>4</td></tr><tr><td>200</td><td>types</td><td>string</td><td>4</td></tr><tr><td>201</td><td>pty</td><td>subprocess</td><td>4</td></tr><tr><td>202</td><td>numbers</td><td>regex</td><td>4</td></tr><tr><td>203</td><td>multiprocessing</td><td>io</td><td>4</td></tr><tr><td>204</td><td>types</td><td>numbers</td><td>4</td></tr><tr><td>205</td><td>io</td><td>string</td><td>4</td></tr><tr><td>206</td><td>pytables</td><td>scipy</td><td>4</td></tr><tr><td>207</td><td>datetime</td><td>csv</td><td>4</td></tr><tr><td>208</td><td>random</td><td>numbers</td><td>4</td></tr><tr><td>209</td><td>json</td><td>pprint</td><td>4</td></tr><tr><td>210</td><td>pprint</td><td>string</td><td>4</td></tr><tr><td>211</td><td>json</td><td>jinja2</td><td>4</td></tr><tr><td>212</td><td>csv</td><td>regex</td><td>4</td></tr><tr><td>213</td><td>decimal</td><td>fractions</td><td>4</td></tr><tr><td>214</td><td>pyparsing</td><td>regex</td><td>4</td></tr><tr><td>215</td><td>biopython</td><td>ipython</td><td>4</td></tr><tr><td>216</td><td>nltk</td><td>pip</td><td>4</td></tr><tr><td>217</td><td>select</td><td>subprocess</td><td>4</td></tr><tr><td>218</td><td>pip</td><td>pillow</td><td>4</td></tr><tr><td>219</td><td>multiprocessing</td><td>gevent</td><td>4</td></tr><tr><td>220</td><td>lxml</td><td>pandas</td><td>4</td></tr><tr><td>221</td><td>networkx</td><td>pandas</td><td>4</td></tr><tr><td>222</td><td>copy</td><td>numpy</td><td>4</td></tr><tr><td>223</td><td>pyqt</td><td>subprocess</td><td>4</td></tr><tr><td>224</td><td>pygame</td><td>wxpython</td><td>4</td></tr><tr><td>225</td><td>pickle</td><td>shelve</td><td>4</td></tr><tr><td>226</td><td>pyqt4</td><td>opencv</td><td>4</td></tr><tr><td>227</td><td>warnings</td><td>matplotlib</td><td>4</td></tr><tr><td>228</td><td>theano</td><td>scipy</td><td>4</td></tr><tr><td>229</td><td>pygtk</td><td>matplotlib</td><td>4</td></tr><tr><td>230</td><td>twisted</td><td>py2exe</td><td>4</td></tr><tr><td>231</td><td>tkinter</td><td>string</td><td>4</td></tr><tr><td>232</td><td>base64</td><td>string</td><td>4</td></tr><tr><td>233</td><td>twisted</td><td>gevent</td><td>4</td></tr><tr><td>234</td><td>rpy2</td><td>pandas</td><td>4</td></tr><tr><td>235</td><td>pyyaml</td><td>json</td><td>4</td></tr><tr><td>236</td><td>cython</td><td>string</td><td>4</td></tr><tr><td>237</td><td>statsmodels</td><td>pymc</td><td>4</td></tr><tr><td>238</td><td>numpy</td><td>heatmap</td><td>4</td></tr><tr><td>239</td><td>tkinter</td><td>py2exe</td><td>4</td></tr><tr><td>240</td><td>scikit-learn</td><td>statsmodels</td><td>4</td></tr><tr><td>241</td><td>calendar</td><td>pandas</td><td>4</td></tr><tr><td>242</td><td>struct</td><td>cython</td><td>4</td></tr><tr><td>243</td><td>pyodbc</td><td>sqlalchemy</td><td>4</td></tr><tr><td>244</td><td>matplotlib</td><td>pyside</td><td>4</td></tr><tr><td>245</td><td>virtualenv</td><td>zlib</td><td>4</td></tr><tr><td>246</td><td>scikit-learn</td><td>pickle</td><td>4</td></tr><tr><td>247</td><td>itertools</td><td>pandas</td><td>4</td></tr><tr><td>248</td><td>opencv</td><td>pyqt</td><td>4</td></tr><tr><td>249</td><td>pygame</td><td>math</td><td>4</td></tr><tr><td>250</td><td>regex</td><td>email</td><td>4</td></tr><tr><td>251</td><td>matplotlib</td><td>reportlab</td><td>4</td></tr><tr><td>252</td><td>pandas</td><td>tensorflow</td><td>4</td></tr><tr><td>253</td><td>py2exe</td><td>pygame</td><td>4</td></tr><tr><td>254</td><td>pandas</td><td>zipline</td><td>4</td></tr><tr><td>255</td><td>multiprocessing</td><td>matplotlib</td><td>4</td></tr><tr><td>256</td><td>blaze</td><td>numpy</td><td>4</td></tr><tr><td>257</td><td>numpy</td><td>numeric</td><td>4</td></tr><tr><td>258</td><td>cython</td><td>opencv</td><td>4</td></tr><tr><td>259</td><td>matplotlib</td><td>pyserial</td><td>4</td></tr><tr><td>260</td><td>pip</td><td>pytz</td><td>4</td></tr><tr><td>261</td><td>ctypes</td><td>opencv</td><td>4</td></tr><tr><td>262</td><td>scikit-learn</td><td>libsvm</td><td>4</td></tr><tr><td>263</td><td>tornado</td><td>json</td><td>4</td></tr><tr><td>264</td><td>multiprocessing</td><td>scipy</td><td>4</td></tr><tr><td>265</td><td>py2exe</td><td>ssl</td><td>4</td></tr><tr><td>266</td><td>mmap</td><td>numpy</td><td>4</td></tr><tr><td>267</td><td>matplotlib</td><td>polygon</td><td>4</td></tr><tr><td>268</td><td>traceback</td><td>logging</td><td>4</td></tr><tr><td>269</td><td>nltk</td><td>pandas</td><td>4</td></tr><tr><td>270</td><td>random</td><td>math</td><td>4</td></tr><tr><td>271</td><td>mysql-python</td><td>pandas</td><td>4</td></tr><tr><td>272</td><td>scipy</td><td>ipython</td><td>4</td></tr><tr><td>273</td><td>opencv</td><td>tensorflow</td><td>4</td></tr><tr><td>274</td><td>pyodbc</td><td>pandas</td><td>4</td></tr><tr><td>275</td><td>virtualenv</td><td>numpy</td><td>4</td></tr><tr><td>276</td><td>py2exe</td><td>pyside</td><td>4</td></tr><tr><td>277</td><td>pip</td><td>pyqt</td><td>4</td></tr><tr><td>278</td><td>logging</td><td>syslog</td><td>4</td></tr><tr><td>279</td><td>pymongo</td><td>datetime</td><td>4</td></tr><tr><td>280</td><td>sqlite3</td><td>pysqlite</td><td>4</td></tr><tr><td>281</td><td>numbers</td><td>numpy</td><td>4</td></tr><tr><td>282</td><td>itertools</td><td>string</td><td>4</td></tr><tr><td>283</td><td>nltk</td><td>gensim</td><td>4</td></tr><tr><td>284</td><td>setuptools</td><td>lxml</td><td>4</td></tr><tr><td>285</td><td>warnings</td><td>pandas</td><td>4</td></tr><tr><td>286</td><td>scikit-image</td><td>scipy</td><td>4</td></tr><tr><td>287</td><td>wave</td><td>scipy</td><td>4</td></tr><tr><td>288</td><td>tornado</td><td>multiprocessing</td><td>4</td></tr><tr><td>289</td><td>spyder</td><td>numpy</td><td>4</td></tr><tr><td>290</td><td>sqlite3</td><td>csv</td><td>4</td></tr><tr><td>291</td><td>regex</td><td>tokenize</td><td>4</td></tr><tr><td>292</td><td>time</td><td>pygame</td><td>4</td></tr><tr><td>293</td><td>pyqt4</td><td>ipython</td><td>4</td></tr><tr><td>294</td><td>ipython</td><td>pyside</td><td>4</td></tr><tr><td>295</td><td>select</td><td>pandas</td><td>4</td></tr><tr><td>296</td><td>gzip</td><td>string</td><td>2</td></tr><tr><td>297</td><td>pip</td><td>jpype</td><td>2</td></tr><tr><td>298</td><td>time</td><td>math</td><td>2</td></tr><tr><td>299</td><td>tty</td><td>pty</td><td>2</td></tr><tr><td>300</td><td>tty</td><td>subprocess</td><td>2</td></tr><tr><td>301</td><td>argparse</td><td>getopt</td><td>2</td></tr><tr><td>302</td><td>getopt</td><td>optparse</td><td>2</td></tr><tr><td>303</td><td>nltk</td><td>string</td><td>2</td></tr><tr><td>304</td><td>sqlite3</td><td>numpy</td><td>2</td></tr><tr><td>305</td><td>pyqt4</td><td>csv</td><td>2</td></tr><tr><td>306</td><td>string</td><td>math</td><td>2</td></tr><tr><td>307</td><td>pyodbc</td><td>select</td><td>2</td></tr><tr><td>308</td><td>spyder</td><td>virtualenv</td><td>2</td></tr><tr><td>309</td><td>warnings</td><td>ipython</td><td>2</td></tr><tr><td>310</td><td>sqlite3</td><td>zlib</td><td>2</td></tr><tr><td>311</td><td>spyder</td><td>nltk</td><td>2</td></tr><tr><td>312</td><td>copy</td><td>distutils</td><td>2</td></tr><tr><td>313</td><td>pyqt4</td><td>numpy</td><td>2</td></tr><tr><td>314</td><td>pip</td><td>twisted</td><td>2</td></tr><tr><td>315</td><td>virtualenv</td><td>twisted</td><td>2</td></tr><tr><td>316</td><td>decimal</td><td>numeric</td><td>2</td></tr><tr><td>317</td><td>types</td><td>csv</td><td>2</td></tr><tr><td>318</td><td>simplejson</td><td>numpy</td><td>2</td></tr><tr><td>319</td><td>twisted</td><td>sqlalchemy</td><td>2</td></tr><tr><td>320</td><td>lxml</td><td>py2exe</td><td>2</td></tr><tr><td>321</td><td>lxml</td><td>wxpython</td><td>2</td></tr><tr><td>322</td><td>pip</td><td>tkinter</td><td>2</td></tr><tr><td>323</td><td>six</td><td>pip</td><td>2</td></tr><tr><td>324</td><td>pocketsphinx</td><td>pyaudio</td><td>2</td></tr><tr><td>325</td><td>numpy</td><td>pyaudio</td><td>2</td></tr><tr><td>326</td><td>ctypes</td><td>locale</td><td>2</td></tr><tr><td>327</td><td>pyqt</td><td>pickle</td><td>2</td></tr><tr><td>328</td><td>python-dateutil</td><td>pytz</td><td>2</td></tr><tr><td>329</td><td>pip</td><td>pyyaml</td><td>2</td></tr><tr><td>330</td><td>gdal</td><td>math</td><td>2</td></tr><tr><td>331</td><td>virtualenv</td><td>mercurial</td><td>2</td></tr><tr><td>332</td><td>pip</td><td>cmd</td><td>2</td></tr><tr><td>333</td><td>distutils</td><td>numpy</td><td>2</td></tr><tr><td>334</td><td>nltk</td><td>ssl</td><td>2</td></tr><tr><td>335</td><td>time</td><td>pygtk</td><td>2</td></tr><tr><td>336</td><td>orange</td><td>pandas</td><td>2</td></tr><tr><td>337</td><td>queue</td><td>tensorflow</td><td>2</td></tr><tr><td>338</td><td>socketserver</td><td>ssl</td><td>2</td></tr><tr><td>339</td><td>pyodbc</td><td>multiprocessing</td><td>2</td></tr><tr><td>340</td><td>pyodbc</td><td>pickle</td><td>2</td></tr><tr><td>341</td><td>base64</td><td>html</td><td>2</td></tr><tr><td>342</td><td>base64</td><td>matplotlib</td><td>2</td></tr><tr><td>343</td><td>zope.interface</td><td>pygtk</td><td>2</td></tr><tr><td>344</td><td>zope.interface</td><td>twisted</td><td>2</td></tr><tr><td>345</td><td>zope.interface</td><td>py2exe</td><td>2</td></tr><tr><td>346</td><td>pygtk</td><td>twisted</td><td>2</td></tr><tr><td>347</td><td>pygtk</td><td>py2exe</td><td>2</td></tr><tr><td>348</td><td>datetime</td><td>itertools</td><td>2</td></tr><tr><td>349</td><td>multiprocessing</td><td>ipython</td><td>2</td></tr><tr><td>350</td><td>multiprocess</td><td>multiprocessing</td><td>2</td></tr><tr><td>351</td><td>ssl</td><td>smtplib</td><td>2</td></tr><tr><td>352</td><td>pip</td><td>pygtk</td><td>2</td></tr><tr><td>353</td><td>pyparsing</td><td>json</td><td>2</td></tr><tr><td>354</td><td>tornado</td><td>gevent</td><td>2</td></tr><tr><td>355</td><td>io</td><td>pytables</td><td>2</td></tr><tr><td>356</td><td>virtualenv</td><td>pycairo</td><td>2</td></tr><tr><td>357</td><td>virtualenv</td><td>nose</td><td>2</td></tr><tr><td>358</td><td>rpy2</td><td>statsmodels</td><td>2</td></tr><tr><td>359</td><td>csv</td><td>pytables</td><td>2</td></tr><tr><td>360</td><td>genshi</td><td>jinja2</td><td>2</td></tr><tr><td>361</td><td>genshi</td><td>mako</td><td>2</td></tr><tr><td>362</td><td>virtualenv</td><td>pywin32</td><td>2</td></tr><tr><td>363</td><td>pygame</td><td>kivy</td><td>2</td></tr><tr><td>364</td><td>pyglet</td><td>virtualenv</td><td>2</td></tr><tr><td>365</td><td>json</td><td>networkx</td><td>2</td></tr><tr><td>366</td><td>pickle</td><td>scipy</td><td>2</td></tr><tr><td>367</td><td>scikit-learn</td><td>gensim</td><td>2</td></tr><tr><td>368</td><td>multiprocessing</td><td>sqlalchemy</td><td>2</td></tr><tr><td>369</td><td>pip</td><td>python-dateutil</td><td>2</td></tr><tr><td>370</td><td>warnings</td><td>ctypes</td><td>2</td></tr><tr><td>371</td><td>tkinter</td><td>pyqt</td><td>2</td></tr><tr><td>372</td><td>opencv</td><td>imread</td><td>2</td></tr><tr><td>373</td><td>scikit-learn</td><td>scikit-image</td><td>2</td></tr><tr><td>374</td><td>scikit-learn</td><td>warnings</td><td>2</td></tr><tr><td>375</td><td>string</td><td>hmac</td><td>2</td></tr><tr><td>376</td><td>base64</td><td>numpy</td><td>2</td></tr><tr><td>377</td><td>ctypes</td><td>types</td><td>2</td></tr><tr><td>378</td><td>warnings</td><td>io</td><td>2</td></tr><tr><td>379</td><td>multiprocess</td><td>logging</td><td>2</td></tr><tr><td>380</td><td>opencv</td><td>wxpython</td><td>2</td></tr><tr><td>381</td><td>numpy</td><td>wxpython</td><td>2</td></tr><tr><td>382</td><td>bokeh</td><td>html</td><td>2</td></tr><tr><td>383</td><td>bokeh</td><td>jinja2</td><td>2</td></tr><tr><td>384</td><td>multiprocess</td><td>csv</td><td>2</td></tr><tr><td>385</td><td>string</td><td>scipy</td><td>2</td></tr><tr><td>386</td><td>networkx</td><td>ipython</td><td>2</td></tr><tr><td>387</td><td>shapely</td><td>pandas</td><td>2</td></tr><tr><td>388</td><td>six</td><td>python-dateutil</td><td>2</td></tr><tr><td>389</td><td>biopython</td><td>numpy</td><td>2</td></tr><tr><td>390</td><td>py2exe</td><td>cython</td><td>2</td></tr><tr><td>391</td><td>sympy</td><td>pickle</td><td>2</td></tr><tr><td>392</td><td>timeit</td><td>string</td><td>2</td></tr><tr><td>393</td><td>cython</td><td>kivy</td><td>2</td></tr><tr><td>394</td><td>tkinter</td><td>msvcrt</td><td>2</td></tr><tr><td>395</td><td>py2exe</td><td>msvcrt</td><td>2</td></tr><tr><td>396</td><td>json</td><td>ipython</td><td>2</td></tr><tr><td>397</td><td>csv</td><td>difflib</td><td>2</td></tr><tr><td>398</td><td>pandas</td><td>difflib</td><td>2</td></tr><tr><td>399</td><td>lxml</td><td>difflib</td><td>2</td></tr><tr><td>400</td><td>pyyaml</td><td>jinja2</td><td>2</td></tr><tr><td>401</td><td>warnings</td><td>scipy</td><td>2</td></tr><tr><td>402</td><td>regex</td><td>subprocess</td><td>2</td></tr><tr><td>403</td><td>h5py</td><td>scipy</td><td>2</td></tr><tr><td>404</td><td>py2exe</td><td>sqlalchemy</td><td>2</td></tr><tr><td>405</td><td>pygtk</td><td>pywin32</td><td>2</td></tr><tr><td>406</td><td>imaplib</td><td>email</td><td>2</td></tr><tr><td>407</td><td>pty</td><td>select</td><td>2</td></tr><tr><td>408</td><td>select</td><td>html</td><td>2</td></tr><tr><td>409</td><td>html</td><td>opencv</td><td>2</td></tr><tr><td>410</td><td>numba</td><td>cython</td><td>2</td></tr><tr><td>411</td><td>glob</td><td>regex</td><td>2</td></tr><tr><td>412</td><td>pycurl</td><td>ssl</td><td>2</td></tr><tr><td>413</td><td>imaplib</td><td>csv</td><td>2</td></tr><tr><td>414</td><td>ctypes</td><td>string</td><td>2</td></tr><tr><td>415</td><td>pymongo</td><td>ssl</td><td>2</td></tr><tr><td>416</td><td>re2</td><td>regex</td><td>2</td></tr><tr><td>417</td><td>pip</td><td>argparse</td><td>2</td></tr><tr><td>418</td><td>scikit-learn</td><td>csv</td><td>2</td></tr><tr><td>419</td><td>opencv</td><td>math</td><td>2</td></tr><tr><td>420</td><td>datetime</td><td>formatter</td><td>2</td></tr><tr><td>421</td><td>msgpack</td><td>pandas</td><td>2</td></tr><tr><td>422</td><td>cython</td><td>pandas</td><td>2</td></tr><tr><td>423</td><td>rpy2</td><td>multiprocessing</td><td>2</td></tr><tr><td>424</td><td>pyqt</td><td>pyserial</td><td>2</td></tr><tr><td>425</td><td>pip</td><td>pyopengl</td><td>2</td></tr><tr><td>426</td><td>numpy</td><td>pyopengl</td><td>2</td></tr><tr><td>427</td><td>pillow</td><td>scipy</td><td>2</td></tr><tr><td>428</td><td>gettext</td><td>babel</td><td>2</td></tr><tr><td>429</td><td>sympy</td><td>ipython</td><td>2</td></tr><tr><td>430</td><td>blaze</td><td>numeric</td><td>2</td></tr><tr><td>431</td><td>distutils</td><td>opencv</td><td>2</td></tr><tr><td>432</td><td>zlib</td><td>zipfile</td><td>2</td></tr><tr><td>433</td><td>libsvm</td><td>csv</td><td>2</td></tr><tr><td>434</td><td>py2exe</td><td>subprocess</td><td>2</td></tr><tr><td>435</td><td>html</td><td>mako</td><td>2</td></tr><tr><td>436</td><td>tornado</td><td>mysql-python</td><td>2</td></tr><tr><td>437</td><td>tkinter</td><td>copy</td><td>2</td></tr><tr><td>438</td><td>io</td><td>gevent</td><td>2</td></tr><tr><td>439</td><td>pip</td><td>pytables</td><td>2</td></tr><tr><td>440</td><td>mysql-python</td><td>peewee</td><td>2</td></tr><tr><td>441</td><td>types</td><td>math</td><td>2</td></tr><tr><td>442</td><td>pycparser</td><td>pip</td><td>2</td></tr><tr><td>443</td><td>spyder</td><td>pdb</td><td>2</td></tr><tr><td>444</td><td>pdb</td><td>matplotlib</td><td>2</td></tr><tr><td>445</td><td>sqlalchemy</td><td>string</td><td>2</td></tr><tr><td>446</td><td>tkinter</td><td>ipython</td><td>2</td></tr><tr><td>447</td><td>networkx</td><td>statsmodels</td><td>2</td></tr><tr><td>448</td><td>wave</td><td>pyaudio</td><td>2</td></tr><tr><td>449</td><td>pickle</td><td>ipython</td><td>2</td></tr><tr><td>450</td><td>select</td><td>peewee</td><td>2</td></tr><tr><td>451</td><td>nltk</td><td>io</td><td>2</td></tr><tr><td>452</td><td>csv</td><td>gzip</td><td>2</td></tr><tr><td>453</td><td>regex</td><td>sqlalchemy</td><td>2</td></tr><tr><td>454</td><td>sys</td><td>cmd</td><td>2</td></tr><tr><td>455</td><td>pip</td><td>gevent</td><td>2</td></tr><tr><td>456</td><td>string</td><td>tokenize</td><td>2</td></tr><tr><td>457</td><td>zipfile</td><td>tarfile</td><td>2</td></tr><tr><td>458</td><td>pygame</td><td>matplotlib</td><td>2</td></tr><tr><td>459</td><td>html</td><td>calendar</td><td>2</td></tr><tr><td>460</td><td>logging</td><td>pyqt</td><td>2</td></tr><tr><td>461</td><td>email</td><td>poplib</td><td>2</td></tr><tr><td>462</td><td>time</td><td>matplotlib</td><td>2</td></tr><tr><td>463</td><td>multiprocessing</td><td>pyside</td><td>2</td></tr><tr><td>464</td><td>scipy</td><td>pymc</td><td>2</td></tr><tr><td>465</td><td>base64</td><td>pickle</td><td>2</td></tr><tr><td>466</td><td>virtualenv</td><td>pyqt</td><td>2</td></tr><tr><td>467</td><td>pyqt</td><td>vispy</td><td>2</td></tr><tr><td>468</td><td>vispy</td><td>matplotlib</td><td>2</td></tr><tr><td>469</td><td>glob</td><td>shutil</td><td>2</td></tr><tr><td>470</td><td>glob</td><td>copy</td><td>2</td></tr><tr><td>471</td><td>shutil</td><td>copy</td><td>2</td></tr><tr><td>472</td><td>networkx</td><td>scipy</td><td>2</td></tr><tr><td>473</td><td>pyodbc</td><td>csv</td><td>2</td></tr><tr><td>474</td><td>pip</td><td>mercurial</td><td>2</td></tr><tr><td>475</td><td>uuid</td><td>random</td><td>2</td></tr><tr><td>476</td><td>jupyter</td><td>tensorflow</td><td>2</td></tr><tr><td>477</td><td>statsmodels</td><td>ipython</td><td>2</td></tr><tr><td>478</td><td>twisted</td><td>pygame</td><td>2</td></tr><tr><td>479</td><td>virtualenv</td><td>pygame</td><td>2</td></tr><tr><td>480</td><td>multiprocessing</td><td>pycuda</td><td>2</td></tr><tr><td>481</td><td>setuptools</td><td>twisted</td><td>2</td></tr><tr><td>482</td><td>twisted</td><td>distutils</td><td>2</td></tr><tr><td>483</td><td>uuid</td><td>sqlalchemy</td><td>2</td></tr><tr><td>484</td><td>pyqt4</td><td>tkinter</td><td>2</td></tr><tr><td>485</td><td>readline</td><td>subprocess</td><td>2</td></tr><tr><td>486</td><td>json</td><td>regex</td><td>2</td></tr><tr><td>487</td><td>pygame</td><td>console</td><td>2</td></tr><tr><td>488</td><td>ode</td><td>matplotlib</td><td>2</td></tr><tr><td>489</td><td>hashlib</td><td>regex</td><td>2</td></tr><tr><td>490</td><td>pygtk</td><td>vpython</td><td>2</td></tr><tr><td>491</td><td>numba</td><td>scipy</td><td>2</td></tr><tr><td>492</td><td>io</td><td>tensorflow</td><td>2</td></tr><tr><td>493</td><td>pygtk</td><td>pygame</td><td>2</td></tr><tr><td>494</td><td>pyhook</td><td>pywin32</td><td>2</td></tr><tr><td>495</td><td>scikit-learn</td><td>timeit</td><td>2</td></tr><tr><td>496</td><td>pyyaml</td><td>ruamel.yaml</td><td>2</td></tr><tr><td>497</td><td>pyserial</td><td>numpy</td><td>2</td></tr><tr><td>498</td><td>pymongo</td><td>pip</td><td>2</td></tr><tr><td>499</td><td>cython</td><td>ipython</td><td>2</td></tr><tr><td>500</td><td>csv</td><td>ipython</td><td>2</td></tr><tr><td>501</td><td>pyqt</td><td>regex</td><td>2</td></tr><tr><td>502</td><td>regex</td><td>pyside</td><td>2</td></tr><tr><td>503</td><td>pyserial</td><td>tkinter</td><td>2</td></tr><tr><td>504</td><td>pyserial</td><td>decimal</td><td>2</td></tr><tr><td>505</td><td>pyserial</td><td>string</td><td>2</td></tr><tr><td>506</td><td>tkinter</td><td>decimal</td><td>2</td></tr><tr><td>507</td><td>scikit-learn</td><td>tokenize</td><td>2</td></tr><tr><td>508</td><td>h5py</td><td>io</td><td>2</td></tr><tr><td>509</td><td>sympy</td><td>numexpr</td><td>2</td></tr><tr><td>510</td><td>persistent</td><td>subprocess</td><td>2</td></tr><tr><td>511</td><td>gdal</td><td>pip</td><td>2</td></tr><tr><td>512</td><td>base64</td><td>pillow</td><td>2</td></tr><tr><td>513</td><td>shutil</td><td>zipfile</td><td>2</td></tr><tr><td>514</td><td>numpy</td><td>xgboost</td><td>2</td></tr><tr><td>515</td><td>pyqt4</td><td>subprocess</td><td>2</td></tr><tr><td>516</td><td>theano</td><td>pdb</td><td>2</td></tr><tr><td>517</td><td>pygtk</td><td>pycairo</td><td>2</td></tr><tr><td>518</td><td>tkinter</td><td>pillow</td><td>2</td></tr><tr><td>519</td><td>time</td><td>numpy</td><td>2</td></tr><tr><td>520</td><td>shapely</td><td>scipy</td><td>2</td></tr><tr><td>521</td><td>jupyter</td><td>sympy</td><td>2</td></tr><tr><td>522</td><td>spyder</td><td>mayavi</td><td>2</td></tr><tr><td>523</td><td>itertools</td><td>csv</td><td>2</td></tr><tr><td>524</td><td>jupyter</td><td>tornado</td><td>2</td></tr><tr><td>525</td><td>warnings</td><td>virtualenv</td><td>2</td></tr><tr><td>526</td><td>tkinter</td><td>logging</td><td>2</td></tr><tr><td>527</td><td>sqlite3</td><td>pip</td><td>2</td></tr><tr><td>528</td><td>virtualenv</td><td>wxpython</td><td>2</td></tr><tr><td>529</td><td>pygtk</td><td>subprocess</td><td>2</td></tr><tr><td>530</td><td>virtualenv</td><td>python-ldap</td><td>2</td></tr><tr><td>531</td><td>shutil</td><td>io</td><td>2</td></tr><tr><td>532</td><td>py2exe</td><td>pytz</td><td>2</td></tr><tr><td>533</td><td>vtk</td><td>matplotlib</td><td>2</td></tr><tr><td>534</td><td>vtk</td><td>numpy</td><td>2</td></tr><tr><td>535</td><td>queue</td><td>pickle</td><td>2</td></tr><tr><td>536</td><td>random</td><td>cython</td><td>2</td></tr><tr><td>537</td><td>virtualenv</td><td>pdb</td><td>2</td></tr><tr><td>538</td><td>pip</td><td>readline</td><td>2</td></tr><tr><td>539</td><td>gdal</td><td>matplotlib</td><td>2</td></tr><tr><td>540</td><td>gevent</td><td>psycopg</td><td>2</td></tr><tr><td>541</td><td>opencv</td><td>flann</td><td>2</td></tr><tr><td>542</td><td>pyodbc</td><td>pywin32</td><td>2</td></tr><tr><td>543</td><td>matplotlib</td><td>math</td><td>2</td></tr><tr><td>544</td><td>nltk</td><td>random</td><td>2</td></tr><tr><td>545</td><td>select</td><td>multiprocessing</td><td>2</td></tr><tr><td>546</td><td>traceback</td><td>inspect</td><td>2</td></tr><tr><td>547</td><td>traceback</td><td>sys</td><td>2</td></tr><tr><td>548</td><td>inspect</td><td>sys</td><td>2</td></tr><tr><td>549</td><td>simplejson</td><td>types</td><td>2</td></tr><tr><td>550</td><td>types</td><td>json</td><td>2</td></tr><tr><td>551</td><td>pytables</td><td>h5py</td><td>2</td></tr><tr><td>552</td><td>spyder</td><td>pyqt</td><td>2</td></tr><tr><td>553</td><td>spyder</td><td>pyside</td><td>2</td></tr><tr><td>554</td><td>argparse</td><td>py2exe</td><td>2</td></tr><tr><td>555</td><td>opencv</td><td>kivy</td><td>2</td></tr><tr><td>556</td><td>sympy</td><td>pyside</td><td>2</td></tr><tr><td>557</td><td>ode</td><td>numpy</td><td>2</td></tr><tr><td>558</td><td>pip</td><td>cython</td><td>2</td></tr><tr><td>559</td><td>lxml</td><td>cython</td><td>2</td></tr><tr><td>560</td><td>posix</td><td>stat</td><td>2</td></tr><tr><td>561</td><td>gzip</td><td>pandas</td><td>2</td></tr><tr><td>562</td><td>select</td><td>ssl</td><td>2</td></tr><tr><td>563</td><td>pyqt4</td><td>asyncore</td><td>2</td></tr><tr><td>564</td><td>scikit-learn</td><td>xgboost</td><td>2</td></tr><tr><td>565</td><td>regex</td><td>locale</td><td>2</td></tr><tr><td>566</td><td>collections</td><td>matplotlib</td><td>2</td></tr><tr><td>567</td><td>imaplib</td><td>html</td><td>2</td></tr><tr><td>568</td><td>sqlite3</td><td>virtualenv</td><td>2</td></tr><tr><td>569</td><td>queue</td><td>pygame</td><td>2</td></tr><tr><td>570</td><td>queue</td><td>numpy</td><td>2</td></tr><tr><td>571</td><td>pygame</td><td>numpy</td><td>2</td></tr><tr><td>572</td><td>pyqt</td><td>pandas</td><td>2</td></tr><tr><td>573</td><td>twisted</td><td>ssl</td><td>2</td></tr><tr><td>574</td><td>sqlite3</td><td>regex</td><td>2</td></tr><tr><td>575</td><td>pickle</td><td>regex</td><td>2</td></tr><tr><td>576</td><td>ssl</td><td>python-ldap</td><td>2</td></tr><tr><td>577</td><td>tkinter</td><td>numpy</td><td>2</td></tr><tr><td>578</td><td>pip</td><td>mayavi</td><td>2</td></tr><tr><td>579</td><td>pip</td><td>vtk</td><td>2</td></tr><tr><td>580</td><td>tkinter</td><td>virtualenv</td><td>2</td></tr><tr><td>581</td><td>virtualenv</td><td>ipython</td><td>2</td></tr><tr><td>582</td><td>pywin32</td><td>email</td><td>2</td></tr><tr><td>583</td><td>sqlalchemy</td><td>nose</td><td>2</td></tr><tr><td>584</td><td>sqlite3</td><td>pandas</td><td>2</td></tr><tr><td>585</td><td>jinja2</td><td>sqlalchemy</td><td>2</td></tr><tr><td>586</td><td>shlex</td><td>subprocess</td><td>2</td></tr><tr><td>587</td><td>json</td><td>tensorflow</td><td>2</td></tr><tr><td>588</td><td>pyminuit</td><td>numeric</td><td>2</td></tr><tr><td>589</td><td>pyminuit</td><td>scipy</td><td>2</td></tr><tr><td>590</td><td>nltk</td><td>numpy</td><td>2</td></tr><tr><td>591</td><td>lxml</td><td>pickle</td><td>2</td></tr><tr><td>592</td><td>setuptools</td><td>cython</td><td>2</td></tr><tr><td>593</td><td>decimal</td><td>json</td><td>2</td></tr><tr><td>594</td><td>posix</td><td>subprocess</td><td>2</td></tr><tr><td>595</td><td>time</td><td>calendar</td><td>2</td></tr><tr><td>596</td><td>numpy</td><td>pyside</td><td>2</td></tr><tr><td>597</td><td>random</td><td>csv</td><td>2</td></tr><tr><td>598</td><td>python-dateutil</td><td>numpy</td><td>2</td></tr><tr><td>599</td><td>pywin32</td><td>wxpython</td><td>2</td></tr><tr><td>600</td><td>warnings</td><td>traceback</td><td>2</td></tr><tr><td>601</td><td>logging</td><td>matplotlib</td><td>2</td></tr><tr><td>602</td><td>time</td><td>logging</td><td>2</td></tr><tr><td>603</td><td>tornado</td><td>sqlalchemy</td><td>2</td></tr><tr><td>604</td><td>h5py</td><td>pandas</td><td>2</td></tr><tr><td>605</td><td>time</td><td>posix</td><td>2</td></tr><tr><td>606</td><td>nltk</td><td>json</td><td>2</td></tr><tr><td>607</td><td>csv</td><td>networkx</td><td>2</td></tr><tr><td>608</td><td>warnings</td><td>tkinter</td><td>2</td></tr><tr><td>609</td><td>pyqt4</td><td>pandas</td><td>2</td></tr><tr><td>610</td><td>io</td><td>ipython</td><td>2</td></tr><tr><td>611</td><td>csv</td><td>sqlalchemy</td><td>2</td></tr><tr><td>612</td><td>multiprocessing</td><td>mmap</td><td>2</td></tr><tr><td>613</td><td>pyqt</td><td>ssl</td><td>2</td></tr><tr><td>614</td><td>numpy</td><td>shapely</td><td>2</td></tr><tr><td>615</td><td>twisted</td><td>asyncore</td><td>2</td></tr><tr><td>616</td><td>subprocess</td><td>ipython</td><td>2</td></tr><tr><td>617</td><td>pyzmq</td><td>jupyter</td><td>2</td></tr><tr><td>618</td><td>pyzmq</td><td>ipython</td><td>2</td></tr><tr><td>619</td><td>scikit-learn</td><td>random</td><td>2</td></tr><tr><td>620</td><td>setuptools</td><td>pyqt</td><td>2</td></tr><tr><td>621</td><td>pyqt</td><td>distutils</td><td>2</td></tr><tr><td>622</td><td>gdal</td><td>numpy</td><td>2</td></tr><tr><td>623</td><td>simplejson</td><td>pickle</td><td>2</td></tr><tr><td>624</td><td>py2exe</td><td>scipy</td><td>2</td></tr><tr><td>625</td><td>random</td><td>io</td><td>2</td></tr><tr><td>626</td><td>numpy</td><td>sys</td><td>2</td></tr><tr><td>627</td><td>traceback</td><td>multiprocessing</td><td>2</td></tr><tr><td>628</td><td>pyqt4</td><td>pickle</td><td>2</td></tr><tr><td>629</td><td>setuptools</td><td>zlib</td><td>2</td></tr><tr><td>630</td><td>ftplib</td><td>ssl</td><td>2</td></tr><tr><td>631</td><td>matplotlib</td><td>cgi</td><td>2</td></tr><tr><td>632</td><td>polygon</td><td>scipy</td><td>2</td></tr><tr><td>633</td><td>pip</td><td>pyqt4</td><td>2</td></tr><tr><td>634</td><td>types</td><td>regex</td><td>2</td></tr><tr><td>635</td><td>decimal</td><td>numpy</td><td>2</td></tr><tr><td>636</td><td>lxml</td><td>regex</td><td>2</td></tr><tr><td>637</td><td>virtualenv</td><td>pytz</td><td>2</td></tr><tr><td>638</td><td>ctypes</td><td>subprocess</td><td>2</td></tr><tr><td>639</td><td>numpy</td><td>subprocess</td><td>2</td></tr><tr><td>640</td><td>pyqt4</td><td>virtualenv</td><td>2</td></tr><tr><td>641</td><td>virtualenv</td><td>pyside</td><td>2</td></tr><tr><td>642</td><td>pyopengl</td><td>logging</td><td>2</td></tr><tr><td>643</td><td>pyopengl</td><td>wxpython</td><td>2</td></tr><tr><td>644</td><td>datetime</td><td>random</td><td>2</td></tr><tr><td>645</td><td>pip</td><td>zipline</td><td>2</td></tr><tr><td>646</td><td>collections</td><td>lxml</td><td>2</td></tr><tr><td>647</td><td>copy</td><td>pandas</td><td>2</td></tr><tr><td>648</td><td>tkinter</td><td>smtplib</td><td>2</td></tr><tr><td>649</td><td>subprocess</td><td>console</td><td>2</td></tr><tr><td>650</td><td>numbers</td><td>math</td><td>2</td></tr><tr><td>651</td><td>locale</td><td>ipython</td><td>2</td></tr><tr><td>652</td><td>io</td><td>subprocess</td><td>2</td></tr><tr><td>653</td><td>datetime</td><td>pytables</td><td>2</td></tr><tr><td>654</td><td>warnings</td><td>nose</td><td>2</td></tr><tr><td>655</td><td>matplotlib</td><td>email</td><td>2</td></tr><tr><td>656</td><td>uuid</td><td>string</td><td>2</td></tr><tr><td>657</td><td>multiprocessing</td><td>shelve</td><td>2</td></tr><tr><td>658</td><td>mayavi</td><td>numpy</td><td>2</td></tr><tr><td>659</td><td>logging</td><td>pickle</td><td>2</td></tr><tr><td>660</td><td>subprocess</td><td>gevent</td><td>2</td></tr><tr><td>661</td><td>wxpython</td><td>console</td><td>2</td></tr><tr><td>662</td><td>networkx</td><td>wxpython</td><td>2</td></tr><tr><td>663</td><td>sympy</td><td>cython</td><td>2</td></tr><tr><td>664</td><td>logging</td><td>doctest</td><td>2</td></tr><tr><td>665</td><td>theano</td><td>tensorflow</td><td>2</td></tr><tr><td>666</td><td>numba</td><td>ipython</td><td>2</td></tr><tr><td>667</td><td>imaplib</td><td>poplib</td><td>2</td></tr><tr><td>668</td><td>scikit-learn</td><td>string</td><td>2</td></tr><tr><td>669</td><td>pytables</td><td>numexpr</td><td>2</td></tr><tr><td>670</td><td>fractions</td><td>numpy</td><td>2</td></tr><tr><td>671</td><td>datetime</td><td>stat</td><td>2</td></tr><tr><td>672</td><td>blaze</td><td>multiprocessing</td><td>2</td></tr><tr><td>673</td><td>blaze</td><td>pandas</td><td>2</td></tr><tr><td>674</td><td>cartopy</td><td>heatmap</td><td>2</td></tr><tr><td>675</td><td>mysql-python</td><td>sqlalchemy</td><td>2</td></tr><tr><td>676</td><td>pyodbc</td><td>pyqt4</td><td>2</td></tr><tr><td>677</td><td>pyodbc</td><td>pyqt</td><td>2</td></tr><tr><td>678</td><td>select</td><td>numpy</td><td>2</td></tr><tr><td>679</td><td>pandas</td><td>reportlab</td><td>2</td></tr><tr><td>680</td><td>pyqt4</td><td>sqlalchemy</td><td>2</td></tr><tr><td>681</td><td>struct</td><td>pyopencl</td><td>2</td></tr><tr><td>682</td><td>mysql-python</td><td>ssl</td><td>2</td></tr><tr><td>683</td><td>scikit-learn</td><td>ipython</td><td>2</td></tr><tr><td>684</td><td>tornado</td><td>ssl</td><td>2</td></tr><tr><td>685</td><td>tkinter</td><td>pywin32</td><td>2</td></tr><tr><td>686</td><td>multiprocessing</td><td>theano</td><td>2</td></tr><tr><td>687</td><td>gensim</td><td>tensorflow</td><td>2</td></tr><tr><td>688</td><td>copy</td><td>string</td><td>2</td></tr><tr><td>689</td><td>hashlib</td><td>pickle</td><td>2</td></tr><tr><td>690</td><td>time</td><td>string</td><td>2</td></tr><tr><td>691</td><td>libsvm</td><td>pickle</td><td>2</td></tr><tr><td>692</td><td>lxml</td><td>virtualenv</td><td>2</td></tr><tr><td>693</td><td>pip</td><td>nose</td><td>2</td></tr><tr><td>694</td><td>pymongo</td><td>twisted</td><td>2</td></tr><tr><td>695</td><td>configparser</td><td>logging</td><td>2</td></tr><tr><td>696</td><td>struct</td><td>numpy</td><td>2</td></tr><tr><td>697</td><td>tkinter</td><td>calendar</td><td>2</td></tr><tr><td>698</td><td>pygame</td><td>pickle</td><td>2</td></tr><tr><td>699</td><td>tornado</td><td>cgi</td><td>2</td></tr><tr><td>700</td><td>sendkeys</td><td>pywin32</td><td>2</td></tr><tr><td>701</td><td>kivy</td><td>glumpy</td><td>2</td></tr><tr><td>702</td><td>kivy</td><td>vispy</td><td>2</td></tr><tr><td>703</td><td>glumpy</td><td>vispy</td><td>2</td></tr><tr><td>704</td><td>spyder</td><td>tkinter</td><td>2</td></tr><tr><td>705</td><td>qutip</td><td>numpy</td><td>2</td></tr><tr><td>706</td><td>qutip</td><td>scipy</td><td>2</td></tr><tr><td>707</td><td>cgi</td><td>sys</td><td>2</td></tr><tr><td>708</td><td>pillow</td><td>opencv</td><td>2</td></tr><tr><td>709</td><td>pillow</td><td>scikit-image</td><td>2</td></tr><tr><td>710</td><td>queue</td><td>gevent</td><td>2</td></tr><tr><td>711</td><td>pyqt4</td><td>copy</td><td>2</td></tr><tr><td>712</td><td>pip</td><td>gmpy</td><td>2</td></tr><tr><td>713</td><td>pyqt4</td><td>pygame</td><td>2</td></tr><tr><td>714</td><td>pyqt</td><td>pygame</td><td>2</td></tr><tr><td>715</td><td>csv</td><td>html</td><td>2</td></tr><tr><td>716</td><td>csv</td><td>jinja2</td><td>2</td></tr><tr><td>717</td><td>tkinter</td><td>pyhook</td><td>2</td></tr>

</tbody>
</table>
