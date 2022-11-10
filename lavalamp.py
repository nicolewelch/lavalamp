
# Sources
# https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7515030/#sec4dot1-entropy-21-00541
# https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.45.6174&rep=rep1&type=pdf
# https://www.pnas.org/doi/epdf/10.1073/pnas.94.8.3513
# https://www.pnas.org/doi/pdf/10.1073/pnas.93.5.2083
# https://en.wikipedia.org/wiki/Approximate_entropy
# https://ieeexplore.ieee.org/abstract/document/5335714

import random
import cv2
import numpy
import time


def getFrame():
    vidcap = cv2.VideoCapture(0)
    if vidcap.isOpened():
        ret, frame = vidcap.read()
        if ret:
            # Display Frame

            # while(True):
            #     cv2.imshow("Frame", frame)

            #     if cv2.waitKey(1) & 0xFF == ord('q'):
            #         break
            return frame
        else:
            print("Error: failed to capture frame")
    else:
        print("Cannot open camera")

    # save frame to file
    # name = "OneDrive/Desktop/Projects/lavalamp/frame.jpg"
    # cv2.imwrite(name, frame)

    return frame


def genTrueRand(lamplist, FRAMENUM, IMGLEN):
    count = 0  # increment after storing value in lamplist

    # loop by frame
    for _ in range(FRAMENUM):
        frame = getFrame()

        # loop by row
        for i in range(IMGLEN):
            row = frame[i]
            # add together RBG values of all pixels in a row
            value = sum(map(sum, row)) % 10
            lamplist[count] = value
            count += 1


def genRandom(genlist, LISTSIZE):
    for i in range(LISTSIZE):
        genlist[i] = random.randint(0, 9)


def wiki_ApEn(U, m, r) -> float:
    """Approximate_entropy."""
    # https://en.wikipedia.org/wiki/Approximate_entropy

    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        C = [len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) / (N - m + 1.0) for x_i in x]
        return (N - m + 1.0) ** (-1) * sum(numpy.log(C))
    N = len(U)
    return _phi(m) - _phi(m + 1)


def main():
    start_time = time.time()
    frame = getFrame()
    IMGLEN = frame.shape[0]
    FRAMENUM = 5
    LISTSIZE = FRAMENUM * IMGLEN

    lamplist = numpy.zeros(LISTSIZE, int)
    genlist = numpy.zeros(LISTSIZE, int)
    # lamplist = [0] * LISTSIZE
    # genlist = [0] * LISTSIZE

    genTrueRand(lamplist, FRAMENUM, IMGLEN)
    genRandom(genlist, LISTSIZE)

    pattern = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    patternlist = pattern * (LISTSIZE // 10)

    # save list
    # with open('OneDrive/Desktop/Projects/lavalamp/lamptest.txt', 'w') as file:
        # file.write(', '.join(str(num) for num in lamplist))

    # read in list
    # genlist = numpy.genfromtxt('OneDrive/Desktop/Projects/lavalamp/test.csv', delimiter=',', dtype=int)

    print('numbers generated: ' + str(LISTSIZE))
    print("Generated random: " + str(wiki_ApEn(genlist, 2, (0.2 * numpy.std(genlist)))))
    print("True random: " + str(wiki_ApEn(lamplist, 2, (0.2 * numpy.std(lamplist)))))
    print("Pattern random: " + str(wiki_ApEn(patternlist, 2, (0.2 * numpy.std(patternlist)))))
    print("--- %s seconds ---" % (time.time() - start_time))


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    main()
