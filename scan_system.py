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
from socket import getservbyname, getservbyport

st.set_page_config(layout="wide")

@st.cache
def list_files(file_loc: str) -> List:
    """
        Function to list files on a local file system
    """

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
    """
        List running processes
    """
    res = []
    for proc in psutil.process_iter(['pid', 'name', 'username', 'exe']):
        res.append(proc.info)

    return pd.DataFrame(res)

def get_network():
    """
        Function gets all the connections and maps to actual port types
    """
    network_df = pd.DataFrame.from_dict(list(map(lambda x: { 'pid': str(x.pid), 'laddr': str(x.laddr), 
                            'raddr': str(x.raddr), 'status': str(x.status), 'type': str(x.type), 
                            'rport_type': map_port(x.raddr),
                            'lport_type': map_port(x.laddr)} ,  
                            psutil.net_connections(kind='inet'))))

    #network_df.set_index('pid', inplace=True)
    return network_df                            

def map_port(addr):
    """
        Helper for port name resolution
    """
    if addr:
        try:
            return getservbyport(addr.port)
        except OSError:
            return ""
    else:
        return ""

def get_win_services():
    """
        Windows service listing
    """
    services = []
    for ser in psutil.win_service_iter():
        services.append(ser.as_dict())

    ret = pd.DataFrame.from_dict(services)

    return ret
    


def search_frame(df, srch_str):
    """
        Generic data frame searching function, assumes OR search across all columns
    """
    base = pd.Series([False] *df.shape[0])
    for col in df.columns:
        base|= df[col].astype('str').str.contains(srch_str)
    
    return df[base]


st.title("🐞 System report! 🐞 ")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Suspicious files")
    result = st.multiselect("Files to find", options=extension_series.values, help="find these files", 
                            default=['.cpp'])                

    mask = file_series.str.contains('🐞', regex = False)  # all false
    for res in result:
        mask = mask | file_series.str.contains(res, regex=False)
        
    st.dataframe(file_series[mask])

    st.markdown("### Windows Services")
    srch_val_sv = st.text_input('Search services table')
    srv_df = get_win_services()
    st.dataframe(search_frame(srv_df, srch_val_sv))


with col2:
    st.markdown("### Running processes")
    srch_val_ps = st.text_input('Search process table')
    ps = list_processes()
    
    st.dataframe(search_frame(ps, srch_val_ps))

    st.markdown("### Network connections")
    srch_val_nf = st.text_input('Search network connections')
    nf_df = get_network()
    st.dataframe(search_frame(nf_df, srch_val_nf))


