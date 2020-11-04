from processtxt import processTXT
from lcs import getSimilarity

def main():
    file1 = "testfile1.txt"
    file2 = "testfile2.txt"

    data1 = processTXT(file1)
    data2 = processTXT(file2)
    print("Data processed!")

    sim = getSimilarity(data1, data2)
    print(sim)

    avgPlag = round(sum(sim)/len(sim)*100, 5)
    print("The percentage of similarity between {} and {} is {}%".format(file1, file2, avgPlag))

if __name__ == "__main__":
    main()