
def symbol_pharser(symbol, num)->str:
    symbols = {'<=': 'lte', '>=': 'gte', '>': 'lt', '<': 'gt'}
    return '{$' + symbols[symbol] + ':' + num + '}'


def and_or_func_helper(cond1,cond2, oper) -> str:
    cond1_after_check = contain_and_or(cond1)
    cond2_after_check = contain_and_or(cond2)
    if (cond1_after_check)!=None:
        if (cond2_after_check(cond2))!=None:
            return '"$' + oper + '": [{' \
                   + and_or_func_helper(cond1_after_check[0][0],cond1_after_check[0][1]
                                        ,cond1_after_check[1]) + ' },{' + and_or_func_helper(cond2_after_check[0][0],
                                        cond2_after_check[0][1],cond2_after_check[1]) + '}]' + '}'
        else:
            #only the first part in recursion the second is a regular statement
            #need to add code here, im not sure yet how to do this
            pass
    elif (cond2_after_check)!=None:
        # only the second part in recursion the first is a regular statement
        pass
    # if we got until here we defintly dont have another sub-statment and we can return statement
    return '"$' + oper + '": [{'+cond1+' },{'+cond2+'}]'+'}'

def contain_and_or(cond)-> tuple:
    for i in cond:
        if i=='and':
            return str(cond).split('and'),'and'
        if i=='or':
            return str(cond).split('or'),'or'
    return None

def where_pharser(where_lst) -> list:
    pass


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