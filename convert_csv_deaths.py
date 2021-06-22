# coding=UTF-8
'''
@Description: file content
@Author: Chen Zhiwei
@Date: 2020-04-22 17:10:25
@LastEditTime: 2020-04-22 17:15:06
'''
import numpy as np
import pandas as pd
import json
import requests

FILE_INPUT_PATH = './COVID_19/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
FILE_China_OUTPUT_PATH = 'China_deaths.csv'
FILE_Global_OUTPUT_PATH = 'Global_deaths.csv'
# True
ENG = True


def translate(word):
    # 有道词典 api
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
    # 传输的参数，其中 i 为需要翻译的内容
    key = {
        'type': "AUTO",
        'i': word,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "ue": "UTF-8",
        "action": "FY_BY_CLICKBUTTON",
        "typoResult": "true"
    }
    # key 这个字典为发送给有道词典服务器的内容
    response = requests.post(url, data=key)
    # 判断服务器是否相应成功
    if response.status_code == 200:
        # 然后相应的结果
        return response.text
    else:
        print("有道词典调用失败")
        # 相应失败就返回空
        return None


def get_relative_confirmed(df):
    # 新增一列
    new_colum = [int(i) for i in np.zeros(df.shape[0])]
    df.insert(0, 'Temp', new_colum)
    # 转置
    df_T = df.T
    # 获取新增病例
    df_T = df_T.diff()
    # 删除之前新增的列
    df_T = df_T.drop('Temp')
    df_T = df_T.astype('int')
    assert True in (df_T[df_T >= 0].values), 'Data Error!'
    return df_T


def translate_format(df):
    names = df.columns.tolist()
    if ENG:
        return names
    new_names = []
    for i in names:
        # 翻译
        result = json.loads(translate(i))
        new_names.append(result['translateResult'][0][0]['tgt'])
    return new_names


if __name__ == "__main__":
    df = pd.DataFrame(pd.read_csv(FILE_INPUT_PATH))

    # 中国数据
    df_China = df.loc[(df['Country/Region'] == 'China')
                      | (df['Country/Region'] == 'Taiwan*')]
    # 单独处理台湾
    tw_r = df[(df['Country/Region'] == 'Taiwan*')].index.tolist()[0]
    df_China.loc[tw_r, 'Province/State'] = 'Taiwan'

    df_China = df_China.drop(columns=['Country/Region', 'Lat', 'Long'])
    df_China = df_China.set_index('Province/State')
    # df_China = get_relative_confirmed(df_China)
    df_China = df_China.T
    df_China['SUM'] = df_China.apply(lambda x: x.sum(), axis=1)
    new_names = translate_format(df_China)
    df_China.columns = new_names
    df_China.to_csv(FILE_China_OUTPUT_PATH)

    # 全球数据
    df_global = df.drop(columns=['Province/State', 'Lat', 'Long'])
    # 单独处理台湾
    tw_r = df[(df['Country/Region'] == 'Taiwan*')].index.tolist()[0]
    df_global.loc[tw_r, 'Country/Region'] = 'China'
    # 国家合并
    df_global = df_global.groupby('Country/Region').sum()
    # df_global = get_relative_confirmed(df_global)
    df_global = df_global.T
    df_global['SUM'] = df_global.apply(lambda x: x.sum(), axis=1)
    new_names = translate_format(df_global)
    df_global.columns = new_names
    df_global.to_csv(FILE_Global_OUTPUT_PATH)

    print("Complete!")