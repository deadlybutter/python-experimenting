import pandas
import seaborn as sns
sns.set(style="darkgrid", color_codes=True)

prison = pandas.read_csv('Prison_Admissions__Beginning_2008.csv', header=1, dtype=str)
prison.columns = ["year", "month", "month_code", "admin_type", "county_commit", "county_residence", "gender", "age", "crime"]
# print(prison.head())

g = sns.jointplot("admin_type", "county_commit", data=prison, kind="reg", xlim=(0, 60), ylim=(0, 12), color="r", size=7)
