# Test the output of CSV files

import os
import pandas as pd

#Test for data creation on file
def test_outputs():
    data_dir = "historical_data"
    assert os.path.exists(data_dir), "Data not created"
    
    # test for output
    files = os.listdir(data_dir)
    assert len(files) > 0, "No output file found"
    
    
    #check one file below 
    # Process can be repeated for the other stocks within CSV file 
    
    aapl_data = pd.read_csv(f"{data_dir}/AAPL_historical.csv")
    assert not aapl_data.empty, "AAPL data not found"
    assert "Date" in aapl_data.columns, "Column Missing"
    
    print("All tests passed")
    
if __name__ == "__main__":
    test_outputs()
    
    