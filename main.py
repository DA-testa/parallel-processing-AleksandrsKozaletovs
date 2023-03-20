# python3

def parallel_processing(count, m, data):
    output = []
    threadCount = [0]*count
    workedTime = 0
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    i = 0
    j = 0
    while i < m:
        for j in range(count):
            if threadCount[j] == 0:
                output.append([j,workedTime])
                threadCount[j] = data[i]           
                i += 1
            if threadCount[j] != 0:
                threadCount[j] = threadCount[j] -1        
        workedTime += 1  
    return output

def main():
    # TODO: create input from keyboard    
    
    if "i" == "i":
        n,m = map(int,input().split())
        data = list(map(int,input().split()))
    elif "f" == "f":
        openFilename = input()
        if "a" in openFilename.lower():
            return
        else:
            with open(openFilename, mode = "r", encoding = "utf8") as f:
                n,m = map(int,f.readline().split())
                data = list(map(int,f.readline().split()))                               
    else:
        return
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for k, r in result:
        print(k,r)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
