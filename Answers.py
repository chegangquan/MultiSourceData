import pandas as pd
import math


# 均值函数 E(x)=1/n∑xi
def avg(a):
    return sum(a) / len(a)


# x与y的斜方差 cov(x,y)=E( (x-E(x))*(y-E(y)) )
def covf(x, y):
    return avg((x - avg(x)) * (y - avg(y)))


# 标准差 √a=√(E[a-E(a)]^2)
def std(a):
    return math.sqrt(avg((a - avg(a)) ** 2))


# 相关系数 pxy=cov(x,y)/(√x*√y)
def cor(x, y):
    return covf(x, y) / (std(x) * std(y))


def calculate():
    #读取处理完成的数据文件
    df = pd.read_excel('MultiSourceData.xlsx')
    # 将体能测试成绩各个等级转换为数值成绩
    df.loc[df['Constitution'] == 'excellent', 'Constitution'] = 90  # Constitution等于‘excellent’的Constitution赋值90
    df.loc[df['Constitution'] == 'good', 'Constitution'] = 80  # Constitution等于‘good’的Constitution赋值80
    df.loc[df['Constitution'] == 'general', 'Constitution'] = 70  # Constitution等于‘general’的Constitution赋值70
    df.loc[df['Constitution'] == 'bad', 'Constitution'] = 50  # Constitution等于‘bad’的Constitution赋值50
    # 由于C10,成绩缺失，将其赋值为C6的成绩
    df['C10'] = df['C6']

    BjCAvg = []
    for i in range(11):
        if i < 10:
            BjCAvg.append((df.loc[df['City'] == 'Beijing', ['C%d' % (i + 1)]]).mean())  # C1...C10的平均成绩
        else:
            BjCAvg.append((df.loc[df['City'] == 'Beijing', ['Constitution']]).mean())  # 体能测试平均成绩
    print("1.	北京学生所有课程平均成绩:")
    for i in range(1, 12):  # 输出北京学生所有课程平均成绩
        if i < 11:
            print("C", i, ":", BjCAvg[i - 1].values)
        else:
            print("Constitution", BjCAvg[i - 1].values, "\n")

    print("2.	学生中家乡在广州，课程1在80分以上，且课程9在9分以上的男同学的数量:",
          df.loc[(df['City'] == 'Guangzhou') & (df['C1'] > 80) & (df['Gender'] == 'male') & (df['C9'] >= 9)].shape[0],
          "\n")

    print("3.	比较广州和上海两地女生的平均体能测试成绩，哪个地区的更强些？")
    GzStudentNum = df.loc[(df['City'] == 'Guangzhou') & (df['Gender'] == 'female')].shape[0]  # 广州女学生人数
    ShStudentNum = df.loc[(df['City'] == 'Shanghai') & (df['Gender'] == 'female')].shape[0]  # 上海女学生人数
    GzConstitutionAvg = df.loc[(df['City'] == 'Guangzhou') & (df['Gender'] == 'female'), ['Constitution']].sum(
        axis=0) / GzStudentNum  # 广州学生女生的平均体能测试成绩
    ShConstitutionAvg = df.loc[(df['City'] == 'Shanghai') & (df['Gender'] == 'female'), ['Constitution']].sum(
        axis=0) / ShStudentNum  # 上海学生女生的平均体能测试成绩
    GzConstitutionAvg = float(round(GzConstitutionAvg, 2))
    ShConstitutionAvg = float(round(ShConstitutionAvg, 2))
    print("广州学生女生的平均体能测试成绩:", GzConstitutionAvg)
    print("上海学生女生的平均体能测试成绩:", ShConstitutionAvg)

    if int(GzConstitutionAvg) > int(ShConstitutionAvg):
        print("女生平均体能测试成绩：广州地区更强\n")
    else:
        if int(GzConstitutionAvg) < int(ShConstitutionAvg):
            print("女生平均体能测试成绩：上海地区更强\n")
        else:
            print("女生平均体能测试成绩：两地区一样强\n")

    print("4.	学习成绩和体能测试成绩，两者的相关性是多少？")
    EC = []  # 课程Ci均值
    cov = []  # 课程Ci与体能成绩的协方差
    STDC = []  # 课程Ci与体能成绩的标准差
    Correlation = []  # 课程Ci与体能成绩的相关系数

    # 计算体能测试成绩的期望值EConstitution
    # EConstitution = avg(df['Constitution'])
    # print("E体能：", EConstitution)
    # 计算课程Ci的期望值ECi
    # for i in range(1, 10):
    #     EC.append(avg(df['C%d' % i]))
    #     print("EC%d:" % i, EC[i - 1])

    # 计算各个C与体能的协方差
    # for i in range(1, 10):
    #     cov.append(covf(df['C%d' % i], df['Constitution']))
    #     print(cov[i - 1])
    # 体能测试的标准差
    # STDConstitution = std(df['Constitution'])
    # print('体能标准差：', STDConstitution)
    # 各个课程Ci的标准差
    # for i in range(1, 10):
    #     for j in [df['C%d' % i]]:
    #         STDC.append(math.sqrt(sum((j - EC[i - 1]) ** 2) / studentnum))
    #         print(std(j))
    #         print("stdc:", STDC[i - 1])
    # 各个课程Ci与体能成绩的相关系数
    for i in range(0, 9):
        Correlation.append(cor(df['C%d' % (i + 1)], df['Constitution']))
    # 4.	学习成绩和体能测试成绩，两者的相关性是多少？
    for i in range(0, 9):
        print("课程C%d成绩与体能成绩的相关系数为：" % (i + 1), Correlation[i])
