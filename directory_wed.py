import os

def print_directory(path, indent, depth=0):
    '''
    (str, str) -> None
    Print out the entire directory structure for the given path
    using the indent to indicate subdirectories.
    '''
    
    #print the current directory
    print(indent*depth + path + ":")
    
    #print all the subfiles and subdirectories.
    #for each file and subdirectory, print them
    # then recurse on the subdirectories
    for item in os.listdir(path):
        print(indent*depth+item)
        
    for item in os.listdir(path):
        # each item is only the filename, does not include
        # the path
        # check is the item a subdirectory
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print_directory(full_path,  indent, depth+1)
        
            
if __name__ == '__main__':
    
    path = '/Users/'
    print_directory(path, '-->')
    
    # get the current working directory
    #path = os.getcwd()   
    #print(path)
    file_list = os.listdir(path)
    print(file_list)
    #print(os.path.isdir(path))
    #print(os.path.join(path, file_list[1]))