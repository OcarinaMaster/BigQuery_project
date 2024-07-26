import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

QUERY = ('''SELECT BUSINESS_UNIT,BUSINESS_UNIT_GL,VOUCHER_ID,DESCR,VOUCHER_LINE_NUM,DISTRIB_LINE_NUM,INVOICE_ID,
INVOICE_DT,
GROSS_AMT,
HEADER_FREIGHT,
JOURNAL_DATE,
ACCOUNTING_DT,
DEPTID,
DEPT_DESCR,
ACCOUNT,
ACCOUNT_DESCR,
PRODUCT,
PROJECT_ID,
VENDOR_ID,
VENDOR_NAME,
BUSINESS_UNIT_PO,
PO_ID,
PO_DT,
PO_LINE_NBR,
ITEM_ID,
ITEM_DESCR,
VENDOR_CATALOG,
MFG_ID,
MANUFACTURER_NAME,
MFG_CATALOG,
CATEGORY_CD,
ITEM_GROUP,
ITEM_FAMILY,
VOUCHER_PRICE,
VOUCHER_EXTENDED_AMT,
FISCAL_YEAR,
ACCOUNTING_PERIOD,
LINE_FREIGHT,
AFFILIATE,
BANK_SETID,
BANK_CD,
BANK_ACCT_KEY,
PYMNT_METHOD,
PYMNT_ID_REF,
PYMNT_DT,
SCHEDULED_PYMNT_DT,
OPRID,
VOUCHER_STYLE,
VOUCHER_TYPE,
SHORT_PAY_FLAG
FROM `supply-chain-382719.MMISDB_RPT.all_vouchers_v1`;''')
query_job = client.query(QUERY)
table = pd.DataFrame(query_job.result())
st.write("Hello World")
st.table(table.head())
