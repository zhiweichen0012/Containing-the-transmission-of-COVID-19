# Containing the transmission of COVID-19: a modelling study in 160 countries

By [Jia Rui](), [Yan Niu](), [Qiupeng Wang](), [Wei Zhang](), [Zhiwei Chen](), [Zeyu Zhao](), [Shengnan Lin](), [Yuanzhao Zhu](), [Yao Wang](), [Jingwen Xu](), [Xingchun Liu](), [Meng Yang](), [Wei Zheng](), [Kaixin Chen](), [Yilan Xia](), [Lijuan Xu](), [Rongrong Ji](), [Taisong Jin](), [Yong Chen](), [Benhua Zhao](), [Yanhua Su](), [Tie Song](), [Guoqing Hu](), [Tianmu Chen]().



## Data

The data in the folder  [./CONV_19](https://github.com/CSSEGISandData/COVID-19/tree/0689091b310b6d1a8884f7d19fa7a0f35772ac52) is operated by the Johns Hopkins University Center for Systems Science and Engineering (JHU CSSE). Also, Supported by ESRI Living Atlas Team and the Johns Hopkins University Applied Physics Lab (JHU APL).

**DATA SOURCES:** This list includes a complete list of all sources ever used in the data set, since January 21, 2010. Some sources listed here (e.g. ECDC, US CDC, BNO News) are not currently relied upon as a source of data. (Please see  [CONV_19](https://github.com/CSSEGISandData/COVID-19/tree/0689091b310b6d1a8884f7d19fa7a0f35772ac52) for details.)



## Installation

#### Requirements
- Python=3.5+
- pandas==0.23.0

Install the repository (we recommend to use [Anaconda](https://www.anaconda.com/) for installation.)

```
conda create -n CTCOVID python=3.6 -y
conda activate CTCOVID
pip install pandas==0.23.0

git clone https://github.com/zhiweichen0012/Containing-the-transmission-of-COVID-19
cd Containing-the-transmission-of-COVID-19
```



## Usage: 

###  To generate the file of confirmed cases' number.

```
python convert_csv.py
```
- China.csv: Number of confirmed cases in each province of China.
- Global.csv: Number of confirmed cases worldwide.

### To generate the file of deaths' number.
```
python convert_csv_deaths.py
```

- China_deaths.csv: Number of deaths in each province of China.
- Global_deaths.csv: Number of deaths worldwide.