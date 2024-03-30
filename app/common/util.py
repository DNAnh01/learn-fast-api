from typing import List


def pick_(source: any, keys: List[str]) -> dict:
    """
    This function tasks a source obj and a list of keys and return a new dictionary that includes only the keys present in the list.
    If the source is a dictionary, it directly fetches the values for the keys.
    If the source is not a dictionary, it treats it as an object and tries to fetch the attributes corresponding to the keys using getattr().
    """
    if type(source) is dict:
        return {key: source[key] for key in keys}

    return {key: getattr(source, key) for key in keys}


def clone_model(model):
    """
    Clone an arbitrary sqlalchemy model object without its primary key values.
    """
    # Ensure the model’s data is loaded before copying.
    model.id

    table = model.__table__
    non_pk_columns = [k for k in table.columns.keys() if k not in table.primary_key]
    data = {c: getattr(model, c) for c in non_pk_columns}
    if "id" in data:
        data.pop("id")
    return data
