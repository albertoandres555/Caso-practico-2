import pandas as pd
import numpy as np
from tabulate import tabulate

def profiling1(df):
    print("\nPROFILING\n")
    from ydata_profiling import ProfileReport
    profile = ProfileReport(df, title="Profiling_Report")
    profile.to_notebook_iframe()
    profile.to_file('Profile_report.html')