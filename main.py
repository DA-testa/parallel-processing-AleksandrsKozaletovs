# python3

def parallel_processing(count, m, data):
    output = []
    threadCount = [0]*count
    workedTime = [0]*count
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    i = 0
    while i < m:
        for j in range(count):
            if threadCount[j] == 0:
                output.append([j,workedTime[j]])
                threadCount[j] = data[i]    
                workedTime[j] += data[i]           
                i += 1
            if threadCount[j] != 0:
                threadCount[j] = threadCount[j] -1        
    return output

def main():
    # TODO: create input from keyboard    
    n = 0
    m = 0
    data = []
    actionInput = input()
    if "i" in actionInput.lower():
        n,m = map(int,input().split())
        data = list(map(int,input().split()))
    elif "f" in actionInput.lower():
        openFilename = input()
        if not "a" in openFilename.lower():
        
            with open("./tests"+openFilename, mode = "r") as f:
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
        print(k, r)
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
