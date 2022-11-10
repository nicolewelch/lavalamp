# lavalamp
An exploration of Approximate Entropy

inspired by CloudFlare's 'wall of entropy', a simple program that generates a list of true random integers from 0 to 9, and measures
how random the generated list is using approximate entropy. We then compare this value with the approximate entropy of a list of pseudo random numbers generated
in python, and another list containing a patterned sequence. The camera must be pointed at a source of unpredictibility, such as a lava lamp in order for
the generated numbers to be considered true random.


### Required
openCV  
`pip install opencv-python`

A camera is also required to run this program, as this is how random values are generated.
