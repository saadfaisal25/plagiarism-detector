from processtxt import processTXT
from lcs import getLCSSim
from senMatch import getSenSim
from rabinKarp import getRKSim

def main():
    file1 = "testfiles/testfile1.txt"
    file2 = "testfiles/testfile2.txt"

    data1 = processTXT(file1)
    data2 = processTXT(file2)
    print("\nData processed!\n")

    # LCS Algorithm Results
    simlcs = getLCSSim(data1, data2)
    print("LCS Algorithm: ")
    print("The percentage of similarity between {} and {} is {}%\n".format(file1, file2, simlcs))

    # Sentence Matching Results
    simsen = getSenSim(data1, data2) 
    print("Sentence Matching Algorithm: ")
    print("The percentage of similarity between {} and {} is {}%\n".format(file1, file2, simsen))

    # Rabin Karp Algorithm Results
    simrk = getRKSim(data1, data2) 
    print("Rabin Karp Algorithm: ")
    print("The percentage of similarity between {} and {} is {}%\n".format(file1, file2, simrk))

if __name__ == "__main__":
    main()