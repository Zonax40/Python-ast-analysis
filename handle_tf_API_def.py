import ast
import inspect
import tensorflow
""" 
@para function_name: the last name:string
@para file_path: the function's file's path
@para parse_result: the result of the file's parsing
@return: no return value
"""
visit_stack = []
def strip_function(function_name, file_path, parse_result):
    index = 0
    # if_located used to refer if successfully find the specific function
    while True:
        if_located = False
        # here, update the index
        # here, wrong handle way
        search_result = parse_result[index:].find("FunctionDef(name='")
        if search_result == -1:
            # used to represent finished
            break
        # then check the name
        if parse_result[search_result + index: search_result  + index + len("FunctionDef(name='") ] != "FunctionDef(name='":
            # something goes wrong
            print("In recursive, something goes wrong.")
            print(parse_result[search_result + index: search_result  + index + len("FunctionDef(name='")])
        # get the name
        tmp = parse_result[search_result + index+ len("FunctionDef(name='"):].find("'")
        # print(tmp)
        # with successful repair
        name = parse_result[search_result +index +len("FunctionDef(name='") : search_result +index +len("FunctionDef(name='") + tmp ]
        # successfully validate
        # compare the name 
        # print(name+":"+function_name)
        if name == function_name:
            # print(name+":"+function_name)
            # if the name matches, then store this parts, and then store this part into a file stored in /tmp
            # first locate such pattern: FunctionDef(.......)
            # use the simplest way to finish traversing
            # when bracket_count goes to 0, then finish
            bracket_count = 1
            # temp_index is used to account the length of traversing length
            # The actual index is search_result + leng("FunctionDef(" + temp_index)
            temp_index = 0
            for letter in parse_result[search_result + index + len("FunctionDef("):]:
                if letter == "(":
                    bracket_count = bracket_count + 1
                elif letter == ")":
                    bracket_count = bracket_count - 1
                # check out if it is time to finish
                if bracket_count == 0:
                    # if_located works 
                    if_located = True
                    break
                temp_index = temp_index + 1
            # now get the successful substring, it is time.
            
            if if_located:
                # if_located is true, means find the defination of the function , recording the inner called functions
                check_string = parse_result[search_result + index+ len("FunctionDef"):search_result+index + len("FunctionDef(")+temp_index+1]
                # print("+++"+check_string)
                # now it is time to deal with the call function
                # here is the furthur trace of the function, obtain the contained function and just add it to visit_stack
                # similarity, deal with the string result 
                new_index = 0
                while True:
                    temp_search_result = check_string[new_index:].find("Call(func=")
                    if temp_search_result == -1:
                        break
                    # to make the program more stable use some fool methods
                    bracket_count = 1
                    # temp_index is used to account the length of traversing length
                    temp_index = 0
                    for letter in check_string[temp_search_result + new_index + len("Call(func="):]:
                        if letter == "(":
                            bracket_count = bracket_count + 1
                        elif letter == ")":
                            bracket_count = bracket_count - 1
                        # check out if it is time to finish
                        if bracket_count == 0:
                            # if_located works 
                            break
                        temp_index = temp_index + 1
                    # call_string validate, it is complete
                    call_string = check_string[temp_search_result+new_index:temp_search_result+new_index+temp_index+len("Call(func=")+1]
                    # first, check out the first few characters if they are Call(func=Name, if so just get id
                    # work properly
                    if check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Name")] == "Call(func=Name":
                        # just compare the first few chars if it is Call(func=Name(id=
                        if check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Name(id='")] == "Call(func=Name(id='":
                            symbol_index = check_string[temp_search_result+new_index+len("Call(func=Name(id='"):].find("'")
                            # validate
                            id_name = check_string[temp_search_result+new_index+len("Call(func=Name(id='"):temp_search_result+new_index+len("Call(func=Name(id='")+symbol_index]
                            visit_stack.append(id_name)
                    elif check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Attribute")] == "Call(func=Attribute":
                        bracket_count = 1
                        temp_index = 0
                        for letter in check_string[temp_search_result + new_index + len("Call(func=Attribute("):]:
                            if letter == "(":
                                bracket_count = bracket_count + 1
                            elif letter == ")":
                                bracket_count = bracket_count - 1
                            # check out if it is time to finish
                            if bracket_count == 0:
                                # if_located works 
                                break
                            temp_index = temp_index + 1
                        func_string = check_string[temp_search_result + new_index+ len("Call("):temp_search_result + new_index + len("Call(func=Attribute(")+temp_index+1]
                        # call_string is the correct array, just get the last attr
                        # print(call_string)
                        symbol_index =  func_string.rfind("attr='")
                        if symbol_index == -1:
                            print("Attribute: error:"+func_string)
                            new_index = new_index + temp_search_result + len("Call(func=")
                            continue
                            
                        temp_index = 0
                        for letter in func_string[symbol_index + len("attr='"):]:
                            if letter != "'":
                                temp_index = temp_index + 1
                            else:
                                break
                        attriute_name = func_string[symbol_index + len("attr='"): symbol_index + len("attr='") + temp_index]
                        # print(attriute_name)
                        # print(attriute_name)
                        visit_stack.append(attriute_name)
                    else:
                        # print("Call(func= appears error:"+check_string[temp_search_result+new_index:temp_search_result+new_index+len("Call(func=Attribute")])
                        # here just Call and call 
                        pass
                    # print(call_string)
                    new_index = new_index + temp_search_result + len("Call(func=")

                pass
            else:
                # pass
                # stop tracing
                index = search_result + index + len("FunctionDef(name='") - 1
                continue
            break
        else:
            # change index to fit the next coming cycle
            index = search_result + index + len("FunctionDef(name='") - 1
            pass


# the basic idea is: use the inspect.getfile() to check out the file as getfile() might return error results ,which need extra handle
getfile_error=[]
if __name__ == "__main__":
    # try to read the file
    with open("./tf_APIdef.txt", "r") as f:
        for line in f.readlines():
            function_call = "tensorflow" + line[2:-1]
            # 
            bracket_index = function_call.find("(")
            if bracket_index == -1:
                print("Error in bracket_index")
                continue
            function_call = function_call[:bracket_index]
            function_call_last_name =  function_call.split(".")[-1]
            # print(function_call)
            try:
                file_path = inspect.getfile(eval(function_call))
            except:
                # actually, this is a quite small set, therefore, just skip it without great influence
                getfile_error.append(function_call)
                continue    
            # by ast tree, it is easy to judge if file_path file contains the function.
            with open(file_path, "r") as f:
                tree = ast.parse(f.read())
                # string
                parse_result = ast.dump(tree)
            if parse_result.find("FunctionDef(name='" + function_call_last_name + "'") >= 0:
                # 561 / 1442
                # print(function_call)
                strip_function(function_call_last_name, file_path, parse_result)
            else:
                # extra_handle()
                pass
    # print("***************************************")
    # print(getfile_error)