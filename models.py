from dashboard.apps.pages.experiments.XML_parser import Tables
from django.db import models


def table_atts(table_name):
    return Tables.table_atts(table_name)


def table_data(table_name):
    att_list = table_atts(table_name)
    data_in_tuples = Tables.table_data(table_name)
    list_of_lists = [list(elem) for elem in data_in_tuples]
    list_of_lists.insert(0, att_list)
    return list_of_lists
    


