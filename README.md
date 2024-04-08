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


# Dataset
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

![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/b46671c2-3193-4344-9448-5e871bc67450)
 

2.Price Variation by Property Type: Is there a price difference between house and condo types across regions?<br />
Ans.The project found that, in Bangkok, detached houses are generally the most expensive, followed by townhouses, semi-detached houses, and condominiums.
![image](https://user-images.githubusercontent.com/61573397/195838527-d64780ee-90fa-4a39-8b63-cb8c297c62dc.png)
However, the price differences between property types were less pronounced in other provinces like Rayong.<br />

![image](https://user-images.githubusercontent.com/61573397/195840161-f65062ac-cffc-45a4-8d7a-eb1e68e27e49.png)

Nakhon Ratchasima and Chonburi provinces, condo prices are quite high compared to other types of real estate.  <br />
![image](https://user-images.githubusercontent.com/61573397/195840210-005b5aca-5b43-4534-8f05-b2db483f0234.png)


3.Top Ranked Provinces by Median and Mean Price: Are expensive properties concentrated in specific areas?<br />
While the initial analysis suggested Kanchanaburi might have the highest median price, further investigation revealed a data error. <br />
![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/d7556c02-3944-4d27-a7a6-f848ff9e697d)


In reality, #7Nakhon Ratchasima and #8Chonburi emerged as the provinces with the highest median and mean condo prices. 
![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/3928b0fe-9287-40d0-aa6b-8996fd91b70b)

For number 1, Kanchanaburi has only 1 project priced at 9.9 million, which when searching for more information, found that the actual price is 990,000.<br />
![image](https://user-images.githubusercontent.com/61573397/195841753-e58f236d-d740-4deb-885c-9d8974c22144.png)

After updating the correct information causing the ranking of leaders to change Kanchanaburi to the last place Prachuap rose to number 1

![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/e787af64-1d1b-4526-9d15-a177c1cdeb6a)

4.Prices of detached houses, twin houses, and townhomes: Bangkok is likely to be the highest?<br />
Detached houses:
Phang Nga is the first place with a median of 49.5 MB.
Krabi is the second place.
Bangkok is the third place<br />
![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/d9ef7c71-9a23-4473-a2dd-2a20c7334430)


Twin houses:
Bangkok is the first place, as hypothesized.<br />
![image](https://user-images.githubusercontent.com/61573397/195838859-786c6627-875b-4272-94d7-d1612ff8466a.png)

Townhomes:
Roi Et is the first place.
Phayao is the second place.
Bangkok is the third place.<br />
![image](https://user-images.githubusercontent.com/61573397/195838880-239bf9b0-b8b1-461e-8a66-0993d648d0d7.png)

5.High land prices should lead to high-value projects?<br />

Answer: When considering detached house projects in Khlong Toei Nuea, Khlong Tan Nuea, and Khlong Tan , which are not areas with the most expensive land, this may not always be the case.<br />
Analysis:High land prices may not make it worthwhile to build detached houses that require a large area. Compared to condo project units, you may be able to make more profit.
This is because the cost of land is a significant factor in the overall cost of building a detached house. When land prices are high, it may be more difficult to make a profit on detached house projects.
On the other hand, condo project units typically have a smaller footprint, which means that the cost of land is a less significant factor in the overall cost of the project. Additionally, condo units are often in high demand, which can lead to higher profits.

![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/c5006fac-7429-4375-b736-60fe12d3fe66)

However, when considering condominiums:
Chakkraphet is located in the Samphanthawong district.
Dusit district.
Lumpini in the Pathumwan district, which are all in the group with the highest land valuation.
This suggests that land prices may play a more significant role in determining the value of condominium projects than detached house projects. This could be due to the fact that condominiums are typically located in more central areas, where land prices are higher. Additionally, condominiums are often built on smaller parcels of land, which makes the cost of land a more significant factor in the overall cost of the project.<br />
 
![image](https://user-images.githubusercontent.com/61573397/195839029-36767f61-3a52-4677-9de3-6cb593d6ca90.png)

6.If we create Data Visualization demographic analytics, it should be able to help answer more of our questions?<br />
 
![image](https://github.com/Hakulani/miniprojectDADS5001/assets/61573397/55d82019-e647-452a-b42c-189587538e19)

Data Visualization demographic analytics is a powerful tool that can help you see patterns and trends in your data that would be difficult to identify in a table or spreadsheet. By using different visual elements, such as color, size, and position, you can create a map that is both informative and easy to understand.

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
Chonburi condo next to the sea This may cause the price to be quite high when compared to the prices of various types of houses.

![image](https://user-images.githubusercontent.com/61573397/195839145-74350628-ebd6-484b-8891-0f7d1a28cf25.png)

สามารถ download HTML ใน githubนี้ได้
https://github.com/Hakulani/miniprojectDADS5001/blob/main/file.html

![image](https://miro.medium.com/max/828/1*QPq6lqtMz11GGpSYHXwj0A.gif)
 

# Challenges Faced:<br />
1. Data Acquisition and Selection<br />
-Difficulty in finding suitable datasets within a limited timeframe.<br />
-Uncertainty regarding potential discoveries within the chosen dataset.<br />
2. Health Issues<br />
-Exhaustion due to overlapping commitments during the exam period and contracting COVID-19.<br />
-Reduced cognitive function and limited time for analysis due to illness.<br />
3. Map Vector Creation<br />
-Steep learning curve for map creation, including understanding libraries and sourcing vector data for Bangkok.<br />
-Time-consuming process, but ultimately rewarding as it provides a holistic view of the data (e.g., land price data is incomprehensible without mapping).<br />
4.Missing value
-Over 50% of data was lost during initial map creation due to data droppage.<br />
-Implemented left join to preserve critical data.<br />
5.Disparate Bubble Sizes on Map
-Employed Min Max scaling to address the issue of vastly different bubble sizes.<br />

Lessons Learned
1. Data Exploration and Preparation

Importance of exploring and understanding the data before analysis.
Careful data preparation to ensure accuracy and reliability of results.
2. Time Management and Prioritization

Effective time management and prioritization of tasks to mitigate the impact of unexpected challenges.
Balancing academic commitments with personal health and well-being.
3. Learning New Skills

Willingness to learn new skills and technologies to address project requirements.
Continuous learning and adaptation to improve analytical capabilities.
4. Data Visualization

Importance of data visualization in enhancing data comprehension and communicating insights effectively.
Exploration of different visualization techniques to suit the specific data and audience.
5. Problem Solving and Troubleshooting

Ability to identify and address data-related issues and challenges.
Adoption of a proactive approach to problem-solving and troubleshooting.

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




