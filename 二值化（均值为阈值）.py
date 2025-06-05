import pandas as pd
import numpy as np

# 构建透视图——矩阵
data_pt = pd.pivot_table(
    data,
    index = 'reporter',
    columns = 'partner',
    values = 'xxx',
)

# 构建透视图列表
data_list = [data_pt_1, data_pt_2, ……]
print(type(cost_list))

# 二值化
# 定义二值化函数
def binarize_by_rowmean(df_list):
    for df in df_list:
        # 计算每行均值（排除非数值列）
        row_means = df.mean(axis=1)
        
        # 遍历所有列进行二值化
        for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = (df[col] >= row_means).astype(int)
    
    return df_list

# 将列表中的矩阵二值化
data_bi = binarize_by_rowmean(data_list)
data_bi[0] # 检验列表中的第一个

# 全部导出成.csv
for i, df in enumerate(data_bi):
    filename = f'data_bi_{i+20xx}.csv'# 文件命名为"data_bi_20xx.csv"
    df.to_csv(filename, index=True)
