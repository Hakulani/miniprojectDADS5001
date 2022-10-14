# miniprojectDADS5001
Mini-Project  DADS5001  Data Analytics and Data Science Tools and Programming.
Project  by Witsarut Wongsim DADS2  6420422017
# Topic Big Data กับโลกอสังหาริมทรัพย์เข้าใจง่ายด้วย Data Visualization
# Library and Install

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

# Raw Dataset
Dataset มีจำนวน 23604 rows , 45 columns เป็นข้อมูลที่เกี่ยวกับอสังหาอย่างเช่น ราคา ประเภทอสังหา เขต จังหวัด ละติจูด ลองติจูด เป็นต้น
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
# Q&A:
เนื่องจากเขียนเป็นบทความสามารถเข้าไปอ่านใน medium > https://medium.com/@row3no6/big-data-%E0%B8%81%E0%B8%B1%E0%B8%9A%E0%B9%82%E0%B8%A5%E0%B8%81%E0%B8%AD%E0%B8%AA%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%B4%E0%B8%A1%E0%B8%97%E0%B8%A3%E0%B8%B1%E0%B8%9E%E0%B8%A2%E0%B9%8C%E0%B9%80%E0%B8%82%E0%B9%89%E0%B8%B2%E0%B9%83%E0%B8%88%E0%B8%87%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%94%E0%B9%89%E0%B8%A7%E0%B8%A2-data-visualization-f17c079f4d67 
1.ราคาอสังหาริมทรัพย์น่าจะมีการแจกแจงแบบ Normal<br />
คำตอบ คือมีลักษณะการกระจายตัวแบบไม่เป็น Normal แต่เป็นลักษณะเบ้ขวาและเมื่อดูจากทางด้านขวามี outlier<br />
2.ราคาบ้านเดี่ยว >บ้านแฝด>ทาวโฮม>คอนโด ทั้งในกรุงเทพ ปริมณฑล และต่างจังหวัด<br />
คำตอบคือ ในกรุงเทพ บ้านเดียว>บ้านแฝด> ทาวโฮม>คอนโด แต่ในจังหวัดระยองพบว่าราคาแต่ละประเภทไม่ได้แตกต่างกันมากเมื่อเทียบกับกรุงเทพ<br />
และจังหวัดนครราชสีมา และชลบุรี ราคาคอนโดค่อนข้างสูงเมื่อเทียบกับอสังหาประเภทอื่น  <br />
3.ราคาคอนโดชลบุรีและนครราชสีมาหากเรียงตาม mean และ median น่าจะติด TO10 แพงที่สุดในประเทศ<br />
คำตอบคือใช่แต่อันดับ 1 กาญจนบุรี ไม่น่าจะถูกต้อง<br />
median และ mean descending นครราชสีมาอันดับ 7 อันดับ 8 ชลบุรี สำหรับอันดับ 1 กาญจนบุรี มีเพียง 1 โครงการ ราคา 9.9 ล้าน ซึ่งเมื่อทำการหาข้อมูลเพิ่มเติม ก็เจอว่าราคาจริงคือ 9.9แสน<br />
4.ราคาบ้านเดี่ยว บ้านแฝดและทาวโฮม เรียงตาม median กรุงเทพน่าจะสูงที่สุด<br />
บ้านเดี่ยว อันดับ 1   คือพังงา med 49.5 MB โครงการมูลค่าสูง อันดับ 2 กระบี่ ส่วนกรุงเทพมาในอันดับ 3<br />
บ้านแฝด กรุงเทพมาอันดับที่ 1 ตามสมมติฐาน<br />
ทาว์โฮม อันดับ 1เป็นร้อยเอ็ด อันดับ2 คือพะเยา อันดับ 3 คือกรุงเทพ<br />
5.ราคาที่ดินสูง น่าจะทำให้โครงการมูลค่าสูง<br />
คำตอบหากพิจาณาโครงการบ้านเดี่ยว 8คลองเตยเหนือ  คลองตันเหนือ คลองตันซึ่งไม่ใช่เขตที่มีที่ดินแพงที่สุด<br />
หากพิจารณาคอนโด 1.จักรวรรดิ์อยู่ในเขตสัมพันธ์วงศ์ 2.เขตดุสิต3.ลุมพินีในเขตปทุมวันซึ่งอยู่ในกลุ่มที่มีราคาประเมิณที่ดินสูงที่สุด<br />
6.หากเราสร้าง Map Data Visualization ขึ้นมาน่าจะช่วยไขคำตอบที่เราสงสัยได้มากขึ้น
คำตอบ โดยสรุปการนำBig data มาสร้างเป็น Map Data Visualization ช่วยให้เราเข้าใจภาพรวมมากขึ้น และให้ขอมูลหลายๆอย่างที่กราฟให้ไม่ได้<br />
# Challenge: 
 ปัญหาและอุปสรรค์ในการทำงาน<br />
1.ความยากในการหา dataset และ จะเลือก dataset ไหนมาทำเลือกยากเพราะเวลามีจำกัด และเราไม่รู้ว่าจะวิเคราะห์แล้วเจออะไรบ้าง<br />
2.ปัญหาสุขภาพ เนื่องจากเป็นช่วงสอบที่พักผ่อนนอก และได้เป็นโควิด-19 ทำให้ ค่อนข้างเหนื่อยล้าในการคิดและต้องพักผ่อนทำให้เวลาเหลือน้อยลง<br />
3.ไม่เคยสร้าง Map  ทำให้ต้องใช้เวลาศึกษานานเป็นพิเศษ ทั้งทำความเข้าใจ lib การหา data vector จาก กทม. แต่ก็คุ้มที่จะทำยกอย่างเช่น ข้อมูลราคาที่ดินเป็นแค่ตาราง ถ้าไม่นำ plot เป็นแผนที่ก็คงไม่เข้าใจภาพรวม<br />
4.ข้อมูลหาย ในช่วงแรกที่สร้าง Map ข้อมูลหายไปเกินครึ่ง เนื่องจากข้อมูลบางส่วนถูก drop ไป วิธีแก้ไขคือใช้ Left join เพื่อเก็บข้อมูลสำคัญๆให้อยู่ครบ<br />
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

# 4.Dataset
![alt text](https://scontent.fbkk3-6.fna.fbcdn.net/v/t39.30808-6/295833511_145014654868736_3529467263153893155_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=730e14&_nc_eui2=AeFk0ek4UyFEBk8VS5qlm-jnUFU3aE1H2qNQVTdoTUfao53JWzG3k46jpYlBG68mqKk&_nc_ohc=Lfl-OYKRLFoAX9PacXd&_nc_zt=23&_nc_ht=scontent.fbkk3-6.fna&oh=00_AT-PYdQe3R8H-V6XUwWcURbYwhqhzT23dWpx6tbOJWK8Fw&oe=634DFF3A)

4.1 Bannai.com via facebook post: https://web.facebook.com/dataholicth/photos/a.110167148353487/145014661535402/<br />
source: https://gobestimate.com/data?fbclid=IwAR1VAJP5mLxHPr4ia8BZBpqMd790CAmUPU-lmLQKzHmiJOgMBmWXCSSOLeo<br />
copy:  https://docs.google.com/spreadsheets/d/1zEu6Lrk7LTGL3ukbJR7UwZf8f04hSeuOrIvdc2ClWyw/edit?fbclid=IwAR1IcEkPwaC_W-Gl3WXwANVj7T-Eo8bx9a8m6L4o-G7GqJvf7cRO1O2dRI0#gid=722411706<br />
4.2 ประเมินราคาที่ดินในเขตกรุงเทพมหานคร  Bangkokgis  http://www.bangkokgis.com/modules.php?m=download_shapefile<br />
ShapeFile ข้อมูลสารสนเทศภูมิศาสตร์ (แผนที่มาตราส่วน 1:20,000)<br />
Shapefile คือข้อมูลสารสนเทศภูมิศาสตร์ประเภทหนึ่งที่เก็บข้อมูลอยู่ในรูปของเวคเตอร์ (Vector) ใน 3 ลักษณะ คือ จุด (Point) เส้น (Line) และรูปปิด (Polygon) ซึ่งจะแยกเก็บออกเป็นแต่ละชั้นข้อมูล (Layer)<br /> ซึ่ง Shape File หนึ่ง ๆ จะประกอบด้วยไฟล์อย่างน้อย 3 ไฟล์ที่มีการอ้างถึงกันและกันและไม่สามารถขาดไฟล์ใดไฟล์หนึ่งไปได้ ได้แก่ ไฟล์ประเภท (.shp) ไฟล์นี้จะประกอบไปด้วยข้อมูลเวคเตอร์แต่ละประเภท <br />ซึ่งแต่ละเวคเตอร์ประกอบเป็น Shape File นั้นจะอ้างอิงพิกัด UTM ไฟล์ประเภท (.dbf) ไฟล์นี้จะประกอบไปด้วยข้อมูลในรูปแบบตารางฐานข้อมูลเพื่อแสดงรายละเอียดของแต่ละเวคเตอร์ ไฟล์ประเภท (.shx) ไฟล์นี้จะทำหน้าที่ผสานไฟล์ (.shp) และ (.dbf) เข้าด้วยกัน<br />
