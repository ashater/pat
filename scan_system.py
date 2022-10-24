# abspath to a folder as a string
#folder = '/home/myname/a_folder/'
# in windows:
folder = r'C:\\'
# or folder = 'C:/a_folder/'

import os
import re
from typing import List
import pandas as pd
import streamlit as st
import psutil

@st.cache
def list_files(file_loc: str) -> List:

    file_list = []
    extension_list = set()
    for dirname, dirs, files in os.walk(folder):    
        for filename in files:
            filename_without_extension, extension = os.path.splitext(filename)
            extension_list.add(extension.lower())
            file_list.append(os.path.join(dirname, filename))

    return pd.Series(file_list), pd.Series(list(extension_list))


file_series, extension_series = list_files(folder)


def list_processes():
    res = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        res.append(proc.info)

    return pd.DataFrame(res).set_index('pid')



st.title("🐞 Malware report! 🐞 ")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Suspicious files")
    result = st.multiselect("Files to find", options=extension_series.values, help="find these files", 
                            default=['.xlsx'])                

    mask = file_series.str.contains('🐞', regex = False)  # all false
    for res in result:
        mask = mask | file_series.str.contains(res, regex=False)
        

    st.dataframe(file_series[mask])


with col2:
    st.markdown("### Running processes")
    srch_val = st.text_input('Search process name')
    ps = list_processes()
    mask = ps.name.str.contains(srch_val)
    st.dataframe(ps[mask])