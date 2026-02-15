
# TopoJSON

## Link

* wiki：[https://en.wikipedia.org/wiki/GeoJSON#TopoJSON](https://en.wikipedia.org/wiki/GeoJSON#TopoJSON)
* 官方 github：[https://github.com/topojson](https://github.com/topojson)

## Wiki Notes

* TopoJSON 是GeoJSON 按拓扑学编码后的扩展形式，是曲D3的作者 Mike Bostock制定的。相比 GeoJSON 直接使用 Polygon、Point之类的几何体来表示图形的方法，TopoJSON
   中的每一个几何体都是通过将共享边（被称为arcs）整合后组成的。
* TopoJSON 消除了冗余，文件大小缩小了 80%，因为：边界线只记录一次（例如广西和广东的交界线只记录一次）地理坐标使用整数，不使用浮点数。
* TopoJSON文件中的几何图形不是离散地表示几何图形，而是从称为\_**弧**的\_共享线段缝合在一起。
* 弧是点的序列，而线串和多边形被定义为弧的序列。

<figure><img src="../../.gitbook/assets/image (15).png" alt=""><figcaption></figcaption></figure>
