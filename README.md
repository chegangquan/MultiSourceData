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

### 数据预处理主要步骤
#### 将txt文件转换为excel文件：txt2xls( )函数
	① 按行读取txt文件
	② 利用逗号分隔符将每一项的数据提取出来
	③ 判断每一项数据的数据类型，将数据从字符串类型转换为整型或浮点数型（比如身高和成绩）
	④ 将数据写入excel表里，并保存为“new_data2.xlsx”
        
#### 将两个数据文件进行规范化：standard( )函数
	① 读取data_1.xlsx和new_data2.xlsx文件，遍历
        ② 将学号统一为“2020XX”的格式，将性别统一为“male”或“female”，将身高的单位统一为米
        ③ 保存文件

#### 三、将两个数据文件拼接在一起：combine( )函数
	① 创建new.xlsx文件
	② 将new_data1.xlsx文件的数据按顺序写入new.xlsx文件
	③ 将data_1.xlsx文件的数据写入new.xlsx文件
	④ 将new.xlsx文件按学号进行排序
	⑤ 去掉new.xlsx文件中完全一样的数据
	⑥ 保存文件
        
#### 四、去冗余：remove( )函数
	① 按照学号遍历new.xlsx文件。先将指针指向new.xlsx文件的第一行数据，将该指针指向的数据与下一行的数据进行比较
	② 判断两个数据的学号是否重复，如果重复转向③，否则转向④
	③ 分别判断两个数据的缺失度，留下缺失度小的数据，删除缺失度大的数据，如果缺失度一样就选第一个数据。在删除数据之前，将要留下来的数据跟要删除的数据进行比对，并补全要留下来的数据。保存文件。
	④ 指针转向下一行
	⑤ 当指针指向的数据为空时，结束循环
	⑥ 将文件保存为combine.xlsx文件
        
#### 五、填补空白值：fill_empty( )函数
	① 在进行去冗余操作的时候，就把数据的空白值的位置（第几行第几列）记录下来，并保存到empty_pot列表里面
	② 根据empty_pot列表里的位置，进行填补空白值。填取空白值的内容就是上一个同学的同一项数据
	③ 保存文件

### 难题与解决
参考资料：[pandas库中读取指定行或列数据](https://blog.csdn.net/weixin_45082522/article/details/106364847)
## 总结
对两个数据源的数据进行整合清洗，对数据预处理有了进一步的认识，同时知道了数据预处理的步骤：数据清洗、数据集成、数据变换和数据规约。

本次实验主要涉及数据清洗，如针对数据数值上的各种异常情况，根据数值异常情况的不同，对数据清理具体包括移除异常值、替换缺失值、将干扰数据进行平滑处理以及纠正不一致数据。
