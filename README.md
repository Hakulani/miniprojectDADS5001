# miniprojectDADS5001
Mini-Project  DADS5001  Data Analytics and Data Science Tools and Programming.
Project  by Witsarut Wongsim DADS2  6420422017
# Big Data with Real Estate in Thailand
Abstract
This mini-project utilizes data visualization tools to uncover insights from a real estate dataset in Thailand. The project explores price distributions, property type variations across regions, and the potential influence of land prices on project value.


#Update Nov2022  ไฟล์ app.py  เพิ่มพื้นหลังแผนที่ประเทศไทย
วิธีใช้งาน download csv file วางไว้ใน Folder เดียวกับ app.py
```
คำสั่ง
python
>>python app.py
```


# Data Acquisition

The dataset used in this project was retrieved from

1.Bannai.com via facebook post:  
<br>https://web.facebook.com/dataholicth/photos/a.110167148353487/145014661535402/</br>
The data source can be accessed through this Google Sheet: 
<br>source: https://gobestimate.com/data?fbclid=IwAR1VAJP5mLxHPr4ia8BZBpqMd790CAmUPU-lmLQKzHmiJOgMBmWXCSSOLeo</br>
<br>copy:  https://docs.google.com/spreadsheets/d/1zEu6Lrk7LTGL3ukbJR7UwZf8f04hSeuOrIvdc2ClWyw/edit?fbclid=IwAR1IcEkPwaC_W-Gl3WXwANVj7T-Eo8bx9a8m6L4o-G7GqJvf7cRO1O2dRI0#gid=722411706</br>)
<br>
2.ประเมินราคาที่ดินในเขตกรุงเทพมหานคร  Bangkokgis  http://www.bangkokgis.com/modules.php?m=download_shapefile<br />
ShapeFile ข้อมูลสารสนเทศภูมิศาสตร์ (แผนที่มาตราส่วน 1:20,000)<br/>
Shapefile คือข้อมูลสารสนเทศภูมิศาสตร์ประเภทหนึ่งที่เก็บข้อมูลอยู่ในรูปของเวคเตอร์ (Vector) ใน 3 ลักษณะ คือ จุด (Point) เส้น (Line) และรูปปิด (Polygon) ซึ่งจะแยกเก็บออกเป็นแต่ละชั้นข้อมูล (Layer)<br /> ซึ่ง Shape File หนึ่ง ๆ จะประกอบด้วยไฟล์อย่างน้อย 3 ไฟล์ที่มีการอ้างถึงกันและกันและไม่สามารถขาดไฟล์ใดไฟล์หนึ่งไปได้ ได้แก่ ไฟล์ประเภท (.shp) ไฟล์นี้จะประกอบไปด้วยข้อมูลเวคเตอร์แต่ละประเภท <br />ซึ่งแต่ละเวคเตอร์ประกอบเป็น Shape File นั้นจะอ้างอิงพิกัด UTM ไฟล์ประเภท (.dbf) ไฟล์นี้จะประกอบไปด้วยข้อมูลในรูปแบบตารางฐานข้อมูลเพื่อแสดงรายละเอียดของแต่ละเวคเตอร์ ไฟล์ประเภท (.shx) ไฟล์นี้จะทำหน้าที่ผสานไฟล์ (.shp) และ (.dbf) เข้าด้วยกัน<br />

The dataset contains information about 23,604 real estate projects across Thailand. It includes details such as:
Price
Property type
District
Province
Latitude & Longitude
Facilities Offered
```
RangeIndex: 23604 entries, 0 to 23603
Data columns (total 45 columns):
 #   Column                  Non-Null Count  Dtype  
---  ------                  --------------  -----  
 0   row_number              23599 non-null  float64
 1   project_id              23604 non-null  object 
 2   name_en                 23604 non-null  object 
 3   name_th                 23604 non-null  object 
 4   propertytype_id         23604 non-null  object 
 5   propertytype_name_en    23604 non-null  object 
 6   propertytype_name_th    23604 non-null  object 
 7   price_min               23489 non-null  object 
 8   developer_id            23604 non-null  object 
 9   developer_name_en       10896 non-null  object 
 10  developer_name_th       14837 non-null  object 
 11  latitude                23604 non-null  float64
 12  longitude               23599 non-null  float64
 13  neighborhood_id         19373 non-null  object 
 14  neighborhood_name_en    19374 non-null  object 
 15  neighborhood_name_th    19368 non-null  object 
 16  subdistrict_id          23584 non-null  float64
 17  subdistrict_name_en     23589 non-null  object 
 18  subdistrict_name_th     23587 non-null  object 
 19  district_id             23594 non-null  float64
 20  district_name_en        23594 non-null  object 
 21  district_name_th        23594 non-null  object 
 22  province_id             23595 non-null  float64
 23  province_name_en        23594 non-null  object 
 24  province_name_th        23594 non-null  object 
 25  zipcode                 23571 non-null  float64
 26  count_elevator          1896 non-null   object 
 27  count_elevator_service  611 non-null    object 
 28  count_floor             4727 non-null   object 
 29  count_parking           2014 non-null   object 
 30  count_tower             5 non-null      object 
 31  count_unit              21685 non-null  float64
 32  count_unittype          18597 non-null  float64
 33  facility_clubhouse      6796 non-null   float64
 34  facility_fitness        8912 non-null   float64
 35  facility_meeting        2779 non-null   float64
 36  facility_park           11744 non-null  float64
 37  facility_playground     6218 non-null   float64
 38  facility_pool           9740 non-null   float64
 39  facility_security       16261 non-null  float64
 40  date_created            23594 non-null  object 
 41  date_finish             20884 non-null  object 
 42  date_updated            23594 non-null  object 
 43  source                  23594 non-null  object 
 44  url_project             23594 non-null  object 
dtypes: float64(16), object(29)
```

# Library and Installation
Libraries and Installation
This project utilizes several Python libraries for data manipulation, geospatial analysis, and visualization. Here's how to install the required libraries:
```python
pip install Shapely
pip install geopandas
pip install joypy

!wget -q http://www.arts.chula.ac.th/ling/wp-content/uploads/TH-Sarabun_Chula1.1.zip -O font.zip
!unzip -qj font.zip TH-Sarabun_Chula1.1/THSarabunChula-Regular.ttf
# !pip install -U --pre matplotlib  
import matplotlib as mpl
mpl.font_manager.fontManager.addfont('THSarabunChula-Regular.ttf')
mpl.rc('font', family='TH Sarabun Chula')

import pandas as pd
import numpy as np
import plotly.express as px
from matplotlib.patches import Rectangle
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from shapely.geometry import Point
import geopandas as gpd
from geopandas import GeoDataFrame
from geopy.geocoders import Nominatim
import seaborn as sns
from matplotlib import pyplot as plt
```

# Q&A: Key Findings
Read in medium for better format > https://medium.com/@row3no6/big-data-%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B9%82%E0%B8%A5%E0%B8%81%E0%B8%AD%E0%B8%AA%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%97%E0%B8%A3%E0%B8%B1%E0%B8%9E%E0%B8%A2%E0%B9%8C%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B9%83%E0%B8%88%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-data-visualization-f17c079f4d67

This section explores interesting questions and insights derived from the data analysis:

1.Price Distribution: Does the real estate price follow a normal distribution?<br />
Ans.The analysis revealed a right-skewed distribution for property prices, with a longer tail towards higher values. Outliers were also identified on the higher end of the price range.<br />

![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/2842768b-b9ed-4efc-87f5-eb1bc1ffd5eb)

![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/dab7bb4f-0a88-46e3-9a15-fccab89d3d1d)


![image](https://user-images.githubusercontent.com/61573397/195838421-9472cdfb-2c26-4674-a4e3-f7a36350837c.png)
![image](https://user-images.githubusercontent.com/61573397/195838254-b0a09ed5-5fc7-40ce-923b-3f69831914f4.png)

2.Price Variation by Property Type: Is there a price difference between house and condo types across regions?<br />
Ans.The project found that, in Bangkok, detached houses are generally the most expensive, followed by townhouses, semi-detached houses, and condominiums.
![image](https://user-images.githubusercontent.com/61573397/195838527-d64780ee-90fa-4a39-8b63-cb8c297c62dc.png)
However, the price differences between property types were less pronounced in other provinces like Rayong.<br />

![image](https://user-images.githubusercontent.com/61573397/195840161-f65062ac-cffc-45a4-8d7a-eb1e68e27e49.png)

Nakhon Ratchasima and Chonburi provinces, condo prices are quite high compared to other types of real estate.  <br />
![image](https://user-images.githubusercontent.com/61573397/195840210-005b5aca-5b43-4534-8f05-b2db483f0234.png)


3.Top Ranked Provinces by Median and Mean Price: Are expensive properties concentrated in specific areas?<br />
While the initial analysis suggested Kanchanaburi might have the highest median price, further investigation revealed a data error. <br />
![image](https://user-images.githubusercontent.com/61573397/195843879-85fdc7b7-f000-4e9b-ae79-a999c2b9071c.png)

In reality, Nakhon Ratchasima and Chonburi emerged as the provinces with the highest median and mean condo prices. 
สำหรับอันดับ 1 กาญจนบุรี มีเพียง 1 โครงการ ราคา 9.9 ล้าน ซึ่งเมื่อทำการหาข้อมูลเพิ่มเติม ก็เจอว่าราคาจริงคือ 9.9แสน<br />
![image](https://user-images.githubusercontent.com/61573397/195841753-e58f236d-d740-4deb-885c-9d8974c22144.png)

![image](https://user-images.githubusercontent.com/61573397/195840323-5fb1d399-53e2-4b16-84fd-4c26177c87e8.png)
![image](https://user-images.githubusercontent.com/61573397/195840618-84d804cf-1072-4494-87a6-b0f85dc1d7b6.png)

4.Prices of detached houses, twin houses, and townhomes: Bangkok is likely to be the highest?<br />
Detached houses:
Phang Nga is the first place with a median of 49.5 MB.
Krabi is the second place.
Bangkok is the third place<br />
![image](https://user-images.githubusercontent.com/61573397/195838826-f242efcc-3545-4814-b6bc-b88a63c57e1d.png)

Twin houses:
Bangkok is the first place, as hypothesized.<br />
![image](https://user-images.githubusercontent.com/61573397/195838859-786c6627-875b-4272-94d7-d1612ff8466a.png)

Townhomes:
Roi Et is the first place.
Phayao is the second place.
Bangkok is the third place.<br />
![image](https://user-images.githubusercontent.com/61573397/195838880-239bf9b0-b8b1-461e-8a66-0993d648d0d7.png)

5.High land prices should lead to high-value projects?.
Answer: When considering detached house projects in Khlong Toei Nuea, Khlong Tan Nuea, and Khlong Tan, which are not areas with the most expensive land, this may not always be the case.<br />
Analysis:
There are a few possible explanations for this finding. One possibility is that the cost of land is not the only factor that determines the value of a project. Other factors, such as the location of the project, the amenities offered, and the quality of the construction, may also play a role.
Another possibility,This could be due to a number of factors, such as the zoning restrictions in the area, the availability of land.
![image](https://user-images.githubusercontent.com/61573397/195964220-70d4d361-990a-4753-94dc-3254ead966b8.png)

However, when considering condominiums:
Chakkraphet is located in the Samphanthawong district.
Dusit district.
Lumpini in the Pathumwan district, which are all in the group with the highest land valuation.
This suggests that land prices may play a more significant role in determining the value of condominium projects than detached house projects. This could be due to the fact that condominiums are typically located in more central areas, where land prices are higher. Additionally, condominiums are often built on smaller parcels of land, which makes the cost of land a more significant factor in the overall cost of the project.<br />
![image](https://user-images.githubusercontent.com/61573397/195838981-3eb254de-94f8-4aa8-99aa-9eef7572c179.png)
![image](https://user-images.githubusercontent.com/61573397/195839029-36767f61-3a52-4677-9de3-6cb593d6ca90.png)

6.หากเราสร้าง Map Data Visualization ขึ้นมาน่าจะช่วยไขคำตอบที่เราสงสัยได้มากขึ้น<br />
คำตอบ โดยสรุปการนำBig data มาสร้างเป็น Map Data Visualization ช่วยให้เราเข้าใจภาพรวมมากขึ้น และให้ขอมูลหลายๆอย่างที่กราฟให้ไม่ได้
![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/55d82019-e647-452a-b42c-189587538e19)

Map Data Visualization is a powerful tool that can help you see patterns and trends in your data that would be difficult to identify in a table or spreadsheet. By using different visual elements, such as color, size, and position, you can create a map that is both informative and easy to understand.

Components of the Map Data Visualization

Base Map: The base map provides the geographical context for your data. In the example you provided, the base map appears to be a simple world map. However, you can use more detailed base maps, such as street maps or political maps, depending on your data.
Data points: The data points represent the specific pieces of data you are trying to visualize. In the example you provided, the data points are circles (bubbles) in various colors and sizes. The color likely represents different property types (e.g., condo, house) and the size of the bubble might represent the price.
Color: Color can be used to represent different categories of data. For example, in the example you provided, the color of the bubble likely represents the property type.
Size: Size can be used to represent the magnitude of a data point. In the example you provided, the size of the bubble likely represents the property price (larger bubble indicates a higher price).
Benefits of Map Data Visualization

Identify patterns and trends: Map Data Visualization can help you see patterns and trends in your data that would be difficult to identify in a table or spreadsheet. For example, you might be able to see that there are more expensive properties located in certain areas of the city.
Communicate insights: Map Data Visualization can be a very effective way to communicate insights to others. Because maps are visual, they are easy to understand for people with and without a data analysis background.
Make data more engaging: Map Data Visualization can make data more engaging and interesting to look at. This can be especially helpful when you are trying to communicate complex data to a non-technical audience.

<br/>

![image](https://user-images.githubusercontent.com/61573397/195839227-c3659f37-b9cc-41a6-81c9-8fe5c77661a9.png)

![image](https://user-images.githubusercontent.com/61573397/195840744-9cf118de-2ee3-4a6f-a2e6-f591e95e9936.png)


![image](https://user-images.githubusercontent.com/61573397/195839107-295085b1-bc12-4eea-9400-a79504916e56.png)
คอนโดชลบุรีอยู่ติดทะเล อาจจะทำให้ราคาค่อนข้างสูงเมื่อเปรียบเทียบกับราคาบ้านประเภทต่างๆ 
![image](https://user-images.githubusercontent.com/61573397/195839145-74350628-ebd6-484b-8891-0f7d1a28cf25.png)

สามารถ download HTML ใน githubนี้ได้
https://github.com/Hakulani/miniprojectDADS5001/blob/main/file.html

![image](https://miro.medium.com/max/828/1*QPq6lqtMz11GGpSYHXwj0A.gif)
 

# Challenge: 
 ปัญหาและอุปสรรค์ในการทำงาน<br />
1.ความยากในการหา dataset และ จะเลือก dataset ไหนมาทำเลือกยากเพราะเวลามีจำกัด และเราไม่รู้ว่าจะวิเคราะห์แล้วเจออะไรบ้าง<br />
2.ปัญหาสุขภาพ เนื่องจากเป็นช่วงสอบที่พักผ่อนนอก และได้เป็นโควิด-19 ทำให้ ค่อนข้างเหนื่อยล้าในการคิดและต้องพักผ่อนทำให้เวลาเหลือน้อยลง<br />
3.ไม่เคยสร้าง Map  ทำให้ต้องใช้เวลาศึกษานานเป็นพิเศษ ทั้งทำความเข้าใจ lib การหา data vector จาก กทม. แต่ก็คุ้มที่จะทำยกอย่างเช่น ข้อมูลราคาที่ดินเป็นแค่ตาราง ถ้าไม่นำ plot เป็นแผนที่ก็คงไม่เข้าใจภาพรวม<br />
4.ข้อมูลหาย ในช่วงแรกที่สร้าง Map ข้อมูลหายไปเกินครึ่ง เนื่องจากข้อมูลบางส่วนถูก drop ไป วิธีแก้ไขคือใช้ Left join เพื่อเก็บข้อมูลสำคัญๆให้อยู่ครบ<br />
5.ขนาดของ Bubble ใน Map แตกต่างกันมากเกินไป ใช้ Min Max scaling ในการช่วย 
# References
# 1. Numpy
https://numpy.org/doc/stable/user/quickstart.html
https://assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf
# 2. Pandas
https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
https://pandastutor.com/
# 3. Visualization
- 3.1 MatPlotLib https://matplotlib.org/stable/tutorials/index.html
- 3.2 GeoPandas Mapping and Plotting Tools https://geopandas.org/en/stable/docs/user_guide/mapping.html
https://miro.medium.com/max/1100/1*wkFt03GrqlMHOc1ZiI12jw.png




