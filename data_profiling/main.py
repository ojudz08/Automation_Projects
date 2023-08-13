from pathlib import Path
import os
import pandas as pd
import numpy as np
from datetime import datetime as dt


class dataProfiler():

    def __init__(self, source_folder, output_folder, output_filename):
        self.src_folder = os.path.join(Path(__file__).parents[0], source_folder)
        self.output_folder = os.path.join(Path(__file__).parents[0], output_folder)
        self.output_result = os.path.join(Path(__file__).parents[0], output_folder, output_filename)


    def checkFolderExist(self):
        """"Checks whether your folder exist. If not, create that folder"""
        if not os.path.exists(self.src_folder):
            os.makedirs(self.src_folder)
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)


    def readSourceFile(self):
        """Read source data with csv file type within the source data folder"""
        check_folder_exist = self.checkFolderExist()
        file = os.listdir(self.src_folder)
        result = pd.DataFrame()
        for i in range(0, len(file)):
            if file[0][-3:] == 'csv': 
                data_df = pd.read_csv(os.path.join(self.src_folder, file[i]))
                result = pd.concat([result, data_df], axis=0)
        return result
    

    def dataShape(self):
        """Returns column names and data shape"""
        source_data = self.readSourceFile()
        idx, values = zip(source_data.shape)
        data_cols = source_data.columns
        data_columns, data_shape = pd.DataFrame(data_cols).rename(columns={0: 'Column Names'}), pd.DataFrame(idx, values).reset_index().rename(columns={'index': 'Total Columns', 0: 'Total Rows'})
        result = pd.concat([data_columns, data_shape], axis=1)
        return result


    def summaryStatistics(self):
        """Returns the summary statistics of your numeric columns"""
        source_data = self.readSourceFile()
        source_stat = source_data.describe()
        return source_stat


    def columnProfile(self):
        """Returns the combined column data type and column null/distinct"""
        column_dataType = self.columnDataType()
        column_nullDistint = self.columnNullDistinct()
        result = pd.merge(column_dataType, column_nullDistint)
        return result


    def columnDataType(self):
        """Returns the -- Null Count, Distinct Count, Null Count Pct and Distinct Count Pct"""
        source_data = self.readSourceFile().convert_dtypes(infer_objects=True)
        temp_df = source_data[source_data.select_dtypes(include=['string']).columns]
        
        dt_cols = []      
        for col in temp_df.columns:
            try:
                pd.api.types.is_datetime64_dtype(pd.to_datetime(source_data[col], format='mixed')) == True
                source_data[col] = source_data[col].apply(pd.to_datetime)
                dt_cols.append(col)
            except:
                pass
    
        result = pd.DataFrame(source_data.dtypes).reset_index().rename(columns={'index': 'Column Names', 0: 'Column Data Type'})
        
        measurer = np.vectorize(len)
        minLen_df = pd.DataFrame(np.squeeze(measurer(source_data.values.astype(str)).min(axis=0)).tolist()).rename(columns={0: 'Min Length'})
        maxLen_df = pd.DataFrame(np.squeeze(measurer(source_data.values.astype(str)).max(axis=0)).tolist()).rename(columns={0: 'Max Length'})
        result = pd.concat([result, minLen_df, maxLen_df], axis=1)
        
        return result


    def columnNullDistinct(self):
        """Returns the column data type -- string, int64, float64, datetime64[ns]"""
        source_data = self.readSourceFile()

        distinct_col, distinct_count, null_count = {}, {}, {}

        for col in source_data.columns:
            distinct_col[col] = source_data[col].unique()
            distinct_count[col] = source_data[col].nunique()
            null_count[col] = source_data[col].isnull().sum()

        distinct_col_df, distinct_count_df, null_count_df = pd.DataFrame(distinct_col.items()), pd.DataFrame(distinct_count.items()), pd.DataFrame(null_count.items())

        distinct_col_df = distinct_col_df.rename(columns={0: "Column Names", 1: "Distinct Values"})
        distinct_count_df = distinct_count_df.rename(columns={0: "Column Names", 1: "Distinct Count"})
        null_count_df = null_count_df.rename(columns={0: "Column Names", 1: "Null Count"})

        merge_df = [df.set_index(["Column Names"]) for df in [null_count_df, distinct_count_df]]
        merge_df = pd.concat(merge_df, axis=1).reset_index()

        merge_df["Null Count Pct"] = merge_df["Null Count"] / len(source_data)
        merge_df["Distinct Count Pct"] = (merge_df["Distinct Count"] / len(source_data)) * 100

        distinct_col_df = distinct_col_df.set_index("Column Names").T
        result = pd.DataFrame()

        for col in distinct_col_df.columns:
            result = pd.concat([result, pd.DataFrame(distinct_col_df[col][0])], axis=1)
        result.columns = list(distinct_col_df)
        return merge_df
    

    def distinctColumnValues(self):
        """Counts the number of distinct values that occur in the column"""
        source_data = self.readSourceFile()
        result = pd.DataFrame()

        distinct_count_df = pd.DataFrame(pd.Series({col: source_data[col].nunique() for col in source_data}))
        distinct_col_df = pd.DataFrame(pd.Series({col: source_data[col].unique() for col in source_data}))

        df = pd.concat([distinct_count_df, distinct_col_df], axis=1)
        df = df.rename(columns={df.columns[0]: "Distinct Count", df.columns[1]: "Distinct Values"})
        
        temp = pd.DataFrame(df.iloc[:, 1].T).T
        for col in temp.columns:
            result = pd.concat([result, pd.DataFrame(temp[col][0])], axis=1)
        result.columns = list(temp)
        return result
    

    def saveResultToExcel(self):
        """Saves the data shape, column profile, data statistics and distinct values of each columns in separate tab. Output is an xlsx"""
        data_shape = self.dataShape()
        column_profile = self.columnProfile()
        data_statistics = self.summaryStatistics()
        column_distinct = self.distinctColumnValues()
        

        print("Running data profiler script...")
        
        with pd.ExcelWriter(self.output_result) as writer:
            data_shape.to_excel(writer, sheet_name="data_shape", index=False)
            column_profile.to_excel(writer, sheet_name="column_profile", index=False)
            data_statistics.to_excel(writer, sheet_name="data_statistics", index=True)
            column_distinct.to_excel(writer, sheet_name="column_distinct", index=False)
        
        print("Done data profiling! ")



if __name__ == "__main__":
    src_folder = "src_data"
    output_folder = "output"
    output_filename = "data_profile_output.xlsx"

    data = dataProfiler(src_folder, output_folder, output_filename)
    save_data = data.saveResultToExcel()
    