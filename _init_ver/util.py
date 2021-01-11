
def replace(index, Table_):
    focus_item(index, Table_)
    Table_.tree.delete(Table_.tree.selection())

def focus_item(index, Table_):
    child_id = Table_.tree.get_children()[index]
    Table_.tree.focus(child_id)
    Table_.tree.selection_set(child_id)

def wholesale_check(qty, product_):
    if ( qty >= product_[0][5]):
        price = int(product_[0][4])
    else:
        price = int(product_[0][3])
    return price

def check_if_exists(search, list):
    for i in range(0, len(list)):
        if( list[i] == search):
            return 1
    return 0

def get_index(search, list):
    for i in range(0, len(list)):
        if( list[i] == search):
            return i