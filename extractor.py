import FinanceDataReader as fdr
import pandas as pd

start_day = "2021-01-04 00:00:00"
end_day = "2022-01-04 00:00:00"

target_kospi = fdr.StockListing("KOSPI")
target_kosdaq = fdr.StockListing("KOSDAQ")
ret = []
idx = ["code", "start", "end"]
res = pd.DataFrame([], index = idx).transpose()


for t in target_kospi["Symbol"] :
    try :
        ret = []
        
        cur = fdr.DataReader(t, '2021-01-04', '2022-01-04')
        data = cur.transpose()
        ret = [t, data[start_day].loc["Open"], data[end_day].loc["Open"]]

        if (res.empty) :
            df = pd.DataFrame(ret, index = idx)
            df = df.transpose()
            res = df
        else :
            df = pd.DataFrame(ret, index = idx)
            df = df.transpose()
            res = pd.concat([res, df])
        
        
    except:
        print("corrupted data")
        continue


for t in target_kosdaq["Symbol"] :
    try :
        ret = []
        
        cur = fdr.DataReader(t, '2021-01-04', '2022-01-04')
        data = cur.transpose()
        ret = [t, data[start_day].loc["Open"], data[end_day].loc["Open"]]

        if (res.empty) :
            df = pd.DataFrame(ret, index = idx)
            df = df.transpose()
            res = df
        else :
            df = pd.DataFrame(ret, index = idx)
            df = df.transpose()
            res = pd.concat([res, df])
        
        
    except:
        print("corrupted data")
        continue
res.to_csv("C:/Users/user/python-workspace/data_analyze/chart2021.txt", sep = '\t', index = False)

    
