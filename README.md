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

## Stackoverflow中关键词出现次数：
统计了从Stackoverflow的36k个问题中tag中出现频率大于3的关键词。
<table>
    <thead> 
        <thead>
        <tr>
            <th>序号</th>
            <th>关键词名</th>
            <th>出现次数</th>
        </tr>
    </thead>
<tbody>

<tr><td>1</td><td>django</td><td>5600</td></tr><tr><td>2</td><td>numpy</td><td>4448</td></tr><tr><td>3</td><td>pandas</td><td>3799</td></tr><tr><td>4</td><td>matplotlib</td><td>3154</td></tr><tr><td>5</td><td>python-3.x</td><td>2721</td></tr><tr><td>6</td><td>python-2.7</td><td>2504</td></tr><tr><td>7</td><td>list</td><td>2146</td></tr><tr><td>8</td><td>string</td><td>1580</td></tr><tr><td>9</td><td>dictionary</td><td>1347</td></tr><tr><td>10</td><td>scipy</td><td>1303</td></tr><tr><td>11</td><td>flask</td><td>1285</td></tr><tr><td>12</td><td>windows</td><td>1155</td></tr><tr><td>13</td><td>regex</td><td>1044</td></tr><tr><td>14</td><td>google-app-engine</td><td>983</td></tr><tr><td>15</td><td>arrays</td><td>953</td></tr><tr><td>16</td><td>tkinter</td><td>948</td></tr><tr><td>17</td><td>pip</td><td>946</td></tr><tr><td>18</td><td>linux</td><td>850</td></tr><tr><td>19</td><td>multithreading</td><td>833</td></tr><tr><td>20</td><td>macos</td><td>826</td></tr><tr><td>21</td><td>performance</td><td>811</td></tr><tr><td>22</td><td>json</td><td>793</td></tr><tr><td>23</td><td>opencv</td><td>786</td></tr><tr><td>24</td><td>unicode</td><td>774</td></tr><tr><td>25</td><td>csv</td><td>766</td></tr><tr><td>26</td><td>sqlalchemy</td><td>752</td></tr><tr><td>27</td><td>dataframe</td><td>744</td></tr><tr><td>28</td><td>datetime</td><td>715</td></tr><tr><td>29</td><td>selenium</td><td>703</td></tr><tr><td>30</td><td>subprocess</td><td>689</td></tr><tr><td>31</td><td>multiprocessing</td><td>686</td></tr><tr><td>32</td><td>algorithm</td><td>683</td></tr><tr><td>33</td><td>tensorflow</td><td>679</td></tr><tr><td>34</td><td>mysql</td><td>674</td></tr><tr><td>35</td><td>django-models</td><td>628</td></tr><tr><td>36</td><td>virtualenv</td><td>592</td></tr><tr><td>37</td><td>c++</td><td>591</td></tr><tr><td>38</td><td>python-imaging-library</td><td>580</td></tr><tr><td>39</td><td>scikit-learn</td><td>577</td></tr><tr><td>40</td><td>file</td><td>576</td></tr><tr><td>41</td><td>beautifulsoup</td><td>565</td></tr><tr><td>42</td><td>class</td><td>560</td></tr><tr><td>43</td><td>pyqt</td><td>549</td></tr><tr><td>44</td><td>scrapy</td><td>530</td></tr><tr><td>45</td><td>ipython</td><td>526</td></tr><tr><td>46</td><td>unit-testing</td><td>523</td></tr><tr><td>47</td><td>xml</td><td>520</td></tr><tr><td>48</td><td>html</td><td>519</td></tr><tr><td>49</td><td>javascript</td><td>494</td></tr><tr><td>50</td><td>machine-learning</td><td>494</td></tr><tr><td>51</td><td>function</td><td>490</td></tr><tr><td>52</td><td>parsing</td><td>470</td></tr><tr><td>53</td><td>module</td><td>452</td></tr><tr><td>54</td><td>nltk</td><td>443</td></tr><tr><td>55</td><td>java</td><td>442</td></tr><tr><td>56</td><td>c</td><td>436</td></tr><tr><td>57</td><td>plot</td><td>436</td></tr><tr><td>58</td><td>sorting</td><td>435</td></tr><tr><td>59</td><td>image</td><td>425</td></tr><tr><td>60</td><td>import</td><td>425</td></tr><tr><td>61</td><td>image-processing</td><td>412</td></tr><tr><td>62</td><td>python-requests</td><td>409</td></tr><tr><td>63</td><td>logging</td><td>400</td></tr><tr><td>64</td><td>urllib2</td><td>394</td></tr><tr><td>65</td><td>http</td><td>379</td></tr><tr><td>66</td><td>apache-spark</td><td>371</td></tr><tr><td>67</td><td>sockets</td><td>370</td></tr><tr><td>68</td><td>web-scraping</td><td>363</td></tr><tr><td>69</td><td>nlp</td><td>349</td></tr><tr><td>70</td><td>lxml</td><td>346</td></tr><tr><td>71</td><td>math</td><td>338</td></tr><tr><td>72</td><td>pyqt4</td><td>333</td></tr><tr><td>73</td><td>selenium-webdriver</td><td>328</td></tr><tr><td>74</td><td>pycharm</td><td>327</td></tr><tr><td>75</td><td>postgresql</td><td>320</td></tr><tr><td>76</td><td>cython</td><td>319</td></tr><tr><td>77</td><td>user-interface</td><td>315</td></tr><tr><td>78</td><td>file-io</td><td>312</td></tr><tr><td>79</td><td>exception</td><td>311</td></tr><tr><td>80</td><td>sqlite</td><td>307</td></tr><tr><td>81</td><td>tuples</td><td>305</td></tr><tr><td>82</td><td>pyspark</td><td>304</td></tr><tr><td>83</td><td>encoding</td><td>302</td></tr><tr><td>84</td><td>list-comprehension</td><td>301</td></tr><tr><td>85</td><td>anaconda</td><td>299</td></tr><tr><td>86</td><td>python-2.x</td><td>296</td></tr><tr><td>87</td><td>pickle</td><td>296</td></tr><tr><td>88</td><td>python-import</td><td>295</td></tr><tr><td>89</td><td>decorator</td><td>291</td></tr><tr><td>90</td><td>ubuntu</td><td>291</td></tr><tr><td>91</td><td>utf-8</td><td>289</td></tr><tr><td>92</td><td>oop</td><td>282</td></tr><tr><td>93</td><td>celery</td><td>280</td></tr><tr><td>94</td><td>pygame</td><td>279</td></tr><tr><td>95</td><td>random</td><td>277</td></tr><tr><td>96</td><td>variables</td><td>271</td></tr><tr><td>97</td><td>shell</td><td>269</td></tr><tr><td>98</td><td>django-admin</td><td>268</td></tr><tr><td>99</td><td>bash</td><td>268</td></tr><tr><td>100</td><td>database</td><td>264</td></tr><tr><td>101</td><td>argparse</td><td>264</td></tr><tr><td>102</td><td>loops</td><td>263</td></tr><tr><td>103</td><td>ctypes</td><td>262</td></tr><tr><td>104</td><td>generator</td><td>258</td></tr><tr><td>105</td><td>inheritance</td><td>258</td></tr><tr><td>106</td><td>excel</td><td>258</td></tr><tr><td>107</td><td>sql</td><td>257</td></tr><tr><td>108</td><td>debugging</td><td>256</td></tr><tr><td>109</td><td>setuptools</td><td>253</td></tr><tr><td>110</td><td>optimization</td><td>250</td></tr><tr><td>111</td><td>django-forms</td><td>248</td></tr><tr><td>112</td><td>django-templates</td><td>246</td></tr><tr><td>113</td><td>matlab</td><td>246</td></tr><tr><td>114</td><td>wxpython</td><td>246</td></tr><tr><td>115</td><td>r</td><td>240</td></tr><tr><td>116</td><td>qt</td><td>239</td></tr><tr><td>117</td><td>mongodb</td><td>238</td></tr><tr><td>118</td><td>php</td><td>234</td></tr><tr><td>119</td><td>ruby</td><td>234</td></tr><tr><td>120</td><td>syntax</td><td>228</td></tr><tr><td>121</td><td>django-rest-framework</td><td>228</td></tr><tr><td>122</td><td>indexing</td><td>228</td></tr><tr><td>123</td><td>twisted</td><td>228</td></tr><tr><td>124</td><td>jinja2</td><td>227</td></tr><tr><td>125</td><td>floating-point</td><td>221</td></tr><tr><td>126</td><td>matrix</td><td>219</td></tr><tr><td>127</td><td>urllib</td><td>219</td></tr><tr><td>128</td><td>set</td><td>215</td></tr><tr><td>129</td><td>memory</td><td>213</td></tr><tr><td>130</td><td>recursion</td><td>212</td></tr><tr><td>131</td><td>time</td><td>211</td></tr><tr><td>132</td><td>iterator</td><td>209</td></tr><tr><td>133</td><td>date</td><td>208</td></tr><tr><td>134</td><td>python-internals</td><td>207</td></tr><tr><td>135</td><td>email</td><td>206</td></tr><tr><td>136</td><td>statistics</td><td>205</td></tr><tr><td>137</td><td>neural-network</td><td>197</td></tr><tr><td>138</td><td>command-line</td><td>195</td></tr><tr><td>139</td><td>pdf</td><td>194</td></tr><tr><td>140</td><td>ipython-notebook</td><td>192</td></tr><tr><td>141</td><td>text</td><td>192</td></tr><tr><td>142</td><td>path</td><td>189</td></tr><tr><td>143</td><td>tornado</td><td>189</td></tr><tr><td>144</td><td>object</td><td>187</td></tr><tr><td>145</td><td>split</td><td>185</td></tr><tr><td>146</td><td>python-sphinx</td><td>185</td></tr><tr><td>147</td><td>exception-handling</td><td>184</td></tr><tr><td>148</td><td>for-loop</td><td>184</td></tr><tr><td>149</td><td>apache</td><td>183</td></tr><tr><td>150</td><td>installation</td><td>179</td></tr><tr><td>151</td><td>ssl</td><td>178</td></tr><tr><td>152</td><td>audio</td><td>178</td></tr><tr><td>153</td><td>easy-install</td><td>176</td></tr><tr><td>154</td><td>rest</td><td>175</td></tr><tr><td>155</td><td>api</td><td>173</td></tr><tr><td>156</td><td>networking</td><td>172</td></tr><tr><td>157</td><td>amazon-web-services</td><td>172</td></tr><tr><td>158</td><td>heroku</td><td>172</td></tr><tr><td>159</td><td>perl</td><td>171</td></tr><tr><td>160</td><td>stdout</td><td>170</td></tr><tr><td>161</td><td>flask-sqlalchemy</td><td>170</td></tr><tr><td>162</td><td>asynchronous</td><td>169</td></tr><tr><td>163</td><td>popen</td><td>168</td></tr><tr><td>164</td><td>distutils</td><td>167</td></tr><tr><td>165</td><td>pydev</td><td>167</td></tr><tr><td>166</td><td>lambda</td><td>165</td></tr><tr><td>167</td><td>ssh</td><td>165</td></tr><tr><td>168</td><td>slice</td><td>162</td></tr><tr><td>169</td><td>printing</td><td>162</td></tr><tr><td>170</td><td>py2exe</td><td>162</td></tr><tr><td>171</td><td>mocking</td><td>161</td></tr><tr><td>172</td><td>mysql-python</td><td>160</td></tr><tr><td>173</td><td>authentication</td><td>160</td></tr><tr><td>174</td><td>forms</td><td>159</td></tr><tr><td>175</td><td>url</td><td>159</td></tr><tr><td>176</td><td>sqlite3</td><td>158</td></tr><tr><td>177</td><td>unix</td><td>158</td></tr><tr><td>178</td><td>data-structures</td><td>156</td></tr><tr><td>179</td><td>elementtree</td><td>156</td></tr><tr><td>180</td><td>coding-style</td><td>155</td></tr><tr><td>181</td><td>arguments</td><td>155</td></tr><tr><td>182</td><td>hash</td><td>155</td></tr><tr><td>183</td><td>graph</td><td>152</td></tr><tr><td>184</td><td>testing</td><td>152</td></tr><tr><td>185</td><td>methods</td><td>151</td></tr><tr><td>186</td><td>timezone</td><td>151</td></tr><tr><td>187</td><td>ajax</td><td>149</td></tr><tr><td>188</td><td>scope</td><td>149</td></tr><tr><td>189</td><td>memory-management</td><td>147</td></tr><tr><td>190</td><td>replace</td><td>147</td></tr><tr><td>191</td><td>c#</td><td>147</td></tr><tr><td>192</td><td>wsgi</td><td>147</td></tr><tr><td>193</td><td>seaborn</td><td>146</td></tr><tr><td>194</td><td>networkx</td><td>146</td></tr><tr><td>195</td><td>parallel-processing</td><td>144</td></tr><tr><td>196</td><td>binary</td><td>143</td></tr><tr><td>197</td><td>io</td><td>143</td></tr><tr><td>198</td><td>eclipse</td><td>143</td></tr><tr><td>199</td><td>string-formatting</td><td>141</td></tr><tr><td>200</td><td>psycopg2</td><td>138</td></tr><tr><td>201</td><td>paramiko</td><td>138</td></tr><tr><td>202</td><td>pymongo</td><td>138</td></tr><tr><td>203</td><td>winapi</td><td>137</td></tr><tr><td>204</td><td>multidimensional-array</td><td>136</td></tr><tr><td>205</td><td>orm</td><td>136</td></tr><tr><td>206</td><td>mod-wsgi</td><td>136</td></tr><tr><td>207</td><td>documentation</td><td>136</td></tr><tr><td>208</td><td>integer</td><td>135</td></tr><tr><td>209</td><td>keras</td><td>132</td></tr><tr><td>210</td><td>serialization</td><td>130</td></tr><tr><td>211</td><td>jython</td><td>130</td></tr><tr><td>212</td><td>django-views</td><td>130</td></tr><tr><td>213</td><td>importerror</td><td>129</td></tr><tr><td>214</td><td>install</td><td>129</td></tr><tr><td>215</td><td>package</td><td>129</td></tr><tr><td>216</td><td>xpath</td><td>129</td></tr><tr><td>217</td><td>mechanize</td><td>127</td></tr><tr><td>218</td><td>security</td><td>126</td></tr><tr><td>219</td><td>pywin32</td><td>125</td></tr><tr><td>220</td><td>web-crawler</td><td>125</td></tr><tr><td>221</td><td>vim</td><td>125</td></tr><tr><td>222</td><td>if-statement</td><td>124</td></tr><tr><td>223</td><td>terminal</td><td>124</td></tr><tr><td>224</td><td>character-encoding</td><td>123</td></tr><tr><td>225</td><td>pyside</td><td>123</td></tr><tr><td>226</td><td>types</td><td>122</td></tr><tr><td>227</td><td>attributes</td><td>122</td></tr><tr><td>228</td><td>search</td><td>121</td></tr><tr><td>229</td><td>proxy</td><td>121</td></tr><tr><td>230</td><td>python-module</td><td>120</td></tr><tr><td>231</td><td>boolean</td><td>120</td></tr><tr><td>232</td><td>iteration</td><td>119</td></tr><tr><td>233</td><td>ascii</td><td>119</td></tr><tr><td>234</td><td>git</td><td>119</td></tr><tr><td>235</td><td>twitter</td><td>119</td></tr><tr><td>236</td><td>deep-learning</td><td>118</td></tr><tr><td>237</td><td>computer-vision</td><td>118</td></tr><tr><td>238</td><td>pyinstaller</td><td>117</td></tr><tr><td>239</td><td>group-by</td><td>116</td></tr><tr><td>240</td><td>templates</td><td>116</td></tr><tr><td>241</td><td>webdriver</td><td>116</td></tr><tr><td>242</td><td>namespaces</td><td>116</td></tr><tr><td>243</td><td>time-series</td><td>116</td></tr><tr><td>244</td><td>boto</td><td>116</td></tr><tr><td>245</td><td>colors</td><td>115</td></tr><tr><td>246</td><td>pipe</td><td>114</td></tr><tr><td>247</td><td>amazon-s3</td><td>114</td></tr><tr><td>248</td><td>kivy</td><td>113</td></tr><tr><td>249</td><td>pygtk</td><td>112</td></tr><tr><td>250</td><td>swig</td><td>110</td></tr><tr><td>251</td><td>screen-scraping</td><td>109</td></tr><tr><td>252</td><td>cpython</td><td>108</td></tr><tr><td>253</td><td>queue</td><td>108</td></tr><tr><td>254</td><td>pyramid</td><td>108</td></tr><tr><td>255</td><td>input</td><td>106</td></tr><tr><td>256</td><td>django-queryset</td><td>106</td></tr><tr><td>257</td><td>histogram</td><td>106</td></tr><tr><td>258</td><td>python-2.6</td><td>106</td></tr><tr><td>259</td><td>interpolation</td><td>106</td></tr><tr><td>260</td><td>python-asyncio</td><td>106</td></tr><tr><td>261</td><td>process</td><td>104</td></tr><tr><td>262</td><td>cross-platform</td><td>104</td></tr><tr><td>263</td><td>introspection</td><td>104</td></tr><tr><td>264</td><td>html-parsing</td><td>103</td></tr><tr><td>265</td><td>metaclass</td><td>103</td></tr><tr><td>266</td><td>gtk</td><td>103</td></tr><tr><td>267</td><td>comparison</td><td>102</td></tr><tr><td>268</td><td>operators</td><td>102</td></tr><tr><td>269</td><td>google-cloud-datastore</td><td>102</td></tr><tr><td>270</td><td>jupyter</td><td>102</td></tr><tr><td>271</td><td>py.test</td><td>102</td></tr><tr><td>272</td><td>nested</td><td>101</td></tr><tr><td>273</td><td>pyodbc</td><td>101</td></tr><tr><td>274</td><td>range</td><td>100</td></tr><tr><td>275</td><td>scripting</td><td>100</td></tr><tr><td>276</td><td>post</td><td>100</td></tr><tr><td>277</td><td>directory</td><td>99</td></tr><tr><td>278</td><td>zip</td><td>99</td></tr><tr><td>279</td><td>cookies</td><td>98</td></tr><tr><td>280</td><td>jquery</td><td>98</td></tr><tr><td>281</td><td>encryption</td><td>97</td></tr><tr><td>282</td><td>itertools</td><td>97</td></tr><tr><td>283</td><td>formatting</td><td>96</td></tr><tr><td>284</td><td>jupyter-notebook</td><td>96</td></tr><tr><td>285</td><td>deployment</td><td>95</td></tr><tr><td>286</td><td>cgi</td><td>95</td></tr><tr><td>287</td><td>caching</td><td>94</td></tr><tr><td>288</td><td>pypi</td><td>93</td></tr><tr><td>289</td><td>ide</td><td>93</td></tr><tr><td>290</td><td>soap</td><td>92</td></tr><tr><td>291</td><td>merge</td><td>92</td></tr><tr><td>292</td><td>curve-fitting</td><td>92</td></tr><tr><td>293</td><td>packaging</td><td>92</td></tr><tr><td>294</td><td>boost-python</td><td>92</td></tr><tr><td>295</td><td>escaping</td><td>91</td></tr><tr><td>296</td><td>timeout</td><td>91</td></tr><tr><td>297</td><td>validation</td><td>90</td></tr><tr><td>298</td><td>sparse-matrix</td><td>90</td></tr><tr><td>299</td><td>emacs</td><td>90</td></tr><tr><td>300</td><td>hadoop</td><td>89</td></tr><tr><td>301</td><td>int</td><td>88</td></tr><tr><td>302</td><td>properties</td><td>88</td></tr><tr><td>303</td><td>redirect</td><td>88</td></tr><tr><td>304</td><td>firefox</td><td>88</td></tr><tr><td>305</td><td>openpyxl</td><td>88</td></tr><tr><td>306</td><td>python-3.4</td><td>88</td></tr><tr><td>307</td><td>fabric</td><td>88</td></tr><tr><td>308</td><td>hdf5</td><td>88</td></tr><tr><td>309</td><td>android</td><td>88</td></tr><tr><td>310</td><td>packages</td><td>87</td></tr><tr><td>311</td><td>homebrew</td><td>87</td></tr><tr><td>312</td><td>python-3.3</td><td>86</td></tr><tr><td>313</td><td>nan</td><td>86</td></tr><tr><td>314</td><td>events</td><td>86</td></tr><tr><td>315</td><td>pylint</td><td>86</td></tr><tr><td>316</td><td>css</td><td>86</td></tr><tr><td>317</td><td>environment-variables</td><td>85</td></tr><tr><td>318</td><td>dll</td><td>85</td></tr><tr><td>319</td><td>conda</td><td>85</td></tr><tr><td>320</td><td>3d</td><td>85</td></tr><tr><td>321</td><td>error-handling</td><td>84</td></tr><tr><td>322</td><td>session</td><td>84</td></tr><tr><td>323</td><td>tweepy</td><td>83</td></tr><tr><td>324</td><td>pytz</td><td>82</td></tr><tr><td>325</td><td>compilation</td><td>82</td></tr><tr><td>326</td><td>apache-spark-sql</td><td>82</td></tr><tr><td>327</td><td>animation</td><td>82</td></tr><tr><td>328</td><td>nose</td><td>82</td></tr><tr><td>329</td><td>windows-7</td><td>82</td></tr><tr><td>330</td><td>gevent</td><td>82</td></tr><tr><td>331</td><td>hex</td><td>81</td></tr><tr><td>332</td><td>python-multithreading</td><td>80</td></tr><tr><td>333</td><td>xlrd</td><td>80</td></tr><tr><td>334</td><td>.net</td><td>80</td></tr><tr><td>335</td><td>cherrypy</td><td>80</td></tr><tr><td>336</td><td>download</td><td>80</td></tr><tr><td>337</td><td>facebook</td><td>80</td></tr><tr><td>338</td><td>nginx</td><td>79</td></tr><tr><td>339</td><td>sympy</td><td>79</td></tr><tr><td>340</td><td>closures</td><td>78</td></tr><tr><td>341</td><td>design-patterns</td><td>78</td></tr><tr><td>342</td><td>metaprogramming</td><td>78</td></tr><tr><td>343</td><td>web</td><td>78</td></tr><tr><td>344</td><td>python-c-api</td><td>78</td></tr><tr><td>345</td><td>concurrency</td><td>78</td></tr><tr><td>346</td><td>ironpython</td><td>78</td></tr><tr><td>347</td><td>gunicorn</td><td>78</td></tr><tr><td>348</td><td>yaml</td><td>77</td></tr><tr><td>349</td><td>python-idle</td><td>77</td></tr><tr><td>350</td><td>web-services</td><td>77</td></tr><tr><td>351</td><td>operating-system</td><td>77</td></tr><tr><td>352</td><td>python-3.5</td><td>77</td></tr><tr><td>353</td><td>functional-programming</td><td>76</td></tr><tr><td>354</td><td>format</td><td>76</td></tr><tr><td>355</td><td>pdb</td><td>76</td></tr><tr><td>356</td><td>pyserial</td><td>76</td></tr><tr><td>357</td><td>bokeh</td><td>76</td></tr><tr><td>358</td><td>concatenation</td><td>75</td></tr><tr><td>359</td><td>console</td><td>75</td></tr><tr><td>360</td><td>vectorization</td><td>75</td></tr><tr><td>361</td><td>filter</td><td>74</td></tr><tr><td>362</td><td>automation</td><td>74</td></tr><tr><td>363</td><td>signals</td><td>74</td></tr><tr><td>364</td><td>signal-processing</td><td>74</td></tr><tr><td>365</td><td>gcc</td><td>74</td></tr><tr><td>366</td><td>phantomjs</td><td>74</td></tr><tr><td>367</td><td>linear-algebra</td><td>74</td></tr><tr><td>368</td><td>callback</td><td>74</td></tr><tr><td>369</td><td>oauth</td><td>74</td></tr><tr><td>370</td><td>wtforms</td><td>74</td></tr><tr><td>371</td><td>rabbitmq</td><td>74</td></tr><tr><td>372</td><td>statsmodels</td><td>73</td></tr><tr><td>373</td><td>global-variables</td><td>73</td></tr><tr><td>374</td><td>profiling</td><td>72</td></tr><tr><td>375</td><td>stdin</td><td>72</td></tr><tr><td>376</td><td>permutation</td><td>72</td></tr><tr><td>377</td><td>pep8</td><td>72</td></tr><tr><td>378</td><td>uwsgi</td><td>72</td></tr><tr><td>379</td><td>web-applications</td><td>72</td></tr><tr><td>380</td><td>matplotlib-basemap</td><td>72</td></tr><tr><td>381</td><td>duplicates</td><td>71</td></tr><tr><td>382</td><td>eval</td><td>71</td></tr><tr><td>383</td><td>command-line-arguments</td><td>71</td></tr><tr><td>384</td><td>serial-port</td><td>71</td></tr><tr><td>385</td><td>suds</td><td>71</td></tr><tr><td>386</td><td>memory-leaks</td><td>71</td></tr><tr><td>387</td><td>virtualenvwrapper</td><td>70</td></tr><tr><td>388</td><td>daemon</td><td>70</td></tr><tr><td>389</td><td>super</td><td>70</td></tr><tr><td>390</td><td>sum</td><td>70</td></tr><tr><td>391</td><td>pillow</td><td>70</td></tr><tr><td>392</td><td>pool</td><td>70</td></tr><tr><td>393</td><td>boost</td><td>70</td></tr><tr><td>394</td><td>pycrypto</td><td>69</td></tr><tr><td>395</td><td>node.js</td><td>69</td></tr><tr><td>396</td><td>pythonpath</td><td>68</td></tr><tr><td>397</td><td>filesystems</td><td>68</td></tr><tr><td>398</td><td>max</td><td>68</td></tr><tr><td>399</td><td>cx-freeze</td><td>68</td></tr><tr><td>400</td><td>decimal</td><td>68</td></tr><tr><td>401</td><td>typeerror</td><td>68</td></tr><tr><td>402</td><td>video</td><td>68</td></tr><tr><td>403</td><td>tcp</td><td>68</td></tr><tr><td>404</td><td>google-api</td><td>68</td></tr><tr><td>405</td><td>theano</td><td>68</td></tr><tr><td>406</td><td>classification</td><td>67</td></tr><tr><td>407</td><td>append</td><td>66</td></tr><tr><td>408</td><td>indentation</td><td>66</td></tr><tr><td>409</td><td>with-statement</td><td>66</td></tr><tr><td>410</td><td>win32com</td><td>66</td></tr><tr><td>411</td><td>garbage-collection</td><td>65</td></tr><tr><td>412</td><td>login</td><td>65</td></tr><tr><td>413</td><td>google-chrome</td><td>65</td></tr><tr><td>414</td><td>centos</td><td>64</td></tr><tr><td>415</td><td>design</td><td>64</td></tr><tr><td>416</td><td>websocket</td><td>64</td></tr><tr><td>417</td><td>cluster-analysis</td><td>64</td></tr><tr><td>418</td><td>count</td><td>64</td></tr><tr><td>419</td><td>redis</td><td>64</td></tr><tr><td>420</td><td>widget</td><td>64</td></tr><tr><td>421</td><td>copy</td><td>63</td></tr><tr><td>422</td><td>key</td><td>63</td></tr><tr><td>423</td><td>type-conversion</td><td>62</td></tr><tr><td>424</td><td>immutability</td><td>62</td></tr><tr><td>425</td><td>while-loop</td><td>62</td></tr><tr><td>426</td><td>tree</td><td>62</td></tr><tr><td>427</td><td>legend</td><td>62</td></tr><tr><td>428</td><td>spyder</td><td>62</td></tr><tr><td>429</td><td>oauth-2.0</td><td>62</td></tr><tr><td>430</td><td>amazon-ec2</td><td>62</td></tr><tr><td>431</td><td>gmail</td><td>61</td></tr><tr><td>432</td><td>interpreter</td><td>61</td></tr><tr><td>433</td><td>openssl</td><td>60</td></tr><tr><td>434</td><td>cryptography</td><td>60</td></tr><tr><td>435</td><td>ftp</td><td>60</td></tr><tr><td>436</td><td>pytables</td><td>60</td></tr><tr><td>437</td><td>autocomplete</td><td>60</td></tr><tr><td>438</td><td>spark-dataframe</td><td>60</td></tr><tr><td>439</td><td>setup.py</td><td>59</td></tr><tr><td>440</td><td>httplib</td><td>59</td></tr><tr><td>441</td><td>docstring</td><td>59</td></tr><tr><td>442</td><td>yield</td><td>58</td></tr><tr><td>443</td><td>join</td><td>58</td></tr><tr><td>444</td><td>curl</td><td>58</td></tr><tr><td>445</td><td>smtp</td><td>58</td></tr><tr><td>446</td><td>sql-server</td><td>58</td></tr><tr><td>447</td><td>wordnet</td><td>58</td></tr><tr><td>448</td><td>exec</td><td>58</td></tr><tr><td>449</td><td>boto3</td><td>58</td></tr><tr><td>450</td><td>dynamic</td><td>57</td></tr><tr><td>451</td><td>graphics</td><td>57</td></tr><tr><td>452</td><td>svm</td><td>57</td></tr><tr><td>453</td><td>reference</td><td>56</td></tr><tr><td>454</td><td>raspberry-pi</td><td>56</td></tr><tr><td>455</td><td>fft</td><td>56</td></tr><tr><td>456</td><td>request</td><td>56</td></tr><tr><td>457</td><td>subclass</td><td>56</td></tr><tr><td>458</td><td>openerp</td><td>56</td></tr><tr><td>459</td><td>reportlab</td><td>56</td></tr><tr><td>460</td><td>nested-lists</td><td>55</td></tr><tr><td>461</td><td>cron</td><td>55</td></tr><tr><td>462</td><td>internationalization</td><td>55</td></tr><tr><td>463</td><td>variable-assignment</td><td>55</td></tr><tr><td>464</td><td>python-decorators</td><td>54</td></tr><tr><td>465</td><td>primes</td><td>54</td></tr><tr><td>466</td><td>visualization</td><td>54</td></tr><tr><td>467</td><td>timestamp</td><td>54</td></tr><tr><td>468</td><td>tastypie</td><td>54</td></tr><tr><td>469</td><td>contour</td><td>54</td></tr><tr><td>470</td><td>save</td><td>54</td></tr><tr><td>471</td><td>multiple-inheritance</td><td>54</td></tr><tr><td>472</td><td>app-engine-ndb</td><td>54</td></tr><tr><td>473</td><td>rpy2</td><td>54</td></tr><tr><td>474</td><td>permissions</td><td>54</td></tr><tr><td>475</td><td>batch-file</td><td>54</td></tr><tr><td>476</td><td>numbers</td><td>53</td></tr><tr><td>477</td><td>order</td><td>53</td></tr><tr><td>478</td><td>newline</td><td>53</td></tr><tr><td>479</td><td>ms-word</td><td>53</td></tr><tr><td>480</td><td>class-method</td><td>53</td></tr><tr><td>481</td><td>static</td><td>52</td></tr><tr><td>482</td><td>return</td><td>52</td></tr><tr><td>483</td><td>compiler-construction</td><td>52</td></tr><tr><td>484</td><td>svg</td><td>52</td></tr><tr><td>485</td><td>contextmanager</td><td>52</td></tr><tr><td>486</td><td>interactive</td><td>52</td></tr><tr><td>487</td><td>werkzeug</td><td>52</td></tr><tr><td>488</td><td>regression</td><td>52</td></tr><tr><td>489</td><td>scapy</td><td>52</td></tr><tr><td>490</td><td>pylons</td><td>52</td></tr><tr><td>491</td><td>model</td><td>52</td></tr><tr><td>492</td><td>zipfile</td><td>52</td></tr><tr><td>493</td><td>rounding</td><td>51</td></tr><tr><td>494</td><td>caffe</td><td>51</td></tr><tr><td>495</td><td>configuration</td><td>51</td></tr><tr><td>496</td><td>network-programming</td><td>51</td></tr><tr><td>497</td><td>passwords</td><td>50</td></tr><tr><td>498</td><td>multi-index</td><td>50</td></tr><tr><td>499</td><td>find</td><td>50</td></tr><tr><td>500</td><td>executable</td><td>50</td></tr><tr><td>501</td><td>language-agnostic</td><td>50</td></tr><tr><td>502</td><td>timedelta</td><td>50</td></tr><tr><td>503</td><td>compression</td><td>50</td></tr><tr><td>504</td><td>benchmarking</td><td>50</td></tr><tr><td>505</td><td>bottle</td><td>50</td></tr><tr><td>506</td><td>file-upload</td><td>50</td></tr><tr><td>507</td><td>vector</td><td>50</td></tr><tr><td>508</td><td>qt4</td><td>50</td></tr><tr><td>509</td><td>scrapy-spider</td><td>50</td></tr><tr><td>510</td><td>mongoengine</td><td>50</td></tr><tr><td>511</td><td>pyyaml</td><td>49</td></tr><tr><td>512</td><td>combinations</td><td>49</td></tr><tr><td>513</td><td>xml-parsing</td><td>48</td></tr><tr><td>514</td><td>getattr</td><td>48</td></tr><tr><td>515</td><td>https</td><td>48</td></tr><tr><td>516</td><td>egg</td><td>48</td></tr><tr><td>517</td><td>base64</td><td>48</td></tr><tr><td>518</td><td>thread-safety</td><td>48</td></tr><tr><td>519</td><td>button</td><td>48</td></tr><tr><td>520</td><td>colorbar</td><td>48</td></tr><tr><td>521</td><td>combinatorics</td><td>48</td></tr><tr><td>522</td><td>64bit</td><td>48</td></tr><tr><td>523</td><td>h5py</td><td>48</td></tr><tr><td>524</td><td>python-multiprocessing</td><td>48</td></tr><tr><td>525</td><td>byte</td><td>48</td></tr><tr><td>526</td><td>imagemagick</td><td>48</td></tr><tr><td>527</td><td>fortran</td><td>48</td></tr><tr><td>528</td><td>gdb</td><td>48</td></tr><tr><td>529</td><td>osx-snow-leopard</td><td>48</td></tr><tr><td>530</td><td>django-settings</td><td>48</td></tr><tr><td>531</td><td>selenium-chromedriver</td><td>48</td></tr><tr><td>532</td><td>gil</td><td>47</td></tr><tr><td>533</td><td>warnings</td><td>47</td></tr><tr><td>534</td><td>language-design</td><td>46</td></tr><tr><td>535</td><td>sublimetext2</td><td>46</td></tr><tr><td>536</td><td>scala</td><td>46</td></tr><tr><td>537</td><td>fonts</td><td>46</td></tr><tr><td>538</td><td>ffmpeg</td><td>46</td></tr><tr><td>539</td><td>python-2.5</td><td>46</td></tr><tr><td>540</td><td>nonblocking</td><td>46</td></tr><tr><td>541</td><td>geometry</td><td>46</td></tr><tr><td>542</td><td>mapreduce</td><td>46</td></tr><tr><td>543</td><td>pypy</td><td>46</td></tr><tr><td>544</td><td>latex</td><td>46</td></tr><tr><td>545</td><td>series</td><td>46</td></tr><tr><td>546</td><td>stringio</td><td>46</td></tr><tr><td>547</td><td>enthought</td><td>46</td></tr><tr><td>548</td><td>pygobject</td><td>46</td></tr><tr><td>549</td><td>heatmap</td><td>45</td></tr><tr><td>550</td><td>instance</td><td>45</td></tr><tr><td>551</td><td>enums</td><td>44</td></tr><tr><td>552</td><td>stream</td><td>44</td></tr><tr><td>553</td><td>parameters</td><td>44</td></tr><tr><td>554</td><td>collections</td><td>44</td></tr><tr><td>555</td><td>pycurl</td><td>44</td></tr><tr><td>556</td><td>screenshot</td><td>44</td></tr><tr><td>557</td><td>reflection</td><td>44</td></tr><tr><td>558</td><td>django-signals</td><td>44</td></tr><tr><td>559</td><td>pyparsing</td><td>44</td></tr><tr><td>560</td><td>webserver</td><td>44</td></tr><tr><td>561</td><td>scatter-plot</td><td>44</td></tr><tr><td>562</td><td>python-3.6</td><td>43</td></tr><tr><td>563</td><td>browser</td><td>43</td></tr><tr><td>564</td><td>diff</td><td>43</td></tr><tr><td>565</td><td>cmd</td><td>43</td></tr><tr><td>566</td><td>dns</td><td>43</td></tr><tr><td>567</td><td>docker</td><td>43</td></tr><tr><td>568</td><td>parameter-passing</td><td>42</td></tr><tr><td>569</td><td>unique</td><td>42</td></tr><tr><td>570</td><td>gzip</td><td>42</td></tr><tr><td>571</td><td>http-headers</td><td>42</td></tr><tr><td>572</td><td>pretty-print</td><td>42</td></tr><tr><td>573</td><td>monkeypatching</td><td>42</td></tr><tr><td>574</td><td>locking</td><td>42</td></tr><tr><td>575</td><td>constructor</td><td>42</td></tr><tr><td>576</td><td>ip-address</td><td>42</td></tr><tr><td>577</td><td>struct</td><td>42</td></tr><tr><td>578</td><td>django-celery</td><td>42</td></tr><tr><td>579</td><td>mp3</td><td>42</td></tr><tr><td>580</td><td>ipc</td><td>42</td></tr><tr><td>581</td><td>google-api-python-client</td><td>42</td></tr><tr><td>582</td><td>iterable-unpacking</td><td>42</td></tr><tr><td>583</td><td>django-orm</td><td>42</td></tr><tr><td>584</td><td>namedtuple</td><td>42</td></tr><tr><td>585</td><td>imap</td><td>42</td></tr><tr><td>586</td><td>tk</td><td>42</td></tr><tr><td>587</td><td>osx-mavericks</td><td>42</td></tr><tr><td>588</td><td>cx-oracle</td><td>42</td></tr><tr><td>589</td><td>restructuredtext</td><td>42</td></tr><tr><td>590</td><td>ocr</td><td>42</td></tr><tr><td>591</td><td>flask-login</td><td>42</td></tr><tr><td>592</td><td>version</td><td>42</td></tr><tr><td>593</td><td>memcached</td><td>42</td></tr><tr><td>594</td><td>png</td><td>42</td></tr><tr><td>595</td><td>python-unicode</td><td>41</td></tr><tr><td>596</td><td>extract</td><td>41</td></tr><tr><td>597</td><td>global</td><td>41</td></tr><tr><td>598</td><td>distribution</td><td>41</td></tr><tr><td>599</td><td>azure</td><td>41</td></tr><tr><td>600</td><td>build</td><td>41</td></tr><tr><td>601</td><td>idioms</td><td>40</td></tr><tr><td>602</td><td>memoization</td><td>40</td></tr><tr><td>603</td><td>try-catch</td><td>40</td></tr><tr><td>604</td><td>macports</td><td>40</td></tr><tr><td>605</td><td>xlwt</td><td>40</td></tr><tr><td>606</td><td>probability</td><td>40</td></tr><tr><td>607</td><td>django-south</td><td>40</td></tr><tr><td>608</td><td>python.net</td><td>40</td></tr><tr><td>609</td><td>rdd</td><td>40</td></tr><tr><td>610</td><td>webapp2</td><td>40</td></tr><tr><td>611</td><td>smtplib</td><td>40</td></tr><tr><td>612</td><td>decode</td><td>40</td></tr><tr><td>613</td><td>line</td><td>40</td></tr><tr><td>614</td><td>override</td><td>40</td></tr><tr><td>615</td><td>django-authentication</td><td>40</td></tr><tr><td>616</td><td>pyqt5</td><td>40</td></tr><tr><td>617</td><td>foreign-keys</td><td>40</td></tr><tr><td>618</td><td>streaming</td><td>39</td></tr><tr><td>619</td><td>pyobjc</td><td>39</td></tr><tr><td>620</td><td>django-urls</td><td>39</td></tr><tr><td>621</td><td>naming-conventions</td><td>38</td></tr><tr><td>622</td><td>equality</td><td>38</td></tr><tr><td>623</td><td>descriptor</td><td>38</td></tr><tr><td>624</td><td>dependencies</td><td>38</td></tr><tr><td>625</td><td>simplejson</td><td>38</td></tr><tr><td>626</td><td>scientific-computing</td><td>38</td></tr><tr><td>627</td><td>configparser</td><td>38</td></tr><tr><td>628</td><td>graphviz</td><td>38</td></tr><tr><td>629</td><td>self</td><td>38</td></tr><tr><td>630</td><td>elasticsearch</td><td>38</td></tr><tr><td>631</td><td>wav</td><td>38</td></tr><tr><td>632</td><td>haskell</td><td>38</td></tr><tr><td>633</td><td>many-to-many</td><td>38</td></tr><tr><td>634</td><td>runtime-error</td><td>38</td></tr><tr><td>635</td><td>ttk</td><td>38</td></tr><tr><td>636</td><td>command-line-
## Stackoverflow中同一问题下包共同出现情况
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
