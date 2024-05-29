import json


def new_filter(filter_, column_name, value):
    """
    Add a new filter to the existing filter
    :param filter_: The existing filter
    :param column_name: The column name to filter
    :param value: The value to filter
    :return: The new filter
    e.g.
    filter_ = '{"key1":"value1"}'
    column_name = 'key2'
    value = 'value2'
    new_filter(filter_,column_name,value) -> '{"key1":"value1","key2":"value2"}'

    e.g.
    filter_ = '123'
    column_name = 'key2'
    value = 'value2'
    new_filter(filter_,column_name,value) -> '{"0":"123","key2":"value2"}'
    """
    filter_ = json.loads(filter_)
    if isinstance(filter_, dict):
        filter_[column_name] = value
    else:
        filter2 = {}
        filter2["0"] = filter_
        filter2[column_name] = value
        filter_ = filter2
    return json.dumps(filter_)
