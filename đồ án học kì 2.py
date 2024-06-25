import csv
import random
import pandas as pd
import statistics
import scipy.stats
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import sem
import scipy.stats as stats
from scipy.stats import ttest_ind

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('oto.csv')
print("in bảng dữ liệu ra màn hình",df)
first_10_rows=df[:10]
#thay đổi định dạng ngày và giờ
df1=pd.read_csv('oto.csv',index_col=0,parse_dates=True)
print(df1)
# tính tổng các giá trị thieu có trong dataframe
a= df.isnull().sum
print('các giá trị thiếu',a)
# lấy nhanh số lượng hàng và cột có trong dataframe
b=df.shape
print("số lượng hàng cột là ",b)
# lẫy mẫu ngẫu nhiên gồm 5 hàng từ dataframe
print('lấy mẫu từ dataframe ',df.sample(5))
# Chọn cột dữ liệu bạn muốn tạo bảng tần số
count= 'Vehicle Primary Use'
count1= 'Battery Electric Vehicles (BEVs)'
# Tạo bảng tần số
frequencies = df[count].value_counts()
frequencies1= df[count1].value_counts()
plt.pie(frequencies,autopct="%1.1f%%")
plt.title('biểu đồ tròn về xe')
plt.show()

# In bảng tần số
print('in bảng tần số',frequencies)
# Đọc dữ liệu từ tệp CSV
data = []
with open('oto.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(row)

# Khởi tạo biến để lưu trữ thành phố có lượng xe cao nhất
thanh_pho= None
xe_lon_nhat= 0

# Duyệt qua dữ liệu
for row in data:
    # Chuyển đổi giá trị "Vehicle Pri" sang số
    try:
        xe = int(row['Battery Electric Vehicles (BEVs)'])
    except ValueError:
        # Bỏ qua hàng nếu giá trị không thể chuyển đổi sang số
        continue

    # Cập nhật thành phố và số lượng xe  cao nhất
    if xe > xe_lon_nhat:
        thanh_pho = row['County']
        xe_lon_nhat = xe

# In kết quả
print(f"Thành phố có lượng xe điện nhiều nhất: {thanh_pho}")
print(f"Số lượng xe : {xe_lon_nhat}")

# Khởi tạo biến để lưu trữ thành phố có lượng xe cao nhất
thanh_pho1= None
xe_lon_nhat1= 0

# Duyệt qua dữ liệu
for row in data:
    # Chuyển đổi giá trị "Vehicle Pri" sang số
    try:
        xe1 = int(row['Plug-In Hybrid Electric Vehicles (PHEVs)'])
    except ValueError:
        # Bỏ qua hàng nếu giá trị không thể chuyển đổi sang số
        continue

    # Cập nhật thành phố và số lượng xe  cao nhất
    if xe1 > xe_lon_nhat1:
        thanh_pho1 = row['County']
        xe_lon_nhat1 = xe1

# In kết quả
print(f"Thành phố có lượng xe hybrid nhiều nhất: {thanh_pho1}")
print(f"Số lượng xe : {xe_lon_nhat1}")

hat= 'State'
tanso= df[hat].value_counts()
print('số lượng quận của các tiểu bang',tanso)
states = ["WA", "CA", "VA", "FL", "TX", "OR", "MD", "NC", "GA", "NJ"]
counties = [315, 95, 66, 53, 45, 34, 28, 27, 27, 21]
import matplotlib.pyplot as plt

# Tạo biểu đồ
plt.figure(figsize=(10, 6))  # Cài đặt kích thước biểu đồ
plt.bar(states, counties, color='skyblue')  # Vẽ biểu đồ cột

# Thêm tiêu đề và nhãn
plt.title("Số lượng quận theo 10 tiểu bang")
plt.xlabel("Tiểu bang")
plt.ylabel("Số lượng quận")

# Hiển thị biểu đồ
plt.xticks(rotation=0)  # Xoay nhãn x để dễ đọc hơn
plt.tight_layout()  # Tự động điều chỉnh khoảng cách giữa các thành phần
plt.show()

#xem thông tin của dataFrame
print('hiển thị thông tin dataframe')
df.info()
#hiển thị 10 dong dầu tiên
print('hiển thị 10 dong đầu tiên',df.head(10))
print("thống kê tóm tắt")
print (df.describe())
data = df['Percent Electric Vehicles']
Sai_so = sem(data)
print("Sai số tiêu chuẩn của cột là: " ,Sai_so)
data = df['Percent Electric Vehicles']
result = scipy.stats.describe (data, ddof=1, bias=False)
print('in ra phạm vi cột dữ liệu',result)
print("Lọc dữ liệu rác")
print(df.isna().sum(axis=1))
# Lấy số dòng số cột
print('số dòng và cột là ',df.shape)
#lấy mẫu ngẫu nhiên từ hai cột dữ liệu vehicle primary use và total vehicle
np.random.seed(0)
#create DataFrame
df2 = pd.DataFrame({'Vehicle Primary Use': np.repeat(np.arange(1,11), 20),
'Total Vehicles': np.random.normal(loc=7,
scale=1, size=200)})
print ("in data frame ")
print (df2)
# Thống kê số lần xuất hiện của mỗi ngày
day_counts = df['Date'].value_counts()
print (day_counts)
# Tạo biểu đồ cột cho 20 dữ liệu đầu tiên của bộ dữ liệu
fig, ax = plt.subplots()
df_limited = df.head(20)
# Vẽ cột cho dữ liệu
ax.bar(df_limited['Total Vehicles'], df_limited['Non-Electric Vehicle Total'])

# Thêm chú thích
plt.xlabel('Total vehicles')
plt.ylabel('Non-Electric Vehicle Total')
plt.title('Biểu đồ cột - 20 dữ liệu đầu tiên')
plt.xticks(df_limited['Total Vehicles'])

# Hiển thị biểu đồ
plt.show()

# Tạo biểu đồ tròn thể hiện phần trăm của các loại xe
plt.figure(figsize=(8, 8))  # Thay đổi kích thước biểu đồ nếu muốn

# Vẽ các phần trong biểu đồ
plt.pie(df_limited['Percent Electric Vehicles'], labels=df_limited['Percent Electric Vehicles'], autopct="%1.1f%%")

# Thêm tiêu đề
plt.title('Biểu đồ tròn')

# Hiển thị biểu đồ
plt.show()





