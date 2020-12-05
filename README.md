# MultiSourceData
# 实验一《多源数据集成、清洗和统计》
## 组员信息

组长：陈港泉

组员：黎家豪

黎家豪主要负责对两个数据源的数据进行整合清洗，陈港泉对合并后的数据进行统计回答实验的四个问题。
## 作业题目和内容
广州大学某班有同学100人，现要从两个数据源汇总学生数据。第一个数据源在数据库中，第二个数据源在txt文件中，两个数据源课程存在缺失、冗余和不一致性，请用C/C++/Java程序实现对两个数据源的一致性合并以及每个学生样本的数值量化。

● 数据库表：ID (int),  姓名(string), 家乡(string:限定为Beijing / Guangzhou / Shenzhen / Shanghai), 性别（string:boy/girl）、身高（float:单位是cm)）、课程1成绩（float）、课程2成绩（float）、...、课程10成绩(float)、体能测试成绩（string：bad/general/good/excellent）；其中课程1-课程5为百分制，课程6-课程10为十分制。

● txt文件：ID(string：6位学号)，性别（string:male/female）、身高（string:单位是m)）、课程1成绩（string）、课程2成绩（string）、...、课程10成绩(string)、体能测试成绩（string：差/一般/良好/优秀）；其中课程1-课程5为百分制，课程6-课程10为十分制。
参考

### 两个数据源
execl文件和txt文件

一.数据源1.xlsx

一.数据源2-逗号间隔.txt

两个数据源内容存在缺失、冗余和不一致性
数据库中Stu表（execl表）数据


|ID  |Name  |City  | Gender |Heigh  |C1  | ... |C10  |Constitution|
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
|1|Sub|Beijing|boy|160|87||9|good|
|2|Zhu|Shenzhen|girl|177|66||8	|excellent|
|...  |...  |... | ... |  ...|... |  |...  |...  |



student.txt中


ID,Name,City,Gender,Height,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,Constitution

202001,Marks,Shenzhen,male,1.66,77,100,84,71,91,6,7,6,8,,general

202002,Wayne,Shenzhen,female,1.59,77,78,89,59,93,10,6,5,9,,good

...		...		...		..		...	..		...		...		...	...		..		...	..	

### 问题
两个数据源合并后读入内存，并统计：
1. 学生中家乡在Beijing的所有课程的平均成绩。
2. 学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量。(备注：该处做了修正，课程10数据为空，更改为课程9)
3. 比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？
4. 学习成绩和体能测试成绩，两者的相关性是多少？（九门课的成绩分别与体能成绩计算相关性）

提示
参考数据结构：
Student{
int id;
string id;
vector<float> data;
}

可能用到的公式：

1均值公式      ：![在这里插入图片描述](https://img-blog.csdnimg.cn/20201205165657481.png#pic_center)


2协方差公式	：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201205165620490.png#pic_center)

3z-score规范化	：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20201205165729525.png#pic_center)

4数组A和数组B的相关性	：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20201205165750656.png#pic_center)

        这里A=[a1, a2,...ak,..., an],
        B=[b1, b2,...bk,..., bn],
        mean(A)代表A中元素的平均值
        std是标准差，即对协方差的开平方。

注意：计算部分不能调用库函数；画图/可视化显示可以用可视化API或工具实现。



## 作业环境：文件说明，函数说明，调用的函数库以及涉及哪些技术
环境：win10、pycharm、python3.6

语言：python、Markdown

调用的函数库：pandas、openpyxl

### 文件说明
数据源1：data_1.xlsx

数据源2：data_2.txt

数据处理代码文件：DataProcess.py

数据统计代码文件：Answers.py

main:main.py

合并清洗完成后的数据文件：MultiSourceData.xlsx

运行结果截图：运行截图.png

### 函数说明
Answers.py

均值函数： `def avg(a):
    return sum(a) / len(a)`
 
 协方差：`def covf(x, y):
    return avg((x - avg(x)) * (y - avg(y)))`
 
 标准差：`def std(a):
    return math.sqrt(avg((a - avg(a)) ** 2))`

相关系数：`def cor(x, y):
    return covf(x, y) / (std(x) * std(y))`

DataProcess.py

### 难题与解决
参考资料：[pandas库中读取指定行或列数据](https://blog.csdn.net/weixin_45082522/article/details/106364847)
## 总结
