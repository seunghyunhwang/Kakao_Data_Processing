import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

# font_path= 'C:/Windows/Fonts/NanumGothic.ttf'
# 설치된 폰트 출력
font_list = [font.name for font in fm.fontManager.ttflist]
print(font_list)
for i in font_list:
    if 'ing' in i:
        print(i)
font_name='D2Coding' # 글씨체를 변경할 수 있습니다.
# font = fm.FontProperties(fname=font_path).get_name()
# font1 = fm.FontProperties(fname=font_path)
# print(font)
plt.rcParams['axes.unicode_minus'] = False
# plt.rcParams['font.family'] = font
# plt.rcParams['font.family'] = '210 Ssiat'
plt.rcParams['font.family'] = font_name
# plt.rcParams['figure.figsize'] = [5,8]
plt.rcParams['figure.figsize'] = [12,12]
# mpl.rc('font',family=font)
print(mpl.rcParams)
pattern = r'- 202[0-9]년 [0-9]월 [0-9]일 .* -'
regex = re.compile(pattern,flags=re.IGNORECASE)
# file_name=r"2023_09_18___2023_09_21_1"
# file_name=r"2023_09_11___2023_09_17"
file_name=r"2024_01_01(Mon)___2024_02_02(Fri)"

# file_name=r"2023_09_11___2023_09_15.txt"

# file = open(r"C:\Users\hyuny\OneDrive\문서\KakaoTalk Downloads\{}".format(file_name), \
file = open(r"C:\Users\kong\Documents\카카오톡 받은 파일\{}".format(file_name), \
                "r", encoding='utf8')
# file = pd.read_csv(r"C:\Users\hyuny\OneDrive\문서\KakaoTalk Downloads\KakaoTalk_20230730_1508_31_861_group.txt", \
#                 encoding='utf8')
# print(file)
strings = file.readlines()
file.close()
# print(strings)
# print(type(strings))
df = pd.DataFrame(strings)
print(df)
data_list_date=df[0].str.findall(pattern)
print("#####\n",data_list_date,"\n#####\n")
print("#####\n",type(data_list_date),"\n#####\n")
a=data_list_date[data_list_date.str.len()>=1]
print(a)
df[0]=df[0].str.replace('[','#_')
df[0]=df[0].str.replace(']','#_')
df[0]=df[0].str.replace(' ','#_')
data_list = df[0].str.split('#_')
df['이름'] = data_list.str.get(1)
df['연식'] = data_list.str.get(2)
df['성별'] = data_list.str.get(3)
df['MBTI'] = data_list.str.get(4)
df['지역'] = data_list.str.get(5)
df.drop(0,axis='columns',inplace=True)
# print(df.dtypes)
print(df['연식'])
df['연식']=pd.to_numeric(df['연식'], errors='coerce')
# print(df.dtypes)
print(df['연식'])
df.dropna(axis='index',inplace=True)
print(df['연식'])
# quit()
# print(df)
# print(df['이름'].str.count('').astype('int64'))
# print(df['이름'].str.count(''))
# print(df['이름'].str.count('').dtype)
# print(df[df['이름'].str.count('')==3]) #이름 length에 해당하는 것만 출력.
new_df=df[df['이름'].str.count('')==3]
new_series_count=new_df["이름"].value_counts()
print(new_series_count)
# print(new_df.duplicated(subset=["이름"]).sum())
# data_list = df[0].str.split('[')
# data_list = data_list.replace('-',']')
# data_list = data_list.str.split(']')
# print(df[0])
# data_list = data_list[0].str.split(']')
# df['이름'] = data_list.str.get(0)
# df['연식'] = data_list.str.get(1)
# df['성별'] = data_list.str.get(2)
# df['MBTI'] = data_list.str.get(3)
# df['지역'] = data_list.str.get(4)
# print(data_list)
# print(df['이름'])
# print(type(df))
new_series_count.rename('챗수',inplace=True)
print(type(new_series_count))
print(new_series_count)
new_series_count=new_series_count.sort_values()
print(new_series_count)
df_new_series_count=pd.DataFrame(new_series_count)
# print(df_new_series_count.reset_index(drop=False,inplace=True))
df_new_series_count=df_new_series_count.reset_index().rename(columns={"index":"이름"})
print(df_new_series_count)
df_new_series_count
print(len(df_new_series_count["이름"]))
print(len(df_new_series_count["챗수"]))
df_new_series_count_reverse=df_new_series_count.iloc[::-1]
# sns.set_style('ticks')
# fig, ax = plt.subplots()
# fig.set_size_inches(11.7, 8.27)
# plt.yticks(fontsize=1
        #    ,
        #    rotation=90
        #    )
# plt.figure(figsize=(6,8))
# sns.set(rc={'figure.figsize':(11.7,8.27)})
# plt.rc('xtick', labelsize=200)
# plt.rc('ytick', labelsize=200)
# plt.yticks(fontsize=0.01,fontproperties='210 Ssiat')
# plt.xticks(fontsize=0.01,fontproperties='210 Ssiat')
plt.yticks(fontproperties='{}'.format(font_name))
plt.xticks(fontproperties='{}'.format(font_name))
# plt.figure(figsize=(8,64))
# plt.xscale('log')
# sns.set(font_scale=2)
print(df_new_series_count_reverse.dtypes)
print(type(df_new_series_count_reverse))
### 원하는 애들 삭제하기
# remove_list=[
#             # "탈모","콩콩","쿵야","빵또","호잇","후후",
#             # "행운","얼마","섭섭","뭐라","안녕","와우",
#             # "또롱","초롱","튜브","후후","호호","하잉",
#             # "뮤뮤","니니","또잉","히잉","야후","메론","멍뭉","마일"
#              ]
# for i in remove_list:
#     df_new_series_count_reverse = df_new_series_count_reverse[df_new_series_count_reverse["이름"] != i]
###################################
### 원하는 애들만 살리기
survival_list=[
            # "식혜","자베","참새","하이","쿠쿠","가을","건배","고심",
            # "곰돌","그린","까미","나나","다니","댕댕","댱댕","돌쇠",
            # "더쿠","동글","두두","땡보","라라","라우","로운","루팡",
            # "마루","메브","메츄","모찌","무무","무지","미래","미카","뿅뿅",
            # "민이","바다","비키","새로","신남","심심","쑤이","아자","아아",
            # "파카","어대","어피","여름","연두","우산","원숭","월든","이지",
            # "이팅","정이","쨍이","찐자","찐찐","초롱","초월","추노","품바","히히",
            # "콩콩","포니","피치","하윙","히동","히힛"

            # "메츄","원숭","히힛","찐찐","월든","땡보","무무","두두",
            # "비키","하윙","고심","어피","동글","초월","콩콩","건배"

            # "탈모","콩콩","쿵야","빵또","호잇","후후",
            # "행운","얼마","섭섭","뭐라","안녕","와우",
            # "또롱","초롱","튜브","후후","호호","하잉",
            # "뮤뮤","니니","또잉","히잉","야후","메론","멍뭉","마일"
"쿠쿠",
"료니",
"하이",
"곰돌",
"구름",
"꼬기",
"나나",
"네네",
"네오",
"뉴하",
"똠똠",
"로운",
"루미",
"릴라",
"메츄",
"모찌",
"모츠",
"뮤뉴",
"백구",
"보라",
"복지",
"선호",
"셔누",
"소라",
"슬붕",
"신남",
"아리",
"여름",
"우산",
"우아",
"융융",
"인총",
"제로",
"지닝",
"찐자",
"초롱",
"초코",
"추노",
"치피",
"칼퇴",
"케이",
"키커",
"포니",
"호공",

             ]
df_new_series_count_reverse=df_new_series_count_reverse.loc[(df_new_series_count_reverse['이름'].isin(survival_list))]
df_monitoring_out=df_new_series_count_reverse.loc[(df_new_series_count_reverse['챗수']<=30)]
print("_____________________197_line____________________________")
print(df_monitoring_out)
print(df_new_series_count_reverse)
# df_new_series_count_reverse = df_new_series_count_reverse[df_new_series_count_reverse["챗수"] < 100]
print("######방장봇제외.######","\n",len(df_new_series_count_reverse)-2,"\n",df_new_series_count_reverse,"\n#########")
plt.subplot(121)
plt.xscale('log')
ax = sns.barplot(
                y=df_new_series_count_reverse["이름"].head(len(df_new_series_count_reverse)),
                x=df_new_series_count_reverse["챗수"].head(len(df_new_series_count_reverse)),
                data=df_new_series_count_reverse,
                orient='h')
# fig = plt.figure(figsize=(6, 20))
# sns.set(font_scale=0.5)
number_count=0
for p in ax.patches:
    number_count=number_count+1
    # ax.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height() - 30),
    #             ha='center', va='center', fontsize=10, color='black', xytext=(0, 10),
    #             textcoords='offset points')
    print(p.get_width())
    ax.text(p.get_x() + p.get_width(),
            p.get_y() + p.get_height() ,
            f"{p.get_width():.0f}___{number_count}",
            # ha='center',
            # va='center',
            fontsize=7)
            # va='center')
plt.vlines(30,-0.5,len(df_new_series_count_reverse)-0.5,colors='red',linestyle='solid')
plt.hlines(len(df_new_series_count_reverse)-len(df_new_series_count_reverse[df_new_series_count_reverse['챗수']<30])-0.5,0,df_new_series_count_reverse['챗수'].max(),colors='red',linestyle='solid')
print(len(df_new_series_count_reverse[df_new_series_count_reverse['챗수']<30]))
ax.set_title("{}".format(str(file_name)))
plt.subplot(122)
ax=sns.barplot(
                y=df_monitoring_out["이름"].head(len(df_monitoring_out)),
                x=df_monitoring_out["챗수"].head(len(df_monitoring_out)),
                data=df_monitoring_out,
                orient='h')
for p in ax.patches:
    # ax.annotate("%.0f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height() - 30),
    #             ha='center', va='center', fontsize=10, color='black', xytext=(0, 10),
    #             textcoords='offset points')
    print(p.get_width())
    ax.text(p.get_x() + p.get_width(),
            p.get_y() + p.get_height() ,
            f"{p.get_width():.0f}",
            # ha='center',
            # va='center',
            fontsize=7)
            # va='center')
ax.set_title("{}".format("monitoring_list"))
plt.show()
# plt.figure(num=11)
# sns.despine()