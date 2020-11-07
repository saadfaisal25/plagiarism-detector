import time
from processtxt import processTXT
from lcs import getLCSSim
from senMatch import getSenSim
from rabinKarp import getRKSim
from senMatchBinary import getBinarySim
from cosineSim import getCosineSim

def main():
    file1 = "testfiles/testfile1.txt"
    file2 = "testfiles/testfile2.txt"

    data1 = processTXT(file1)
    data2 = processTXT(file2)
    print("\nData processed!\n")

    # LCS Algorithm Results
    start = time.time()
    simlcs = getLCSSim(data1, data2)
    end = time.time()
    print("LCS Algorithm: ")
    print("The percentage of similarity between {} and {} is {}%".format(file1, file2, simlcs))
    print("Function runtime:", end-start , '\n')

    # Sentence Matching Results
    start = time.time()
    simsen = getSenSim(data1, data2)
    end = time.time()
    print("Sentence Matching Algorithm: ")
    print("The percentage of similarity between {} and {} is {}%".format(file1, file2, simsen))
    print("Function runtime:", end-start , '\n')

    # Rabin Karp Algorithm Results
    start = time.time()
    simrk = getRKSim(data1, data2)
    end = time.time() 
    print("Rabin Karp Algorithm: ")
    print("The percentage of similarity between {} and {} is {}%".format(file1, file2, simrk))
    print("Function runtime:", end-start , '\n')

    # Sentence Matching Using Binary Search Algorithm Results
    start = time.time()
    simbinary = getBinarySim(data1, data2)
    end = time.time() 
    print("Sentence Matching (Binary Search) Algorithm: ")
    print("The percentage of similarity between {} and {} is {}%".format(file1, file2, simbinary))
    print("Function runtime:", end-start , '\n')

    # Cosine Similarity Algorithm
    start = time.time()
    simcos = getCosineSim(data1, data2)
    end = time.time() 
    print("Cosine Similarity Algorithm: ")
    print("The percentage of similarity between {} and {} is {}%".format(file1, file2, simcos))
    print("Function runtime:", end-start , '\n')

if __name__ == "__main__":
    main()