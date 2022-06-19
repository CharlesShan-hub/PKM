# GeoJSON与TopoJSON

2022.6.16

[toc]

GeoJsON 和 TopoJSON 是符合 JSON 语法规则的两种数据格式，用于表示**地理信息**。

1. GeoJSON

   [GeoJSON格式在线验证](http://geojson.io/)

   [百度百科](https://baike.baidu.com/item/GeoJson/12011566?fr=aladdin)

   GeoJSON 是用于描达地理空间信息的数据格式。GeoJSON不是一种新的格式，其语法规范是符合 JS0N 格式的，只不过对其名称进行了规范，专门用于表示地理信息。

   GeoJsoN 的最外层是一个单独的对象(object）。这个对象可表示：

   1. ﻿﻿﻿几何体 (Geometry)。
   2. ﻿﻿﻿﻿﻿特征 (Feature)。
   3. ﻿﻿﻿﻿特征集合 (Featurecollection)

   最外层的 GeoJSON 里可能包含有很多子对象，每一个GeoJSON 对象都有一个type属性，表示对象的类型，type 的值必领是下面之一。

   1. ﻿﻿﻿﻿﻿point:点。

      ```json
      {
      	"type":"Point",
        "coordinates":[-105,39]//经度，纬度
      }
      ```

   2. ﻿﻿﻿﻿﻿Multipoint：多点。

   3. ﻿Linestring: 线。

      ```json
      {
      	"type":"LingString",
        "coordinates":[[-105,39],[-107,40]]
      }
      ```

   4. ﻿﻿﻿﻿﻿MultiLinestring：多线。

   5. Polygon：面

      ```json
      {
      	"type":"Polygon",
        "coordinates":[[-105,39],[-107,40],[-90,40]]
      }
      ```

   如果 type的值为 Feature（特征），那么此特征对象必须包含有变量geometry，表示几何体，geometry 的值必须是几何体对象。此特征对象还包含有一个properties，表示特性，properties 的值可以是任意SON 对象或null。例如：

   ```json
   {
     "type":"Feature",
     "properties":{
       "name":"北京"
     },
     "geometry":{
       "type":"Point",
       "coordinnates":[116.36,39.97]
     }
   }
   ```

   如果 type 的值为 Featurecollection(特征集合），则该对象必须有一个名称为 features 的成员。features 的值是一个数组，数组的每一项都是一个特征对象。

2. TopoJSON

   TopoJSON 是GeoJSON 按拓扑学编码后的扩展形式，是曲D3的作者 Mike Bostock制定的。相比 GeoJSON 直接使用 Polygon、Point之类的几何体来表示图形的方法，TOpoJSON
   中的每一个几何体都是通过将共享边（被称为arcs）整合后组成的。
   TopoJSON 消除了冗余，文件大小缩小了 80%，因为：边界线只记录一次（例如广西和广东的交界线只记录一次）地理坐标使用整数，不使用浮点数。

   [在线转换GeoJSON和TopoJSON](http://mapshaper.org)：mapshaper.org