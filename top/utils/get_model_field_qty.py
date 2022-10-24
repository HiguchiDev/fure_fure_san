

def get_model_field_qty(model, filter_name_prefix):
    meta_fields = model._meta.get_fields()

    qty_cnt = 0
    for i, meta_field in enumerate(meta_fields):
        if i > 0 and meta_field.name.startswith(filter_name_prefix):
            qty_cnt += 1

    return qty_cnt