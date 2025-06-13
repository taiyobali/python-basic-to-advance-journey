
# class 9: DataFrame(pandas)
# DataFrame is a class of pandas library, 2D Table(row and columns)
import pandas as pd
df = pd.read_csv("student_info.csv")  #file path
print(df)
print(type(df))
# there are some data types in dataframe
# object=str, int64=int,float64=float,bool
import pandas as pd
student_data = [(1,"Mellor","CST",22,"Florida","Florida Tech"),
                (2,"Alex","CSE",21,"California","Harvard"),
                (3,"Maximus",22,"Applied Math","NewYork","MIT"),
                (4,"Antonio",23,"Chemical","California","Harvard")]
df = pd.DataFrame(student_data,columns=["SL.","Name","Subject","Age","HomeAddress","University"])
print(df)
print(type(df))
# some methods and operations in DataFrame
import pandas as pd
data = pd.read_csv("student_info.csv")
print(data)
print(data.head())
print(data.tail())
print(data.info())
print(data.shape)
print(data.size)
print(data.index)
print(data.dtypes)
print(data.values)
print(data.columns)
print(data.Subject)
print(data["Address"])
print(data[["Name","Subject"]])
