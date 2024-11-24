import pandas as pd
df=pd.read_excel('Data.xlsx')
df['SIMPLE SCORE']=(df['Q1_1_SCORE-Q1_1_SCORE']+
df['Q1_2_SCORE-Q1_2_SCORE']+
df['Q1_3_SCORE-Q1_3_SCORE']+
df['Q1_4_SCORE-Q1_4_SCORE']+
df['Q1_6_SCORE-Q1_6_SCORE']+
df['Q2_5_SCORE-Q2_5_SCORE'])/6

df['QUICK SCORE']=(df['Q2_1_SCORE-Q2_1_SCORE']+
df['Q2_2_SCORE-Q2_2_SCORE']+
df['Q2_6_SCORE-Q2_6_SCORE']+
df['Q2_3_SCORE-Q2_3_SCORE']+
df['Q2_4_SCORE-Q2_4_SCORE']+
df['Q2_5_SCORE-Q2_5_SCORE'])/6

df['TRUST SCORE']=(df['Q3_1_SCORE-Q3_1_SCORE']+
df['Q3_2_SCORE-Q3_2_SCORE']+
df['Q3_3_SCORE-Q3_3_SCORE']+
df['Q3_4_SCORE-Q3_4_SCORE']+
df['Q3_5_SCORE-Q3_5_SCORE']+
df['Q3_6_SCORE-Q3_6_SCORE'])/6

df['WORTH SCORE']=(df['Q4_2_SCORE-Q4_2_SCORE']+
df['Q4_3_SCORE-Q4_3_SCORE'])/2

df['OVERALL SCORE']=(df['SIMPLE SCORE']+df['QUICK SCORE']+df['TRUST SCORE']+df['WORTH SCORE'])/4

Branch_List=list(df['Branch_Name'].unique())



#print("Type Branch list - "+str(type(Branch_List)))
def Score_Generator(Branch_Name):
    Overall=df[df['Branch_Name']==Branch_Name]['OVERALL SCORE'].mean()
    Simple=df[df['Branch_Name']==Branch_Name]['SIMPLE SCORE'].mean()
    Quick=df[df['Branch_Name']==Branch_Name]['QUICK SCORE'].mean()
    Trust=df[df['Branch_Name']==Branch_Name]['TRUST SCORE'].mean()
    Worth=df[df['Branch_Name']==Branch_Name]['WORTH SCORE'].mean()
    return Overall,Simple,Quick,Trust,Worth

def Branch_Name():
    Branch_Name=list(df['Branch_Name'].unique())
    return Branch_Name

def Score_Generator_Dict():
    Global_Overall_Score=round(df['OVERALL SCORE'].mean())
    branch_score_dict={}
    for  items in Branch_List:
        branch_score_dict[items]=round(df[df['Branch_Name']==items]['OVERALL SCORE'].mean())
    return branch_score_dict,Global_Overall_Score



def Easy_To_Handle_Score(Branch_Name):
    E_to_H_Branch=df[df['Branch_Name']==Branch_Name]['Q1_5_SCORE-Q1_5_SCORE'].mean()
    E_to_H_Overall=df['Q1_5_SCORE-Q1_5_SCORE'].mean()
    return round(E_to_H_Branch,2),round(E_to_H_Overall,2)






