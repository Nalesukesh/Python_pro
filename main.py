import pandas as pd
from sqlalchemy import create_engine
from colorama import Fore
import pytest



server = 'PC-PC'
database = 'Automation'
driver = 'ODBC driver 17 for SQL Server'
database_con = f'mssql://@{server}/{database}?driver={driver}'
engine = create_engine(database_con)
connection = engine.connect()

# path = r"C:\Users\nales\OneDrive\Desktop\Test_Case_Evidence.xlsx"
# writer = pd.ExcelWriter(path, engine='xlsxwriter')
writer=pd.ExcelWriter(r"C:\Users\nales\OneDrive\Desktop\Test_Case_Evidence.xlsx")

src_df = pd.read_sql_query('select * from emp;', connection)
tgt_df = pd.read_sql_query('select * from emp;', connection)


@pytest.mark.usefixtures('setup')
class Test_DWH:
    def test_str_val(self):
        print(Fore.BLUE, "Test case 1: Structure Validation")
        src_str = pd.read_sql(
            "select TABLE_NAME,COLUMN_NAME,ORDINAL_POSITION,IS_NULLABLE,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='emp';",
            connection)
        tgt_str = pd.read_sql(
            "select TABLE_NAME,COLUMN_NAME,ORDINAL_POSITION,IS_NULLABLE,DATA_TYPE,CHARACTER_MAXIMUM_LENGTH from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='employees';",
            connection)

        str_val = src_str.eq(tgt_str)

        if src_df.compare(tgt_df).empty:
            print(Fore.GREEN, "structure validation successful")
        else:
            print(Fore.RED, "structure mismatched\nstructure validation Failed")
            print(str_val)

        src_str.to_excel(writer, sheet_name="Source str", index=False)
        tgt_str.to_excel(writer, sheet_name="target str", index=False)
        str_val.to_excel(writer, sheet_name="structure validation", index=False)

    def test_count(self):
        print(Fore.BLUE, "Test case 2:Count Validation")

        src_count = len(src_df)
        tgt_count = len(tgt_df)
        count_val = src_count == tgt_count

        if src_count == tgt_count:
            print(Fore.GREEN, "Count Validation Successful")
        else:
            print(Fore.RED, "Count mismatched \nCount validation Failed")

        count_validation = pd.DataFrame({"src_count": src_count,
                                         "tgt_count": tgt_count,
                                         "count_val": count_val}, index=[0])
        count_validation.to_excel(writer, sheet_name="Count Validation", index=False)

    def test_data(self):
        print(Fore.BLUE, "Test case 3: Data Validation")

        if src_df.compare(tgt_df).empty:
            print(Fore.GREEN, "Data validation successful \n all data matched")
        else:
            print(Fore.RED, "Data validation unsuccessful \n following records are not matched")

        src_df.to_excel(writer, sheet_name="source data", index=False)
        tgt_df.to_excel(writer, sheet_name="target data", index=False)
        src_df.eq(tgt_df).to_excel(writer, sheet_name="Data Validation", index=False)

    def test_null_val(self):
        print(Fore.BLUE, "Test case 4: Null value Validation")

        tgt_null = pd.read_sql("select * from employees where employee_id is null", connection)

        tgt_null_count = tgt_null.isnull().any(axis=1).sum()
        if tgt_null_count > 0:
            print(Fore.RED, "Null value is present\n Null value validation Failed")
        else:
            print(Fore.GREEN, "Null Value Validation Successful")

        null_validation = pd.DataFrame({"tgt_null_count": tgt_null_count}, index=[0])

        null_validation.to_excel(writer, sheet_name="Null_val", index=False)

    def test_duplicate(self):
        print(Fore.BLUE, "Test case 5:Duplicate Validation")

        tgt_dup = tgt_df.duplicated().sum()

        if tgt_dup > 0:
            print(Fore.RED, "Duplicate record is found \nDuplicate Validation unsuccessful")

        else:
            print(Fore.GREEN, "Duplicate Validation Successful")

        duplicate_validation = pd.DataFrame({"tgt_dup": tgt_dup}, index=[0])
        duplicate_validation.to_excel(writer, sheet_name="Duplicate_Val", index=False)

        writer.close()

# # count validation
# print("Count validation")
# src_count = pd.read_sql('select count(*) from emp', connection)
# trg_count = pd.read_sql('select count(*) from emp1', connection)
#
# if src_count.compare(trg_count).empty:
#     print("source and target data count is matched")
# else:
#     print("source and target data count is not matched")
#     print(src_count, trg_count)
#
# src_count.to_excel(writer, sheet_name="source count", index=False)
# trg_count.to_excel(writer, sheet_name="Target count", index=False)
# src_count.eq(trg_count).to_excel(writer, sheet_name="Count validation", index=False)
#
# # Null value validation
# print("Null value Validation")
#
# src_null = pd.read_sql("select count(*)-count(EMPNO) from emp", connection)
# trg_null = pd.read_sql("select count(*)-count(EMPNO) from emp", connection2)
# trg_null.isnull().to_excel(r"C:\Users\PC\Desktop\Test_Val.xlsx")
# src_null_count = src_null.isnull().any(axis=1).sum()
# trg_null_count = trg_null.isnull().any(axis=1).sum()
#
# if src_null_count > 0:
#     print("Null validation is unsuccessful")
#     print(src_null_count)
# else:
#     print("Null validation is successful")
#
# if trg_null_count > 0:
#     print("Null validation is unsuccessful")
#     print(trg_null_count)
# else:
#     print("Null validation is successful")
#
# null_count_df = pd.DataFrame({"Null count in Target table": trg_null_count,
#                               "Null count in src table": src_null_count}, index=[0])
# null_count_df.to_excel(writer, sheet_name="null count validation", index=False)
#
# # Duplicate validation
# print("Duplicate Validation")
# src_dup = pd.read_sql(
#     "select EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO,inc_salary,count(*) from emp group by EMPNO,ENAME,JOB,MGR,HIREDATE,SAL,COMM,DEPTNO,inc_salary having count(*)>1;",
#     connection)
# src_df.duplicated().to_excel(r'C:\Users\PC\Desktop\Test_Val.xlsx')
# if src_df.duplicated().sum() > 0:
#     print("src Duplicate validation unsuccessful")
# else:
#     print("src Duplicate validation successfull")
# if trg_df.duplicated().sum() > 0:
#     print("trg dup val unsuccessful")
# else:
#     print("trg dup val successful")
#
# src_df.duplicated().to_excel(writer, sheet_name="Duplicate val", index=False)
# dup_count = pd.DataFrame({"Total no of Duplicate in Src": src_df.duplicated().sum(),
#                           "Total no of Dup in Target": trg_df.duplicated().sum()}, index=[0])
# dup_count.to_excel(writer, sheet_name='Duplicate count val', index=False)
#
# writer.save()
# writer.close()
#
#
#
#
