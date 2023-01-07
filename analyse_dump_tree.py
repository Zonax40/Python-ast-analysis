def dump_FunctionDef(string):
    # by using find method 
    index = string.find(r", body=[")
    if index == -1:
        with open(log6_path, "a+") as f:
            f.write("Alright, something went wrong in dump_FunctionDef:" + string)
    # Start to match something interesting
    



if __name__ == "__main__":
    pass
