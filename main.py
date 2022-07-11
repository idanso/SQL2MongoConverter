
def symbol_pharser(symbol, num)->str:
    symbols = {'<=': 'lte', '>=': 'gte', '>': 'lt', '<': 'gt'}
    return '{$' + symbols[symbol] + ':' + num + '}'


def and_or_func_helper(cond1,cond2, oper) -> str:
    return '"$' + oper + '": [{'+cond1+' },{'+cond2+'}]'+'}'


def where_pharser(where_lst) -> list:



def select_query(query) -> str:
    from_split = query.split("from")
    from_split[0] = from_split[0].split(" ")[1]
    where_split = from_split[1].split("where")
    columns_lst = from_split[0].split(",")
    tables_lst = where_split[0].split(",")
    columns_lst = list(map(lambda x: x.replace(" ", ""), columns_lst))
    tables_lst = list(map(lambda x: x.replace(" ", ""), tables_lst))
    print("columns: \n" + str(columns_lst))
    print("tables: \n" + str(tables_lst))



if __name__ == '__main__':
    query = "select id,salary from employee where age >= 35 and (designation = 'manager' or (lastname = 'johnson' and firstname like '%john%'))"
    select_query(query)