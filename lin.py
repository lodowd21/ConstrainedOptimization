from scipy.optimize import linprog
import numpy as np


# converts constraints into readable form for linprog function
def to_int(lst):
    if (type(lst[0]) is list):
        for k in range(len(lst)):
            for i in range(len(lst[k])):
                lst[k][i] = eval(lst[k][i])
    else:
        for i in range(len(lst)):
            lst[i] = eval(lst[i])

    return lst


# returns the right side of the constraint
def pop_val(lst):
    lst_res = []
    for k in range(len(lst)):
        lst_res.append(lst[k].pop())

    return lst_res


# Replaces constraint's unneccessary chars
def rep(lst):
    exist = ["-", "=", "(", ")", " ", "++-", "<", ">", "<=", ">="]
    repl = ["+-", "+", "", "", "", "+-", "+", "+", "+", "+"]
    for i in range(len(exist)):
        lst = lst.replace(exist[i], repl[i])
    return lst.split("+")


# removes and replaces variable with a 1
def rem(var, lst):
    if (type(lst) is list):
        for k in range(len(lst)):
            for i in range(len(var)):
                lst[k] = lst[k].replace(var[i], "1")
            lst[k] = rep(lst[k])
    else:
        for i in range(len(var)):
            lst = lst.replace(var[i], "1")
        lst = rep(lst)

    return lst


# checks each constraint to see which variable is not present
def check_index(var, constr):
    not_var = []
    for k in range(len(constr)):
        for i in range(len(var)):
            if var[i] not in constr[k]:
                not_var.append(True)
            else:
                not_var.append(False)
    return not_var


# checks to see whether the constraint contains an inequality or equality
def check_ineq(constr):
    ineq_bool = []
    for i in constr:
        if "<" in i:
            ineq_bool.append(1)
        elif ">" in i:
            ineq_bool.append(-1)
        else:
            ineq_bool.append(0)

    return ineq_bool


# Checks maxi bool to determine negation
def negate(constr, maxi):
    if maxi:
        for i in range(len(constr)):
            constr[i] = constr[i] * -1
    return constr


# Checks for negation for ">" sign
def ge_negate(constr, ineq):
    for i in range(len(ineq)):
        # print(ineq[i])
        if ineq[i] == -1:
            for k in range(len(constr) - 1):
                constr[i][k] = constr[i][k] * -1
                # print(constr[i][k])
    return constr


# iterates through constr and separates eq
def rem_eq(constr, check_ineq):
    constr_eq = []
    for i in range(len(constr)):
        if check_ineq[i] == 0:
            constr_eq.append(constr[i])
    return constr_eq


# iterates through constr and separates ineq
def rem_ineq(constr, check_ineq):
    constr_ineq = []
    for i in range(len(constr)):
        if check_ineq[i] != 0:
            constr_ineq.append(constr[i])
    return constr_ineq


# Checks whether the constraints contain ineqs and eqs as this will throw exceptions if not called right
def ret_result(maxi, constr_eq, constr_ineq, constr_eq_res, constr_ineq_res, obj):
    if constr_eq.size == 0:
        result = linprog(obj, A_ub=constr_ineq, b_ub=constr_ineq_res)
    elif constr_ineq.size == 0:
        result = linprog(obj, A_eq=constr_eq, b_eq=constr_eq_res)
    else:
        result = linprog(obj, A_eq=constr_eq, b_eq=constr_eq_res, A_ub=constr_ineq, b_ub=constr_ineq_res)
    if maxi == True:
        result.fun *= -1
    return result


# Injects a zero with missing variables without having to use 0*(variable)
def inject(constr, not_var, len_var):
    not_var_mat = np.array(not_var)
    not_var_mat = not_var_mat.reshape(len(constr), len_var)

    for i in range(len(not_var_mat)):
        for k in range(len(not_var_mat[i])):
            if not_var_mat[i][k] == True:
                constr[i].insert(k, 0)
    return constr


# returns the final result called from linprog function
def result(var, constr, obj, maxi):
    # Checks which variables are not in the constr
    not_var = check_index(var, constr)
    # checks to see whether the contr contains (< == 1),(> == -1),(= == 0)
    ineq = check_ineq(constr)
    # Replaces vars with 1
    constr = rem(var, constr)
    obj = rem(var, obj)

    # converts constr to int
    constr = to_int(constr)
    # Inejcts non-declared variables into the array
    constr = inject(constr, not_var, len(var))

    # Checks to see if there are any > and negates them to <
    constr = ge_negate(constr, ineq)

    # Iterates through and filters original constr list into to distinct ones, Equalities and Inequalties
    constr_eq = rem_eq(constr, ineq)
    constr_ineq = rem_ineq(constr, ineq)
    # Pops the last values off the list and stores solution in another list
    constr_eq_res = pop_val(constr_eq)
    constr_ineq_res = pop_val(constr_ineq)

    # converts obj entry to int
    obj = to_int(obj)

    # checks to see if negation is needed based on maximization
    obj = negate(obj, maxi)

    # Converts to array
    constr_eq = np.array(constr_eq)
    constr_ineq = np.array(constr_ineq)
    obj = np.array(obj)  # converts list to array

    # Checks to see which appropriate method will be right based off given constraints
    result = ret_result(maxi, constr_eq, constr_ineq, constr_eq_res, constr_ineq_res, obj)

    # print("Maximize?",maxi)
    # print("ineq",ineq)
    # print("vars test",not_var)
    # print("Equality Constraints", constr_eq)
    # print("Inequality Constraints", constr_ineq)
    # print("Equality Resolution", constr_eq_res)
    # print("Inequality Resolution", constr_ineq_res)
    # print("Objective funct",obj)
    # print(result)

    return result