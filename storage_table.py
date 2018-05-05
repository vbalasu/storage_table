
# coding: utf-8

# In[1]:


from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity
import uuid

def put_object(obj, table_name = 'default', account_name='cloudmaticafunc9b4c', account_key='mBTubbUZdHy8Kdje3ukbCz6BXb0vbnmm51a4wTMIcZwjPD3YTXmRPsM3XdfVp4Vdew47lO0iv5EcXUiZCmLxlw==', partition_key='default', row_key=None):
    table_service = TableService(account_name=account_name, account_key=account_key)
    if not table_service.exists(table_name):
        table_service.create_table(table_name)
    if not row_key:
        row_key = str(uuid.uuid4())
    obj['PartitionKey'] = partition_key
    obj['RowKey'] = row_key
    table_service.insert_or_replace_entity(table_name, obj)
    return obj


# In[2]:


put_object({"name":"Vijay"})


# In[3]:


def get_object(row_key, table_name = 'default', account_name='cloudmaticafunc9b4c', account_key='mBTubbUZdHy8Kdje3ukbCz6BXb0vbnmm51a4wTMIcZwjPD3YTXmRPsM3XdfVp4Vdew47lO0iv5EcXUiZCmLxlw==', partition_key='default'):
    table_service = TableService(account_name=account_name, account_key=account_key)
    obj = table_service.get_entity(table_name=table_name, partition_key=partition_key, row_key=row_key)
    return obj 


# In[5]:


get_object('f89caf0f-9efc-43dc-b8d1-fcd6109254a5')

